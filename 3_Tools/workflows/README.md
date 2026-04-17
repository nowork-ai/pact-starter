# 3_Tools/workflows/ — Workflow skripty

> Pomocné skripty pro běžné PACT operace.

---

## `generate-agents-md.py` — Bootstrap & briefing generator

Vytváří a aktualizuje `AGENTS.md` + `.cursor/rules/parent-context.mdc` v projektech, aby agent otevřený jen v podsložce projektu znal nadřazený PACT workspace.

### Tři režimy

```bash
# 1. Vytvořit nový projekt z _template/
python3 3_Tools/workflows/generate-agents-md.py --init muj-projekt
python3 3_Tools/workflows/generate-agents-md.py --init muj-projekt \
    --title "Můj projekt 2026" \
    --desc "Pipeline pro generování XYZ z dat ABC"

# 2. Regenerovat hlavičku v existujícím projektu
#    (zachová ručně psanou sekci "📦 O tomto projektu")
python3 3_Tools/workflows/generate-agents-md.py --refresh muj-projekt

# 3. Refresh všech projektů (po úpravě _template/)
python3 3_Tools/workflows/generate-agents-md.py --refresh-all

# Bonus: výpis existujících projektů
python3 3_Tools/workflows/generate-agents-md.py --list
```

### Co se vytvoří v `0_Projects/<nazev>/`

```
0_Projects/<nazev>/
├── README.md                              ← Lidský popis projektu
├── AGENTS.md                              ← Briefing pro AI (multi-tool standard)
├── .cursor/rules/parent-context.mdc       ← Auto-aplikované Cursor pravidlo
├── inputs/
└── outputs/
```

### Idempotence

Při `--refresh` se **přepíše** auto-generovaná část `AGENTS.md`, ale obsah mezi značkami `<!-- MANUAL:START -->` a `<!-- MANUAL:END -->` (sekce „📦 O tomto projektu") **zůstane zachován**. Můžeš ji bezpečně editovat.

`.cursor/rules/parent-context.mdc` je 100% generovaný, vždy se přepíše.

### Šablona

Šablona je v `0_Projects/_template/`. Pokud chceš upravit, jak vypadají všechny budoucí projekty:

1. Edituj `0_Projects/_template/AGENTS.md` nebo `.cursor/rules/parent-context.mdc`
2. Spusť `python3 3_Tools/workflows/generate-agents-md.py --refresh-all` — propíše do všech existujících projektů
