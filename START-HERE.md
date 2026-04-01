# PACT — Zacni tady

> Tvuj AI workspace za 10 minut. Otevri tuto slozku v Cursoru a nech se provest.

---

## Co je PACT?

**4 slozky. 4 otazky. Jeden system.**

| Slozka | Otazka | Co tam patri |
|--------|--------|-------------|
| **P**rojects/ | CO delam? | Tvoje projekty a vystupy |
| **A**gents/ | JAK to udelat? | Instrukce pro AI — agenti (.md) nebo skills (slozky) |
| **C**ontext/ | KDO to dela? | Tvuj profil, styl, cile |
| **T**ools/ | CIM to udelat? | Skripty a nastroje |

**Proc to funguje:** AI bez kontextu generuje genericky vystup. S PACT vi kdo jsi, jak pises a co delas — a vysledky jsou radove lepsi.

---

## Rychly start (2 moznosti)

### Moznost A: Nech AI, at te provede (doporuceno)

Otevri chat v Cursoru (Cmd+L) a napis:

```
Pomoz mi nastavit PACT
```

AI te provede 5 kroky — zeptá se, kdo jsi, jak pises, jake mas cile, a vytvori ti prvniho agenta. Hotovo za 10 minut.

### Moznost B: Udelej to sam

Projdi kroky nize rucne a vyplň sablony.

---

## 5 kroku k nastavenímu PACT

### Krok 1: Kdo jsi
- [ ] Otevri `Context/identity/about-me.md`
- [ ] Vyplň sve jmeno, roli, firmu, zamereni
- [ ] Uloz

### Krok 2: Jak komunikujes
- [ ] Otevri `Context/identity/tone-of-voice/general.md`
- [ ] Popis svuj styl psani (formalni/neformalni, fraze, priklady)
- [ ] Uloz

### Krok 3: Tvoje cile
- [ ] Otevri `Context/goals/goals.md`
- [ ] Zapis na cem pracujes a kam smerujes
- [ ] Uloz

### Krok 4: Prvni agent
- [ ] Rekni AI: "Precti Agents/agent-prompt-architect.md a vytvor mi agenta na [tvuj ukol]"
- [ ] Napr.: agent na psani emailu, analyzu textu, LinkedIn posty...
- [ ] AI vytvori agenta a ulozi ho do `Agents/`

### Krok 5: Prvni projekt
- [ ] Vytvor slozku `Projects/nazev-projektu/`
- [ ] Pridej `README.md` s popisem a cilem
- [ ] Zacni pracovat — rekni AI co potrebujes

---

## Overte si, ze to funguje

Po nastaveni zkus napr.:

| Rekni AI... | Co se stane |
|------------|-------------|
| "Napis email v mem stylu" | AI precte tvuj tone-of-voice a napise email, ktery zni jako ty |
| "Pouzij agent-expert-panel na tema X" | AI spusti simulovanou expertni diskuzi |
| "Zkontroluj tento text" | AI pouzije agent-quality-gate a da ti feedback |

---

## Struktura slozky

```
pact-starter/
├── START-HERE.md            ← Jsi tady
├── .cursorrules             ← Pravidla pro Cursor AI
├── Projects/                ← Tvoje projekty
├── Agents/                  ← AI agenti a skills
│   ├── agent-prompt-architect.md  ← Vytvari dalsi agenty
│   ├── agent-expert-panel.md      ← Expertni diskuze
│   ├── agent-quality-gate.md      ← Kontrola kvality
│   └── skills/                    ← Skills (slozky s SKILL.md)
├── Context/                 ← Tvuj kontext
│   ├── identity/about-me.md       ← Kdo jsi
│   ├── identity/tone-of-voice/    ← Jak pises
│   ├── goals/goals.md             ← Tvoje cile
│   └── expertise/                 ← Tvoje znalosti
├── Tools/                   ← Nastroje
└── docs/                    ← Dokumentace
```

---

## Tipy

- **Cim vic kontextu, tim lepsi vystupy.** about-me.md a tone-of-voice jsou nejdulezitejsi.
- **Agent = markdown soubor** s instrukcemi, ktere AI precte a ridi se jimi. Pro slozitejsi workflow pouzij **Skill** = slozka s `SKILL.md` (otevreny standard [agentskills.io](https://agentskills.io)). Zacni agentem, upgradni na skill kdyz roste slozitost.
- **PACT funguje s jakymkoliv AI nastrojem.** Cursor, Claude Code, ChatGPT, Windsurf — princip je stejny.
- **Aktualizuj prubezne.** Context je zivy dokument. Pridavej priklady, upresňuj styl.

---

*PACT Framework — Filip Drimalka (nowork.ai) — brezen 2026*
