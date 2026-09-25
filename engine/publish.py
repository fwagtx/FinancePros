"""Schedule a finished video on Instagram Reels, Facebook Reels, TikTok and YouTube Shorts via the Metricool API.

Needs env: METRICOOL_USER_TOKEN (secret), METRICOOL_USER_ID, METRICOOL_BLOG_ID.
Set METRICOOL_DRAFT=true to save posts as drafts for manual approval instead of auto-publishing.
"""
import json, os, sys, time, urllib.request

API = "https://app.metricool.com/api/v2/scheduler/posts"


def body(video_url, ep, when, tz):
    title = ep.get("yt_title") or ep["title"]
    draft = os.environ.get("METRICOOL_DRAFT", "false").lower() == "true"
    return {
        "publicationDate": {"dateTime": when, "timezone": tz},
        "text": ep["caption"],
        "providers": [{"network": n} for n in ("instagram", "facebook", "tiktok", "youtube")],
        "autoPublish": True, "draft": draft, "shortener": False, "saveExternalMediaFiles": True,
        "media": [video_url], "mediaAltText": [], "descendants": [], "firstCommentText": "",
        "hasNotReadNotes": False, "smartLinkData": {"ids": []},
        "instagramData": {"type": "REEL", "showReelOnFeed": True, "isAiGenerated": True},
        "facebookData": {"type": "REEL", "title": title[:100]},
        "tiktokData": {"privacyOption": "PUBLIC_TO_EVERYONE", "title": title[:90], "isAigc": True,
                       "disableComment": False, "disableDuet": False, "disableStitch": False, "autoAddMusic": False},
        "youtubeData": {"title": title[:100], "type": "short", "privacy": "public", "madeForKids": False,
                        "category": "EDUCATION", "tags": ["finance", "money", "personal finance", "FinanceProsTV"],
                        "isAiGeneratedContent": False},
    }


def wait_public(url, tries=30):
    for _ in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=20) as r:
                if r.status == 200: return True
        except Exception:
            pass
        time.sleep(10)
    return False


def schedule(video_url, ep, when, tz="America/New_York"):
    if not wait_public(video_url):
        raise RuntimeError(f"Video is not publicly reachable yet: {video_url}")
    uid, blog, tok = os.environ["METRICOOL_USER_ID"], os.environ["METRICOOL_BLOG_ID"], os.environ["METRICOOL_USER_TOKEN"]
    req = urllib.request.Request(f"{API}?blogId={blog}&userId={uid}", data=json.dumps(body(video_url, ep, when, tz)).encode(),
                                 headers={"Content-Type": "application/json", "X-Mc-Auth": tok}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        text = r.read().decode()
    print("Metricool:", r.status, text[:300])
    return text


if __name__ == "__main__":
    ep = json.load(open(sys.argv[1])); schedule(sys.argv[2], ep, sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "America/New_York")
