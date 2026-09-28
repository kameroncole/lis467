#!/usr/bin/env python3
"""Panopto transcript recovery: fetch stream, download video, transcribe with Whisper,
and export Markdown lecture notes to an Evernote .enex file.

Handles Panopto videos where captions are hard-disabled ("HasCaptions": false).

Usage (run with the workspace venv python):
  python panopto_transcribe.py <input> [--cookies "name=val; name2=val2"] [--model base.en] [-o out.txt]
  python panopto_transcribe.py notes1.md notes2.md ... --enex [-o out.enex]

<input> can be:
  1. A Panopto viewer URL   (https://<host>/Panopto/Pages/Viewer.aspx?id=<deliveryId>)
     -> queries DeliveryInfo.aspx for the PodcastStreams StreamUrl (needs --cookies
        with your browser session cookies if the video requires login)
  2. A direct StreamUrl     (CloudFront/other URL ending in .mp4?...)
  3. A local .mp4 file path
  4. One or more Markdown (.md) lecture-notes files with --enex
     -> converts each note to ENML and bundles them into a single .enex file
        you can import into Evernote (File > Import > ENEX).

If DeliveryInfo lookup fails (auth), fall back to the manual method:
  browser F12 -> Network -> filter "DeliveryInfo" -> DeliveryInfo.aspx -> Response JSON
  -> PodcastStreams -> copy StreamUrl -> re-run this script with that URL.

Output: <video-name>_transcript.txt with [timestamp] lines, or <name>.enex with --enex.
"""

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
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


# ---------------------------------------------------------------------------
# Markdown -> Evernote .enex export
# ---------------------------------------------------------------------------

# ENML allows only a subset of XHTML; these elements/attributes are banned.
_ENML_BANNED_TAGS = re.compile(
    r"</?(?:html|head|body|form|input|button|script|style|iframe|frame|frameset"
    r"|object|embed|applet|base|basefont|dir|isindex|link|map|meta|noframes"
    r"|noscript|param|textarea|select|option|label|fieldset|legend)\b[^>]*>", re.I)
_ENML_BANNED_ATTRS = re.compile(r'\s(?:id|class|onclick|ondblclick|on\w+|accesskey'
                                r'|data-\S+|dynsrc|tabindex)="[^"]*"', re.I)


def md_to_enml(md_text: str) -> str:
    """Convert Markdown to an ENML <en-note> body accepted by Evernote import."""
    import markdown

    html = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    html = _ENML_BANNED_TAGS.sub("", html)
    html = _ENML_BANNED_ATTRS.sub("", html)
    # Style tables so they render with borders in Evernote
    html = html.replace(
        "<table>",
        '<table style="border-collapse:collapse;width:100%;">')
    html = html.replace(
        "<th>", '<th style="border:1px solid #ccc;padding:4px 8px;'
                'background-color:#f0f0f0;text-align:left;">')
    html = html.replace(
        "<td>", '<td style="border:1px solid #ccc;padding:4px 8px;">')
    # Self-close void elements for XML validity
    html = re.sub(r"<(br|hr|img[^>]*)>", r"<\1/>", html)
    html = html.replace("<br/></br>", "<br/>").replace("</br>", "")
    return html


def note_title_from_md(md_path: Path, md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return md_path.stem


def export_enex(md_files: list[Path], out: Path) -> None:
    from xml.sax.saxutils import escape

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    notes_xml = []
    for md_path in md_files:
        md_text = md_path.read_text(encoding="utf-8")
        title = note_title_from_md(md_path, md_text)
        enml = md_to_enml(md_text)
        content = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">\n'
            f"<en-note>{enml}</en-note>"
        )
        notes_xml.append(
            "<note>"
            f"<title>{escape(title)}</title>"
            f"<content><![CDATA[{content}]]></content>"
            f"<created>{now}</created><updated>{now}</updated>"
            "<tag>LIS467</tag><tag>lecture-notes</tag>"
            "<note-attributes><author>panopto_transcribe.py</author>"
            "<source>markdown</source></note-attributes>"
            "</note>"
        )
        print(f"  + {md_path.name}  ->  note: {title}")

    enex = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export4.dtd">\n'
        f'<en-export export-date="{now}" application="panopto_transcribe.py" version="1.0">'
        + "".join(notes_xml) + "</en-export>\n"
    )
    out.write_text(enex, encoding="utf-8")
    print(f"Done -> {out}  ({len(md_files)} note(s); import via Evernote File > Import > ENEX)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", nargs="+",
                    help="Panopto viewer URL, direct StreamUrl, local .mp4 path, "
                         "or one or more .md files with --enex")
    ap.add_argument("--cookies", help='Browser session cookies, e.g. ".ASPXAUTH=...; other=..."')
    ap.add_argument("--model", default="base.en", help="Whisper model (default: base.en)")
    ap.add_argument("--enex", action="store_true",
                    help="Treat inputs as Markdown notes and export an Evernote .enex file")
    ap.add_argument("-o", "--output",
                    help="Output path (default: <name>_transcript.txt, or <name>.enex with --enex)")
    args = ap.parse_args()

    if args.enex:
        md_files = [Path(p) for p in args.input]
        missing = [p for p in md_files if not p.exists()]
        if missing:
            sys.exit(f"Markdown file(s) not found: {', '.join(map(str, missing))}")
        out = Path(args.output) if args.output else (
            md_files[0].with_suffix(".enex") if len(md_files) == 1
            else md_files[0].parent / "lecture_notes.enex")
        export_enex(md_files, out)
        return

    src = args.input[0]
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
