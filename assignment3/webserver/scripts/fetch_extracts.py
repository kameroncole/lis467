"""Download each document linked in the IA spreadsheet (using the working replacement
from data/sources/link_replacements.json where the original link is dead) and save a
short text extract (the opening of the document) to data/sources/pdf_extracts.json.

build_documents.py uses that file, so this only needs to run when the links change.
Requires: openpyxl, requests, beautifulsoup4, and poppler's `pdftotext`.
"""
import json
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import openpyxl
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "data" / "sources" / "Information_Architecture_MOS_Ed_portal.xlsx"
OUT = ROOT / "data" / "sources" / "pdf_extracts.json"
REPLACEMENTS = ROOT / "data" / "sources" / "link_replacements.json"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}
MAX_BYTES = 40 * 1024 * 1024
EXTRACT_CHARS = 1500


def linked_documents():
    replacements = json.loads(REPLACEMENTS.read_text()) if REPLACEMENTS.exists() else {}
    ws = openpyxl.load_workbook(XLSX).active
    urls = []
    for row in ws.iter_rows(min_row=8):
        for cell in row:
            target = cell.hyperlink.target if cell.hyperlink else None
            if not (target and target.lower().split("?")[0].endswith(".pdf")):
                continue
            rep = replacements.get(target)
            if rep and rep.get("drop"):
                continue
            final = rep["url"] if rep else target
            if final not in urls:
                urls.append(final)
    return urls


def clean(text):
    text = re.sub(r"\(cid:\d+\)", " ", text)
    text = re.sub(r"[\x00-\x08\x0b-\x1f\u00ad]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def open_url(url):
    """Some hosts (e.g. fema.gov) reject browser user agents, others reject non-browser ones."""
    last = None
    for headers in (HEADERS, {"User-Agent": "curl/8.7.1"}):
        resp = requests.get(url, headers=headers, timeout=60, stream=True)
        if resp.status_code == 200:
            return resp
        last = resp
        resp.close()
    last.raise_for_status()


def extract(url):
    result = {"url": url, "status": "ok", "extract": ""}
    try:
        with open_url(url) as resp:
            data = bytearray()
            for chunk in resp.iter_content(1 << 16):
                data.extend(chunk)
                if len(data) > MAX_BYTES:
                    result["status"] = "too large"
                    return result
        if bytes(data[:1024]).lstrip().startswith(b"%PDF") or "pdf" in resp.headers.get("content-type", ""):
            with tempfile.NamedTemporaryFile(suffix=".pdf") as tmp:
                tmp.write(data)
                tmp.flush()
                out = subprocess.run(
                    ["pdftotext", "-l", "3", "-enc", "UTF-8", tmp.name, "-"],
                    capture_output=True, text=True, timeout=60,
                ).stdout
        else:
            soup = BeautifulSoup(bytes(data), "html.parser")
            for tag in soup(["script", "style", "nav", "header", "footer", "noscript"]):
                tag.decompose()
            out = soup.get_text(" ")
        text = clean(out)
        if len(text) < 80:
            result["status"] = "no text"
        result["extract"] = text[:EXTRACT_CHARS]
    except Exception as exc:  # network, HTTP, or parse failures are recorded, not fatal
        result["status"] = f"error: {type(exc).__name__}: {exc}"[:200]
    return result


def main():
    urls = linked_documents()
    print(f"Fetching {len(urls)} linked documents...")
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(extract, urls))
    OUT.write_text(json.dumps({r["url"]: r for r in results}, indent=2, ensure_ascii=False))
    bad = [r for r in results if r["status"] != "ok"]
    print(f"{len(results) - len(bad)} ok, {len(bad)} without extract")
    for r in bad:
        print("  ", r["status"], r["url"])


if __name__ == "__main__":
    main()
