# Resource Monitor #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala and other
  NVDA contributors
* Download [stabiele versie][1]
* NVDA compatibility: 2017.4 to 2019.2

This add-on gives information about CPU load, memory usage and other
resource usage information.

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
* NVDA+Shift+7 presents the system's uptime.

Als u NvDA 2013.3 of later heeft geïnstalleerd, kunt u deze sneltoetsen
wijzigen.

## Opmerkingen voor gebruik ##

Deze add-on is geen vervanger van taakbeheer of andere Windows-programma's
die systeem informatie geven. Let ook op het volgende:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores.
* If there is heavy disk activity such as copying large files, there might
  be delays when obtaining disk usage information.
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

Version 18.04.x is the last release to support Windows releases earlier than
7 SP1.

* Last release to support Windows Server 2003, Vista and Server 2008.
* Better detection of Windows 10 releases and distinguishing between public
  and Insider Preview builds.

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

[1]: https://addons.nvda-project.org/files/get.php?file=rm
