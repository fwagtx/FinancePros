"""Original music bed and sound effects, generated from scratch (no licensing needed).

music.wav : a warm, low-key electronic bed (pads + soft pulse + light arpeggio).
sfx.wav   : the three-beep LED sound logo, soft scan whooshes on scene changes.
"""
import json, os, sys
import numpy as np
import soundfile as sf

SR = 48000
BPM = 112
rng = np.random.default_rng(7)


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc; y[i] = acc
    return y


def env_adsr(n, a=0.01, d=0.1, s=0.6, r=0.2):
    t = np.arange(n) / SR; e = np.ones(n) * s
    A, D, R = int(a * SR), int(d * SR), int(r * SR)
    e[:A] = np.linspace(0, 1, A) if A else e[:A]
    e[A:A + D] = np.linspace(1, s, max(1, len(e[A:A + D])))
    if R: e[-R:] *= np.linspace(1, 0, R)
    return e


def note(freq, dur, kind="pad", vol=0.2):
    n = int(dur * SR); t = np.arange(n) / SR
    if kind == "pad":
        x = sum(np.sin(2 * np.pi * freq * m * t + d) / m for m, d in [(1, 0), (2, 0.3), (3, 1.1)])
        x += 0.5 * np.sin(2 * np.pi * freq * 1.003 * t)
        return vol * x * env_adsr(n, 0.6, 0.4, 0.8, 0.8)
    if kind == "pluck":
        x = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(4 * np.pi * freq * t)
        return vol * x * np.exp(-t * 7)
    if kind == "bass":
        x = np.sin(2 * np.pi * freq * t) + 0.2 * np.sin(4 * np.pi * freq * t)
        return vol * x * env_adsr(n, 0.01, 0.15, 0.7, 0.1)
    if kind == "kick":
        f = 110 * np.exp(-t * 25) + 45
        return vol * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)
    if kind == "hat":
        return vol * rng.standard_normal(n) * np.exp(-t * 60)


def hz(m): return 440 * 2 ** ((m - 69) / 12)


def music(duration):
    beat = 60 / BPM; bar = 4 * beat
    n = int((duration + 1) * SR); y = np.zeros(n)
    # Fmaj9 - Am7 - Dm9 - Bbmaj7  (calm, optimistic)
    chords = [[53, 57, 60, 64, 67], [57, 60, 64, 67], [50, 53, 57, 60, 64], [46, 50, 53, 57]]
    bassn = [41, 45, 38, 46]
    arp = [0, 2, 3, 1, 2, 4, 3, 1]
    t = 0.0; c = 0
    while t < duration + 1:
        ch = chords[c % 4]
        for m in ch:
            seg = note(hz(m), bar * 1.05, "pad", 0.028)
            a = int(t * SR); y[a:a + len(seg)] += seg[:max(0, n - a)]
        for b in range(4):
            a = int((t + b * beat) * SR)
            k = note(55, 0.4, "kick", 0.22); y[a:a + len(k)] += k[:max(0, n - a)]
            bs = note(hz(bassn[c % 4] - 12), beat * 0.9, "bass", 0.08); y[a:a + len(bs)] += bs[:max(0, n - a)]
            h = note(0, 0.05, "hat", 0.018); a2 = int((t + b * beat + beat / 2) * SR); y[a2:a2 + len(h)] += h[:max(0, n - a2)]
        for s in range(8):
            a = int((t + s * beat / 2) * SR)
            p = note(hz(ch[arp[s] % len(ch)] + 12), 0.5, "pluck", 0.03); y[a:a + len(p)] += p[:max(0, n - a)]
        t += bar; c += 1
    y = lowpass(y, 5200)
    fade = int(1.5 * SR); y[:int(0.4 * SR)] *= np.linspace(0, 1, int(0.4 * SR)); y[-fade:] *= np.linspace(1, 0, fade)
    return y[:int(duration * SR)]


def beeps(vol=0.28):
    out = np.zeros(int(0.9 * SR))
    for i, m in enumerate([76, 81, 88]):   # E5 A5 E6, rising
        n = int(0.16 * SR); t = np.arange(n) / SR
        x = (np.sin(2 * np.pi * hz(m) * t) + 0.25 * np.sign(np.sin(2 * np.pi * hz(m) * t))) * np.exp(-t * 16)
        a = int(i * 0.13 * SR); out[a:a + n] += vol * x
    return out


def whoosh(vol=0.10, dur=0.38):
    n = int(dur * SR); t = np.arange(n) / SR
    x = rng.standard_normal(n)
    x = lowpass(x, 2500) - lowpass(x, 400)
    e = np.sin(np.pi * t / dur) ** 2
    return vol * x * e * 3


def build(out_dir):
    tl = json.load(open(os.path.join(out_dir, "timeline.json")))
    dur = tl["duration"]
    sf.write(os.path.join(out_dir, "music.wav"), music(dur).astype(np.float32), SR)
    fx = np.zeros(int((dur + 1) * SR))
    def put(sig, at):
        a = int(max(0, at) * SR); fx[a:a + len(sig)] += sig[:max(0, len(fx) - a)]
    put(beeps(), 0.05)
    last = None
    for ln in tl["lines"]:
        kind = ln["scene"].get("type")
        if kind and kind != last and ln["i"] > 0:
            put(whoosh(), ln["s"] - 0.25)
        last = kind or last
    put(beeps(0.22), dur - 2.4)
    sf.write(os.path.join(out_dir, "sfx.wav"), fx[:int(dur * SR)].astype(np.float32), SR)


if __name__ == "__main__":
    build(sys.argv[1])
