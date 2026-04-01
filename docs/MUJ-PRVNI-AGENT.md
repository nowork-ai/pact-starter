# Muj prvni agent — tutorial

> Krok za krokem: jak vytvorit vlastniho AI agenta od nuly. Za 15 minut budes mit agenta, ktery dela presne to, co potrebujes.

---

## Co je agent?

Agent je **textovy soubor s instrukcemi pro AI**. Nic vic.

Kdyz AI precte instrukce, chova se podle nich — vi kdo je, co ma delat, jak ma odpovedet a ceho se vyvarovat.

```
agent-email-writer.md     ← soubor s instrukcemi
       ↓
AI precte instrukce       ← "Jsi expert na emaily, pises strucne..."
       ↓
Pises: "Napis email..."   ← AI odpovi podle instrukci
```

---

## Krok 1: Vyber si ukol

Na co potrebujes pomoc? Vyber si jeden konkretni ukol:

| Priklad | Agent |
|---------|-------|
| Psani emailu | agent-email-writer.md |
| Shrnuti schuzek | agent-meeting-summary.md |
| Tvorba LinkedIn postu | agent-linkedin-writer.md |
| Korektura textu | agent-proofreader.md |
| Priprava prezentaci | agent-presentation-prep.md |

Nevybirej nic sloziteho. **Prvni agent = jednoduchy ukol, ktery delas casto.**

---

## Krok 2: Odpovez na 5 otazek

Pred psanim si odpovez:

| # | Otazka | Tvoje odpoved |
|---|--------|---------------|
| 1 | **Co ma agent delat?** | Napr. "Pise kratke, profesionalni emaily" |
| 2 | **Kdo to je?** (expertiza) | Napr. "Zkuseny business komunikator" |
| 3 | **Jak ma vystup vypadat?** | Napr. "Email: predmet + telo, max 5 vet" |
| 4 | **Co NEDELA?** | Napr. "Nepouziva klise, neni prehnane formalni" |
| 5 | **Mas priklad?** | Napr. skvely email, ktery jsi napsal |

---

## Krok 3: Napis agenta

Vytvor soubor `1_Agents/agent-[tvuj-nazev].md`. Pouzij tuto sablonu:

```markdown
# [Nazev agenta]

> [Jedna veta — co agent dela]

---

## Kdo jsem

[2-3 vety. Ne "jsi expert" — bud konkretni:
- Jaka expertiza?
- Kolik let zkusenosti?
- Jaky pristup/filozofie?]

---

## Co delam

[Seznam ukolu, ktere agent zvlada — jako bullet points]

---

## Jak pracuji

[Krok za krokem — co agent udela kdyz dostane zadani]

1. **Krok** — [co udela]
2. **Krok** — [co udela]
3. **Krok** — [co udela]

---

## Vystupni format

[Presne jak ma vystup vypadat — sablona:]

```
[SABLONA VYSTUPU]
```

---

## Pravidla

### VZDY:
- [co delat]
- [co delat]

### NIKDY:
- [co nedelat]
- [co nedelat]

---

## Priklad

**Vstup:** [priklad zadani]

**Vystup:** [priklad odpovedi]
```

---

## Krok 4: Vyplnena ukazka

Tady je kompletni priklad — agent na psani emailu:

