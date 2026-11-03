"""Fetch every page listed in data/sources/site_links.json (mos.org, yes.mos.org, DESE) and
save its title, meta description and opening text to data/sources/site_pages.json.

build_documents.py uses that file so each YES unit / exhibit document carries the official
description from its real page. Exits non-zero if any link does not return HTTP 200.
Requires: requests, beautifulsoup4.
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
LINKS = ROOT / "data" / "sources" / "site_links.json"
OUT = ROOT / "data" / "sources" / "site_pages.json"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}


def all_urls(links):
    urls = set()
    for value in links.values():
        urls.update(value.values() if isinstance(value, dict) else [value])
    return sorted(urls)


def fetch(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=45)
    except requests.RequestException as exc:
        return {"url": url, "status": f"error: {exc}"[:150]}
    soup = BeautifulSoup(resp.text, "html.parser")
    og = soup.find("meta", property="og:title")
    title = (og.get("content") if og else None) or (soup.title.string if soup.title else "") or ""
    meta = soup.find("meta", attrs={"name": "description"})
    description = (meta.get("content") if meta else "") or ""
    main = soup.find("main") or soup
    for tag in main(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
    body = " ".join(main.get_text(" ").split())
    return {
        "url": url, "status": resp.status_code, "title": title.strip(),
        "description": description.strip(), "body": body[:1500],
    }


def main():
    urls = all_urls(json.loads(LINKS.read_text()))
    print(f"Checking {len(urls)} pages...")
    with ThreadPoolExecutor(max_workers=8) as pool:
        pages = list(pool.map(fetch, urls))
    OUT.write_text(json.dumps({p["url"]: p for p in pages}, indent=1, ensure_ascii=False))
    bad = [p for p in pages if p["status"] != 200]
    print(f"{len(pages) - len(bad)} ok, {len(bad)} failing")
    for p in bad:
        print("  ", p["status"], p["url"])
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
