#!/usr/bin/env python3
"""Build index.html: FMA Chapter 6 (Inventories) class-test guide."""
import html, json, sys
from pathlib import Path

OUT = Path(__file__).with_name("index.html")
sys.path.insert(0, str(Path(__file__).parent))
import content as C  # noqa: E402

esc = html.escape


def table(head, rows, cls="sched", num=()):
    th = "".join(f'<th class="{"n" if i in num else ""}">{h}</th>' for i, h in enumerate(head))
    trs = ""
    for r in rows:
        rcls = ""
        if isinstance(r, tuple):
            r, rcls = r
        cells = "".join(f'<td class="{"n" if i in num else ""}">{c}</td>' for i, c in enumerate(r))
        trs += f'<tr class="{rcls}">{cells}</tr>'
    return f'<div class="tablewrap"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def build():
    C.table = table
    sections = C.sections()
    nav = "".join(f'<a href="#{sid}">{esc(label)}</a>' for sid, label, _ in sections)
    body = "".join(f'<section id="{sid}">{inner}</section>' for sid, _, inner in sections)
    data = json.dumps({"mcq": C.MCQ, "blanks": C.BLANKS, "drill": C.DRILL}, ensure_ascii=False)
    page = (Path(__file__).with_name("template.html").read_text()
            .replace("{{NAV}}", nav).replace("{{BODY}}", body)
            .replace("{{DATA}}", data).replace("{{HERO}}", C.HERO))
    OUT.write_text(page)
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB, {len(sections)} sections, "
          f"{len(C.MCQ)} MCQ, {len(C.BLANKS)} blanks, {len(C.QA)} Q&A)")


if __name__ == "__main__":
    build()
