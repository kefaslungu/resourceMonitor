# Ressourcemonitor #

* Forfattere: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst og andre NVDA-bidragydere
* Download [stable version][1]
* NVDA compatibility: 2021.1 and beyond

Dette tilføjelsesprogram giver information om CPU-belastning, brug af
hukommelse og andre oplysninger om forbrug af ressourcer.

# Genveje

* NVDA+Shift+E: Oplyser hukommelse i brug, processorbelastning og
  batteriinformation, hvis denne er tilgængelig.
* NVDA+Shift+1: Oplyser den gennemsnitlige processorbelastning, og hvis
  multicore-CPU'er er til stede, vil brug for hver kerne også blive oplyst.
* NVDA+Shift+2/5: Oplyser brugt og total plads i fysisk og virtuel
  hukommelse.
* NVDA+Shift+3: Oplyser brugt og samlet plads på de statiske og flytbare
  drev.
* NVDA+Shift+4: Oplyser batteristatus i procent, opladestatus, resterende
  batteritid (hvis det ikke er ved at blive opladet) og en advarsel, hvis
  batteriniveauet er lavt eller kritisk.
* NVDA+Shift+6: Oplyser CPU-arkitektur (32/64-bit) og Windows-version samt
  service pack numre.
* NVDA+Shift+7: Oplyser systemets oppetid.

Hvis du har NvDA 2013.3 eller nyere installeret, kan du ændre disse
genvejstaster under NVDA-menuen/Indstillinger/Håndter kommandoer.

## Brugsanvisninger

Denne tilføjelse erstatter ikke Jobliste og andre
systeminformationsprogrammer til Windows. Bemærk også følgende:

* CPU-brug bliver angivet for logiske processorer, ikke fysiske
  kerner. Dette har betydning for processorer, som bruger
  hypertrådningsteknologi. Her er antallet af CPU'er er det dobbelte af
  CPU-kernerne.
* Hvis der er en stor mængde af diskaktivitet som f.eks. Kopiering af store
  filer, kan der være forsinkelser, når der hentes oplysninger om diskbrug.
* Denne tilføjelse kræver Windows 7 Service Pack 1 eller nyere.

Note on license: this add-on uses Psutil, licensed under 3-Clause BSD
License which is compatible with GNU General Public License.

## Version 21.10

* NVDA 2021.1 or later is required due to changes to NVDA that affects this
  add-on.

## Version 21.08

* Minimum Windows release requirement is now tied to NVDA releases.
* Windows builds 20348 and 22000 are recognized as Windows Server 2022 and
  Windows 11, respectively.
* On Insider Preview builds, Windows release such as "Windows 10" will not
  be used. Instead NvDA will announce "Windows Insider".
* On 64-bit systems, processor architecture (x64 or ARM64) will be announced
  as part of Windows version information.

## Version 21.04

* NVDA 2020.4 eller nyere er påkrævet.
* Opdaterede psutil dependency til 5.8.0.
* Når tilføjelseskommandoer trykkes to gange for at kopiere
  ressourceoplysninger til udklipsholderen, annoncerer NVDA
  ressourceoversigt, der kopieres.

## Version 21.01

* Opdaterede psutil dependency til 5.7.3.
* Forkortede beskeden Windows-version.
* I Windows 8.1 vil build.revision blive annonceret som en del af
  Windows-version beskeden, svarende til Windows 10.

## Version 20.09

* Systemets oppetid angives nu som dage, timer, minutter, sekunder.
* Windows Server Insider Preview build 20201 eller nyere genkendes korrekt
  som en Server Insider build.

## Version 20.07

* Windows 10 version 20H2 genkendes korrekt, når der anmodes om
  Windows-versionoplysninger (NVDA+Shift+6).
* Forenklet Windows 10-versionmeddelelse, dvs. Windows 10 ÅÅ/MM i stedet for
  Windows 10ver/ÅÅ/MM, når du trykker på NVDA+Shift+6.

## Version 20.06

* Løst mange problemer med kodningstil og potentielle fejl med Flake8.

## Version 20.04

* Opdateret psutil dependency til 5.7.0.

## Version 20.01

* NVDA 2019.3 eller nyere er påkrævet på grund af omfattende brug af Python
  3.

## Version 19.11

* Forbedret detektering af Windows Insider Preview builds, især til 20H1 og
  nyere.

## Version 19.07

* Opdateret psutil dependency til 5.6.3.
* Interne ændringer til meddelelse om batteristatus.

## Version 18.12

* Interne ændringer for at bedre kunne understøtte fremtidige versioner af
  NVDA.

## Version 18.10

* Koden er blevet gjort mere kompatibel med Python 3.
* Opdateret psutil dependency til 5.4.7.
* Når der oplyses diskkapacitet og hukommelsesforbrug, vil NVDA ikke længere
  fejle, hvis du bruger en computer eller en tjeneste med mere end en
  petabyte RAM eller diskplads.
* Værdier for hukommelse og diskbrug vises med op til to decimaler (fx 4,00
  GB i stedet for 4,0 GB).
* Forbedret detektering af Windows Insider Preview builds.

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

## Ændringer i 4.5

* Tilføjelsespakkens udviklingssted er flyttet til GitHub (kan findes på
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 er korrekt genkendt.

## Ændringer i4.0 

* Opdateret psutil dependency til 2.2.1.
* Stor forbedring af performance, under opsamlingen af oplysninger om
  CPU-belastning.
* Tilføjet understøttelse af genkendelse af Windows 10.
* I Windows 10 vil build-nummeret også blive annonceret.
* Du kan bruge Styring af tilføjelsesprogrammer til at få hjælp til
  tilføjelsesprogrammet.

## Ændringer i 3.1

* Resource Monitor understøtter officielt Windows 8.1.
* Opdaterede oversættelser.

## Ændringer i 3.0

* Opdateret psutil dependency til 1.2.1.
* Annoncering af Windows-version, CPU-arkitektur og service pack hvis nogen
  (NVDA+Shift+6).
* Mulighed for at ændre genvejstaster (NVDA 2013.3 eller senere).
* Muligt at kopiere individuelle ressourceoplysninger til udklipsholderen
  ved at ved at trykke på genvejstasten to gange.

## Ændringer i 2.4

* Nye sprog: Kinesisk (simplificeret), ukrainsk.
* Opdaterede oversættelser.

## Ændringer i 2.3

* Tilføjet bulgarsk oversættelse.

## Ændringer i 2.2

* Tilføjet følgende oversættelser: Arabisk, aragonesisk, croatisk,
  hollandsk, finsk, fransk, galicisk, tysk, ungarsk, italiensk, japansk,
  koreansk, nepalesisk, polsk, portugisisk (Brasilien), russisk, slovakisk,
  slovensk, spansk, tamilsk og tyrkisk.

## Ændringer i 2.1

* Opdaterede psutil dependency til version 0.6.1.
* Rettet lang forsinkelse, når man bad om informationer om drev.
* Oprydning i koden.

## Ændringer i 2.0

* Tilføjet understøttelse for oversættelse og oversættelseskommentarer.

## Ændringer i 1.0

* Første udgivelse

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
