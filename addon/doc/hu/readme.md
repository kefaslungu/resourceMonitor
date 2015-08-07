# Erőforrás-kilistázó #

* Fejlesztők: Alex Hall , Joseph Lee, beqa gozalishvili és további NVDA
  közreműködők
* Letöltés [Stabil verzió][1]

A kiegészítő hasznos információkat ad a memória, processzor, háttértár, és
az akkumulátor aktuális állapotáról.

Fontos: Az erőforrás-kilistázó legfrissebb verziója nem használható az NVDA
2013.3 vagy annál régebbi NVDA verziókkal. Ezekhez a kiegészítő 3.0-s
változatát ajánljuk.

# Billentyűparancsok #

* NVDA+shift+e Bemondja a memória és az átlagos processzor használatot, és a
  telep töltöttségi szintjét, ha elérhető.
* NVDA+shift+1 Bemondja az átlagos processzor terheltségét együttesen, és
  magokra lebontva egyaránt.
* NVDA+shift+2/NVDA+shift+5 Bemondja a teljes és foglalt fizikai és
  virtuális memória méretét.
* NVDA+shift+3 Bemondja a beépített és hordozható meghajtók teljes és
  lefoglalt méretét.
* NVDA+shift+4 Információkat ad a telep töltöttségéről, a hátralévő időről
  (ha nnincs hálózatra csatlakoztatva), figyelmeztet ha az akkumulátor
  töltöttsége kritikusan alacsony.
* NVDA+Shift+6 Megjeleníti a feltelepített Windows verzióját és szerviz
  csomagját, ha elérhető.

Ha az NVDA 2013.3-as vagy újabb verzióját használja, lehetősége van a
billentyűparancsok megváltoztatására.

## Használati megjegyzések ##

Ez a kiegészítő nem helyettesíti a feladatkezelőt és a többi rendszerfigyelő
Windows-os programot. Fontos megjegyezni a következőket:

* A processzor használata logikai processorok alapján történik, nem a
  fizikai magok szerint. Ez azoknál a processzoroknál észrevehető, amik a
  Hyper Threading technológiát használják, ahol a processzorok száma
  kétszerese a magszámnak.
* Egy kis időbe tellhet a processzor terheltségének lekkérése.

## A 4.0 verzió változásai ##

* A psutil függőség frissítése az 2.2.1. verzióra.
* Jelentősen javult a teljesítmény a processzor terhelésének lekérésekor.
* Hozzáadásra került a Windows 10 támogatása.
* Windows 10 esetén már elhangzik a build szám.
* A kiegészítő súgójának eléréséhez használja a Bővítmények kezelése
  menüpontot.

## A 3.1 verzió változásai ##

* Az Erőforrás-kilistázómár támogatja a Windows 8 operációs rendszert.
* Fordítások frissítése

## A 3.0 verzió változásai ##

* A psutil függőség frissítése az 1.2.1. verzióra.
* Bemondja a feltelepített Windows verzióját és szerviz csomagját, ha
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

[1]: http://addons.nvda-project.org/files/get.php?file=rm [2]:
http://addons.nvda-project.org/files/get.php?file=rm-next
