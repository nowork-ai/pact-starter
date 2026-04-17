# 0_Projects/ — CO dělám

> Aktivní projekty s konkrétními výstupy.

---

## 🚀 Jak založit nový projekt

### Možnost A: Přes agenta (doporučeno)

Řekni AI v Cursoru / Claude Code:

```
Založ projekt [název]
```

Agent `1_Agents/agent-pact-bootstrap.md` se zeptá na 2–3 otázky a vytvoří kompletní strukturu z `_template/` včetně `AGENTS.md` a `.cursor/rules/parent-context.mdc`. Tím dosáhneš toho, že **i když pak otevřeš jen tu projektovou podsložku** v Cursoru, agent ví o nadřazeném PACT workspace, tone-of-voice a dostupných nástrojích.

### Možnost B: Přes skript

```bash
python3 3_Tools/workflows/generate-agents-md.py --init [nazev-projektu]
```

### Možnost C: Manuálně

```bash
cp -R 0_Projects/_template/ 0_Projects/[nazev-projektu]/
```

Pak ručně nahraď placeholdery `{{PROJECT_NAME}}`, `{{PROJECT_TITLE}}`, `{{PROJECT_DESCRIPTION}}` v `README.md`, `AGENTS.md` a `.cursor/rules/parent-context.mdc`.

---

## 📂 Struktura nového projektu (z `_template/`)

```
0_Projects/[nazev-projektu]/
├── README.md                              ← Lidský popis projektu (cíl, vstupy, výstupy)
├── AGENTS.md                              ← Briefing pro AI agenta (multi-tool standard)
├── .cursor/
│   └── rules/
│       └── parent-context.mdc             ← Auto-aplikované Cursor pravidlo (alwaysApply)
├── inputs/                                ← Vstupní materiály
└── outputs/                               ← Hotové výstupy
```

**Proč tato struktura:** Když si v Cursoru otevřeš jenom `0_Projects/[name]/` jako workspace root, kořenové `.cursorrules` ani `AGENTS.md` se nenačtou. Tahle struktura zajistí, že agent **přesto** pozná PACT, najde tone-of-voice (`../../2_Context/...`) a ví, kteří agenti existují (`../../1_Agents/`).

---

## 📋 Šablona `_template/`

Adresář `_template/` je vzorová kostra. **Neupravuj ji v existujících projektech** — slouží jako referenční šablona pro vytváření nových.

Pokud chceš upravit, jak vypadají všechny budoucí nové projekty, edituj `_template/` a:
- Existující projekty zůstanou nedotčené
- Nově založené přes agenta/skript dostanou novou verzi

---

## ✅ Pravidla pro projekty

- Jeden projekt = jedna složka v `0_Projects/`
- Agent v projektu odkazuje na `../../1_Agents/`, `../../3_Tools/` a `../../2_Context/`
- Po dokončení projektu → přesuň do `archive/`
- Velké projekty s více sub-projekty (master projects) mohou mít vnořenou strukturu
