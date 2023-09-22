# Prati stanje resursa (Resource Monitor) #

* Autori: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst i drugi NVDA doprinositelji
* Preuzmi [stabilnu verziju][1]
* NVDA kompatibilnost: 2022.4 i novije verzije

Ovaj dodatak daje informacije o opterećenosti procesora, korištenju memorije
i druge informacije o korištenju resursa.

# Prečaci

* NVDA+šift+E: Prikazuje korištenje ram memorije, prosječno opterećenje
  procesora i informacije o stanju baterije, ako su dostupne.
* NVDA+šift+1: Prikazuje prosječnu opterećenost procesora i ako postoje
  višejezgreni procesori, prikazuje opterećenje svake jezgre.
* NVDA+šift+2/5: Prikazuje korišteni i ukupni kapacitet fizičke I virtualne
  ram memorije.
* NVDA+šift+3: Prikazuje korišteni i ukupni prostor na statičnim i
  prenosivim diskovima.
* NVDA+šift+4: Prikazuje postotak baterije, stanje punjenja, preostalo
  vrijeme (ako se ne puni), te upozorenje, ako je baterija slaba ili skoro
  prazna.
* NVDA+šift+6: Prikazuje arhitekturu procesora, Windows verziju i broj
  service paketa.
* NVDA+šift+7: Prikazuje vrijeme neprekidnog rada sustava.
* NVDA+šift+8: prikazuje informacije o bežičnoj vezi, ime i snagu ssid-a ili
  ne prikazuje ssid ako nije dostupan.

Tipkovničke prečace je moguće mijenjati putem dijaloškog okvira za ulazne
geste.

## Upute za primjenu

Ovaj dodatak ne zamijenjuje upravljača zadataka i druge programe za
informacije o sustavu Windows. Važno je znati i sljedeće:

* Podaci o resursima ne mogu se kopirati u međuspremnik ako se dodatak
  pokreće na sigurnim ekranima.
* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores. On some newer computers, not all CPU
  cores will have hyper-threading enabled.
* Ako je u tijeku velika aktivnost diska, kao što je kopiranje velikih
  datoteka, moguća su kašnjenja prilikom dobivanja informacija o korištenju
  diska.
* Kada se najavljuju informacije o arhitekturi procesora, „x86” i „AMD64”
  odnose se na 32-bitne i 64-bitne (x64) Intel odnosno AMD procesore.
* Ovaj dodatak zahtijeva Windows 10 ili noviju verziju.

Napomena o licenci: ovaj dodatak koristi Psutil, licenciran pod BSD licencom
s 3 klauzule koja je kompatibilna s GNU Općom javnom licencom.

## Version 23.09

* NVDA will no longer log startup error messages on Windows Server systems
  when wireless capability modules are unavailable.

## Version 23.06

* Situation where resourceMonitor doesn't work properly due to
  unavailability of wireless adapters has been fixed.

## Version 23.05.1

wlanReporter NVDA-addon is now part of resourceMonitor!

* The old way of checking for wireless connections has been replaced by the
  windows API from wlanReporter: https://github.com/kvark128/WlanReporter/ .

	* After speaking SSID name and strength, NVDA will also now tell you the
	  security type of your network.
	* NVDA will now alert you when you connect and disconnect from a wireless
	  network.
	* NVDA will now alert you when wireless connections is turned on or off.

## Verzija 23.05

* added the ability to detect and present the state of the connected
  wireless network.

	* Najavljuje ime priključenog bežičnog SSID-a.
	* Announces the strength of the ssid
	* Najavljuje da SSID nije pronađen ako nijedan nije otkriven.

## Verzija 23.03

* Zahtijeva NVDA 2022.4 ili noviju verziju.
* Potreban je sustav Windows 10 21H2 (aktualizirana verzija iz studenog
  2021./izgradnja 19044) ili novija verzija.

## Verzija 23.01

* Zahtijeva NVDA 2022.3 ili noviju verziju.
* Zahtijeva Windows 10 ili noviju verziju, jer od siječnja 2023. Microsoft
  više ne pordržava Windows 7, 8 i 8.1.
