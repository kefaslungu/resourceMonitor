# Resource Monitor (ressourceovervågning) #

* Forfattere: Alex Hall, Joseph Lee, beqa gozalishvili og andre bidragydere
  til NVDA.
* Download [stabil version][1]

Dette tilføjelsesprogram giver information om CPU-belastning, brug af
hukommelse og andre oplysninger om forbrug af ressourcer.

Vigtigt: Resource Monitor 3.1 er ikke kompatibel med NVDA 2013.3 eller
tidligere. Hvis du bruger NVDA 2013.3 eller tidligere, så brug venligst
Resource Monitor 3.0.

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

Hvis du har installeret NVDA 2013.3 eller senere, kan du ændre disse
genvejstaster.

## Bemærkninger om brug ##

Dette tilføjelsesprogram erstatter ikke joblisten eller andre
systemoplysninger.

* CPU-brug bliver angivet for logiske processorer, ikke fysiske
  kerner. Dette har betydning for processorer, som bruger
  hyper-threading. Her er antallet af processorer det dobbelte af antallet
  af processoerkerner.
* Der kan være en kort forsinkelse, når man beder om oplysninger om brug af
  processor.

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

[1]: http://addons.nvda-project.org/files/get.php?file=rm [2]:
http://addons.nvda-project.org/files/get.php?file=rm-next
