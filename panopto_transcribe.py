#!/usr/bin/env python3
"""Panopto transcript recovery: fetch stream, download video, transcribe with Whisper.

Handles Panopto videos where captions are hard-disabled ("HasCaptions": false).

Usage (run with the workspace venv python):
  python panopto_transcribe.py <input> [--cookies "name=val; name2=val2"] [--model base.en] [-o out.txt]

<input> can be:
  1. A Panopto viewer URL   (https://<host>/Panopto/Pages/Viewer.aspx?id=<deliveryId>)
     -> queries DeliveryInfo.aspx for the PodcastStreams StreamUrl (needs --cookies
        with your browser session cookies if the video requires login)
  2. A direct StreamUrl     (CloudFront/other URL ending in .mp4?...)
  3. A local .mp4 file path

If DeliveryInfo lookup fails (auth), fall back to the manual method:
  browser F12 -> Network -> filter "DeliveryInfo" -> DeliveryInfo.aspx -> Response JSON
  -> PodcastStreams -> copy StreamUrl -> re-run this script with that URL.

Output: <video-name>_transcript.txt with [timestamp] lines.
"""

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path


def get_stream_url_from_viewer(viewer_url: str, cookies: str | None) -> str:
    """Query Panopto DeliveryInfo.aspx for the PodcastStreams StreamUrl."""
    parsed = urllib.parse.urlparse(viewer_url)
    qs = urllib.parse.parse_qs(parsed.query)
    delivery_id = qs.get("id", [None])[0] or qs.get("Id", [None])[0]
    if not delivery_id:
        m = re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
                      viewer_url, re.I)
        if not m:
            sys.exit("Could not find a delivery id (GUID) in the viewer URL.")
        delivery_id = m.group(0)

    endpoint = f"{parsed.scheme}://{parsed.netloc}/Panopto/Pages/Viewer/DeliveryInfo.aspx"
    data = urllib.parse.urlencode({
        "deliveryId": delivery_id,
        "responseType": "json",
        "isLiveNotes": "false",
        "isKollectiveAgentInstalled": "false",
        "isEmbed": "false",
    }).encode()

    req = urllib.request.Request(endpoint, data=data, headers={
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        **({"Cookie": cookies} if cookies else {}),
    })
    print(f"Querying DeliveryInfo for delivery id {delivery_id} ...")
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode())

    if payload.get("ErrorCode") or payload.get("ErrorMessage"):
        sys.exit(f"DeliveryInfo error: {payload.get('ErrorMessage')}\n"
                 "Likely an auth problem — pass --cookies from your logged-in browser "
                 "session, or use the manual F12/Network method to copy StreamUrl.")

    delivery = payload.get("Delivery", {})
    streams = delivery.get("PodcastStreams") or delivery.get("Streams") or []
    for s in streams:
        url = s.get("StreamUrl")
        if url:
            print("Found StreamUrl.")
            return url
    sys.exit("No StreamUrl found in DeliveryInfo response.")


def download(url: str, dest: Path) -> Path:
    print(f"Downloading video to {dest} ...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp, open(dest, "wb") as f:
        total = int(resp.headers.get("Content-Length") or 0)
        done = 0
        while chunk := resp.read(1 << 20):
            f.write(chunk)
            done += len(chunk)
            if total:
                print(f"\r  {done / 1e6:.0f}/{total / 1e6:.0f} MB", end="", flush=True)
    print("\nDownload complete.")
    return dest


def transcribe(video: Path, out: Path, model_name: str) -> None:
    from faster_whisper import WhisperModel

    print(f"Transcribing {video.name} with faster-whisper ({model_name}, CPU int8) ...")
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(video), beam_size=5, vad_filter=True)
    print(f"Duration: {info.duration:.0f}s")
    with open(out, "w") as f:
        for seg in segments:
            line = f"[{seg.start:7.1f}s] {seg.text.strip()}"
            f.write(line + "\n")
            print(line, flush=True)
    print(f"Done -> {out}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="Panopto viewer URL, direct StreamUrl, or local .mp4 path")
    ap.add_argument("--cookies", help='Browser session cookies, e.g. ".ASPXAUTH=...; other=..."')
    ap.add_argument("--model", default="base.en", help="Whisper model (default: base.en)")
    ap.add_argument("-o", "--output", help="Transcript output path (default: <name>_transcript.txt)")
    args = ap.parse_args()

    src = args.input
    local = Path(src)
    if local.exists():
        video = local
    else:
        if "Viewer.aspx" in src or "/Panopto/" in src:
            stream_url = get_stream_url_from_viewer(src, args.cookies)
        else:
            stream_url = src  # assume direct StreamUrl
        name = Path(urllib.parse.urlparse(stream_url).path).name or "panopto_video.mp4"
        video = Path.cwd() / name
        download(stream_url, video)

    out = Path(args.output) if args.output else video.with_name(video.stem + "_transcript.txt")
    transcribe(video, out, args.model)


if __name__ == "__main__":
    main()
