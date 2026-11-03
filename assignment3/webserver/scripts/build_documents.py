"""Build data/documents.json for the Museum of Science education portal search.

Inputs (all in data/sources/):
  - Youth Engineering Solutions (YES) Curricula List.md
  - Museum of Science Exhibits to YES Curricula and MA STE Standards Alignment.md
  - Massachusetts STE Standards & YES Curricula Alignment.md
  - Pre-K through Grade 8 STEM Research Documents Directory.md  (titles of the linked documents)
  - Information_Architecture_MOS_Ed_portal.xlsx                  (the linked documents + categories)
  - site_links.json + site_pages.json                            (real mos.org / yes.mos.org / DESE page for each
                                                                  YES unit, exhibit and standard, with its official
                                                                  description; made by fetch_site_pages.py)
  - link_replacements.json                                       (working URL for each dead original link)
  - pdf_extracts.json (optional, from fetch_extracts.py)         (opening text of each linked document)

Each document has: id, type, title, category, text, url (+ link_status for research documents).
`title`, `category` and `text` are what the vector-search demo embeds and displays.
"""
import json
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "sources"
OUT = ROOT / "data" / "documents.json"

YES_MD = SRC / "Youth Engineering Solutions (YES) Curricula List.md"
EXHIBITS_MD = SRC / "Museum of Science Exhibits to YES Curricula and MA STE Standards Alignment.md"
STANDARDS_MD = SRC / "Massachusetts STE Standards & YES Curricula Alignment.md"
DIRECTORY_MD = SRC / "Pre-K through Grade 8 STEM Research Documents Directory.md"
XLSX = SRC / "Information_Architecture_MOS_Ed_portal.xlsx"
EXTRACTS = SRC / "pdf_extracts.json"
REPLACEMENTS = SRC / "link_replacements.json"
SITE_LINKS = SRC / "site_links.json"
SITE_PAGES = SRC / "site_pages.json"

STOP_WORDS = {"engineering", "eie", "wee", "engineer", "a", "an", "units", "unit", "module", "yes", "cs"}


