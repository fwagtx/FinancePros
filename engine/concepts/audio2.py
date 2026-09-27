"""Music and sound effects for the doodle concepts, generated from scratch (no licensing).

style "lofi"  : mellow keys + brushed beat + vinyl hiss (explainer / news feel)
style "bouncy": pizzicato plucks + woodblock + walking bass (comedy / mascot feel)
sfx           : a soft pop whenever a new scene starts, a little chime at the end.
"""
import json, os, sys
import numpy as np
import soundfile as sf

SR = 48000
R = np.random.default_rng(11)


def lp(x, cut):   # gentle FFT low-pass (no scipy needed)
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / np.sqrt(1 + (f / cut) ** 4)
    return np.fft.irfft(X, len(x))


def hp(x, cut):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 - 1 / np.sqrt(1 + (f / cut) ** 4)
    return np.fft.irfft(X, len(x))


def hz(n): return 440 * 2 ** ((n - 69) / 12)


def keys(freq, dur, vol):
    n = int(dur * SR); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * freq * t) + 0.35 * np.sin(4 * np.pi * freq * t) * np.exp(-t * 3) + 0.12 * np.sin(6 * np.pi * freq * t) * np.exp(-t * 5)
    x *= (1 + 0.18 * np.sin(2 * np.pi * 4.5 * t))
    return vol * x * np.minimum(1, t / 0.015) * np.exp(-t * 0.9)


def pluck(freq, dur, vol):
    n = int(dur * SR); t = np.arange(n) / SR
    x = sum(np.sin(2 * np.pi * freq * m * t) / m ** 1.3 * np.exp(-t * (6 + 3 * m)) for m in range(1, 6))
    return vol * x * np.minimum(1, t / 0.004)


def kick(vol=0.9):
    n = int(0.35 * SR); t = np.arange(n) / SR; f = 50 + 70 * np.exp(-t * 30)
    return vol * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)


def noise_hit(dur, decay, vol, cut_hi=None, cut_lo=None):
    n = int(dur * SR); t = np.arange(n) / SR; x = R.standard_normal(n)
    if cut_lo: x = hp(x, cut_lo)
    if cut_hi: x = lp(x, cut_hi)
    return vol * x * np.exp(-t * decay)


def put(buf, sig, at):
    a = int(at * SR)
    if a >= len(buf): return
    buf[a:a + len(sig)] += sig[:len(buf) - a]


def music(dur, style):
    n = int((dur + 2) * SR); m = np.zeros(n)
    if style == "bouncy":
        bpm = 104; beat = 60 / bpm
        prog = [[60, 64, 67], [57, 60, 64], [53, 57, 60], [55, 59, 62]]
        melody = [72, 74, 76, 79, 76, 74, 72, 69]
        t, bar = 0.0, 0
        while t < dur + 1:
            ch = prog[bar % 4]
            for b in range(4):
                put(m, pluck(hz(ch[0] - 24 + (7 if b % 2 else 0)), 0.6, 0.32), t + b * beat)
                for j, nn in enumerate(ch): put(m, pluck(hz(nn), 0.5, 0.10), t + b * beat + beat / 2 + j * 0.012)
                put(m, noise_hit(0.05, 90, 0.08, cut_lo=1500, cut_hi=4000), t + b * beat + beat / 2)
            if bar % 2 == 1:
                for j in range(8): put(m, pluck(hz(melody[(j + bar) % 8]), 0.35, 0.09), t + j * beat / 2)
            t += 4 * beat; bar += 1
        m = lp(m, 6000)
    else:
        bpm = 80; beat = 60 / bpm; sw = 0.06
        prog = [[50, 53, 57, 60, 64], [43, 53, 59, 62, 64], [48, 52, 55, 59, 62], [45, 52, 55, 60, 64]]
        t, bar = 0.0, 0
        while t < dur + 1:
            ch = prog[bar % 4]
            for j, nn in enumerate(ch): put(m, keys(hz(nn), 4 * beat + 0.4, 0.06 if j else 0.09), t + j * 0.018)
            for b in range(4):
                bt = t + b * beat
                if b in (0, 2): put(m, kick(0.55), bt)
                if b == 2: put(m, kick(0.35), bt + beat * 0.75)
                if b in (1, 3): put(m, noise_hit(0.25, 18, 0.13, cut_hi=3500, cut_lo=300), bt)
                for h in (0, 1): put(m, noise_hit(0.06, 70, 0.045, cut_lo=6000), bt + h * (beat / 2 + (sw if h else 0)))
            t += 4 * beat; bar += 1
        m = lp(m, 4200)
        hiss = hp(R.standard_normal(n), 2000) * 0.004
        crack = np.zeros(n); idx = R.integers(0, n, int(dur * 6)); crack[idx] = R.uniform(0.05, 0.18, len(idx)) * R.choice([-1, 1], len(idx))
        m += hiss + lp(crack, 5000)
    fade = int(1.2 * SR); m[:fade] *= np.linspace(0, 1, fade)
    m = m[:int(dur * SR)]; m[-fade:] *= np.linspace(1, 0, fade)
    return 0.5 * m / (np.max(np.abs(m)) + 1e-9)


def pop():
    n = int(0.12 * SR); t = np.arange(n) / SR; f = 520 + 900 * t / 0.12
    return 0.35 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 38)


def chime():
    return sum(keys(hz(nn), 1.6, 0.12) for nn in (72, 76, 79))


def build(out_dir, style="lofi"):
    tl = json.load(open(os.path.join(out_dir, "timeline.json"))); dur = tl["duration"]
    sf.write(os.path.join(out_dir, "music.wav"), music(dur, style).astype(np.float32), SR)
    fx = np.zeros(int((dur + 1) * SR)); last = None
    for ln in tl["lines"]:
        g = ln["scene"].get("group")
        if ln["i"] > 0 and g != last: put(fx, pop(), ln["s"] - 0.1)
        last = g
    put(fx, chime(), dur - 2.2)
    sf.write(os.path.join(out_dir, "sfx.wav"), fx[:int(dur * SR)].astype(np.float32), SR)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "lofi")
