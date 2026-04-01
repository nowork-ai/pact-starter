# 0_Projects/ — CO delam

> Aktivni projekty s konkretnimi vystupy.

## Jak zalozit novy projekt

1. Vytvor slozku: `0_Projects/nazev-projektu/`
2. Pridej `README.md` s popisem projektu
3. Volitelne: pridej `agent-*.md` pro workflow specificke pro tento projekt
4. Vstupy do `inputs/`, vystupy do `outputs/`

## Priklad struktury

```
0_Projects/muj-projekt/
├── README.md           ← Co je cilem
├── agent-workflow.md   ← Jak to zpracovat (volitelne)
├── inputs/             ← Vstupni materialy
└── outputs/            ← Hotove vystupy
```

## Pravidla

- Agent v projektu odkazuje na `1_Agents/`, `3_Tools/` a `2_Context/`
- Po dokonceni → presun do `archive/`
