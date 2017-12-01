# Resource Monitor (ressourceovervågning) #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala and other
  NVDA contributors
* Download [stabil version][1]

This add-on gives information about CPU load, memory usage and other
resource usage information.

# Genvejstaster  #

* NVDA+Shiftj+e viser brugt RAM, gennemsnitlig processorbelastning og
  batterioplysninger, hvis de er til rådighed.
* NVDA+Shift+1 viser gennemsnitlig processorbelastning, og hvis der er flere
  kerner tilstede, belastningen for hver kerne.
* NVDA+Shift+2/5 giver brugt og total plads i fysisk og virtuel hukommelse.
* NVDA+Shift+3 giver brugt og samlet plads på faste og flytbare drev.
* NVDA+Shift+4 giver batteristatus i procent, opladestatus, resterende
  batteritid (hvis det ikke er ved at blive opladet) og endelig en advarsel,
  hvis batteriniveauet er lavt eller kritisk.
* NVDA+Shift+6 giver CPU-arkitektur, 32/64 bit, Windows-version og numre på
  service packs.
* NVDA+Shift+7 presents the system's uptime.

Hvis du har installeret NVDA 2013.3 eller senere, kan du ændre disse
genvejstaster.

## Bemærkninger om brug ##

Dette tilføjelsesprogram erstatter ikke joblisten eller andre
systemoplysninger.

* CPU-brug bliver angivet for logiske processorer, ikke fysiske
  kerner. Dette har betydning for processorer, som bruger
  hyper-threading. Her er antallet af processorer det dobbelte af antallet
  af processoerkerner.
* If there is heavy disk activity such as copying large files, there might
  be delays when obtaining disk usage information.
* Support for Windows XP from this add-on will end on December 31,
  2017. Support for Windows Server 2003 and Windows Vista will end on June
  30, 2018.

## Version 17.12

* Added support for 64-bit ARM processors on Windows 10.

## Version 17.09

Important: Version 17.09.x is the last version to support Windows XP.

* Last version to run on Windows XP.
* Windows 10 build 16278 and later is recognized as Version 1709. A minor
  revision for this add-on will be released once Version 1709 stable build
  is released.

## Version 17.07.1

* Reintroduce support for Windows XP (broken since version 17.02).

## Version 17.05

* Announcement of system uptime (time passed since last boot; NVDA+Shift+7).

## Version 17.02

* Updated psutil dependency to 5.0.1.
* When checking disk usage, NVDA will no longer present an error dialog on
  some systems where a removable media is not properly recognized (such as
  when a card isn't inserted into a card reader).)

## Version 16.08

Starting with version 16.08, add-on releases will be shown as
year.month.revision.

* Various revisions of Windows 10 are now properly recognized (such as 1607
  for build 14393).
* Windows 10 build revisions (after installing cumulative updates) are
  properly recognized (such as 14393.51).
* If using Insider Preview builds, this fact is recognized.

## Changes for 4.5 ##

* Add-on repository has moved to GitHub (can be found at
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 is properly recognized.

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
