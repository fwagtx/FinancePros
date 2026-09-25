"""Turn an episode script into narration audio plus a timeline.

Each line is spoken by Ticker or Dot with a free Kokoro voice (Apache 2.0).
Output: <out>/voice.wav and <out>/timeline.json holding, for every line,
its start/end time, word timings (for captions) and a per-frame loudness
envelope (for Ticker's lip-sync).
"""
import json, os, re, sys
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.environ.get("KOKORO_MODEL", os.path.join(HERE, "models", "kokoro-v1.0.onnx"))
VOICES = os.environ.get("KOKORO_VOICES", os.path.join(HERE, "models", "voices-v1.0.bin"))
FPS = 30
SR = 24000

# Brand voices: blends of two stock voices, so they're unique to the channel.
CAST = {
    "ticker": {"mix": [("am_michael", 0.6), ("am_fenrir", 0.4)], "speed": 1.06, "lang": "en-us"},
    "dot": {"mix": [("af_heart", 0.55), ("af_nicole", 0.45)], "speed": 1.08, "lang": "en-us"},
}
GAP = {"ticker": 0.22, "dot": 0.22}          # pause after a line
HANDOFF = 0.34                              # extra pause when the speaker changes


def style_for(k, who):
    return sum(k.get_voice_style(n) * w for n, w in CAST[who]["mix"])


def trim(x, thr=0.012):
    """Trim leading/trailing near-silence, keep a few ms of air."""
    idx = np.where(np.abs(x) > thr)[0]
    if len(idx) == 0:
        return x
    a = max(0, idx[0] - int(0.02 * SR))
    b = min(len(x), idx[-1] + int(0.06 * SR))
    return x[a:b]


def word_times(text, start, end):
    """Spread words across the spoken span, weighted by length (syllable proxy)."""
    words = text.split()
    weights = [max(2, len(re.sub(r"[^A-Za-z0-9$%]", "", w))) + (3 if re.search(r"[,.;:?!]$", w) else 0) for w in words]
    total = sum(weights)
    t, out = start, []
    for w, wt in zip(words, weights):
        d = (end - start) * wt / total
        out.append({"w": w, "s": round(t, 3), "e": round(t + d, 3)})
        t += d
    return out


def build(episode_path, out_dir):
    ep = json.load(open(episode_path))
    k = Kokoro(MODEL, VOICES)
    styles = {who: style_for(k, who) for who in CAST}
    audio, lines, t, prev = [], [], 0.35, None      # small lead-in so frame 0 is a clean title card
    audio.append(np.zeros(int(0.35 * SR), dtype=np.float32))
    for i, line in enumerate(ep["lines"]):
        who = line.get("who", "ticker")
        if prev and prev != who:
            audio.append(np.zeros(int(HANDOFF * SR), dtype=np.float32)); t += HANDOFF
        say = line.get("say", line["text"])      # "say" = pronunciation-friendly version
        x, sr = k.create(say, voice=styles[who], speed=CAST[who]["speed"], lang=CAST[who]["lang"])
        x = trim(np.asarray(x, dtype=np.float32))
        dur = len(x) / SR
        lines.append({"i": i, "who": who, "text": line["text"], "s": round(t, 3), "e": round(t + dur, 3),
                      "words": word_times(line["text"], t, t + dur), "scene": line.get("scene", {})})
        audio.append(x); t += dur
        gap = line.get("pause", GAP[who])
        audio.append(np.zeros(int(gap * SR), dtype=np.float32)); t += gap
        prev = who
    tail = ep.get("tail", 2.6)                     # time for the end card
    audio.append(np.zeros(int(tail * SR), dtype=np.float32)); t += tail
    y = np.concatenate(audio)
    y = 0.9 * y / (np.max(np.abs(y)) + 1e-9)
    os.makedirs(out_dir, exist_ok=True)
    sf.write(os.path.join(out_dir, "voice.wav"), y, SR)
    # per-frame loudness for lip-sync (0..1)
    hop = SR // FPS
    n = int(np.ceil(len(y) / hop))
    env = np.array([np.sqrt(np.mean(y[j * hop:(j + 1) * hop] ** 2)) if j * hop < len(y) else 0 for j in range(n)])
    env = env / (np.percentile(env[env > 0], 95) + 1e-9)
    env = np.clip(env, 0, 1)
    tl = {"duration": round(len(y) / SR, 3), "fps": FPS, "lines": lines, "env": [round(float(v), 3) for v in env]}
    json.dump(tl, open(os.path.join(out_dir, "timeline.json"), "w"))
    return tl


if __name__ == "__main__":
    tl = build(sys.argv[1], sys.argv[2])
    print(f"{len(tl['lines'])} lines, {tl['duration']}s")