* Aktualizirana je psutil ovisnost na 5.9.4.
* NVDA će najaviti arhitekturu procesora (x86/AMD64/ARM64) kao dio
  informacije Windows verzije.
* Na sustavima s jednom jezgrom, NVDA više neće najavljivati opterećenje
  jezgre CPU-a jer je prosječno opterećenje CPU-a isto kao i opterećenje
  jezgre.

## Verzija 22.03

Verzija 22.03 je posljednje izdanje koje će podržavati sustav Windows 7
Service Pack 1, 8 i 8.1.

* Potrebna je NVDA verzija 2021.3 ili novija.
* Poruka upozorenja će se prikazati kad pokušaš instalirati dodatak na
  sustavima Windows 7, 8 i 8.1.
* Aktualizirana je psutil zavisnost na 5.9.0.

## Verzija 22.01

* Potrebna je NVDA verzija 2021.2 ili novija.

## Verzija 21.10

* Potrebna je NVDA verzija 2021.1 ili novija zbog promjena u NVDA čitaču
  koje utječu na ovaj dodatak.

## Verzija 21.08

* Minimum Windows release requirement is now tied to NVDA releases.
* Windows builds 20348 and 22000 are recognized as Windows Server 2022 and
  Windows 11, respectively.
* On Insider Preview builds, Windows release such as "Windows 10" will not
  be used. Instead NvDA will announce "Windows Insider".
* On 64-bit systems, processor architecture (x64 or ARM64) will be announced
  as part of Windows version information.

## Verzija 21.04

* Potrebna je NVDA verzija 2020.4 ili novija.
* Ažurirana je psutil zavisnost na 5.8.0.
* When pressing add-on commands twice to copy resource information to
  clipboard, NVDA will announce resource summary that is being copied.

## Verzija 21.01

* Ažurirana je psutil zavisnost na 5.7.3.
* Skraćena je poruka Windows verzije.
* On Windows 8.1, build.revision will be announced as part of Windows
  version message, similar to Windows 10.

## Verzija 20.09

* Vrijeme neprekidnog rada sustava sada se navodi kao dani, sati, minute,
  sekunde.
* Windows Server Insider Preview izgradnja 20201 ili novija, ispravno se
  prepoznaje kao Server Insider izgradnja.

## Verzija 20.07

* Windows 10 verzija 20H2 pravilno se prepoznaje prilikom dohvaćanja
  podataka o Windows verziji (NVDA+šift+6).
* Pojednostavljena poruka verzije sustava Windows 10, tj. Windows 10 YYMM
  umjesto Windows 10verYYMM kad se pritisne NVDA+šift+6.

## Verzija 20.06

* Riješeni su mnogi problemi sa stilom kodiranja i potencijalnih grešaka sa
  Flake8.

## Verzija 20.04

* Ažurirana je psutil zavisnost na 5.7.0.

## Verzija 20.01

* Potrebna je verzija NVDA 2019.3 zbog iskorištavanja mogućnosti Pythona 3.

## Verzija 19.11

* Poboljšano otkrivanje za Windows Insider Preview gradnje, posebice za 20H1
  i nadalje.

## Verzija 19.07

* Ažurirana je psutil zavisnost na 5.6.3.
* Interna promjena za naredbu najavljivanja stanja baterija.

## Verzija 18.12

* Unutarnje promjene, kako bi se podržala buduća NVDA izdanja.

## Verzija 18.10

* Kod je sada kompatibilniji s Python 3.
* Ažurirana je psutil zavisnost na 5.4.7.
* Prilikom dobivanja kapaciteta diska i upotrebe memorije, NVDA više neće
  pogriješiti, ako koristi računalo ili uslugu s više od petabajta RAM-a ili
  veličine diska.
* Vrijednosti za memoriju i upotrebu diska prikazuju se s najviše dva
  decimalna mjesta (npr. 4,00 GB umjesto 4,0 GB).
* Poboljšano otkrivanje za Windows Insider Preview gradnje.

## Verzija 18.04

