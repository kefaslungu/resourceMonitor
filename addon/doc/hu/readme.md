# Erőforrás-kilistázó #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst and other NVDA contributors
* Letöltés [Stabil verzió][1]
* NVDA compatibility: 2019.3 to 2020.2

This add-on gives information about CPU load, memory usage and other
resource usage information.

# Billentyűparancsok #

* NVDA+Shift+E: presents used ram, average processor load, and battery info
  if available.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's
  are present the load of each core.
* NVDA+Shift+2/5: presents the used and total space for both physical and
  virtual ram.
* NVDA+Shift+3: presents the used and total space of the static and
  removable drives.
* NVDA+Shift+4: presents battery percentage, charging status, remaining time
  (if not charging), and a warning if the battery is low or critical.
* NVDA+Shift+6: presents CPU Architecture 32/64-bit and Windows version and
  service pack numbers.
* NVDA+Shift+7: presents the system's uptime.

If you have NvDA 2013.3 or later installed, you can change these shortcut
keys via input gestures dialog.

## Használati megjegyzések ##

Ez a kiegészítő nem helyettesíti a feladatkezelőt és a többi rendszerfigyelő
Windows-os programot. Fontos megjegyezni a következőket:

* A processzor használata logikai processzorok alapján történik, nem a
  fizikai magok szerint. Ez azoknál a processzoroknál észrevehető, amelyek a
  Hyper Threading technológiát használják, ahol a processzorok száma
  kétszerese a magszámnak.
* If there is heavy disk activity such as copying large files, there might
  be delays when obtaining disk usage information.
* This add-on requires Windows 7 Service Pack 1 or later.

## Version 20.07

* Windows 10 Version 20H2 is properly recognized when obtaining Windows
  version information (NVDA+Shift+6).
* Simplified Windows 10 version message i.e. Windows 10 YYMM instead of
  Windows 10verYYMM when pressing NVDA+Shift+6.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Updated psutil dependency to 5.7.0.

## Version 20.01

* NVDA 2019.3 or later is required due to extensive use of Python 3.

## Version 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1
  and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

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

## A 4.5 verzió változásai ##

* A bővítmény tárolóját áthelyezték a GitHubra (Megtalálható a
  https://github.com/josephsl/resourcemonitor oldalon).
* A bővítmény már megfelelően felismeri a Windows server 2016-ot.

## A 4.0 verzió változásai ##

* A psutil függőség frissítése az 2.2.1. verzióra.
* Jelentősen javult a teljesítmény a processzor terhelésének lekérésekor.
* Hozzáadtáka Windows 10 támogatását.
* Windows 10 esetén már elhangzik a build szám.
* A kiegészítő súgójának eléréséhez használja a Bővítménykezelőt.

## A 3.1 verzió változásai ##

* Az Erőforrás-kilistázómár támogatja a Windows 8 operációs rendszert.
* Fordítások frissítése

## A 3.0 verzió változásai ##

* A psutil függőség frissítése az 1.2.1. verzióra.
* Bemondja a feltelepített Windows verzióját és szervizcsomagját, ha
  elérhető. (NVDA+Shift+6)
* Lehetőség van a kiegészítő billentyűparancsainak megváltoztatására (NVDA
  2013.3-tól)
* Lehetőség van az egyéni erőforrás információkat a vágólapra másolni egy
  kiválasztott erőforrás billentyűparancsának kétszeri lenyomásával.

## A 2.4. verzió változásai ##

* Új nyelvek: egyszerűsített kínai, ukrán.
* Fordítások frissítése

## A 2.3. verzió változásai ##

* Bolgár fordítás hozzáadása.

## A 2.2. verzió változásai ##

* Új fordítások: Arab, Aragóniai, Horvát, Holland, Finn, Francia, Galíciai,
  Német, Magyar, Olasz, Japán, Koreai, Nepáli, Lengyel, Portugál
  (Brazíliai), Orosz, Szlovák, Szlovén, Spanyol, Tamil és Török.

## A 2.1. verzió változásai ##

* A psutil függőség frissítése a 0.6.1 verzióra.
* A hosszú várakozás kiküszöbölése a meghajtókról való információk
  beszerzése közben.
* Kódtisztítás.

## A 2.0 verzió változásai ##

* Fordítások támogatása, és fordítási megjegyzések hozzáadása.

## Az 1.0 változásai ##

* Első kiadás

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
