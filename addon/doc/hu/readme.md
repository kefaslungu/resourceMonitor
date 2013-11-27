# Erőforrás-kilistázó #

* Fejlesztők: Alex Hall , Joseph Lee, beqa gozalishvili és további NVDA
  közreműködők
* Stabil verzió: [2.4][1]
* Fejlesztői verzió: [3.0-dev][2]

A kiegészítő hasznos információkat ad a memória, processzor, háttértár, és
az akkumulátor aktuális állapotáról.

# Billentyűparancsok #

* NVDA+shift+e Bemondja a memória és az átlagos processzor használatot, és a
  telep töltöttségi szintjét (ha elérhető),
* NVDA+shift+1 Bemondja az átlagos processzor terheltségét, majd ezt magokra
  lebontva is,
* NVDA+shift+2/5 Bemondja a teljes és foglalt fizikai és virtuális memória
  méretét,
* NVDA+shift+3 Bemondja a beépített és hordozható meghajtók teljes és
  lefoglalt méretét,
* NVDA+shift+4 Információkat ad a telep töltöttségéről, figyelmeztet ha az
  akkumulátor töltöttsége kritikusan alacsony,
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or
  64-bit) and service pack if any (version 3.0-dev).

## Használati megjegyzések ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Changes for 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## A 2.4. verzió változásai ##

* Új nyelvek: egyszerűsített kínai, ukrán.
* Fordítások frissítése

## A 2.3. verzió változásai ##

* Bolgár fordítás hozzáadása.

## A 2.2. verzió változásai ##

* Új fordítások: Arab, Aragóniai, Horvát, Holland, Finn, Francia, Galíciai,
  Német, Magyar, Olasz, Japán, Kóreai, Nepáli, Lengyel, Portugál
  (Brazíliai), Orosz, Szlovák, Szlovén, Spanyol, Tamil és Török.

## A 2.1. verzió változásai ##

* A psutil függőség frissítése a 0.6.1 verzióra.
* A hosszú várakozás kiküszöbölése a meghajtókról való információk
  beszerzése közben.
* A %s kicserélése {barátságosváltozónevekre}
* Kis kódtisztítás

## A 2.0 verzió változásai ##

* Fordítások támogatása, és fordítási megjegyzések hozzáadása.

## Az 1.0 változásai ##

* Első kiadás

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
