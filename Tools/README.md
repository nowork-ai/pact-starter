# Tools/ — CIM to udelat

> Reusable nastroje a skripty. Kazdy nastroj dela jednu konkretni vec.

## Pravidla

- Kazda slozka = jeden nastroj
- Nastroj je ATOMICKY — dela jednu vec
- Vystupy ukladej vedle vstupu
- API klice a tokeny schovej (ne do repa)
- Nastroje jsou REUSABLE napric projekty

## Jak pridat nastroj

1. Vytvor slozku: `Tools/nazev-nastroje/`
2. Pridej skript + `requirements.txt` (Python) nebo `package.json` (JS)
3. Pridej `README.md` s popisem co nastroj dela a jak ho pouzit

## Priklad

```
Tools/transcribe/
├── transcribe.py       ← Hlavni skript
├── requirements.txt    ← Dependencies
└── README.md           ← Dokumentace
```
