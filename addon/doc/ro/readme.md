# Resursele Monitorului #

* Autori: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala și alți
  contribuitori NVDA
* Descărcați [versiunea stabilă][1]

Acest supliment oferă informații despre media procesorului, utilizarea
memoriei și alte resurse de utilizare a informației.

# Scurtături #

* NVDA+Shift+E Spune ramul utilizat, activitatea medie a procesorului și
  informații despre starea bateriei dacă este disponibilă.
* NVDA+Shift+1 Spune activitatea medie de procesare și în cazul în care
  procesoarele multicore sunt prezente, activitatea fiecărui nucleu.
* NVDA+Shift+2/5 Spune spațiul utilizat și cel total pentru ramul fizic și
  cel virtual.
* NVDA+Shift+3 Spune spațiul total și cel utilizat al driverelor statice și
  eliminabile.
* NVDA+Shift+4 Spune procentajul bateriei, starea de încărcare, timpul rămas
  (dacă nu se încarcă) și un avertisment dacă bateria este descărcată sau
  critică.
* NVDA+Shift+6 Spune arhitectura procesorului, 32/64-biți, versiunea de
  Windows și numerele pachetelor de servicii.
* NVDA+Shift+7 prezintă rularea sistemului.

Dacă aveți NvDA 2013.3 sau mai nou instalat, Puteți modifica aceste comenzi
rapide.

## Notele utilizării ##

Acest add-on nu înlocuiește managerul de activități și alte informații ale
programelor de sistem pentru Windows. De asemenea, notați următoarele:

* Utilizarea procesorului este dată pentru procesoare logice, nu nuclee
  fizice. Acest lucru este vizibil pentru procesoare care utilizează
  Hyper-Threading în cazul în care numărul de procesoare este de două ori
  mai mare decât numărul de nuclee CPU.
* În cazul în care există o activitate grea pe disc, cum ar fi copierea
  fișierelor de mari dimensiuni, ar putea exista întârzieri la obținerea
  informațiilor de utilizare a discului.
* Suportul pentru Windows XP de la acest supliment va înceta pe 31 decembrie
  2017. Suporturile pentru Windows Server 2003 și pentru Windows Vista vor
  înceta pe 30 iunie 2018.

## Versiunea 17.09

Important: Versiunea 17.09.x este ultima care suportă Windows XP.

* Ultima versiune care rulează pe Windows XP.
* Windows 10 build 16278 și mai nou este recunoscut ca versiunea 1709. O
  revizie minoră pentru acest supliment va fi lansată odată ce versiunea
  1709 Stable Build va fi lansată.

## Versiunea 17.07.1

* A fost reintrodus suportul pentru Windows XP (eliminat din versiunea
  17.02).

## Versiunea 17.05

* Anunțarea rulării sistemului (timp trecut de la ultima încărcare;
  NVDA+Shift+7).

## Versiunea 17.02

* Actualizat la dependența psutil 5.0.1.
* La verificarea utilizării discului, NVDA nu va mai prezenta un dialog de
  eroare pe unele sisteme unde un media eliminabil nu este recunoscut
  corespunzător (cum ar fi atunci când un card nu este inserat într-un
  cititor de card).)

## Versiunea 16.08

Începând cu versiunea 16.08, lansările add-on-ului vor fi anuale.

* Diferite versiuni ale Windows 10 sunt acum recunoscute în mod
  corespunzător (cum ar fi 1607 pentru build 14393). 
* Versiunile Windows 10 build (după instalarea actualizărilor cumulative)
  sunt acum recunoscute în mod corespunzător (cum ar fi 14393.51).
* Dacă folosiți versiunile builds pentru Insideri, acest fapt este
  recunoscut.

## Modificări aduse în versiunea 4.5 ##

* Repository-ul add-on-ului a fost mutat pe GitHub (poate fi găsit la
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 este recunoscut în mod corespunzător.

## Modificări aduse în versiunea 4.0 ##

* Actualizat la dependența psutil 2.2.1.
* A fost îmbunătățită considerabil performanța la obținerea informațiilor cu
  privire la activitatea medie a procesorului.
* A fost îmbunătățit suportul pentru recunoașterea lui Windows 10.
* În Windows 10, numărul build-ului  Windows-ului va fi, de asemenea,
  anunțat.
* Puteți folosi managerul de add-on-uri pentru a accesa ghidul add-on-ului.

## Modificări aduse în versiunea 3.1 ##

* Resource Monitor suportă oficialWindows 8.1.
* Au fost actualizate traducerile.

## Modificări aduse în versiunea 3.0 ##

* Actualizat la dependența psutil to 1.2.1.
* Anunțarea versiunii curente a Windows-ului, arhitectura procesorului și
  pachetul de servicii dacă există (NVDA+Shift+6).
* Abilitatea de a modifica combinațiile de taste ale add-on-ului(NVDA 2013.3
  sau mai nou).
* Abilitatea de a copia informația resurselor individuale pe planșetă
  apăsând comenzile resursei de două ori.

## Modificări aduse în versiunea 2.4 ##

* Limbi noi: Chineză (simplificată), Ucraineană,.
* Au fost actualizate traducerile.

## Modificări aduse în versiunea 2.3 ##

* A fost adăugată traducerea în limba Bulgară.

## Modificări aduse în versiunea 2.2 ##

* Au fost adăugate următoarele traduceri: Arabă, Aragoneză, Croată,
  Olandeză, Finlandeză, Franceză, Galiciană, Germană, Maghiară, Italiană,
  Japoneză, Coreeană, Nepaleză, Poloneză, Portugheză (Brazilia), Rusă,
  Slovacă, Slovenă, Spaniolă, Tamilă și Turcă.

## Modificări aduse în versiunea 2.1 ##

* A fost actualizată dependența psutil la versiunea 0.6.1.
* A fost reparată întârzierea lungă atunci când se obțin informațiile
  driverelor.
* Curățarea codului.

## Modificări aduse în versiunea 2.0 ##

* A fost adăugat suportul pentru traduceri și comentariile pentru acestea.

## Modificări aduse în versiunea 1.0 ##

* Lansarea inițială

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
