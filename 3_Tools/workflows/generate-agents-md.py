#!/usr/bin/env python3
"""
generate-agents-md.py — PACT project bootstrap & briefing generator
====================================================================

Tři režimy:

1. **--init <name>** — vytvoří nový projekt v `0_Projects/<name>/` zkopírováním
   `0_Projects/_template/` a vyplněním placeholderů ({{PROJECT_NAME}},
   {{PROJECT_TITLE}}, {{PROJECT_DESCRIPTION}}, {{DATE}}).

2. **--refresh <name>** — regeneruje hlavičku `AGENTS.md` a
   `.cursor/rules/parent-context.mdc` v existujícím projektu ze šablony.
   Sekce mezi <!-- MANUAL:START --> a <!-- MANUAL:END --> v `AGENTS.md`
   zůstává zachována.

3. **--refresh-all** — totéž pro všechny projekty v `0_Projects/`
   (kromě `_template/` a skrytých složek).

Použití:

    python3 3_Tools/workflows/generate-agents-md.py --init muj-projekt
    python3 3_Tools/workflows/generate-agents-md.py --init muj-projekt --title "Můj projekt" --desc "Co dělá"
    python3 3_Tools/workflows/generate-agents-md.py --refresh muj-projekt
    python3 3_Tools/workflows/generate-agents-md.py --refresh-all
    python3 3_Tools/workflows/generate-agents-md.py --list
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
PROJECTS_DIR = WORKSPACE_ROOT / "0_Projects"
TEMPLATE_DIR = PROJECTS_DIR / "_template"

PLACEHOLDERS = ("{{PROJECT_NAME}}", "{{PROJECT_TITLE}}", "{{PROJECT_DESCRIPTION}}", "{{DATE}}")

MANUAL_RE = re.compile(
    r"<!-- MANUAL:START.*?-->(?P<body>.*?)<!-- MANUAL:END -->",
    re.DOTALL,
)

SKIP_NAMES = {"_template", "archive"}


def humanize(name: str) -> str:
    return name.replace("-", " ").replace("_", " ").title()


def fill_placeholders(text: str, name: str, title: str, description: str) -> str:
    return (
        text.replace("{{PROJECT_NAME}}", name)
            .replace("{{PROJECT_TITLE}}", title)
            .replace("{{PROJECT_DESCRIPTION}}", description)
            .replace("{{DATE}}", date.today().isoformat())
    )


def extract_manual_block(path: Path) -> str | None:
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8", errors="ignore")
    m = MANUAL_RE.search(content)
    return m.group("body").strip() if m else None


def replace_manual_block(text: str, manual_body: str) -> str:
    """Replace whatever is between MANUAL:START..MANUAL:END with manual_body."""
    def _sub(m: re.Match[str]) -> str:
        start = m.group(0).split("-->", 1)[0] + "-->"
        return f"{start}\n{manual_body}\n<!-- MANUAL:END -->"
    return MANUAL_RE.sub(_sub, text, count=1)


def init_project(name: str, title: str | None, description: str | None, force: bool) -> int:
    if not TEMPLATE_DIR.is_dir():
        print(f"❌ Šablona neexistuje: {TEMPLATE_DIR}", file=sys.stderr)
        return 1
    target = PROJECTS_DIR / name
    if target.exists() and not force:
        print(f"❌ Projekt už existuje: {target}\n   Použij --force pro přepsání nebo --refresh pro update hlavičky.", file=sys.stderr)
        return 1
    title = title or humanize(name)
    description = description or "_TODO: Doplň krátký popis projektu (1–2 věty)._"

    if target.exists() and force:
        shutil.rmtree(target)
    shutil.copytree(TEMPLATE_DIR, target)

    for path in target.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(ph in text for ph in PLACEHOLDERS):
            path.write_text(fill_placeholders(text, name, title, description), encoding="utf-8")

    print(f"✅ Vytvořen projekt: {target.relative_to(WORKSPACE_ROOT)}")
    print(f"   • README.md")
    print(f"   • AGENTS.md (briefing pro AI)")
    print(f"   • .cursor/rules/parent-context.mdc (auto-apply)")
    print(f"   • inputs/  outputs/")
    print(f"\n💡 Otevři projekt v Cursoru a začni: `cd 0_Projects/{name}`")
    return 0


def refresh_project(name: str) -> dict:
    project_dir = PROJECTS_DIR / name
    if not project_dir.is_dir():
        return {"name": name, "status": "MISSING"}
    title = humanize(name)

    # Refresh AGENTS.md
    target_agents = project_dir / "AGENTS.md"
    template_agents = TEMPLATE_DIR / "AGENTS.md"
    if not template_agents.exists():
        return {"name": name, "status": "NO_TEMPLATE"}
    new_agents_text = fill_placeholders(
        template_agents.read_text(encoding="utf-8"),
        name=name,
        title=title,
        description="_TODO: Doplň krátký popis projektu._",
    )
    manual = extract_manual_block(target_agents)
    if manual:
        new_agents_text = replace_manual_block(new_agents_text, manual)
    target_agents.write_text(new_agents_text, encoding="utf-8")

    # Refresh parent-context.mdc
    target_rule = project_dir / ".cursor" / "rules" / "parent-context.mdc"
    template_rule = TEMPLATE_DIR / ".cursor" / "rules" / "parent-context.mdc"
    if template_rule.exists():
        target_rule.parent.mkdir(parents=True, exist_ok=True)
        target_rule.write_text(
            fill_placeholders(template_rule.read_text(encoding="utf-8"), name, title, ""),
            encoding="utf-8",
        )

    return {"name": name, "status": "OK"}


def list_projects() -> list[str]:
    if not PROJECTS_DIR.is_dir():
        return []
    return sorted(
        d.name
        for d in PROJECTS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".") and d.name not in SKIP_NAMES
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=False)
    mode.add_argument("--init", metavar="NAME", help="Vytvořit nový projekt z _template/")
    mode.add_argument("--refresh", metavar="NAME", help="Regenerovat hlavičku v existujícím projektu")
    mode.add_argument("--refresh-all", action="store_true", help="Refresh všechny projekty")
    mode.add_argument("--list", action="store_true", help="Vypsat existující projekty")

    parser.add_argument("--title", help="Lidsky čitelný název projektu (default: humanizováno z NAME)")
    parser.add_argument("--desc", help="Krátký popis projektu (1–2 věty)")
    parser.add_argument("--force", action="store_true", help="Přepsat existující projekt při --init")
    args = parser.parse_args()

    if args.list:
        for n in list_projects():
            print(n)
        return 0

    if args.init:
        return init_project(args.init, args.title, args.desc, args.force)

    if args.refresh:
        result = refresh_project(args.refresh)
        if result["status"] == "MISSING":
            print(f"❌ Projekt neexistuje: {args.refresh}", file=sys.stderr)
            return 1
        if result["status"] == "NO_TEMPLATE":
            print(f"❌ Chybí šablona v {TEMPLATE_DIR}", file=sys.stderr)
            return 1
        print(f"✅ Refreshed: {args.refresh}")
        return 0

    if args.refresh_all:
        names = list_projects()
        results = [refresh_project(n) for n in names]
        ok = sum(1 for r in results if r["status"] == "OK")
        print(f"✅ Refreshed {ok}/{len(results)} projektů:")
        for r in results:
            mark = "✅" if r["status"] == "OK" else "⚠️ "
            print(f"  {mark} {r['name']:30s} {r['status']}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
