# PACT Workspace — Agent Briefing

> **Otevřený multi-tool standard** ([agentmd.com](https://agentmd.com)). Tento soubor čte Cursor, Claude Code, OpenAI Codex, Cline, Aider a další AI agenti, když pracují v tomto repozitáři.

Pokud jsi AI agent — **přečti si tento soubor jako první**. Dá ti vše, co potřebuješ, abys mohl správně pracovat s tímto workspace.

---

## 🏗️ Architektura: PACT

Tento workspace používá **PACT** strukturu — čtyři složky, čtyři otázky:

| Složka | Otázka | Co tam patří |
|--------|--------|--------------|
| `0_Projects/` | **CO** dělám? | Aktivní projekty s konkrétními výstupy |
| `1_Agents/` | **JAK** to udělat? | Instrukce pro AI — agenti (`.md`) a skills (složky s `SKILL.md`) |
| `2_Context/` | **KDO** jsem? | Identita, tone of voice, expertiza, cíle |
| `3_Tools/` | **ČÍM** to udělat? | Skripty, API integrace, utility |

**Proč to funguje:** AI bez kontextu generuje generický výstup. S PACT máš přístup k tomu, kdo je user, jak komunikuje, co dělá — a výstupy jsou řádově lepší.

---

## 🧭 Klíčové cesty (relativní k rootu repa)

### Identita & styl psaní (`2_Context/`)
| Potřebuješ… | Cesta |
|---|---|
| Kdo je user (jméno, role, expertiza) | `2_Context/identity/about-me.md` |
| **Tone of voice — obecný** | `2_Context/identity/tone-of-voice/general.md` |
| Tone of voice per kanál | `2_Context/identity/tone-of-voice/` (pokud user vyplnil) |
| Cíle a focus | `2_Context/goals/goals.md` |
| Expertiza, znalosti | `2_Context/expertise/` |
| Příklady obsahu | `2_Context/content-examples/` |
| Designové principy | `2_Context/design/` |

### Agenti (`1_Agents/`)
| | |
|---|---|
| **Přehled všech 12 agentů** | `1_Agents/AGENT-REGISTRY.md` |
| Workflow recepty (řetězení) | `1_Agents/RECIPES.md` |
| Skills (otevřený standard [agentskills.io](https://agentskills.io)) | `1_Agents/skills/` |

### Nástroje (`3_Tools/`)
| | |
|---|---|
| API klíče (OpenRouter, OpenAI, Apify) | `3_Tools/api/README.md` |
| Workflow skripty | `3_Tools/workflows/` |
| Roadmapa nástrojů | `3_Tools/README.md` |

---

## 🎬 Jak interpretovat běžné requesty

| Když user řekne… | Co udělej |
|---|---|
| **„Pomoz mi nastavit PACT"**, „setup", „start" | Spusť 6krokový onboarding v `START-HERE.md` (sekce „Workshop Setup Mode" v `.cursor/rules/pact.mdc`) |
| **„Napiš email / post / text v mém stylu"** | Načti `2_Context/identity/about-me.md` + `2_Context/identity/tone-of-voice/general.md`, drž stylistické principy |
| **„Vytvoř prompt"**, „napiš system prompt" | Použij `1_Agents/agent-prompt-architect.md` |
| **„Expert panel"**, „diskuze expertů", „více úhlů pohledu" | `1_Agents/agent-expert-panel.md` |
| **„Prozkoumej / research / najdi info"** | `1_Agents/agent-deep-researcher.md` |
| **„Analyzuj data / dokumenty / CSV"** | `1_Agents/agent-data-analyst.md` |
| **„Zkontroluj / quality check / je to dobré?"** | `1_Agents/agent-quality-gate.md` |
| **„Specifikace produktu / PRD / nápad na produkt"** | `1_Agents/agent-product-architect.md` |
| **„Analyzuj můj styl / tone of voice"** | `1_Agents/agent-personal-voice-analyst.md` |
| **„Extrahuj znalosti / vytvor agenta z dokumentů"** | `1_Agents/agent-knowledge-extractor.md` |
| **„Vytvoř skill / SKILL.md"** | `1_Agents/agent-skill-builder.md` |
| **„Převed do HTML / publikuj dokument"** | `1_Agents/agent-markdown-to-html.md` |
| **„Založ projekt / nový projekt / start project"** | `1_Agents/agent-pact-bootstrap.md` (vytvoří strukturu z `0_Projects/_template/`) |
| **„Recept / workflow / jak řetězit agenty"** | `1_Agents/RECIPES.md` |

**Pravidlo č. 1:** Než něco napíšeš od nuly, **prohledej `1_Agents/` a `3_Tools/`** — možná to už existuje.

---

## ✅ Pravidla pro AI agenta v tomto workspace

1. **Pro každý text určený userovi** — vždy načti `2_Context/identity/tone-of-voice/general.md` a drž jeho styl. Pokud je soubor stále s placeholdery `[DOPLNIT]`, oznam to userovi a navrhni vyplnění.
2. **Pro tvorbu nového agenta** — použij `1_Agents/agent-prompt-architect.md` (jednoduchý) nebo `1_Agents/agent-skill-builder.md` (komplexní workflow jako skill).
3. **Pro zakládání nového projektu** — použij `1_Agents/agent-pact-bootstrap.md`. Vždy zkopíruje `0_Projects/_template/`, takže nový projekt automaticky obsahuje briefing pro AI.
4. **Výstupy ukládej do `0_Projects/<nazev>/outputs/`**, ne do rootu workspace.
5. **Sdílené utility, API klienti, skripty pro znovupoužití** patří do `3_Tools/`, ne do projektu.
6. **Citlivá data / API klíče** — nikdy do souborů, nikdy do gitu. Jsou v `3_Tools/api/` a `.gitignore` je vylučuje.

---

## 🔁 Když pracuješ jen v podsložce projektu

Když user otevře pouze `0_Projects/<nazev>/` jako workspace root, **najdeš v té složce vlastní `AGENTS.md`** (vytvořený z `_template/`), který odkazuje zpět na tento root briefing relativními cestami (`../../2_Context/...`).

Pokud `AGENTS.md` v projektu chybí, pošli usera na příkaz:
```bash
python3 3_Tools/workflows/generate-agents-md.py --init <nazev-projektu>
```

---

## 📚 Zdroje

- `START-HERE.md` — lidský onboarding pro nového usera
- `README.md` — popis projektu pro GitHub
- `docs/PACT-ARCHITECTURE.md` — detailní architektura
- `docs/MUJ-PRVNI-AGENT.md` — tutorial: vytvoření vlastního agenta
- `docs/PACT-ZA-5-MINUT.md` — rychlý průvodce

---

*PACT Framework — Filip Drimalka ([nowork.ai](https://nowork.ai)) · [github.com/drimalka/pact-starter](https://github.com/drimalka/pact-starter)*
