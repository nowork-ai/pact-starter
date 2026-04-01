# PACT za 5 minut

> Rychly pruvodce jak si nastavit PACT workspace a zacit efektivneji pracovat s AI.

---

## Co je PACT?

**4 slozky. 4 otazky. 1 framework.**

```
P  Projects/  → CO delam?      (projekty, vystupy)
A  Agents/    → JAK to udelat? (agenti = .md, skills = slozky s SKILL.md)
C  Context/   → KDO to dela?   (tvuj styl, znalosti, cile)
T  Tools/     → CIM to udelat? (skripty, nastroje)
```

Proc to funguje: AI potrebuje kontext. Bez nej generuje genericky vystup. S PACT ma AI pristup k tomu, kdo jsi, jak komunikujes a co delas — a vysledky jsou radove lepsi.

---

## Krok 1: Vytvor slozky (30 sekund)

Vytvor tuto strukturu kdekoliv na disku:

```
MojeJmeno-2026/
├── Projects/
├── Agents/
├── Context/
│   ├── identity/
│   │   └── tone-of-voice/
│   ├── expertise/
│   └── goals/
└── Tools/
```

Nebo zkopiruj `pact-starter/` — uz to tam vse je.

---

## Krok 2: Vyplň kdo jsi (2 minuty)

Otevri `Context/identity/about-me.md` a vyplň:
- Jmeno, role, firma
- Co delas (2-3 vety)
- Pro koho pracujes
- Cim jsi specificky

Otevri `Context/identity/tone-of-voice/general.md` a vyplň:
- Jaky mas styl (formalni/neformalni)
- Jake fraze pouzivas
- Jake fraze NEPOUZIVAS
- Vloz 1-2 priklady textu ve tvem stylu

**Toto je NEJDULEZITEJSI krok.** Cim lepsi kontext, tim lepsi vystupy.

---

## Krok 3: Pridej jednoho agenta (1 minuta)

V `Agents/` uz mas `agent-prompt-architect.md`. Rekni AI:

> "Precti si Agents/agent-prompt-architect.md a vytvor mi agenta na [tvuj ukol]"

Napr.:
- "...agenta na psani LinkedIn postu"
- "...agenta na analyzu konkurence"
- "...agenta na zpracovani schuzek"

AI vytvori agenta, ktery zna tvuj styl (protoze cte Context/).

---

## Krok 4: Zaloz prvni projekt (1 minuta)

```
Projects/muj-prvni-projekt/
├── README.md    ← Co chces dosahnout
└── inputs/      ← Vstupni materialy
```

Rekni AI: "Pracuj na projektu v Projects/muj-prvni-projekt/"

---

## Krok 5: Pouzivej (prubezne)

### Zakladni prikazy:

| Chci... | Rekni AI... |
|---------|-------------|
| Noveho agenta | "Pouzij agent-prompt-architect a vytvor agenta na [X]" |
| Text v mem stylu | "Napis [X], pouzij Context/identity/tone-of-voice/" |
| Expertni pohled | "Pouzij agent-expert-panel na tema [X]" |
| Zkontrolovat vystup | "Pouzij agent-quality-gate a zkontroluj [X]" |

### Prubezne vylepsuj:

- Pridavej do `Context/expertise/` — clanky, prednasky, poznamky
- Pridavej do `Context/content-examples/` — priklady tvych nejlepsich textu
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
2. **Prilis obecni agenti** — Cim konkretnejsi agent, tim lepsi vystup. "Napis email" < "Napis follow-up email po workshopu, kratky, pratelsky ton". Kdyz agent roste na slozitosti, upgradni ho na **skill** (slozka s SKILL.md).
3. **Zapominani aktualizovat** — Context je zivy dokument. Aktualizuj ho s novym obsahem.

---

## Dalsi kroky

- Pridej **Skills** (strukturovane workflow dle [agentskills.io](https://agentskills.io)) — viz `Agents/skills/README.md`
- Vytvor **projektove kontexty** — viz `Context/projects/`
- Pridej **Tools** — skripty pro automatizaci

---

*PACT Framework — vytvoril Filip Drimalka (nowork.ai)*
*Verze: 1.0 — brezen 2026*
