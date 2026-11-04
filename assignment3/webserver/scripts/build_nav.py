#!/usr/bin/env python3
"""Build the site navigation from the Information Architecture spreadsheet.

Reads Information_Architecture_MOS_Ed_portal.xlsx (Level 1 persona nav through
Level 5 direct link, plus URL Path) and replaces the block between
<!-- NAV:START --> and <!-- NAV:END --> in each HTML page with generated markup.

Requires: pip install openpyxl

Usage:
    python3 build_nav.py                       # default xlsx, pages in ../public, depth 4
    python3 build_nav.py --depth 3             # persona > main nav > dropdown only
    python3 build_nav.py --dry-run             # print the nav HTML, change nothing
    python3 build_nav.py --xlsx IA.xlsx --pages ../public/index.html
"""
import argparse
import re
import sys
from html import escape
from pathlib import Path

import openpyxl

ASSIGNMENT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_XLSX = ASSIGNMENT_DIR / "Information_Architecture_MOS_Ed_portal.xlsx"
DEFAULT_PAGES = [
    ASSIGNMENT_DIR / "webserver/public/index.html",
    ASSIGNMENT_DIR / "webserver/public/search-results.html",
]

# Left-to-right order from the wireframe; the spreadsheet lists Educators before Parents.
PERSONA_ORDER = ["Students", "Parents", "Educators", "About"]
# Top-bar labels from the wireframe; the spreadsheet uses the bare persona names.
PERSONA_LABELS = {"Students": "For Students", "Parents": "For Parents", "Educators": "For Educators"}
LOGO_HTML = (
    '<a class="logo" href="index.html">'
    '<img src="images/logo.png" alt="ACI Inc. logo - back to dashboard"></a>'
)
START, END = "<!-- NAV:START -->", "<!-- NAV:END -->"


class Node:
    def __init__(self, label):
        self.label = label
        self.children = {}
        self.urls = []

    def child(self, label):
        return self.children.setdefault(label, Node(label))

    @property
    def href(self):
        """One shared URL becomes the link target; several (a category) stays '#'."""
        unique = list(dict.fromkeys(self.urls))
        return unique[0] if len(unique) == 1 and not self.children else "#"


def clean(value):
    return str(value).strip() if value is not None and str(value).strip() else None


def read_tree(xlsx_path):
    ws = openpyxl.load_workbook(xlsx_path, read_only=True).active
    rows = list(ws.iter_rows(values_only=True))
    header = next(
        (i for i, r in enumerate(rows) if r and str(r[0] or "").startswith("Level 1")), None
    )
    if header is None:
        sys.exit("Could not find the 'Level 1 (Persona Nav)' header row in the spreadsheet.")

    root = Node("root")
    for row in rows[header + 1:]:
        levels = [clean(c) for c in row[:5]]
        url = clean(row[5]) if len(row) > 5 else None
        if not levels[0] or levels[0] not in PERSONA_ORDER:
            continue
        node = root
        for label in levels:
            if not label:
                break
            node = node.child(label)
        if url:
            node.urls.append(url)
    return root


def make_href(url):
    """Internal sheet paths like /exhibits/# become relative so they work under ~user/."""
    if url.startswith(("http://", "https://", "#")):
        return url
    return url.lstrip("/")


def render_item(node, depth, max_depth):
    kids = list(node.children.values()) if depth < max_depth else []
    href = make_href(node.href)
    attrs = f'href="{escape(href)}"'
    if href.startswith("http"):
        attrs += ' target="_blank" rel="noopener"'
    link = f"<a {attrs}>{escape(node.label)}</a>"
    if not kids:
        return f"<li>{link}</li>"
    return f'<li class="has-sub">{link}{render_list(kids, depth + 1, max_depth)}</li>'


def render_list(nodes, depth, max_depth):
    # Leaf-only menus can be long (26 exhibits), so they scroll; menus that hold
    # flyouts must not scroll or the flyouts would be clipped.
    leaf_only = all(not n.children or depth >= max_depth for n in nodes)
    cls = "sub menu-scroll" if leaf_only else "sub"
    items = "\n".join(render_item(n, depth, max_depth) for n in nodes)
    return f'<ul class="{cls}">\n{items}\n</ul>'


def render_nav(root, max_depth):
    top = []
    for name in PERSONA_ORDER:
        persona = root.children.get(name)
        if not persona:
            continue
        # A persona with a same-named child (About > About) links straight to that page.
        own = persona.children.get(name)
        if own and not own.children:
            persona_href = own.href
            del persona.children[name]
        else:
            persona_href = "#"
        kids = list(persona.children.values())
        link_attrs = f'href="{escape(make_href(persona_href))}"'
        link = f"<a {link_attrs}>{escape(PERSONA_LABELS.get(name, name))}</a>"
        if kids and max_depth > 1:
            top.append(
                f'<li class="has-sub">{link}{render_list(kids, 2, max_depth)}</li>'
            )
        else:
            top.append(f"<li>{link}</li>")
    body = "\n".join(top)
    return (
        f"{START}\n"
        f'<nav class="site-nav" aria-label="Main">\n{LOGO_HTML}\n'
        f'<ul class="nav-list">\n{body}\n</ul>\n</nav>\n'
        f"{END}"
    )


def inject(page, nav_html):
    text = page.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit(f"{page}: missing {START} ... {END} markers.")
    page.write_text(pattern.sub(lambda _m: nav_html, text, count=1), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--xlsx", type=Path, default=DEFAULT_XLSX)
    ap.add_argument("--pages", type=Path, nargs="+", default=DEFAULT_PAGES)
    ap.add_argument("--depth", type=int, default=4, help="levels to show: 2=persona>main nav, 3=+dropdown, 4=+category/link (default), 5=all")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    # Level 1 is the persona itself, so depth counts from 1.
    nav_html = render_nav(read_tree(args.xlsx), args.depth)
    if args.dry_run:
        print(nav_html)
        return
    for page in args.pages:
        inject(page, nav_html)
        print(f"updated {page}")


if __name__ == "__main__":
    main()