```markdown
# Email Writer

> Pise kratke, jasne, profesionalni emaily. Zadny fluff, zadne klise.

---

## Kdo jsem

Jsi zkuseny business komunikator s 10 lety praxe v B2B prostredi.
Tvuj styl: primo k veci, respekt k casu prijemce, kazdy email ma jasny
ucel a jednu konkretni akci (CTA).

---

## Co delam

- Pisu emaily na zaklade strucneho zadani
- Odpocidam na emaily (prepisu draft)
- Navrhuji predmety emailu (subject lines)

---

## Jak pracuji

1. **Pochop cil** — Co chce odesilatel dosahnout?
2. **Identifikuj akci** — Co ma prijemce udelat?
3. **Napis email** — Predmet + telo, max 5 vet
4. **Over** — Je jasne co a proc? Je tam CTA?

---

## Vystupni format

**Predmet:** [kratky, konkretni predmet]

---

[Osloveni],

[1-2 vety: kontext nebo duvod emailu]

[1-2 vety: hlavni sdeleni nebo zadost]

[CTA — co ma prijemce udelat + do kdy]

[Podpis]

---

## Pravidla

### VZDY:
- Max 5 vet v tele emailu
- Jasny predmet (prijemce vi o cem to je bez otevreni)
- Jedna akce na email (ne "a jeste bych chtel...")
- Predmet zacina akci: "Potvrzeni:", "Dotaz:", "Navrh:"

### NIKDY:
- "Doufam, ze se mate dobre" (ztrata casu)
- "S pozdravem" (pouzij jen jmeno)
- Pasivni konstrukce ("Bylo by mozne...")
- Vic nez 1 CTA v emailu

---

## Priklad

**Vstup:** Napis email Petrovi — chci potvrzeni schuzky v utery v 10:00

**Vystup:**

**Predmet:** Potvrzeni: schuzka utery 10:00

---

Petro,

potvrzujes schuzku v utery 22. 4. v 10:00? Mam pripravene podklady k rozpoctu Q2.

Dej vedet do pondeli vecera.

Martin
```

---

## Krok 5: Otestuj

Otevri Cursor (nebo Claude Code) v PACT slozce a rekni:

```
Pouzij @agent-email-writer.md a napis email Janě — chci presunout schuzku z patku na pondeli
```

Funguje? Super. Nefunguje jak chces? Uprav instrukce a zkus znovu.

**Iterace je normalni.** Prvni verze agenta nikdy neni perfektni. Uprav pravidla, pridej priklady, zpresni format.

---

## Krok 6: Zaregistruj

Pridej agenta do `1_Agents/AGENT-REGISTRY.md`:

```markdown
| **[agent-email-writer.md](agent-email-writer.md)** | Pise kratke, profesionalni emaily | Kdyz potrebujes napsat nebo prepsat email |
```

---

## Tipy pro lepsi agenty

### 1. Konkretni > vagne

```
❌ "Pis dobre emaily"
✅ "Max 5 vet. Predmet zacina akci. Jedna CTA."
```

### 2. Priklady > pravidla

Jeden dobry priklad vstupu → vystupu nauci AI vic nez 10 pravidel.

### 3. Rekni co NEDELA

AI ma tendenci byt "uzitecna" — prida klise, bude prehnane zdvorila, napise roman misto odstavce. Explicitne rekni co nechces.

### 4. Pouzij svuj kontext

Pokud mas vyplneny `2_Context/identity/tone-of-voice/`, pridej do agenta:

```markdown
## Kontext
Pro styl komunikace viz: `2_Context/identity/tone-of-voice/general.md`
```

### 5. Zacni jednoduchy, pridavej postupne

Prvni verze = 30 radku. Pak iteruj: pridej pravidla kdyz narazi na problem, pridej priklady kdyz vystup neni co chces.

---

## Dalsi kroky

- **Chces slozitejsi workflow?** Podivej se na [RECIPES.md](../1_Agents/RECIPES.md) — recepty kombinuji vic agentu
- **Chces opakovatelny proces?** Podivej se na [skills/README.md](../1_Agents/skills/README.md) — skills jsou agenti na steroidech
- **Chces agenta z existujicich dokumentu?** Pouzij `agent-knowledge-extractor.md` — precte 5-50 dokumentu a vytvori agenta
- **Chces profesionalne napsany prompt?** Pouzij `agent-prompt-architect.md` — vytvori precizni prompt s persona, guardrails a priklady

---

*Cas na vytvoreni prvniho agenta: ~15 minut. Cas, ktery ti usetri: hodiny.*
