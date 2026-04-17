# Agent Registry

> Prehled vsech agentu v PACT systemu. Kazdy agent je markdown soubor s instrukcemi pro AI.

---

## Jak agenty pouzivat

### V Cursoru
```
Pouzij @agent-prompt-architect.md a vytvor prompt pro [ukol]
```

### V Claude Code
```
Precti 1_Agents/agent-expert-panel.md a ridis se instrukcemi. Tema: [tema]
```

### Obecne
Staci AI rict: **"Pouzij agenta [nazev]"** a ukazu na soubor. AI si precte instrukce a ridí se jimi.

---

## Prehled agentu

### Tvorba a prompty

| Agent | Co dela | Kdy pouzit |
|-------|---------|------------|
| **[agent-prompt-architect.md](agent-prompt-architect.md)** | Transformuje vagne pozadavky na precizni, strukturovane prompty pro LLM | Kdyz potrebujes kvalitni prompt pro jakekoliv AI — od chat promptu po system prompty pro agenty |
| **[agent-skill-builder.md](agent-skill-builder.md)** | Vytvari strukturovane Skills (SKILL.md) pro Claude Code, Cursor i PACT | Kdyz chces vytvorit opakovatelny workflow jako skill — "vytvor skill", "novy skill" |
| **[agent-knowledge-extractor.md](agent-knowledge-extractor.md)** | Extrahuje znalosti z research dokumentu a transformuje je do agent promptu | Kdyz mas 5-50 clanku/dokumentu na tema a chces z nich vytvorit specializovaneho agenta |

### Analyza a vyzkum

| Agent | Co dela | Kdy pouzit |
|-------|---------|------------|
| **[agent-expert-panel.md](agent-expert-panel.md)** | Simuluje diskuzi 3-5 realnch expertu na jakekoliv tema — generuje prulomove insighty | Kdyz resis slozity problem, ktery benefituje z vice uhlu pohledu — strategie, rozhodnuti, kreativni vyzvy |
| **[agent-deep-researcher.md](agent-deep-researcher.md)** | Provadi hloubkovy vyzkum s citacemi a zdroji pomoci AI vyzkumnych nastroju | Kdyz potrebujes evidence-based report — trh, konkurence, technologie, trendy |
| **[agent-data-analyst.md](agent-data-analyst.md)** | Analyzuje velka data — dokumenty, tabulky, prepisy — s chunkingem a map-reduce | Kdyz mas velke mnozstvi dat a chces z nich strukturovane, actionable vystupy |
| **[agent-personal-voice-analyst.md](agent-personal-voice-analyst.md)** | Analyzuje komunikacni styl z textu — tone of voice, frameworky, shareable content | Kdyz chces poznat svuj komunikacni styl, extrahovat insighty z konverzaci, najit obsah pro social media |

### Projektove nastroje

| Agent | Co dela | Kdy pouzit |
|-------|---------|------------|
| **[agent-pact-bootstrap.md](agent-pact-bootstrap.md)** | Zaklada novy projekt v `0_Projects/` z `_template/` — vcetne `AGENTS.md` a `.cursor/rules/parent-context.mdc` aby agent fungoval i kdyz user otevre jen tu podslozku | Kdyz user rekne "zaloz projekt", "novy projekt", "vytvor projekt" |
| **[agent-product-architect.md](agent-product-architect.md)** | Transformuje vagne napady na kompletni PRD + Developer Brief | Kdyz mas napad na produkt a chces z nej udelat specifikaci pripravenou pro vyvojare |
| **[agent-context-builder.md](agent-context-builder.md)** | Prozkouma projektovou slozku a vytvori strukturovany kontextovy dokument | Kdyz mas slozku plnou souboru a chces z ni jeden uceleny dokument pro dalsi praci |
| **[agent-quality-gate.md](agent-quality-gate.md)** | Finalni kontrola vystupu — text, kod, design — s verdiktem PASS/FAIL | Na konci kazdeho workflow — kdyz chces nezavisly review vystupu pred odevzdanim |

### Utility

