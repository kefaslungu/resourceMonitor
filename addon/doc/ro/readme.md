# Resource Monitor #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst and other NVDA contributors
* Descărcați [versiunea stabilă][1]
* NVDA compatibility: 2019.3 to 2020.4

Acest supliment oferă informații despre media procesorului, utilizarea
memoriei și alte resurse de utilizare a informației.

# Scurtături #

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

If you have NVDA 2013.3 or later installed, you can change these shortcut
keys via input gestures dialog.

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
* This add-on requires Windows 7 Service Pack 1 or later.

## Version 20.09

* System uptime is now given as days, hours, minutes, seconds.
* Windows Server Insider Preview build 20201 or later is properly recognized
  as a Server Insider build.

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

## Versiunea 18.10

* Codul a fost făcut mai compatibil cu Python 3.
* S-a actualizat la dependența psutil 5.0.7.
* La obținerea capacității discului și a utilizării memoriei, NVDA nu va mai
  da erori folosind un computer sau un service cu mai mult de un petabyte de
  ram sau spațiu pe disc.
* Valorile pentru memorie și pentru utilizarea discului sunt afișate cu până
  la două zecimale (e.x. 4.00 GB în loc de 4.0 GB).
* S-a îmbunătățit detectarea compilărilor de Insider ale Windows 10.

## Versiunea 18.04

Versiunea 17.09.x este ultima care suportă Windows XP.

* Ultima versiune care suportă Windows Server 2003, Vista și Server 2008.
* O detectare mai bună a versiunilor de Windows 10 și diferențierea dintre
  compilările publice și cele Insider Preview.

## Versiunea 17.12

* Suport adăugat pentru procesoarele ARM pe 64 de biți din Windows 10.

## Versiunea 17.09

Important: Versiunea 17.09.x este ultima care suportă Windows XP.

* Ultima versiune care rulează pe Windows XP.
* Windows 10 build 16278 și mai nou este recunoscut ca versiunea 1709. O
  revizie minoră pentru acest supliment va fi lansată odată ce versiunea
  1709 Stable Build va fi lansată.

## Versiunea 17.07.1

* Reintroducerea suportului pentru Windows XP (eliminat din versiunea
  17.02).

## Versiunea 17.05

* Anunțarea rulării sistemului (timp trecut de la ultima încărcare;
  NVDA+Shift+7).

## Versiunea 17.02

* S-a actualizat la dependența psutil 5.0.1.
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

* S-a actualizat la dependența psutil 2.2.1.
* S-a îmbunătățit considerabil performanța la obținerea informațiilor cu
  privire la activitatea medie a procesorului.
* Suport adăugat pentru recunoașterea lui Windows 10.
* În Windows 10, numărul build-ului  Windows-ului va fi, de asemenea,
  anunțat.
* Puteți folosi managerul de add-on-uri pentru a accesa ghidul add-on-ului.

## Modificări aduse în versiunea 3.1 ##

* Resource Monitor suportă oficialWindows 8.1.
* S-au actualizat traducerile.

## Modificări aduse în versiunea 3.0 ##

* S-a actualizat la dependența psutil to 1.2.1.
* Anunțarea versiunii curente a Windows-ului, arhitectura procesorului și
  pachetul de servicii dacă există (NVDA+Shift+6).
* Abilitatea de a modifica combinațiile de taste ale add-on-ului(NVDA 2013.3
  sau mai nou).
* Abilitatea de a copia informația resurselor individuale pe planșetă
  apăsând comenzile resursei de două ori.

## Modificări aduse în versiunea 2.4 ##

* Limbi noi: Chineză (simplificată), Ucraineană,.
* S-au actualizat traducerile.

## Modificări aduse în versiunea 2.3 ##

* S-a adăugat traducerea bulgărească.

## Modificări aduse în versiunea 2.2 ##

* S-au adăugat următoarele traduceri: Arabă, Aragoneză, Croată, Olandeză,
  Finlandeză, Franceză, Galiciană, Germană, Maghiară, Italiană, Japoneză,
  Coreeană, Nepaleză, Poloneză, Portugheză (Brazilia), Rusă, Slovacă,
  Slovenă, Spaniolă, Tamilă și Turcă.

## Modificări aduse în versiunea 2.1 ##

* S-a actualizată dependența psutil la versiunea 0.6.1.
* S-a reparat întârzierea lungă atunci când se obțin informațiile
  driverelor.
* Curățarea codului.

## Modificări aduse în versiunea 2.0 ##

* s-a adăugat suportul pentru traduceri și comentariile pentru acestea.

## Modificări aduse în versiunea 1.0 ##

* Lansarea inițială

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
