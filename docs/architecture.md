# Architektura PACTu

PACT dává práci s AI čtyři srozumitelné vrstvy: Projects, Agents, Context a
Tools. Člověk nemusí použít stejné názvy složek ani stejnou aplikaci. Potřebuje
jasně určit, kde žije aktuální práce, pravidla pro AI, znovupoužitelné znalosti
a spustitelné nástroje.

## Projects

Projects obsahují pracovní i soukromé projekty a aktivity. Základ tvoří krátké
`README.md` s účelem, současným stavem a podmínkou dokončení. Projekt může podle
potřeby přidat `AGENTS.md` s pravidly pro AI, `TASKS.md` s otevřenými úkoly a
`WORKLOG.md` s výsledky, rozhodnutími a checkpointy.

Projekt zůstává hlavním domovem pro svoje rozhodnutí, rozpracované dokumenty,
zdrojové soubory, výsledné výstupy a aktuální čísla. Soukromé projekty mohou mít
přísnější pravidla přístupu a sdílení. Obecná znalost vznikne až ve chvíli, kdy
ji lze bezpečně použít i jinde.

## Agents

Tato vrstva drží pravidla a schopnosti AI. Může obsahovat jednoduchou instrukci,
specializovaného agenta, skill pro opakovanou práci nebo pravidla konkrétního
projektu.

Dobré pravidlo popisuje požadovaný výsledek, zdroje, hranice a způsob ověření.
Agent nemusí být samostatná aplikace; často stačí dobře napsaný Markdown.

## Context

Context obsahuje znalosti, které mají smysl napříč více projekty. Patří sem
pracovní profil, komunikační pravidla, ověřené know-how a odkazy na zdroje.
Součástí mohou být i raw podklady, například poznámky, přepisy hovorů, exporty a
další zdrojové dokumenty, které ještě neprošly ověřením.

Každé důležité tvrzení má původ, stav a datum ověření. Aktuální projektová data
zůstávají v projektu, aby se starší shrnutí netvářilo jako dnešní realita.

## Tools

Tools provádějí konkrétní akce: přečtou data, vytvoří výstup, synchronizují
zdroj nebo zkontrolují kvalitu. Patří sem lokální skripty, integrace a napojení
na další služby, importy a exporty, kontroly i automatizace.

Nástroj má dělat jednu jasnou věc a vracet ověřitelný výsledek. Přístupové klíče
a hesla zůstávají mimo dokumentaci a projektové soubory.

## Jedna autorita pro každou informaci

Stejný aktivní úkol, rozhodnutí nebo znalost nemají současně dvě hlavní místa.
Odvozené přehledy mohou data číst, ale nevytvářejí druhou frontu ani paralelní
historii.

Toto pravidlo chrání člověka i AI před situací, kdy dva soubory tvrdí něco
jiného a nikdo neví, který platí.

[Zpět na hlavní přehled](../README.md)
