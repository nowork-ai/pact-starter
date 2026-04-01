# 3_Tools/ — CIM to udelat

> Reusable nastroje a skripty. Kazdy nastroj dela jednu konkretni vec.

---

## Zacni tady

1. **Nastav si API klice** — viz `api/README.md`
2. **Vyber nastroj** z roadmapy nize
3. Nebo rekni AI: *"Vytvor mi nastroj na [ukol]"*

---

## Pravidla

- Kazda slozka = jeden nastroj
- Nastroj je ATOMICKY — dela jednu vec
- Vystupy ukladej vedle vstupu
- API klice schovej do `api/` (ne do repa)
- Nastroje jsou REUSABLE napric projekty

---

## Jak pridat nastroj

1. Vytvor slozku: `3_Tools/nazev-nastroje/`
2. Pridej skript + `requirements.txt` (Python) nebo `package.json` (JS)
3. Pridej `README.md` s popisem co nastroj dela a jak ho pouzit

```
3_Tools/muj-nastroj/
├── muj_nastroj.py      ← Hlavni skript
├── requirements.txt    ← Dependencies
└── README.md           ← Dokumentace
```

---

## API klice

Vsechny klice jsou v `api/` — podrobny navod jak je ziskat viz `api/README.md`.

| Soubor | Sluzba | Co dava |
|--------|--------|---------|
| `api/openrouter-api.txt` | OpenRouter | 300+ AI modelu (Claude, GPT, Gemini...) |
| `api/openai-api.txt` | OpenAI | Audio prepis (transkripce) |
| `api/apify-api.txt` | Apify | Web scraping, automatizace |

---

## Roadmapa nastroju

Nastroje, ktere muzes postupne pridat do sveho PACT workspace. Rekni AI napr.: *"Vytvor mi nastroj na prepis audia"* a on ho postavi podle teto roadmapy.

### Prace s textem a dokumenty (OpenRouter)

| Nastroj | Co dela |
|---------|---------|
| **Analyza dokumentu** | Nahraj PDF, DOCX, jakykoli dokument — AI ho shrne, extrahuje klicove info, odpovi na otazky |
| **Datovy analytik** | Nahraj CSV/Excel — AI najde trendy, anomalie, vytvori shrnuti, navrhne grafy |
| **Hromadne zpracovani** | Zpracuj desitky souboru najednou pres AI (batch sumarizace, extrakce, preklad) |
| **Prekladac** | Preloz dokument s zachovanim formatovani a tonu — ne doslovne, ale smysluplne |
| **Research asistent** | Hloubkovy vyzkum na jake koliv tema se zdroji a citacemi |

### Audio a video (OpenAI API)

| Nastroj | Co dela |
|---------|---------|
| **Prepis audio/videa** | Nahraj nahravku — AI ji prepise s timestamps, detekci recniku, automatickym rozdelenim na casti |

### Web a data (Apify)

| Nastroj | Co dela |
|---------|---------|
| **Web scraper** | Zadej URL — dostanes cisty text v markdownu, pripraveny pro AI zpracovani |
| **LinkedIn profil** | Extrahuj verejna data z LinkedIn profilu (bio, zkusenosti, dovednosti) |
| **Web monitoring** | Sleduj stranku — kdyz se neco zmeni, dostanes upozorneni |

### Kreativni nastroje (OpenRouter)

| Nastroj | Co dela |
|---------|---------|
| **Generovani obrazku** | Popis -> obraz pres AI modely (Flux, Gemini, DALL-E) |

---

## Filozofie

```
DOBRY nastroj:
  - Dela JEDNU vec dobre
  - Funguje s JAKYMKOLIV vstupem
  - Ma CLI + Python API
  - Uklada vystupy vedle vstupu

SPATNY nastroj:
  - Projektove specificky
  - Hardcoded hodnoty
  - Jen wrapper bez pridane hodnoty
```
