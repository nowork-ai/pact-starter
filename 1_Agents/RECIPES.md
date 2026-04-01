# Recepty — jak retezit agenty

> Copy-paste workflow, ktere kombinuji agenty pro bezne ukoly. Kazdy recept = sekvence agentu, kde vystup jednoho je vstup dalsiho.

---

## Jak recepty pouzivat

Staci rict AI (v Cursoru nebo Claude Code):

```
Pouzij recept "Z napadu do specifikace" na muj napad: [popis napadu]
```

Nebo rucne krok za krokem — kazdy agent funguje i samostatne.

---

## Recept 1: Z napadu do specifikace

> Mas napad na produkt/projekt. Chces z nej udelat jasnou specifikaci pripravenou pro realizaci.

```
VSTUP: Vagne "chci udelat X"

1. @agent-context-builder.md
   → Prozkoumej slozku projektu (pokud existuje)
   → Vystup: kontextovy dokument

2. @agent-product-architect.md
   → Vstup: napad + kontext
   → Vystup: PRD + Developer Brief

3. @agent-quality-gate.md
   → Vstup: hotova specifikace
   → Vystup: PASS/FAIL + pripominky

VYSTUP: Kompletni specifikace pripravena k realizaci
```

**Kdy pouzit:** Novy projekt, novy produkt, nova feature.

---

## Recept 2: Prozkoumej tema a vytvor agenta

> Mas hromadu clanku/dokumentu na tema. Chces z nich udelat specializovaneho AI agenta.

```
VSTUP: 5-50 dokumentu/clanku na jedno tema

1. @agent-deep-researcher.md
   → Vstup: "Prozkoumej [tema]"
   → Vystup: strukturovany vyzkumny report se zdroji

2. @agent-knowledge-extractor.md
   → Vstup: vyzkumny report + zdrojove dokumenty
   → Vystup: strukturovany znalostni vytah (koncepty, pravidla, anti-patterns)

3. @agent-prompt-architect.md
   → Vstup: znalostni vytah
   → Vystup: hotovy agent prompt (.md soubor)

VYSTUP: Novy specializovany agent v 1_Agents/
```

**Kdy pouzit:** Chces AI experta na tema, ke kteremu mas materialy.

---

## Recept 3: Poznej svuj styl a vytvor content strategii

> Chces zjistit, jak komunikujes, a vyuzit to pro tvorbu obsahu.

```
VSTUP: Tvoje texty (emaily, zpravy, posty, poznamky)

1. @agent-personal-voice-analyst.md
   → Vstup: kolekce tvych textu
   → Vystup: tone of voice profil + shareable content library

2. Uloz tone of voice do 2_Context/identity/tone-of-voice/general.md

3. @agent-prompt-architect.md
   → Vstup: "Vytvor agenta na psani LinkedIn postu v mem stylu"
   → Kontext: tone of voice profil z kroku 1
   → Vystup: personalizovany content agent

VYSTUP: Tvuj komunikacni profil + agent, ktery pise tvym stylem
```

**Kdy pouzit:** Chces konzistentni osobni brand a obsah, ktery zni jako ty.

---

## Recept 4: Hloubkova analyza dat

> Mas velke mnozstvi dat (dokumenty, tabulky, prepisy) a chces z nich actionable insighty.

```
VSTUP: Slozka se soubory (CSV, MD, TXT, JSON, PDF)

1. @agent-context-builder.md
   → Vstup: cela slozka
   → Vystup: prehled co vsechno tam je

2. @agent-data-analyst.md
   → Vstup: soubory + cil analyzy
   → Strategie: auto (prima / chunking / map-reduce)
   → Vystup: strukturovany analytickyreport

3. @agent-expert-panel.md (volitelne)
   → Vstup: "Co znamenaji tyhle vysledky pro [kontext]?"
   → Vystup: expertni interpretace dat z vice uhlu

VYSTUP: Report + interpretace + doporuceni
```

**Kdy pouzit:** Mas data a potrebujes z nich rozhodnuti.

---

## Recept 5: Expert panel pro strategicke rozhodnuti

> Stojis pred dulezitym rozhodnutim a chces vic uhlu pohledu.

```
VSTUP: Otazka nebo dilema

1. @agent-deep-researcher.md (volitelne)
   → Vstup: "Prozkoumej [tema rozhodnuti]"
   → Vystup: evidence-based podklady

2. @agent-expert-panel.md
   → Vstup: otazka + vyzkumne podklady
   → Vystup: diskuze 3-5 expertu, insighty, doporuceni A/B/C

3. @agent-quality-gate.md
   → Vstup: finalni rozhodnuti
   → Vystup: kontrola logiky a rizik

VYSTUP: Informovane rozhodnuti podlozene vice perspektivami
```

**Kdy pouzit:** Strategicke rozhodnuti, pricing, positioning, technologicka volba.

---

## Recept 6: Dokumentace → krasny HTML

> Mas markdown dokument a chces z nej publikovatelny HTML.

```
VSTUP: Markdown soubor (clanek, report, kapitola)

1. @agent-quality-gate.md
   → Vstup: markdown dokument
   → Vystup: PASS/FAIL + pripominky k textu

2. (Oprav podle pripominek)

3. @agent-markdown-to-html.md
   → Vstup: finalni markdown + pozadavky na styl
   → Vystup: self-contained HTML soubor

VYSTUP: Publikovatelny HTML dokument s profesionalnim designem
```

**Kdy pouzit:** Report pro klienta, clanek na web, kniha/kapitola.

---

## Recept 7: Postav novy skill od nuly

> Chces vytvorit opakovatelny workflow jako skill.

```
VSTUP: Popis workflow, ktery chces zautomatizovat

1. @agent-knowledge-extractor.md (volitelne)
   → Vstup: existujici materialy k workflow
   → Vystup: strukturovane znalosti

2. @agent-skill-builder.md
   → Vstup: popis + znalosti + cilova platforma (Cursor/Claude/PACT)
   → Vystup: kompletni SKILL.md + registrace

3. Otestuj skill na 2-3 realistickych vstupech

VYSTUP: Production-ready skill v 1_Agents/skills/
```

**Kdy pouzit:** Opakujes stejny workflow vic nez 3x.

---

## Jak vytvorit vlastni recept

```markdown
## Recept N: [Nazev]

> [Jednoveta popis — jaky problem resi]

VSTUP: [Co uzivatel poskytne]

1. @agent-[prvni].md
   → Vstup: [co dostane]
   → Vystup: [co vytvori]

2. @agent-[druhy].md
   → Vstup: [vystup z kroku 1]
   → Vystup: [co vytvori]

VYSTUP: [Finalni vysledek]

**Kdy pouzit:** [Konkretni situace]
```

Pravidla:
- Max 4 agenti v jednom receptu (vic = rozbit na dva recepty)
- Kazdy krok ma jasny vstup a vystup
- Volitelne kroky oznac "(volitelne)"
- Pridej "Kdy pouzit" — pomaha lide vybrat spravny recept
