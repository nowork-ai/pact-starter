# PACT: Superpowered OS

**Framework pro vytvoření vlastního operačního systému pro Superpowered
Professionals™ (znalostní pracovníky, kteří chtějí využívat umělou inteligenci
naplno).**

PACT propojuje projekty, pracovní pravidla, znalosti a nástroje. AI díky tomu
rozumí tomu, na čem pracujete, dokáže bezpečně pokračovat a neztrácí důležitý
kontext mezi jednotlivými chaty, agenty a aplikacemi.

## Co vám vlastní PACT přinese

- **Budujete si druhý mozek.** Znalosti, rozhodnutí, projekty a zkušenosti
  nezůstávají rozptýlené v chatech a poznámkách. Postupně vzniká dokumentovaný
  systém, který roste spolu s vaší prací.
- **Vy i AI najdete potřebné informace během několika vteřin.** Každý projekt,
  úkol a typ znalosti má svoje místo, takže nemusíte znovu hledat nebo
  vysvětlovat celý kontext.
- **AI vám dává stále lepší výstupy.** Pracuje s vašimi pravidly, ověřenými
  zdroji, předchozími rozhodnutími a zkušenostmi z dokončené práce.
- **Můžete plynule pokračovat napříč nástroji.** Práci převezme jiný agent,
  aplikace nebo člověk, aniž by začínal od nuly.
- **Systém se zlepšuje s každým projektem.** Výsledky ukazují, které postupy se
  vyplatí zachovat, co je potřeba opravit a kterou opakovanou práci lze převést
  na workflow nebo automatizaci.

