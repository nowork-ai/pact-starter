# 2_Context/ — KDO jsem a co delam

> Tvuj osobni kontext pro AI. Zdroj pravdy o tom, kdo jsi, co vis a kam smerujes.

## Struktura

| Slozka | Obsah |
|--------|-------|
| `identity/` | Kdo jsi — about-me, tone of voice |
| `expertise/` | Co vis — clanky, prednasky, poznamky |
| `goals/` | Kam smerujes — cile a priorita |
| `design/` | Vizualni pravidla — barvy, fonty, layout |
| `projects/` | Kanonicka dokumentace hlavnich projektu |
| `content-examples/` | Vzory obsahu pro ruzne kanaly |

## Jak to pouzivaji agenti

Agent v projektu odkazuje na Context takto:

```markdown
## Kontext
Pro tone of voice viz: 2_Context/identity/tone-of-voice/
Pro info o projektu viz: 2_Context/projects/[nazev].md
```

## Dulezite

- Toto NENI projekt — nema vystupy ani deadline
- Toto JE reference — zdroj pravdy pro konzistentni styl
- Prubezne aktualizuj novym obsahem
