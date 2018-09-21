# Resource Monitor #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala and other
  NVDA contributors
* Stiahnuť [stabilnú verziu][1]

This add-on gives information about CPU load, memory usage and other
resource usage information.

# Klávesové skratky #

* NVDA+Shift+E oznámy využitie pamäte ram, priemerné zaťaženie procesora a
  stav batérie, ak je dostupná.
* NVDA+Shift+1 oznámy vyťaženie procesora a jednotlivých jadier.
* NVDA+Shift+2/5 povie využitú a celkovú pamäť pre fyzickú a virtuálnu ram
  pamäť.
* NVDA+Shift+3 povie využité a celkové miesto pre pevné a pamäťové disky
  pripojené k počítaču.
* NVDA+Shift+4 oznámy stav batérie v percentách, stav napájania, zostávajúci
  čas (ak sa vybíja) a prípadne upozornenie ak je batéria vybytá alebo v
  kritickom stave.
* NVDA+Shift+6 prečíta architektúru procesora (32 alebo 64 bit), verziu
  Windows a Service packu.
* NVDA+Shift+7 presents the system's uptime.

Ak používate verziu NVDA 2013.3 alebo novšiu, môžete si skratky upraviť.

## Všimnite si ##

Tento doplnok nie je náhradou za správcu úloh a iné programy na zisťovanie
informácii v systéme Windows. Vezmite preto navedomie tieto skutočnosti:

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

## Zmeny vo verzii 3.1 ##

* Resource monitor oficiálne podporuje Windows 8.1
* Aktualizované preklady.

## Zmeny vo verzii 3.0 ##

* Aktualizovaná knižnica psutil na verziu 1.2.1.
* Oznamovanie architektúri procesora (32 aebo 64 bit), verzie windows a
  Service Packu ((NVDA+Shift+6).
* Možnosť zmeniť klávesové skratky (NVDA 2013 a vyššie).
* Možnosť kopírovať údaje do schránky dvojitým stlačením danej skratky.

## Zmeny vo verzii 2.4 ##

* Nové jazyky: Ukrajinčina, zjednodušená Čínština
* Aktualizované preklady.

## Zmeny vo verzii 2.3 ##

* pridaný preklad do bulharčiny

## Zmeny vo verzii 2.2 ##

* Pridané preklady: Arabčina, Aragónčina, chorvátčina, holandčina, fínčina,
  francúzština, Galijcíjčina, nemčina, maďarčina, taliančina, japončina,
  kórejčina, nepálčina, poľština, brazílska portugalčina, ruština,
  slovenčina, slovinčina, španielčina, Tamilčina a turečtina.

## Zmeny vo verzii 2.1 ##

* Aktualizovaná knižnica psutil na verziu 0.6.1.
* Skrátený čas na zistenie kapacity a miesta na diskoch.
* drobné úpravy v kóde.

## Zmeny vo verzii 2.0 ##

* Podpora pre preklady vrátane komentárov pre prekladateľov.

## Zmeny vo verzii 1.0 ##

* prvé vydanie

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
