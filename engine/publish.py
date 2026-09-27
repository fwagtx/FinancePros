"""Schedule finished videos through the Metricool API, formatted for each platform.

Shorts (9:16)  -> three posts at the same time:
   1. Instagram Reel + Facebook Reel (shared caption, custom 9:16 cover)
   2. TikTok (short caption + hashtags, cover)
   3. YouTube Short (title with #Shorts, description, tags)
Long-form (16:9) -> one YouTube video (title, description with chapters, tags, custom thumbnail).

Needs env: METRICOOL_USER_TOKEN (secret), METRICOOL_USER_ID, METRICOOL_BLOG_ID.
METRICOOL_DRAFT=true saves everything as drafts to approve in Metricool first.
"""
import json, os, sys, time, urllib.request

API = "https://app.metricool.com/api/v2/scheduler/posts"
BASE = {"autoPublish": True, "shortener": False, "saveExternalMediaFiles": True, "mediaAltText": [], "descendants": [],
        "firstCommentText": "", "hasNotReadNotes": False, "smartLinkData": {"ids": []}}
YT_TAGS = ["personal finance", "money", "finance explained", "FinanceProsTV"]


def _draft(): return os.environ.get("METRICOOL_DRAFT", "false").lower() == "true"


def wait_public(url, tries=30):
    for _ in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=20) as r:
                if r.status == 200: return True
        except Exception:
            pass
        time.sleep(10)
    return False


def _post(body):
    uid, blog, tok = os.environ["METRICOOL_USER_ID"], os.environ["METRICOOL_BLOG_ID"], os.environ["METRICOOL_USER_TOKEN"]
    req = urllib.request.Request(f"{API}?blogId={blog}&userId={uid}", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "X-Mc-Auth": tok}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        text = r.read().decode()
    print("Metricool:", r.status, text[:200]); return text


def short_posts(video, cover, post, when, tz):
    """The three per-platform posts for one vertical short."""
    title = post["title"].strip()
    common = dict(BASE, publicationDate={"dateTime": when, "timezone": tz}, media=[video], draft=_draft())
    ig = dict(common, text=post["ig"], providers=[{"network": "instagram"}, {"network": "facebook"}],
              instagramData={"type": "REEL", "showReelOnFeed": True, "isAiGenerated": True},
              facebookData={"type": "REEL", "title": title[:100]})
    tt = dict(common, text=post["tiktok"][:2200], providers=[{"network": "tiktok"}],
              tiktokData={"privacyOption": "PUBLIC_TO_EVERYONE", "title": title[:90], "isAigc": True, "disableComment": False,
                          "disableDuet": False, "disableStitch": False, "autoAddMusic": False})
    yt_title = (title if "#shorts" in title.lower() else f"{title} #Shorts")[:100]
    yt = dict(common, text=post["yt_desc"], providers=[{"network": "youtube"}],
              youtubeData={"title": yt_title, "type": "short", "privacy": "public", "madeForKids": False, "category": "EDUCATION",
                           "tags": (post.get("tags") or [])[:10] + YT_TAGS[:2], "isAiGeneratedContent": False})
    if cover: ig["videoThumbnailUrl"] = cover; tt["videoThumbnailUrl"] = cover
    return [ig, tt, yt]


def long_post(video, thumb, post, when, tz):
    b = dict(BASE, publicationDate={"dateTime": when, "timezone": tz}, media=[video], draft=_draft(), text=post["yt_desc"][:4900],
             providers=[{"network": "youtube"}],
             youtubeData={"title": post["title"][:100], "type": "video", "privacy": "public", "madeForKids": False, "category": "EDUCATION",
                          "tags": (post.get("tags") or [])[:12] + YT_TAGS, "isAiGeneratedContent": False})
    if thumb: b["videoThumbnailUrl"] = thumb
    return [b]


def schedule(video, cover, post, when, tz="America/New_York", longform=False):
    if not wait_public(video):
        raise RuntimeError(f"Video is not publicly reachable yet: {video}")
    if cover and not wait_public(cover, 6): cover = None
    bodies = long_post(video, cover, post, when, tz) if longform else short_posts(video, cover, post, when, tz)
    out = []
    for b in bodies:
        try: out.append(_post(b))
        except urllib.error.HTTPError as e:   # a cover the network can't take must not block the post
            if b.get("videoThumbnailUrl"):
                print("retrying without cover:", e.code, e.read()[:200]); b.pop("videoThumbnailUrl"); out.append(_post(b))
            else: raise
    return out


if __name__ == "__main__":
    sc = json.load(open(sys.argv[1]))
    schedule(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None, sc["post"], sys.argv[4], longform=sc.get("format") == "landscape")
