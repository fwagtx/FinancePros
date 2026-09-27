"""Build a video from a template script: layout -> episode JSON -> concepts/build.py. Also renders its cover.
usage: python concepts/run.py concepts/scripts/<file>.json [--stills t1,t2]"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import layout, build


def make(script_path, stills=None):
    sc = json.load(open(script_path)); ep = layout.build_episode(sc)
    os.makedirs(os.path.join(HERE, "episodes", "auto"), exist_ok=True)
    ep_path = os.path.join(HERE, "episodes", "auto", sc["id"] + ".json"); json.dump(ep, open(ep_path, "w"), indent=1, ensure_ascii=False)
    out = build.build(ep_path, stills)
    size = (1080, 1920) if sc.get("format", "vertical") != "landscape" else (1280, 720)
    cv = layout.cover(sc, size); cp = os.path.join(HERE, "out", sc["id"] + "-covers.json"); json.dump([cv], open(cp, "w"))
    subprocess.run(["node", os.path.join(HERE, "thumbs.js")], check=True, env=dict(os.environ, THUMBS=os.path.relpath(cp, HERE)))
    return out, os.path.join(HERE, "out", "thumbs", cv["id"] + ".png")


def cover_only(script_path):
    sc = json.load(open(script_path)); size = (1080, 1920) if sc.get("format", "vertical") != "landscape" else (1280, 720)
    cv = layout.cover(sc, size); cp = os.path.join(HERE, "out", sc["id"] + "-covers.json"); json.dump([cv], open(cp, "w"))
    subprocess.run(["node", os.path.join(HERE, "thumbs.js")], check=True, env=dict(os.environ, THUMBS=os.path.relpath(cp, HERE)))
    return os.path.join(HERE, "out", "thumbs", cv["id"] + ".png")


if __name__ == "__main__":
    st = sys.argv[sys.argv.index("--stills") + 1] if "--stills" in sys.argv else None
    print(*make(sys.argv[1], st))