| Agent | Co dela | Kdy pouzit |
|-------|---------|------------|
| **[agent-markdown-to-html.md](agent-markdown-to-html.md)** | Konvertuje Markdown na krasny, self-contained HTML s change trackingem | Kdyz chces z markdown dokumentu udelat publikovatelny HTML — s oznacenim novych/zmenenych casti |
| **[agent-claude-code-guide.md](agent-claude-code-guide.md)** | Osobni pruvodce Claude Code — instalace, nastaveni, prikazy, troubleshooting | Kdyz se chces naucit Claude Code nebo resis konkretni problem s nastrojem |

---

## Skills (slozky)

Skills jsou alternativa k jednoduchym agentum. Kde **agent = jeden markdown soubor**, **skill = slozka** s instrukcemi, skripty a referencemi.

| Skill | Co dela | Kde |
|-------|---------|-----|
| **content-review** | Kontrola textu — tone of voice, srozumitelnost, kvalita | `skills/content-review/SKILL.md` |

Vice o skills: viz [skills/README.md](skills/README.md)

---

## Jak agenti spolupracuji

```
agent-context-builder        → vytvori kontext z projektove slozky
       ↓
agent-product-architect      → z kontextu vytvori PRD
       ↓
agent-prompt-architect       → vytvori prompty pro implementaci
       ↓
agent-quality-gate           → zkontroluje finalni vystup
```

```
agent-deep-researcher        → vyzkum na tema
       ↓
agent-knowledge-extractor    → extrahuje znalosti do struktury
       ↓
agent-prompt-architect       → vytvori agenta ze znalosti
       ↓
agent-skill-builder          → zabali workflow jako skill
```

```
agent-personal-voice-analyst → analyzuje komunikacni styl
       ↓
agent-expert-panel          → diskuze expertu o strategii
       ↓
agent-product-architect     → specifikace produktu
```

---

## Pravidla pro vytvareni novych agentu

### Struktura

Kazdy agent ma tento zakladni format:

```markdown
# [Nazev agenta]

> Jednoveta popis — co agent dela a kdy ho pouzit.

---

## Role a identita
[Kdo agent je, jaka ma expertiza, jaky je jeho pristup]

## Co delam
[Seznam schopnosti a use cases]

## Workflow / Jak pracuji
[Krok za krokem — jak agent postupuje]

## Vystupni format
[Presna specifikace vystupu — sablona nebo popis]

## Pravidla
### VZDY: [co delat]
### NIKDY: [co nedelat]

## Priklady
[Minimalne 1 konkretni priklad vstup → vystup]

## Language handling
- Input in Czech → Output in Czech
- Input in English → Output in English
```

### Pojmenovani

- Format: `agent-[nazev-kebab-case].md`
- Nazev je popisny: `agent-data-analyst.md`, ne `agent-da.md`
- Vzdy v anglictine (i pro ceske agenty)

### Kvalitativni standardy

| Check | Otazka |
|-------|--------|
| **Specificky** | Ma kazde pravidlo konkretni priklad? |
| **Actionable** | Vi agent presne co delat v kazde situaci? |
| **Kompletni** | Pokryva 80% ocekavanych use cases? |
| **Strucny** | Lze neco smazat bez ztraty hodnoty? |
| **No-BS test** | Jsou tam generic fraze typu "bud uzitecny"? (→ smazat) |

### Anti-patterns

| Spatne | Spravne |
|--------|---------|
| "Jsi expert na vsechno" | "Jsi senior data analyst se specializaci na..." |
| "Bud uzitecny a kvalitni" | Konkretni checklist co = kvalitni |
| Zadne priklady | Minimalne 1 vstup → vystup |
| "Muzes pouzit ruzne pristupy" | IF-THEN rozhodovaci pravidla |
| 1000+ radku bez struktury | Pod 500 radku, detaily v references/ |

### Registrace

Po vytvoreni noveho agenta:
1. Pridej radek do prislusne tabulky v tomto souboru
2. (Volitelne) Pridej trigger do `.cursorrules`

---

## Statistiky

| Metrika | Hodnota |
|---------|---------|
| Celkem agentu | 12 |
| Celkem skills | 1 |
| Kategorie | 4 (Tvorba, Analyza, Projekty, Utility) |

---

*Posledni aktualizace: brezen 2026*
