# Ressourcemonitor

* Forfattere: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst og andre NVDA-bidragydere

Dette tilføjelsesprogram giver information om CPU-belastning, brug af hukommelse og andre oplysninger om forbrug af ressourcer.

## Genveje

All commands support speech on demand mode.

* NVDA+Shift+E: Oplyser hukommelse i brug, processorbelastning og batteriinformation, hvis denne er tilgængelig.
* NVDA+Shift+1: Oplyser den gennemsnitlige processorbelastning, og hvis multicore-CPU'er er til stede, vil brug for hver kerne også blive oplyst.
* NVDA+Shift+2/5: Oplyser brugt og total plads i fysisk og virtuel hukommelse.
* NVDA+Shift+3: Oplyser brugt og samlet plads på de statiske og flytbare drev.
* NVDA+Shift+4: Oplyser information om den trådløse forbindelse, ssid-navn og signalstyrke, eller ingen ssid, hvis der ikke er nogen tilgængelig.
* NVDA+Shift+6: Oplyser CPU-arkitekturen, WIndows version og servicepakke.
* NVDA+Shift+7: Oplyser systemets oppetid.
* Unassigned: presents information about the graphics processing unit (GPU; unavailable in secure mode).
* Unassigned: presents graphics processing unit (GPU memory usage information; unavailable in secure mode).

Du kan ændre disse genveje via dialogen "Håndter kommandoer".

## Brugsanvisninger

Denne tilføjelse erstatter ikke Jobliste og andre systeminformationsprogrammer til Windows. Bemærk også følgende:

* Apart from overall resource usage command (NVDA+Shift+E), pressing other commands twice will copy resource usage information to the clipboard.
* Ressourceoplysninger kan ikke kopieres til udklipsholderen, hvis tilføjelsen kører på sikre skærme.
* CPU-brug bliver angivet for logiske processorer, ikke fysiske kerner. Dette har betydning for processorer, som bruger hypertrådningsteknologi. Her er antallet af CPU'er er det dobbelte af CPU-kernerne. På nogle nyere CPU'er, vil denne teknologi ikke nødvendigvis være aktiveret.
* Hvis der er en stor mængde af diskaktivitet som f.eks. Kopiering af store filer, kan der være forsinkelser, når der hentes oplysninger om diskbrug.
* GPU information is given for Nvidia GPU's.
* Når der annoncerer processorarkitekturoplysninger, henviser "x86" og "AMD64" til henholdsvis 32-bit og 64-bit (x64) Intel- og AMD-processorer.
* Installing the add-on on Windows 10/11 LTSC is not supported.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
