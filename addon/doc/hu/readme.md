# Erőforrás-kilistázó #

* Fejlesztők: Alex Hall , Joseph Lee, beqa gozalishvili és további NVDA
  közreműködők
* Letöltés [Stabil verzió][1]

A kiegészítő hasznos információkat ad a memória, processzor, háttértár és az
akkumulátor aktuális állapotáról.

# Billentyűparancsok #

* NVDA+shift+e Bemondja a memória és az átlagos processzor használatot és a
  telep töltöttségi szintjét, ha elérhető.
* NVDA+shift+1 Bemondja az átlagos processzor terheltségét együttesen és
  magokra lebontva egyaránt.
* NVDA+shift+2/NVDA+shift+5 Bemondja a teljes és foglalt fizikai és
  virtuális memória méretét.
* NVDA+shift+3 Bemondja a beépített és hordozható meghajtók teljes és
  lefoglalt méretét.
* NVDA+shift+4 Információkat ad a telep töltöttségéről, a hátralévő időről
  (ha nincs hálózatra csatlakoztatva), figyelmeztet, ha az akkumulátor
  töltöttsége kritikusan alacsony.
* NVDA+Shift+6 Megjeleníti a feltelepített Windows verzióját és
  szervizcsomagját, ha elérhető.

Ha az NVDA 2013.3-as vagy újabb verzióját használja, lehetősége van a
billentyűparancsok megváltoztatására.

## Használati megjegyzések ##

Ez a kiegészítő nem helyettesíti a feladatkezelőt és a többi rendszerfigyelő
Windows-os programot. Fontos megjegyezni a következőket:

* A processzor használata logikai processzorok alapján történik, nem a
  fizikai magok szerint. Ez azoknál a processzoroknál észrevehető, amelyek a
  Hyper Threading technológiát használják, ahol a processzorok száma
  kétszerese a magszámnak.
* If there is heavy disk activity such as copying large files, there might
  be delays when obtaining disk usage information.

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
