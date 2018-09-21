# Ressourcemonitor #

* Forfattere: Alex Hall, Joseph Lee, Beqa Gozalishvili, Tuukka Ojala og
  andre NVDA-bidragydere
* Download [stable version][1]

Dette tilføjelsesprogram giver information om CPU-belastning, brug af
hukommelse og andre oplysninger om forbrug af ressourcer.

# Genveje #

* NVDA+Skift+E: Oplyser hukommelse i brug, processorbelastning og
  batteriinformation (hvis denne er tilgængelig).
* NVDA+Skift+1: Oplyser den gennemsnitlige processorbelastning, og hvis
  multicore-CPU'er er til stede, belastes hver kerne.
* NVDA+Skift+2/5: Oplyser brugt og total plads i fysisk og virtuel
  hukommelse.
* NVDA+Skift+3: Oplyser brugt og samlet plads på de statiske og flytbare
  drev.
* NVDA+Skift+4: Oplyser batteristatus i procent, opladestatus, resterende
  batteritid (hvis det ikke er ved at blive opladet) og endelig en advarsel,
  hvis batteriniveauet er lavt eller kritisk.
* NVDA+Skift+6: Oplyser CPU-arkitektur (32/64-bit) og Windows-version samt
  service pack numre.
* NVDA+Skift+7: Oplyser systemets oppetid.

Hvis du har NvDA 2013.3 eller nyere installeret, kan du ændre disse
genvejstaster.

## Brugsanvisninger ##

Denne tilføjelse erstatter ikke Jobliste og andre
systeminformationsprogrammer til Windows. Bemærk også følgende:

* CPU-brug bliver angivet for logiske processorer, ikke fysiske
  kerner. Dette har betydning for processorer, som bruger
  hypertrådningsteknologi. Her er antallet af CPU'er er det dobbelte af
  CPU-kernerne.
* Hvis der er en stor mængde af diskaktivitet som f.eks. Kopiering af store
  filer, kan der være forsinkelser, når der hentes oplysninger om diskbrug.
* Support for Windows XP from this add-on ended on December 31,
  2017. Support for Windows Server 2003, Vista and Server 2008 ended on June
  30, 2018.

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## Version 18.04

Version 18.04.x er den sidste version, der understøtter udgaver af Windows
ældre end 7 SP1.

* Sidste version der understøtter Windows Server 2003, Vista og Server 2008.
* Forbedret detektion af udgaver af Windows 10 og bedre til at skelne mellem
  offentlige builds af Windows og Insider Preview.

## Version 17.12

* Tilføjet support til 64-bit ARM-processorer på Windows 10.

## Version 17.09

Vigtigt: Version 17.09.x er den sidste version, der understøtter Windows XP.

* Sidste version til at køre på Windows XP.
* Windows 10 build 16278 og senere er anerkendt som Version 1709. En mindre
  revision for denne tilføjelse frigives, når version 1709 stabil build er
  udgivet.

## Version 17.07.1

* Genindførte understøttelse for Windows XP (understøttelse har ikke virket
  siden version 17.02).

## Version 17.05

* Annoncering af systemopetid (tid gået siden sidste opstart, NVDA + Shift
  +7).

## Version 17.02

* Opdateret psutil afhængighed til 5.0.1.
* Når du kontrollerer diskbrug, vil NVDA ikke længere præsentere en
  fejldialog på nogle systemer, hvor et flytbart medie ikke er korrekt
  genkendt (f.eks. Når et kort ikke er indsat i en kortlæser).

## Version 16.08

Begyndende med version 16.08 vises tilføjelsespakkens fremtidige udgivelser
som år.måned.revision.

* Forskellige revisioner af Windows 10 er nu korrekt genkendt (f.eks. 1607
  til build 14393).
* Windows 10 build revisions (efter installation af kumulative opdateringer)
  er korrekt genkendt (såsom 14393.51).
* Hvis du bruger Insider-preview-builds, genkendes dette.

## Ændringer i 4.5 ##

* Tilføjelsespakkens udviklingssted er flyttet til GitHub (kan findes på
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 er korrekt genkendt.

## Ændringer i4.0  ##

* Opdateret psutil dependency til 2.2.1.
* Stor forbedring af performance, under opsamlingen af oplysninger om
  CPU-belastning.
* Tilføjet understøttelse af genkendelse af Windows 10.
* I Windows 10 vil build-nummeret også blive annonceret.
* Du kan bruge Styring af tilføjelsesprogrammer til at få hjælp til
  tilføjelsesprogrammet.

## Ændringer i 3.1 ##

* Resource Monitor understøtter officielt Windows 8.1.
* Opdaterede oversættelser.

## Ændringer i 3.0 ##

* Opdateret psutil dependency til 1.2.1.
* Annoncering af Windows-version, CPU-arkitektur og service pack hvis nogen
  (NVDA+Shift+6).
* Mulighed for at ændre genvejstaster (NVDA 2013.3 eller senere).
* Muligt at kopiere individuelle ressourceoplysninger til udklipsholderen
  ved at ved at trykke på genvejstasten to gange.

## Ændringer i 2.4 ##

* Nye sprog: Kinesisk (simplificeret), ukrainsk.
* Opdaterede oversættelser.

## Ændringer i 2.3 ##

* Tilføjet bulgarsk oversættelse.

## Ændringer i 2.2 ##

* Tilføjet følgende oversættelser: Arabisk, aragonesisk, croatisk,
  hollandsk, finsk, fransk, galicisk, tysk, ungarsk, italiensk, japansk,
  koreansk, nepalesisk, polsk, portugisisk (Brasilien), russisk, slovakisk,
  slovensk, spansk, tamilsk og tyrkisk.

## Ændringer i 2.1 ##

* opdated psutil dependency til version 0.6.1.
* Rettet lang forsinkelse, når man bad om informationer om drev.
* Oprydning i koden.

## Ændringer i 2.0 ##

* Tilføjet understøttelse af oversættelse og oversættelseskommentarer.

## Ændringer i 1.0 ##

* Første udgivelse

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
