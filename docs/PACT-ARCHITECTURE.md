# PACT — AI Workspace Architecture

> **P**rojects • **A**gents • **C**ontext • **T**ools
>
> Framework pro organizaci pracovniho prostoru pro efektivni spolupraci cloveka a AI.

---

## Filosofie

Pracovni prostor je rozdeleny do **ctyr zakladnich piliru**, z nichz kazdy odpovida na jinou otazku:

| Pilir | Otazka | Obsah |
|-------|--------|-------|
| **Projects** | CO delam? | Aktivni projekty s vystupy |
| **Agents** | JAK to udelat? | Instrukce pro AI — agenti (.md) a skills (slozky s SKILL.md) |
| **Context** | KDO to dela? | Identita, styl, expertiza, cile |
| **Tools** | CIM to udelat? | Nastroje, skripty, API |

---

## Klicove principy

1. **Single Source of Truth** — pravidla ziji na jednom miste (v `Context/`), agenti na ne odkazuji
2. **Agent = instrukce pro AI** — markdown soubor nebo skill (slozka s SKILL.md)
3. **Reference, ne hardcode** — agenti odkazuji na slozky, ne na konkretni soubory
4. **DRY** — zmena na jednom miste se projevi vsude
5. **AI je orchestrator** — AI cte agenta/skill a samo najde potrebne nastroje

---

## Jak to funguje

```
Uzivatel: "Zpracuj toto video z podcastu"
    |
    v
AI cte: Projects/podcast/agent-podcast-processor.md
    |
    +---> Context/identity/tone-of-voice/
    |     (pro spravny styl vystupu)
    |
    +---> Tools/
    |     (najde potrebne nastroje)
    |
    +---> Vytvori vystupy podle workflow v agentovi
```

---

## Vazby mezi slozkami

```
        PROJECTS/
        (aktivni projekty)
            |
     Agent v projektu odkazuje na:
            |
     +------+------+
     |      |      |
  AGENTS/  TOOLS/ CONTEXT/
  (JAK)   (CIM)  (KDO)
```

- **Agent ≠ Tool:** Agent popisuje CO a JAK, tool dela konkretni operaci
- **Agent vs Skill:** Agent = jednoduchy markdown soubor. Skill = slozka s `SKILL.md` + skripty, sablony, reference. Zacni agentem, upgradni na skill kdyz roste slozitost.
- **Skill = otevreny standard:** Skills nasleduji [Agent Skills](https://agentskills.io) format — prenositelne mezi nastroji (Cursor, Claude Code, atd.)
- **AGENT-REGISTRY:** Centralni prehled vsech agentu a skills = org chart systemu

---

*PACT Framework — vytvoril Filip Drimalka (nowork.ai)*
