# PACT — AI Workspace Framework

> **P**rojects · **A**gents · **C**ontext · **T**ools

Framework pro organizaci pracovniho prostoru pro efektivni spolupraci cloveka a AI.

---

## Jak zacit

**Otevri tuto slozku v Cursoru** a podivej se na `START-HERE.md`.

Nebo rovnou otevri chat (Cmd+L) a napis:

```
Pomoz mi nastavit PACT
```

AI te provede 6 kroky — vyplnis kdo jsi, jak pises, jake mas cile, nastavis API klice, a vytvoris si prvniho agenta. Hotovo za 10 minut.

---

## Co je PACT?

Ctyri slozky, ctyri otazky:

| Slozka | Otazka | Co tam patri |
|--------|--------|-------------|
| `0_Projects/` | CO delam? | Aktivni projekty s vystupy |
| `1_Agents/` | JAK to udelat? | Instrukce pro AI — agenti (.md) nebo skills (slozky s SKILL.md) |
| `2_Context/` | KDO jsem a co delam? | Tvoje identita, styl, expertiza, cile |
| `3_Tools/` | CIM to udelat? | Skripty, API integrace, utility |

**Proc to funguje:** AI bez kontextu generuje genericky vystup. S PACT ma AI pristup k tomu, kdo jsi, jak komunikujes a co delas — a vysledky jsou radove lepsi.

---

## Struktura

```
pact-starter/
├── START-HERE.md                  ← Zacni tady
├── AGENTS.md                      ← Agent briefing (multi-tool: Cursor, Claude Code, Codex, Cline...)
├── .cursor/rules/pact.mdc         ← Cursor pravidla (alwaysApply: true) — moderni format
├── .cursorrules                   ← Legacy fallback pro starsi Cursor (pointer na AGENTS.md)
├── 0_Projects/                    ← Tvoje projekty
│   ├── _template/                 ← Sablona noveho projektu (README, AGENTS.md, .cursor/rules)
│   └── README.md                  ← Jak zalozit novy projekt
├── 1_Agents/                      ← AI agenti a skills (13 agentu)
│   ├── AGENT-REGISTRY.md          ← Prehled vsech agentu + pravidla pro tvorbu
│   ├── RECIPES.md                 ← 7 workflow retezu (jak kombinovat agenty)
│   ├── agent-pact-bootstrap.md    ← Zaklada nove projekty z _template/
│   ├── agent-prompt-architect.md  ← Vytvari prompty a dalsi agenty
│   ├── agent-expert-panel.md      ← Simuluje diskuzi 3-5 real. expertu
│   ├── agent-deep-researcher.md   ← Hloubkovy vyzkum s citacemi
│   ├── agent-data-analyst.md      ← Analyza dat (chunking, map-reduce)
│   ├── agent-product-architect.md ← Z napadu → PRD + Developer Brief
│   ├── agent-quality-gate.md      ← PASS/FAIL kontrola vystupu
│   ├── ...a dalsi                 ← Viz AGENT-REGISTRY.md
│   └── skills/                    ← Skills (slozky s SKILL.md)
├── 2_Context/                     ← Tvuj kontext
│   ├── identity/about-me.md
│   ├── identity/tone-of-voice/
│   ├── goals/goals.md
│   └── expertise/
├── 3_Tools/                       ← Nastroje
│   ├── api/                       ← API klice + navod
│   ├── workflows/                 ← Workflow skripty (vc. generate-agents-md.py)
│   └── README.md                  ← Roadmapa nastroju
└── docs/                          ← Dokumentace
    ├── MUJ-PRVNI-AGENT.md         ← Tutorial: jak vytvorit agenta
    ├── PACT-ARCHITECTURE.md       ← Architektura systemu
    └── PACT-ZA-5-MINUT.md         ← Rychly prehled
```

---

## Principy

1. **Single Source of Truth** — kontext zije na jednom miste, agenti na nej odkazuji
2. **Agent = instrukce pro AI** — jednoduchy markdown soubor, nebo skill (slozka s SKILL.md dle [agentskills.io](https://agentskills.io))
3. **DRY** — zmena na jednom miste se projevi vsude
4. **Funguje s jakymkoliv AI** — Cursor, Claude Code, ChatGPT, Windsurf

---

## Dalsi materialy

- `AGENTS.md` — multi-tool agent briefing ([agentmd.com](https://agentmd.com) standard)
- `1_Agents/AGENT-REGISTRY.md` — prehled vsech 13 agentu s popisy
- `1_Agents/RECIPES.md` — 7 workflow retezu (jak kombinovat agenty)
- `0_Projects/README.md` — jak zalozit novy projekt (3 zpusoby)
- `3_Tools/workflows/README.md` — workflow skripty (vc. generate-agents-md.py)
- `docs/MUJ-PRVNI-AGENT.md` — tutorial: jak vytvorit vlastniho agenta za 15 minut
- `docs/PACT-ZA-5-MINUT.md` — rychly pruvodce
- `docs/PACT-ARCHITECTURE.md` — architektura frameworku
- `1_Agents/skills/README.md` — skills = strukturovane workflow (otevreny standard [agentskills.io](https://agentskills.io))
- `3_Tools/api/README.md` — navod na API klice (OpenRouter, OpenAI, Apify)
- `3_Tools/README.md` — roadmapa nastroju

---

*PACT Framework — Filip Drimalka (nowork.ai) — brezen 2026*
