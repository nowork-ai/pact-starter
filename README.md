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

AI te provede 5 kroky — vyplnis kdo jsi, jak pises, jake mas cile, a vytvoris si prvniho agenta. Hotovo za 10 minut.

---

## Co je PACT?

Ctyri slozky, ctyri otazky:

| Slozka | Otazka | Co tam patri |
|--------|--------|-------------|
| **Projects/** | CO delam? | Aktivni projekty s vystupy |
| **Agents/** | JAK to udelat? | Instrukce pro AI — agenti (.md) nebo skills (slozky s SKILL.md) |
| **Context/** | KDO to dela? | Tvoje identita, styl, expertiza, cile |
| **Tools/** | CIM to udelat? | Skripty, API integrace, utility |

**Proc to funguje:** AI bez kontextu generuje genericky vystup. S PACT ma AI pristup k tomu, kdo jsi, jak komunikujes a co delas — a vysledky jsou radove lepsi.

---

## Struktura

```
pact-starter/
├── START-HERE.md            ← Zacni tady
├── .cursorrules             ← Pravidla pro Cursor AI
├── Projects/                ← Tvoje projekty
├── Agents/                  ← AI agenti
│   ├── agent-prompt-architect.md
│   ├── agent-expert-panel.md
│   └── agent-quality-gate.md
├── Context/                 ← Tvuj kontext
│   ├── identity/about-me.md
│   ├── identity/tone-of-voice/
│   ├── goals/goals.md
│   └── expertise/
├── Tools/                   ← Nastroje
└── docs/                    ← Dokumentace
```

---

## Principy

1. **Single Source of Truth** — kontext zije na jednom miste, agenti na nej odkazuji
2. **Agent = instrukce pro AI** — jednoduchy markdown soubor, nebo skill (slozka s SKILL.md dle [agentskills.io](https://agentskills.io))
3. **DRY** — zmena na jednom miste se projevi vsude
4. **Funguje s jakymkoliv AI** — Cursor, Claude Code, ChatGPT, Windsurf

---

## Dalsi materialy

- `docs/PACT-ZA-5-MINUT.md` — rychly pruvodce
- `docs/PACT-ARCHITECTURE.md` — architektura frameworku
- `Agents/skills/README.md` — skills = strukturovane workflow (otevreny standard [agentskills.io](https://agentskills.io))

---

*PACT Framework — Filip Drimalka (nowork.ai) — brezen 2026*
