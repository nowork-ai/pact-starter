---
name: content-review
description: Zkontroluje text z hlediska tonu, srozumitelnosti a kvality. Pouzij kdyz uzivatel rekne "zkontroluj text", "review", "zpetna vazba na text".
---

# Content Review

> Skill pro komplexni kontrolu textu — tone of voice, srozumitelnost, gramatika, a doporuceni na zlepseni.

## Kdy pouzit

Pouzij tento skill kdyz:
- Uzivatel chce zkontrolovat hotovy text pred publikovanim
- Potrebuje zpetnou vazbu na email, post, clanek nebo prezentaci
- Chce overit, ze text odpovida jeho tone of voice

## Kontext

- `2_Context/identity/tone-of-voice/` — pravidla pro styl komunikace
- `2_Context/identity/about-me.md` — kdo je autor

## Pipeline

### Krok 1: Nacti kontext
1. Precti `2_Context/identity/tone-of-voice/general.md`
2. Precti `2_Context/identity/about-me.md`
3. Zapamatuj si klicove vzorce (formalita, typicke fraze, co nepouzivat)

### Krok 2: Analyzuj text
1. Zkontroluj shodu s tone of voice
2. Over srozumitelnost (kratke vety, jasna struktura)
3. Zkontroluj gramatiku a pravopis
4. Over delku (neni prilis dlouhy/kratky pro dany format?)
5. Zkontroluj CTA (je jasne co ma ctenar udelat dal?)

### Krok 3: Vytvor report
Vystup ve formatu nize.

## Vystup

```markdown
## Content Review

**Text:** [nazev/typ textu]
**Status:** PASS / NEEDS EDIT

### Tone of Voice
- [Odpovida / Neodpovida] — [konkretni poznamka]

### Srozumitelnost
- [Hodnoceni] — [co zlepsit]

### Gramatika
- [OK / nalezene chyby]

### Doporuceni
1. [Konkretni zmena 1]
2. [Konkretni zmena 2]

### Upraveny text (pokud NEEDS EDIT)
> [Navrzena uprava s vysvetlenim co a proc se zmenilo]
```
