# {{PROJECT_TITLE}} — Agent Briefing

> **Tento projekt je sub-složka [PACT workspace](../../AGENTS.md).**
> Pokud jsi otevřel jen tento adresář v editoru/agentovi, **vždycky pracuj s vědomím nadřazeného workspace** níže.
>
> **Pro lidský popis projektu** viz [`README.md`](./README.md).

---

## 📍 Kde jsi

| | |
|---|---|
| **Workspace root** | `../../` (PACT framework) |
| **Tento projekt** | `0_Projects/{{PROJECT_NAME}}/` |
| **Architektura** | PACT — **P**rojects · **A**gents · **C**ontext · **T**ools |

PACT v jedné větě:
- **`0_Projects/`** = CO dělám (tady jsi)
- **`1_Agents/`** = JAK to udělat (instrukce, workflow)
- **`2_Context/`** = KDO to dělá (identita, tone of voice, expertiza)
- **`3_Tools/`** = ČÍM to udělat (skripty, API integrace)

---

## 🧭 Kde co najdeš (relativní cesty z této složky)

### Identita & styl psaní userem
| Potřebuješ… | Cesta |
|---|---|
| Kdo je user (jméno, role, expertiza) | `../../2_Context/identity/about-me.md` |
| **Tone of voice — obecný** | `../../2_Context/identity/tone-of-voice/general.md` |
| Tone of voice per kanál (pokud existuje) | `../../2_Context/identity/tone-of-voice/` |
| Cíle a focus | `../../2_Context/goals/goals.md` |
| Expertiza, znalosti | `../../2_Context/expertise/` |
| Příklady obsahu (referenční texty) | `../../2_Context/content-examples/` |

### Hotoví agenti
| Potřebuješ… | Cesta |
|---|---|
| **Přehled všech agentů** | `../../1_Agents/AGENT-REGISTRY.md` |
| Workflow recepty (řetězení) | `../../1_Agents/RECIPES.md` |
| Vytvořit nový prompt / agenta | `../../1_Agents/agent-prompt-architect.md` |
| Expert panel / diskuze | `../../1_Agents/agent-expert-panel.md` |
| Hloubkový research | `../../1_Agents/agent-deep-researcher.md` |
| Analýza dat / dokumentů | `../../1_Agents/agent-data-analyst.md` |
| Quality check výstupu | `../../1_Agents/agent-quality-gate.md` |
| Specifikace produktu / PRD | `../../1_Agents/agent-product-architect.md` |
| Skills (složky s `SKILL.md`) | `../../1_Agents/skills/` |

### Nástroje
| | |
|---|---|
| API klíče (OpenRouter, OpenAI…) | `../../3_Tools/api/` |
| Workflow skripty | `../../3_Tools/workflows/` |
| Roadmapa nástrojů | `../../3_Tools/README.md` |

---

## 🎬 Jak interpretovat běžné requesty v kontextu tohoto projektu

| Když user řekne… | Co udělej |
|---|---|
| **„Napiš email / post / text"** | Načti `../../2_Context/identity/tone-of-voice/general.md`, drž userův styl |
| **„Vytvoř prompt"** | Použij `../../1_Agents/agent-prompt-architect.md` |
| **„Expert panel / diskuze expertů"** | `../../1_Agents/agent-expert-panel.md` |
| **„Prozkoumej / research"** | `../../1_Agents/agent-deep-researcher.md` |
| **„Analyzuj data / CSV / dokumenty"** | `../../1_Agents/agent-data-analyst.md` |
| **„Zkontroluj / quality check"** | `../../1_Agents/agent-quality-gate.md` |
| **„PRD / specifikace produktu"** | `../../1_Agents/agent-product-architect.md` |
| **„Udělej nástroj, co volá AI / API"** | Nejdřív prohledej `../../3_Tools/`, případně dopiš tam — ne sem |
| **„Převed do HTML"** | `../../1_Agents/agent-markdown-to-html.md` |

**Pravidlo č. 1:** Než něco napíšeš od nuly, **prohledej `../../1_Agents/` a `../../3_Tools/`** — možná to už existuje.

---

## ✅ Pravidla pro tento projekt

1. **Výstupy** ukládej do `outputs/`, vstupy do `inputs/`
2. **Sdílené utility, API klienti, znovu-použitelné skripty** → `../../3_Tools/`, ne sem
3. **Texty pro usera** vždy přes tone-of-voice z `../../2_Context/identity/`
4. **Citlivá data / API klíče** nikdy do souborů — používej `.env` nebo `../../3_Tools/api/`

---

<!-- MANUAL:START — vše mezi těmito značkami se při regeneraci nepřepíše -->
## 📦 O tomto projektu

{{PROJECT_DESCRIPTION}}

> Plný popis, struktura a workflow: viz [`README.md`](./README.md).
<!-- MANUAL:END -->

---

*Generováno z `0_Projects/_template/AGENTS.md`. Hlavička se aktualizuje skriptem `3_Tools/workflows/generate-agents-md.py --refresh {{PROJECT_NAME}}`. Sekce „📦 O tomto projektu" je ruční — nepřepíše se.*
