# Řízení projektů s AI

Řízení projektů s AI pomáhá plánovat a řídit společnou práci člověka a AI.
Větší práce potřebuje jasné vlastnictví, závislosti a ověření.

## Minimální projekt

Na začátku často stačí `README.md` se čtyřmi částmi:

- účel a očekávaný výsledek;
- současný stav;
- zdroje, podle kterých se rozhoduje;
- podmínka, podle níž poznáme dokončení.

Další soubory vznikají podle potřeby. Plochá struktura bývá přehlednější než
sada prázdných složek připravených pro hypotetickou budoucnost.

## TASKS

`TASKS.md` drží otevřené úkoly, které musí přežít aktuální chat. Úkol obsahuje
záměr, kontext, výstup, podmínky přijetí, závislosti a vlastníka.

Každý projekt má jednu aktivní frontu úkolů. Společný dashboard ji může číst a
filtrovat, ale nesmí vytvářet druhou kopii se samostatným stavem.

## AI-WBS

AI Work Breakdown Structure neboli AI-WBS je nová generace projektového řízení
pro situace, kdy většinu práce odpracovává AI. Rozpadne větší zadání na
schvalitelnou mapu práce a u každé části určí:

- vlastníka a potřebnou aktivní pozornost člověka;
- závislosti a skutečné externí čekání;
- očekávaný výstup;
- ověřitelnou podmínku dokončení;
- vhodný typ agenta nebo modelu.

AI-WBS je plán realizace, ne paralelní seznam úkolů. Po schválení se trvalé
jednotky zapíší do `TASKS.md` odpovědných projektů.

## Dokončení práce

Hotový úkol nekončí označením checkboxu. AI nebo člověk ověří výsledek podle
předem určených podmínek, uloží výstup do projektu a zapíše důležité rozhodnutí
do `WORKLOG.md`.

Tento cyklus umožňuje jinému agentovi pokračovat bez rekonstrukce celé historie
z chatu.

[Zpět na hlavní přehled](../README.md)