def strip_md(text):
    text = re.sub(r"\[<u>(.*?)</u>\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[(.*?)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"</?u>", "", text)
    text = text.replace("\\|", "|").replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", text).strip()


def table_rows(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or re.match(r"^\|[-\s|]+\|$", line):
            continue
        cells = [strip_md(c) for c in re.split(r"(?<!\\)\|", line.strip()[1:-1])]
        rows.append(cells)
    return rows[1:]  # drop header row


def norm(name):
    name = re.sub(r"\(.*?\)", " ", name.lower())
    words = re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
    return " ".join(w for w in words if w not in STOP_WORDS)


def activity_names(text):
    """Split an 'activity' cell like 'Wee Engineer Units (A, B) / Engineering C' into normalized names."""
    names = []
    for inner in re.findall(r"\(([^)]*,[^)]*)\)", text):
        names += [norm(p) for p in inner.split(",")]
    outer = re.sub(r"\([^)]*,[^)]*\)", " ", text)
    names += [norm(p) for p in re.split(r"[/,]", outer)]
    return [n for n in names if n]


def matches(unit_norm, names):
    return any(unit_norm == n or (len(n) >= 4 and unit_norm.endswith(" " + n)) for n in names)


def ste_code(cell):
    return re.sub(r"^MA\s+", "", cell).strip()


def parse_yes():
    sections, cur = [], None
    for raw in YES_MD.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        m = re.match(r"^## \d+\.\s*(.+)$", line)
        if m:
            cur = {"name": strip_md(m.group(1)), "desc": "", "units": []}
            sections.append(cur)
        elif cur is None or not line or line.startswith("# "):
            continue
        elif line.startswith("- "):
            cur["units"].append({"name": strip_md(line[2:]), "grade": ""})
        elif line.startswith("|"):
            cells = [strip_md(c) for c in line.strip("|").split("|")]
            if cells[0] not in ("Unit Title",) and not set(cells[0]) <= set("-"):
                cur["units"].append({"name": cells[0], "grade": cells[1]})
        else:
            cur["desc"] = (cur["desc"] + " " + strip_md(line)).strip()
    return sections


def bullets(path, heading):
    out, on = [], False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            on = heading in line
        elif on and line.startswith("- "):
            out.append(strip_md(line[2:]))
    return out


def parse_directory():
    docs, section = [], ""
    for line in DIRECTORY_MD.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## \d+\.\s*(.+)$", line)
        if m:
            section = m.group(1).strip()
            continue
        m = re.match(r"^\d+\.\s+\[<u>(.*?)</u>\]\((.*?)\)", line)
        if m:
            docs.append({"title": m.group(1).strip(), "url": m.group(2).strip(), "section": section})
    return docs


def xlsx_categories():
    """url -> category (Level 4 in the IA spreadsheet) for every linked document."""
    cats = {}
    ws = openpyxl.load_workbook(XLSX).active
    for row in ws.iter_rows(min_row=8):
        for cell in row:
            target = cell.hyperlink.target if cell.hyperlink else None
            if target and target.lower().split("?")[0].endswith(".pdf"):
                cats.setdefault(target, row[3].value)
    return cats


def official_description(pages, url):
    page = pages.get(url, {})
    return page.get("description") or ""


def main():
    docs = []
    links = json.loads(SITE_LINKS.read_text())
    pages = json.loads(SITE_PAGES.read_text())
    STE_URL = links["ste_standards"]
    yes_sections = parse_yes()
    exhibit_rows = table_rows(EXHIBITS_MD)  # name, activity, standard, rationale
    standard_rows = table_rows(STANDARDS_MD)  # category, activity, standard, description

    exhibits = [
        {"name": r[0], "activity": r[1], "code": ste_code(r[2]), "why": r[3], "names": activity_names(r[1])}
        for r in exhibit_rows
    ]
    standards = [
        {"category": r[0], "activity": r[1], "code": ste_code(r[2]), "desc": r[3], "names": activity_names(r[1])}
        for r in standard_rows
    ]

    # --- YES curriculum units (and one overview per YES section) -----------------------------
    n = 0
    unit_url = {}
    for sec in yes_sections:
        unit_list = ", ".join(u["name"] for u in sec["units"])
        n += 1
        docs.append({
            "id": f"yes-{n:03d}", "type": "yes-overview", "title": f"YES: {sec['name']}",
            "category": "YES Curriculum Overview",
            "text": f"{sec['desc']} Units: {unit_list}.", "url": links["yes_sections"][sec["name"]],
        })
        for unit in sec["units"]:
            n += 1
            un = norm(unit["name"])
            url = links["yes_units"][unit["name"]]
            unit_url[un] = url
            parts = [f"{unit['name']} is a {sec['name']} unit from the Museum of Science, Boston."]
            official = official_description(pages, url)
            if official:
                parts.append(official)
            if unit["grade"]:
                parts.append(f"Grade band: {unit['grade']}.")
            matched_standards = [s for s in standards if matches(un, s["names"])]
            matched_exhibits = [e for e in exhibits if matches(un, e["names"])]
            for s in matched_standards:
                parts.append(f"Aligned MA STE standard {s['code']}: {s['desc']}")
            if not matched_standards and matched_exhibits:
                codes = sorted({e["code"] for e in matched_exhibits})
                parts.append("Aligned MA STE standard(s) via related exhibits: " + ", ".join(codes) + ".")
            if matched_exhibits:
                parts.append("Related museum exhibits: " + ", ".join(e["name"] for e in matched_exhibits) + ".")
            docs.append({
                "id": f"yes-{n:03d}", "type": "yes-unit", "title": unit["name"],
                "category": f"YES - {sec['name']}", "text": " ".join(parts), "url": url,
            })
    for title, url in links["yes_careers"].items():
        n += 1
        docs.append({
            "id": f"yes-{n:03d}", "type": "yes-unit", "title": title,
            "category": "YES - Career Explorations",
            "text": f"{title} is a YES Career Exploration from the Museum of Science, Boston. "
                    f"{official_description(pages, url)}",
            "url": url,
        })

    # --- Museum exhibits -------------------------------------------------------------------
    for i, e in enumerate(exhibits, 1):
        gap = e["activity"].lower().startswith("curriculum gap")
        yes_part = (
            "No matching YES activity (a curriculum gap), but it aligns with MA STE content standards."
            if gap else f"Matched YES learning activity: {e['activity']}."
        )
        url = links["exhibits"][e["name"]]
        parts = [f"{e['name']} is an exhibit at the Museum of Science, Boston. {e['why']}"]
        official = official_description(pages, url)
        if official and url != links["exhibits_listing"]:
            parts.append(f"From the Museum of Science website: {official}")
        parts += [yes_part, f"Primary MA STE standard: {e['code']}."]
        docs.append({
            "id": f"exh-{i:03d}", "type": "exhibit", "title": e["name"],
            "category": "Museum of Science Exhibit", "text": " ".join(parts), "url": url,
        })

    # --- Massachusetts STE standards -------------------------------------------------------
    objectives = bullets(STANDARDS_MD, "Framework Objectives")
    docs.append({
        "id": "ste-000", "type": "ste-overview", "title": "Massachusetts STE Curriculum Framework objectives",
        "category": "MA STE Standards", "text": " ".join(objectives), "url": STE_URL,
    })
    for i, s in enumerate(standards, 1):
        related = [e["name"] for e in exhibits if s["code"] and e["code"] in s["code"]]
        text = f"{s['desc']} Curriculum category: {s['category']}. YES unit(s): {s['activity']}."
        if related:
            text += " Museum exhibits with this standard: " + ", ".join(related) + "."
        related_units = sorted({unit_url[k] for k in unit_url if matches(k, s["names"])})
        doc = {
            "id": f"ste-{i:03d}", "type": "ste-standard", "title": f"MA STE {s['code']} - {s['activity']}",
            "category": f"MA STE Standards - {s['category']}", "text": text, "url": STE_URL,
        }
        if related_units:
            doc["related_urls"] = related_units
        docs.append(doc)

    # --- Linked STEM research documents ----------------------------------------------------
    extracts = json.loads(EXTRACTS.read_text()) if EXTRACTS.exists() else {}
    replacements = json.loads(REPLACEMENTS.read_text()) if REPLACEMENTS.exists() else {}
    cats = xlsx_categories()
    skipped = []
    i = 0
    for d in parse_directory():
        rep = replacements.get(d["url"])
        if rep and rep.get("drop"):
            skipped.append(d["title"])
            continue
        category = cats.get(d["url"]) or d["section"]
        if rep:
            url, publisher, kind = rep["url"], rep["publisher"], rep["kind"]
            title = rep["title"] if rep["title"].startswith(publisher) else f"{publisher} - {rep['title']}"
        else:
            url, kind = d["url"], "pdf"
            publisher, _, _ = d["title"].partition(" - ")
            title = d["title"]
        info = extracts.get(url, {})
        if info.get("status") not in ("ok", "no text"):  # "no text" = valid scanned PDF
            skipped.append(title)  # dead or unreachable links are left out of the index
            continue
        i += 1
        text = (f"{title}. A curated STEM {'research document' if kind == 'pdf' else 'resource page'} from "
                f"{publisher} on {category}, for Pre-K through Grade 8 learners and educators, aligned with "
                f"YES activities, Museum of Science exhibits and Massachusetts STE standards.")
        if info.get("extract"):
            text += " Opening text: " + info["extract"][:700]
        docs.append({
            "id": f"doc-{i:03d}", "type": "research-document", "title": title,
            "category": f"STEM Research Documents - {category}", "text": text, "url": url,
            "format": kind, "link_status": "ok",
        })
    if skipped:
        print(f"Left out {len(skipped)} research documents without a working, readable link:")
        for t in skipped:
            print("  -", t)

    OUT.write_text(json.dumps(docs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    by_type = {}
    for d in docs:
        by_type[d["type"]] = by_type.get(d["type"], 0) + 1
    print(f"Wrote {len(docs)} documents to {OUT}")
    print(by_type)


if __name__ == "__main__":
    main()
