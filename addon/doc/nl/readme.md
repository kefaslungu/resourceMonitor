# Resource Monitor #

* Auteurs: Alex Hall, Joseph Lee, beqa gozalishvili en anderen
* Download [stabiele versie][1]

Deze add-on geeft informatie over CPU- en geheugengebruik en andere
statusinformatie.

Belangrijk: Resource Monitor 3.1 is niet compatibel met NVDA 2013.3 of
ouder. Als u 2013.3 of ouder gebruikt, gebruik dan aub Resource Monitor 3.0.

# Sneltoetsen #

* NVDA+Shift+E geeft gebruikt RAM-geheugen, gemiddeld processorgebruik en
  batterij-informatie indien beschikbaar
* NVDA+Shift+1 Geeft de gemiddelde processorbelasting en de belasting van
  elke kern als er een multicore processor aanwezig is
* NVDA+Shift+2 Geeft de totale en gebruikte ruimte van fysiek en virtueel
  RAM-geheugen
* NVDA+Shift+3 Geeft de gebruikte en totale ruimte voor vaste en
  verwisselbare schijven
* NVDA+Shift+4 Geeft batterijpercentage, oplaadstatus, resterende tijd (als
  er niet wordt opgeladen) en een waarschuwing als de batterij bijna leeg is
* NVDA+Shift+6 Geeft CPU-Architectuur 32/64-bit, de huidige Windows-versie
  en eventuele service packs.

Als u NvDA 2013.3 of later heeft geïnstalleerd, kunt u deze sneltoetsen
wijzigen.

## Opmerkingen voor gebruik ##

Deze add-on is geen vervanger van taakbeheer of andere Windows-programma's
die systeem informatie geven. Let ook op het volgende:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores.
* Er kan een korte vertraging zijn bij het verkrijgen van informatie over
  het processor-gebruik.

## Changes for 4.5 ##

* Add-on repository has moved to GitHub (can be found at
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 is properly recognized.

## Changes for 4.0 ##

* Updated psutil dependency to 2.2.1.
* Vastly improved performance when obtaining information on CPU load.
* Added support for recognition of Windows 10.
* In Windows 10, the build number of Windows will also be announced.
* You can use Add-ons Manager to access add-on help.

## Veranderingen in 3.1 ##

* Resource Monitor ondersteunt officieel Windows 8.1.
* Vertalingen bijgewerkt.

## Veranderingen in 3.0 ##

* Psutil afhankelijkheid bijgewerkt naar versie 1.2.1
* NVDA+Shift+6 kondigt de huidige Windows-versie, CPU-architectuur en
  eventuele service packs aan.
* Mogelijkheid om de sneltoetsen van de add-on te wijzigen (NVDA 2013.3 of
  later).
* Mogelijkheid om individuele informatie naar het klembord te kopiëren door
  commando's tweemaal in te drukken.

## Veranderingen in 2.4 ##

* Nieuwe vertalingen: Chinees (vereenvoudigd), Oekraïens.
* Vertalingen bijgewerkt.

## Veranderingen in 2.3 ##

* Bulgaarse vertaling toegevoegd.

## Veranderingen in 2.2 ##

* De volgende vertalingen toegevoegd: Arabisch, Aragonees, Croatisch,
  Nederlands, Fins, Frans, Galacisch, Duits, Hongaars, Italiaans, Japans,
  Koreaans, Nepali, Pools, Portugees (Brazilië), Russisch, Slowaaks,
  Sloveens, Spaans, Tamil en Turks

## Veranderingen in 2.1 ##

* Psutil afhankelijkheid bijgewerkt naar versie 0.6.1
* Vertraging bij het opvragen van schijf-informatie opgelost
* Code opgeruimd.

## Veranderingen in 2.0 ##

* Ondersteuning voor vertalingen en commentaar voor vertalers toegevoegd

## Veranderingen in 1.0 ##

* Eerste versie

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm [2]:
http://addons.nvda-project.org/files/get.php?file=rm-next