Verzija 18.04.x je posljednje izdanje koje će podržavati verzije Windowsa
starije od Windowsa 7 SP1.

* Posljednje izdanje koje podržava Windows Server 2003, Vistu i Server 2008.
* Poboljšano otkrivanje za Windowsa 10 izdanja i bolje razlikovanje između
  javnih i Insider Preview izdanja.

## Verzija 17.12

* Dodana podrška za 64-bitne ARM procesore na Windowsima 10.

## Verzija 17.09

Važno: Verzija 17.09 je posljednje izdanje koje podržava Windows XP.

* Zadnja verzija koja radi na Windowsima XP.
* Windows 10 verzija 16278 i novija prepoznata je kao Verzija 17.09. Manje
  izdanje ovog dodatka bit će objavljeno nakon objave stabilne verzije
  2017.9.

## Verzija 17.07.1

* Ponovo uvedena podrška za Windows XP (prekinuta od verzije 17.02).

## Verzija 17.05

* Najava trajanja pokretanja sustava (vrijeme proteklo od zadnjeg pokretanja
  računala); NVDA+Shift+7).

## Verzija 17.02

* Ažurirana je psutil zavisnost na 5.0.1.
* Tijekom provjere upotrebljivosti diska, NVDA više neće prikazivati
  dijaloški okvir pogreške na nekim sustavima gdje izmjenjivi medij nije
  ispravno prepoznat (primjerice kada kartica nije umetnuta u čitač
  kartica.)

## Verzija 16.08

Počevši od verzije 16.08, izdanja ovog dodatka prikazivat će se u formatu
godina.mjesec.izdanje.

* Različite verzije Windowsa 10 se sada ispravno prepoznaju (kao što je 1607
  za verziju 14393).
* Revizije Windows 10 gradnji (nakon instalacije kumulativnih ažuriranja)
  ispravno se prepoznaju (kao što je 14.393.51).
* Ako koristite Insider Preview gradnje, ta se činjenica prepoznaje.

## Promjene u verziji 4.5

* Repozitorij dodatka premješten je na GitHub (možete ga pronaći na
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016. se ispravno prepoznaje.

## Promjene u verziji 4.0

* Ažurirana je opsutil zavisnost na 2.2.1.
* Izrazito poboljšana učinkovitost pri dobivanju informacija o opterećenosti
  procesora.
* Dodana podrška za prepoznavanje Windowsa 10.
* U Windowsima 10, broj verzije Windowsa također će biti izgovoren.
* Moguće je koristiti Upravljač za dodatke za pristup pomoći.

## Promjene u verziji 3.1

* „Prati stanje resursa” službeno podržava Windows 8.1.
* Ažurirani prijevodi.

## Promjene u verziji 3.0

* Ažurirana psutil zavisnost na 1.2.1.
* Izgovor trenutne verzije Windowsa, arhitekture procesora i servisnog
  paketa ako postoji (NVDA+Shift+6).
* Mogućnost promjene tipkovnih prečica (NVDA verzija 2013.3 ili novija).
* Mogućnost kopiranja pojedinačnih informacija o resursima u međuspremnik
  pritiskom naredbi resursa dva puta.

## Promjene u verziji 2.4

* Novi jezici: kineski (pojednostavljeni), ukrajinski.
* Ažurirani prijevodi.

## Promjene u verziji 2.3

* Dodan prijevod na bugarski jezik.

## Promjene u verziji 2.2

* Dodani prijevodi na sljedeće jezike: arapski, aragonski, hrvatski,
  nizozemski, finski, francuski, galicijski, njemački, mađarski, talijanski,
  japanski, korejski, nepaljski, poljski, portugalski (Brazil), ruski,
  slovački, slovenski, španjolski, tamilski i turski.

## Promjene u verziji 2.1

* Ažurirana psutil zavisnost na verziju 0.6.1.
* Riješen problem velikog kašnjenja pri dobivanju informacija o particijama.
* Čišćenje koda.

## Promjene u verziji 2.0

* Dodana podrška za prijevode i komentare prijevoda.

## Promjene u verziji 1.0

* Prvo izdanje

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