> **Stav veřejné verze:** Tento repozitář nyní slouží jako veřejný přehled nové
> generace PACTu. Plnou verzi dostanou jako první k dispozici účastníci
> [Future AI Leader](https://drimalka.com/fail) a během programu si ji nastaví
> podle vlastní práce. Jednodušší veřejný starter připravíme podle zkušeností z
> programu. [Původní PACT Starter](START-HERE.md) zůstane dostupný jako legacy
> release a samostatná větev.

## Čtyři vrstvy PACTu

PACT je zkratka pro Projects, Agents, Context a Tools. Konkrétní názvy složek a
aplikace se mohou lišit; každá informace ale potřebuje jasný domov a vlastníka.

- **Projects:** pracovní i soukromé projekty a aktivity. Každý projekt může mít
  vlastní zadání, pravidla pro AI, úkoly, historii rozhodnutí, dokumenty a
  výsledné soubory.
- **Agents:** agenti, pravidla, skills a pracovní postupy, které určují, jak má
  AI při konkrétní práci postupovat, co smí udělat a jak ověří výsledek.
- **Context:** znalosti použitelné napříč prací, například know-how, pracovní
  profily a ověřená fakta, ale také zdrojové poznámky, přepisy hovorů a další
  raw podklady.
- **Tools:** skripty, integrace, napojení na další služby, kontroly a
  automatizace, pomocí kterých AI provádí konkrétní akce.

## Jak může struktura PACTu vypadat

Každý PACT se přizpůsobí práci svého majitele. Základní struktura může vypadat
třeba takto:

```text
PACT/
├── Projects/
│   ├── work/
│   │   └── new-book/
│   │       ├── README.md
│   │       ├── AGENTS.md
│   │       ├── TASKS.md
│   │       ├── WORKLOG.md
│   │       ├── manuscript/
│   │       ├── research/
│   │       └── author-notes/
│   └── private/
│       └── home/
│           ├── README.md
│           ├── TASKS.md
│           ├── contracts/
│           └── documentation/
├── Agents/
│   ├── agent-pact-assistant.md
│   ├── agent-executive-assistant.md
│   ├── agent-personal-assistant.md
│   ├── skills/
│   └── workflows/
├── Context/
│   ├── knowledge/
│   ├── raw/
│   │   ├── call-transcripts/
│   │   ├── slack-conversations/
│   │   └── plans/
│   ├── idea-files/
│   └── handoffs/
└── Tools/
    ├── integrations/
    ├── workflows/
    └── automations/
```

`README.md` vysvětluje smysl a současný stav projektu. `AGENTS.md` dává AI
pravidla pro práci v daném projektu, `TASKS.md` drží otevřené úkoly a
`WORKLOG.md` zachovává výsledky a důležitá rozhodnutí.

## Pět částí PACTu

### Architektura PACTu

Architektura určuje, kde žijí projekty, pravidla, znalosti a nástroje. Každý
úkol, údaj a rozhodnutí má jedno platné místo.

### Pracovní koncepty

Pracovní koncepty pomáhají zachytit myšlenku, přenést know-how nebo předat
rozdělanou práci.

- **Idea File:** samostatně srozumitelný koncept, který můžete poslat člověku
  nebo vložit do jeho AI bez přístupu k vašemu internímu systému.
- **Handoff:** předání konkrétní práce kolegovi nebo AI.
- **Runbook:** opakovatelný postup pro práci, která používá podobné kroky,
  podmínky a kontrolu výsledku.
- **Clean:** připravovaný koncept, který zpracuje informaci, nápad nebo
  myšlenku. Vytáhne obsah z poznámky, obrázku nebo jiného vstupu, odstraní šum,
  připraví ho do čitelné podoby a podle vašeho pokynu ho uloží do projektu,
  obsahu, znalostí nebo jinam.

### Řízení projektů s AI

Projektové řízení pomáhá plánovat a řídit společnou práci člověka a AI.

- **README:** účel projektu, současný stav, důležité zdroje a podmínka
  dokončení.
- **TASKS:** úkoly, které musí přežít aktuální chat, včetně vlastníka,
  závislostí a podmínek přijetí.
- **AI-WBS:** nová generace projektového řízení pro situace, kdy většinu práce
  odpracovává AI. Rozdělí větší zadání na části, které lze přidělit, ověřit a
  postupně dokončit.
- **WORKLOG:** výsledky, rozhodnutí a checkpointy, ze kterých může další agent
  bezpečně pokračovat.

### Paměť, orientace a bezpečnost

[Paměť a bezpečnost](docs/memory-and-safety.md) udržují PACT použitelný i ve
chvíli, kdy obsahuje desítky projektů a tisíce souborů.

- **Work Radar:** pomáhá najít, kde a na čem se nedávno pracovalo.
- **Work Desk:** skládá aktuální úkoly, termíny a signály do jednoho pracovního
  pohledu, aniž by vytvářel druhou kopii dat.
- **Čištění znalostí:** odděluje ověřené know-how od raw podkladů, konfliktů a
  informací, které ještě potřebují lidskou kontrolu.
- **Bezpečnostní checkpointy:** zastaví publikaci, mazání, práci s citlivými
  daty a další významné kroky, dokud člověk nepotvrdí přesný dopad.

### Vlastní agenti, nástroje a automatizace

[Rozšiřování PACTu](docs/extending-pact.md) vychází z práce, kterou skutečně
děláte. Opakující se potřeba může postupně vyrůst v pojmenované workflow,
specializovaného agenta, integraci nebo automatizaci.

Ve svém PACTu mám například **Book Capture**, protože píšu novou knihu. Když
narazím na příběh nebo poznatek, jedním pokynem ho uložím do autorského
zápisníku. **Content Manager** podobně zachytává a třídí myšlenky pro přednášky,
videa, newsletter nebo sociální sítě.

Někdo jiný si může vytvořit systém pro klientské projekty, výzkum, nábor,
investice nebo rodinnou administrativu. Společná architektura zůstává stejná,
konkrétní schopnosti si každý skládá podle vlastní práce.

## Postavte si vlastní Superpowered OS

Novou verzi PACTu teď rozvíjím jako součást podzimního běhu programu
Future AI Leader, jehož hlavním tématem bude **Superpowered OS**. Účastníci si
během programu postaví a vyladí vlastní systém pro práci s AI agenty, projekty a
znalostmi, použitelný v práci i osobním životě. Zkušenosti z programu potom
použijeme při přípravě jednodušší veřejné verze PACTu.

[Zjistit více o programu Future AI Leader](https://drimalka.com/fail)

---

PACT vytváří [Filip Dřímalka](https://drimalka.com) a komunita Future AI
Leader.
