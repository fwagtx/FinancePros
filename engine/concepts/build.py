"""Build a doodle-concept episode: voice -> music/sfx -> hand-drawn frames -> mix.
usage: python concepts/build.py concepts/episodes/<file>.json [--stills t1,t2,...]
Uses the same free Kokoro voices as the main engine; nothing in the main pipeline is changed.
"""
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ENG = os.path.dirname(HERE)
sys.path.insert(0, ENG); sys.path.insert(0, HERE)
import voice, audio2

FF = os.environ.get("FFMPEG", "ffmpeg")
voice.CAST["nutty"] = {"mix": [("am_adam", 1.0)], "speed": 1.04, "lang": "en-us"}; voice.GAP["nutty"] = 0.24


def run(cmd): subprocess.run(cmd, check=True)


def build(ep_path, stills=None):
    ep = json.load(open(ep_path))
    out = os.path.join(HERE, "out", ep["id"]); os.makedirs(out, exist_ok=True)
    if not (stills and os.path.exists(os.path.join(out, "timeline.json")) and os.environ.get("REUSE")):
        voice.build(ep_path, out)
    if stills:
        subprocess.run(["node", os.path.join(HERE, "render.js"), ep_path, out], check=True, env=dict(os.environ, FRAMES=stills)); return out
    audio2.build(out, ep.get("music", "lofi"))
    subprocess.run(["node", os.path.join(HERE, "render.js"), ep_path, out], check=True)
    vpre = f"asetrate={24000 * ep['pitch']:.0f},aresample=48000,atempo={1 / ep['pitch']:.4f}," if ep.get("pitch") else "aresample=48000,"
    run([FF, "-y", "-loglevel", "error", "-i", os.path.join(out, "voice.wav"), "-i", os.path.join(out, "music.wav"), "-i", os.path.join(out, "sfx.wav"),
         "-filter_complex",
         f"[0:a]{vpre}highpass=f=75,equalizer=f=200:t=q:w=1:g=1.5,equalizer=f=3200:t=q:w=1.2:g=2,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=2,asplit=2[v][vs];"
         f"[1:a]volume={ep.get('musicVol', 0.45)}[m];[m][vs]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];"
         "[2:a]volume=0.8[fx];[v][md][fx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9",
         "-ar", "48000", os.path.join(out, "mix.wav")])
    meas = subprocess.run([FF, "-i", os.path.join(out, "mix.wav"), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", meas)[-1])
    run([FF, "-y", "-loglevel", "error", "-i", os.path.join(out, "mix.wav"), "-af", f"volume={-14 - I:.2f}dB,alimiter=limit=0.74:attack=5:release=50:level=false", "-ar", "48000", os.path.join(out, "mix2.wav")])
    os.replace(os.path.join(out, "mix2.wav"), os.path.join(out, "mix.wav"))
    final = os.path.join(out, ep["id"] + ".mp4")
    run([FF, "-y", "-loglevel", "error", "-i", os.path.join(out, "video.mp4"), "-i", os.path.join(out, "mix.wav"),
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ac", "2", "-shortest", "-movflags", "+faststart", final])
    return final


if __name__ == "__main__":
    st = sys.argv[sys.argv.index("--stills") + 1] if "--stills" in sys.argv else None
    print(build(sys.argv[1], st))
