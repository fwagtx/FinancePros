"""Build one finished episode: voice -> music/sfx -> frames -> mixed MP4.
usage: python build.py episodes/<file>.json [--stills]
"""
import json, os, subprocess, sys
import voice, audio

HERE = os.path.dirname(os.path.abspath(__file__))
FF = os.environ.get("FFMPEG", "ffmpeg")


def run(cmd):
    subprocess.run(cmd, check=True)


def build(ep_path, stills=False):
    ep = json.load(open(ep_path))
    out = os.path.join(HERE, "out", ep["id"]); os.makedirs(out, exist_ok=True)
    voice.build(ep_path, out)
    if stills:
        env = dict(os.environ, FRAMES=stills)
        subprocess.run(["node", os.path.join(HERE, "render.js"), ep_path, out], check=True, env=env); return out
    audio.build(out)
    subprocess.run(["node", os.path.join(HERE, "render.js"), ep_path, out], check=True)
    # mix: voice (clean + broadcast polish) + music ducked under voice + sfx, then loudness -14 LUFS
    run([FF, "-y", "-loglevel", "error", "-i", os.path.join(out, "voice.wav"), "-i", os.path.join(out, "music.wav"), "-i", os.path.join(out, "sfx.wav"),
         "-filter_complex",
         "[0:a]aresample=48000,highpass=f=80,equalizer=f=3200:t=q:w=1.2:g=2.5,acompressor=threshold=-20dB:ratio=3:attack=4:release=90:makeup=3,asplit=2[v][vs];"
         "[1:a]volume=0.4[m];[m][vs]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=350[md];"
         "[2:a]volume=0.9[fx];[v][md][fx]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9",
         "-ar", "48000", os.path.join(out, "mix.wav")])
    final = os.path.join(out, ep["id"] + ".mp4")
    run([FF, "-y", "-loglevel", "error", "-i", os.path.join(out, "video.mp4"), "-i", os.path.join(out, "mix.wav"),
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ac", "2", "-shortest", "-movflags", "+faststart", final])
    return final


if __name__ == "__main__":
    stills = None
    if "--stills" in sys.argv: stills = sys.argv[sys.argv.index("--stills") + 1]
    print(build(sys.argv[1], stills))
