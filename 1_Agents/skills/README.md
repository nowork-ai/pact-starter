# Skills — Standardizovane workflow

> Skills jsou alternativa k jednoduchym agentum. Kde **agent = jeden markdown soubor**, **skill = slozka** s instrukcemi, skripty a referencemi.

---

## Agent vs. Skill

| | Agent | Skill |
|---|-------|-------|
| **Format** | Jeden `.md` soubor | Slozka s `SKILL.md` + dalsi soubory |
| **Kdy pouzit** | Jednoduchy ukol (napis email, zkontroluj text) | Slozitejsi workflow (vytvor web, zpracuj podcast) |
| **Slozitost** | Instrukce + kontext | Pipeline, skripty, sablony, reference |
| **Prenositelnost** | Kopiruj soubor | Kopiruj slozku |
| **Standard** | PACT konvence | [Agent Skills](https://agentskills.io) otevreny format |

**Pravidlo:** Zacni agentem. Kdyz roste slozitost, upgradni na skill.

---

## Co je Skill?

Skill je slozka obsahujici `SKILL.md` — soubor s metadaty a instrukcemi. Volitelne muze obsahovat skripty, sablony a referencni materialy.

```
1_Agents/skills/
└── muj-skill/
    ├── SKILL.md          ← Povinny: instrukce + metadata
    ├── scripts/          ← Volitelne: spustitelny kod
    ├── references/       ← Volitelne: dokumentace, priklady
    └── templates/        ← Volitelne: sablony pro vystupy
```

---

## Format SKILL.md

Kazdy skill zacina YAML frontmatter s metadaty a pokracuje markdown instrukcemi:

```markdown
---
name: nazev-skillu
description: Co skill dela. Pouzij kdyz uzivatel rekne "trigger1", "trigger2".
---

# Nazev skillu

## Kdy pouzit
Pouzij tento skill kdyz...

## Pipeline

### Krok 1: [nazev]
1. Udelej X
2. Nacti 2_Context/identity/tone-of-voice/
3. ...

### Krok 2: [nazev]
...

## Vystup
[Popis ocekavaneho vystupu]
```

### Povinne frontmatter

- `name` — kratky identifikator (kebab-case)
- `description` — kdy skill pouzit (AI cte toto pri rozhodovani)

### Volitelne frontmatter

- `version` — verze skillu
- `author` — autor
- `tools` — seznam potrebnych nastroju
- `context` — seznam potrebnych kontextovych souboru

---

## Jak skill funguje

1. **Objeveni:** AI nacte jen `name` a `description` ze vsech skills — vi co je dostupne
2. **Aktivace:** Kdyz ukol odpovida popisu, AI precte cely `SKILL.md`
3. **Provedeni:** AI nasleduje instrukce, nacita referencni soubory a spousti skripty podle potreby

Tento pristup (progressive disclosure) drzi kontext maly, dokud ho neni skutecne treba.

---

## Jak vytvorit skill

1. Vytvor slozku: `1_Agents/skills/[nazev-skillu]/`
2. Vytvor `SKILL.md` s YAML frontmatter (`name`, `description`)
3. Napis instrukce — pipeline, kroky, quality gates
4. Volitelne pridej `scripts/`, `references/`, `templates/`

---

## Priklady

| Skill | Ucel | Triggery |
|-------|------|----------|
| `content-generation/` | Tvorba obsahu (posty, emaily, newsletter) | "napis post", "newsletter", "email" |
| `web-creation/` | Tvorba webovych stranek | "vytvor web", "landing page" |
| `research-analysis/` | Hloubkova analyza a research | "analyzuj", "expert panel" |

---

## Dalsi informace

- Standard: [agentskills.io](https://agentskills.io)
- Specifikace: [agentskills.io/specification](https://agentskills.io/specification)
- Priklady skills: [github.com/anthropics/skills](https://github.com/anthropics/skills)

---

*PACT Framework — Skills nasleduji otevreny [Agent Skills](https://agentskills.io) standard.*
