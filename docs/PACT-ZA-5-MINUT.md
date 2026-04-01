# PACT za 5 minut

> Rychly pruvodce jak si nastavit PACT workspace a zacit efektivneji pracovat s AI.

---

## Co je PACT?

**4 slozky. 4 otazky. 1 framework.**

```
P  0_Projects/  → CO delam?           (projekty, vystupy)
A  1_Agents/    → JAK to udelat?      (agenti = .md, skills = slozky s SKILL.md)
C  2_Context/   → KDO jsem a co delam? (tvuj styl, znalosti, cile)
T  3_Tools/     → CIM to udelat?      (skripty, nastroje, API klice)
```

Proc to funguje: AI potrebuje kontext. Bez nej generuje genericky vystup. S PACT ma AI pristup k tomu, kdo jsi, jak komunikujes a co delas — a vysledky jsou radove lepsi.

---

## Krok 1: Vytvor slozky (30 sekund)

Vytvor tuto strukturu kdekoliv na disku:

```
MojeJmeno-2026/
├── 0_Projects/
├── 1_Agents/
├── 2_Context/
│   ├── identity/
│   │   └── tone-of-voice/
│   ├── expertise/
│   └── goals/
└── 3_Tools/
    └── api/
```

Nebo zkopiruj `pact-starter/` — uz to tam vse je.

---

## Krok 2: Vyplň kdo jsi (2 minuty)

Otevri `2_Context/identity/about-me.md` a vyplň:
- Jmeno, role, firma
- Co delas (2-3 vety)
- Pro koho pracujes
- Cim jsi specificky

Otevri `2_Context/identity/tone-of-voice/general.md` a vyplň:
- Jaky mas styl (formalni/neformalni)
- Jake fraze pouzivas
- Jake fraze NEPOUZIVAS
- Vloz 1-2 priklady textu ve tvem stylu

**Toto je NEJDULEZITEJSI krok.** Cim lepsi kontext, tim lepsi vystupy.

---

## Krok 3: Nastav API klice (2 minuty)

Otevri `3_Tools/api/README.md` — tam je podrobny navod.

Nejrychlejsi start:
1. Zaregistruj se na [openrouter.ai](https://openrouter.ai)
2. Vytvor API klic
3. Uloz ho do `3_Tools/api/openrouter-api.txt`

Jeden klic = pristup ke stovkam AI modelu (Claude, GPT, Gemini, Llama...).

---

## Krok 4: Pridej jednoho agenta (1 minuta)

V `1_Agents/` uz mas `agent-prompt-architect.md`. Rekni AI:

> "Precti si 1_Agents/agent-prompt-architect.md a vytvor mi agenta na [tvuj ukol]"

Napr.:
- "...agenta na psani LinkedIn postu"
- "...agenta na analyzu konkurence"
- "...agenta na zpracovani schuzek"

AI vytvori agenta, ktery zna tvuj styl (protoze cte 2_Context/). Kdyz agent roste na slozitosti, upgradni ho na **skill** (slozka s SKILL.md).

---

## Krok 5: Zaloz prvni projekt (1 minuta)

```
0_Projects/muj-prvni-projekt/
├── README.md    ← Co chces dosahnout
└── inputs/      ← Vstupni materialy
```

Rekni AI: "Pracuj na projektu v 0_Projects/muj-prvni-projekt/"

---

## Krok 6: Pouzivej (prubezne)

### Zakladni prikazy:

| Chci... | Rekni AI... |
|---------|-------------|
| Noveho agenta | "Pouzij agent-prompt-architect a vytvor agenta na [X]" |
| Text v mem stylu | "Napis [X], pouzij 2_Context/identity/tone-of-voice/" |
| Expertni pohled | "Pouzij agent-expert-panel na tema [X]" |
| Zkontrolovat vystup | "Pouzij agent-quality-gate a zkontroluj [X]" |
| Novy nastroj | "Mrkni na 3_Tools/README.md a vytvor mi nastroj na [X]" |

### Prubezne vylepsuj:

- Pridavej do `2_Context/expertise/` — clanky, prednasky, poznamky
- Pridavej do `2_Context/content-examples/` — priklady tvych nejlepsich textu
- Pridavej nove agenty podle potreby

---

## Pro ruzne AI nastroje

| Nastroj | Jak pouzit |
|---------|-----------|
| **Cursor** | Otevri celou slozku. `.cursorrules` se nacte automaticky. |
| **Claude Code** | `claude` v rootu slozky. |
| **ChatGPT/Claude web** | Nahraj `about-me.md` + agenta ke konverzaci. |

---

## Nejcastejsi chyby

1. **Prazdny Context/** — AI pak generuje genericky obsah. Vyplň alespon about-me a tone-of-voice.
2. **Prilis obecni agenti** — Cim konkretnejsi agent, tim lepsi vystup. "Napis email" < "Napis follow-up email po workshopu, kratky, pratelsky ton".
3. **Zapominani aktualizovat** — Context je zivy dokument. Aktualizuj ho s novym obsahem.

---

## Dalsi kroky

- Pridej **Skills** (strukturovane workflow dle [agentskills.io](https://agentskills.io)) — viz `1_Agents/skills/README.md`
- Vytvor **projektove kontexty** — viz `2_Context/projects/`
- Pridej **Tools** — viz roadmapu v `3_Tools/README.md`
- Nastav **dalsi API klice** — viz `3_Tools/api/README.md`

---

*PACT Framework — vytvoril Filip Drimalka (nowork.ai)*
*Verze: 2.0 — brezen 2026*
