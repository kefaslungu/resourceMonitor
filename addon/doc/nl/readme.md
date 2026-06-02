# Resource Monitor

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## Sneltoetsen

* NVDA+Shift+E geeft gebruikt RAM-geheugen, gemiddeld processorgebruik en batterij-informatie indien beschikbaar
* NVDA+Shift+1 Geeft de gemiddelde processorbelasting en de belasting van elke kern als er een multicore processor aanwezig is
* NVDA+Shift+2 Geeft de totale en gebruikte ruimte van fysiek en virtueel RAM-geheugen
* NVDA+Shift+3 Geeft de gebruikte en totale ruimte voor vaste en verwisselbare schijven
* NVDA+Shift+4 Geeft batterijpercentage, oplaadstatus, resterende tijd (als er niet wordt opgeladen) en een waarschuwing als de batterij bijna leeg is
* NVDA+Shift+6 Geeft CPU-Architectuur 32/64-bit, de huidige Windows-versie en eventuele service packs.
* NVDA+Shift+7 presents the system's uptime.

Als u NvDA 2013.3 of later heeft geïnstalleerd, kunt u deze sneltoetsen wijzigen.

## Opmerkingen voor gebruik

Deze add-on is geen vervanger van taakbeheer of andere Windows-programma's die systeem informatie geven. Let ook op het volgende:

* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores.
* If there is heavy disk activity such as copying large files, there might be delays when obtaining disk usage information.
* Support for Windows XP from this add-on ended on December 31, 2017. Support for Windows Server 2003, Vista and Server 2008 ended on June 30, 2018.
