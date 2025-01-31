# Monitor resursa #

* Autori: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst i drugi NVDA saradnici

Ovaj dodatak pruža informacije o opterećenju procesora, iskorišćenoj
memoriji i druge informacije o korišćenju resursa.

# Prečice

All commands support speech on demand mode.

* NVDA+Šift+E: Prikazuje iskorišćeni RAM, prosečno opterećenje procesora i
  informacije o bateriji ako su dostupne.
* NVDA+Šift+1: Prikazuje prosečno opterećenje procesora i ako su prisutni
  procesori sa više jezgara opterećenost svakog jezgra.
* NVDA+Šift+2/5: Prikazuje iskorišćeni i ukupan prostor za fizički i
  virtuelni RAM.
* NVDA+Šift+3: prikazuje iskorišćeni i ukupan prostor statičkih diskova i
  diskova koji se mogu ukloniti.
* NVDA+Šift+4: prikazuje procenat baterije, status punjenja, preostalo vreme
  (ako se baterija ne puni) i upozorenje ako je baterija slaba ili kritična.
* NVDA+Šift+6: prikazuje arhitekturu procesora, Windows verziju i brojeve
  servisnog paketa.
* NVDA+Šift+7: prikazuje vreme rada sistema.
* NVDA+Šift+8: prikazuje informacije o bežičnoj mreži, ssid ime i jačinu,
  ili bez ssid-a ako nema povezane mreže.

Možete promeniti ove prečice iz dijaloga ulaznih komandi.

## Napomene o korišćenju

Ovaj dodatak ne menja upravljača zadacima i druge programe za informacije o
sistemu za Windows. Takođe imajte sledeće na umu:

* Informacije o resursima se ne mogu kopirati u privremenu memoriju ako
  pokrećete dodatak na bezbednim ekranima.
* Iskorišćenost procesora se pruža za logičke procesore, ne fizička
  jezgra. Ovo se može uočiti na procesorima koji koriste Hyper-Threading na
  kojima je broj procesora dva puta veći u odnosu na broj jezgara
  procesora. Na nekim novijim računarima, neće sva jezgra procesora imati
  hyper-threading omogućen.
* Ako je u toku zahtevna aktivnost na disku kao što je kopiranje velikih
  datoteka, može doći do kašnjenja prilikom preuzimanja informacija o
  iskorišćenosti diskova.
* Kada se izgovaraju informacije o arhitekturi procesora, "x86" i "AMD64" se
  odnose na 32-bitne i 64-bitne (x64) Intel i AMD procesore.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.

Napomena o licenci: ovaj dodatak koristi Psutil, koji je licenciran pod
3-Clause BSD licencom koja je kompatibilna sa GNU opštom javnom licencom.

## Version 25.02

* Restored limited support for Windows 8.1.
* Improved accuracy of used and total memory information announcement
  (@danstiv).
* NVDA will no longer appear to freeze briefly when performing memory usage
  command (NVDA+Shift+2/5) the first time after starting NVDA.
* Windows Insider Preview releases are no longer reported as "Windows
  Insider".

## Version 24.08

* NVDA 2024.2 or later is required. This allows psutil dependency to be
  removed from the add-on as NVDA includes it.
* Updated psutil dependency to the version included with NVDA 2024.2
  (6.0.0).
* Ruff replaces Flake8 as code linter.

## Verzija 24.05

* NVDA 2024.1 ili noviji je neophodan.
* NVDA će prepoznati bežične mreže sa WPA3 metodama autentikacije kao što su
  simultaneous authentication of equals (SAE).

## Verzija 24.04

* Ažurirana psutil biblioteka na 5.9.8.
* Dodata podrška za režim govora na zahtev kako bi informacije o resursima
  mogle da se izgovore u ovom režimu.

## Verzija 23.11

* Vraćena psutil biblioteka na 5.9.4 zbog problema sa izgovorom iskorišćene
  memorije.

## Verzija 23.10

* Ažurirana psutil biblioteka na 5.9.5.

## Verzija 23.09

* NVDA više neće evidentirati greške pri pokretanju na Windows Server
  sistemima kada mogućnosti bežičnog modula nisu dostupne.

## Verzija 23.06

* Greška u kojoj Monitor resursa ne radi ispravno kada bežični adapteri nisu
  dostupni je ispravljena.

## Verzija 23.05.1

wlanReporter NVDA dodatak je sada deo Monitora resursa!

* Stari način provere bežičnih mreža je zamenjen Windows API-em iz
  wlanReportera: https://github.com/kvark128/WlanReporter/ .

	* Nakon što izgovori SSID ime i jačinu, NVDA će vam sada takođe reći vrstu
	  bezbednosti vaše mreže.
	* NVDA će vas sada upozoriti kada se povežete ili prekinete vezu sa
	  bežičnom mrežom.
	* NVDA će vas sada upozoriti kada se bežične mreže omoguće ili onemoguće.

## Verzija 23.05

* dodata mogućnost da se prepozna i prikaže stanje povezanih bežičnih mreža.

	* Izgovara ime povezanog bežičnog SSID-a.
	* Izgovara jačinu SSID-a
	* Izgovara SSID nije pronađen ako nijedan nije otkriven.

## Verzija 23.02

* NVDA 2022.4 ili noviji je neophodan.
* Windows 10 21H2 (ažuriranje iz novembra 2021. podverzija 19044) ili noviji
  je neophodan.

## Verzija 23.01

* NVDA 2022.3 ili noviji je neophodan.
* Windows 10 ili noviji je neophodan budući da Microsoft više ne podržava
  Windows 7, 8 i 8.1 od januara 2023.
* Ažurirana psutil biblioteka na 5.9.4.
* NVDA će izgovoriti stvarnu arhitekturu procesora (x86/AMD64/ARM64) kao deo
  informacija o Windows verziji.
* Na sistemima sa jednim jezgrom, NVDA više neće izgovarati opterećenost
  procesora budući da je prosečna opterećenost procesora ista kao
  opterećenost jezgra.

## Verzija 22.03

Verzija 22.03 je poslednja stabilna verzija koja podržava Windows 7 servisni
paket 1, 8 i 8.1.

* NVDA 2021.3 ili noviji je neophodan.
* Prikazaće se poruka kada pokušate da instalirate dodatak na Windowsu 7, 8
  i 8.1.
* Ažurirana psutil biblioteka na 5.9.0.

## Verzija 22.01

* NVDA 2021.2 ili noviji je neophodan.

## Verzija 21.10

* NVDA 2021.1 ili noviji je neophodan zbog NVDA promena koje utiču na ovaj
  dodatak.

## Verzija 21.08

* Najmanja zahtevana Windows verzija sada zavisi od NVDA verzije.
* Windows podverzije 20348 i 22000 se prepoznaju kao Windows Server 2022 i
  Windows 11.
* Na insajder verzijama za testiranje, Windows verzija kao što je "Windows
  10" se neće koristiti. Umesto toga NVDA će izgovoriti "Windows Insider".
* Na 64-bitnim sistemima, arhitektura procesora (x64 ili ARM64) će biti
  izgovorena kao deo informacija o Windows verziji.

## Verzija 21.04

* NVDA 2020.4 ili noviji je neophodan.
* Ažurirana psutil biblioteka na 5.8.0.
* Kada se pritisnu komande dodatka dva puta kako bi se kopirale informacije
  o resursima u privremenu memoriju, NVDA će izgovoriti kratak opis resursa
  koji se kopira.

## Verzija 21.01

* Ažurirana psutil biblioteka na 5.7.3.
* Skraćena poruka o verziji Windowsa.
* Na Windowsu 8.1, verzija.podverzija će biti izgovoreno kao deo poruke o
  Windows verziji, slično Windowsu 10.

## Verzija 20.09

* Vreme rada sistema se sada daje u danima, satima, minutima i sekundama.
* Windows Server insajder verzija za testiranje 20201 ili novija se sada
  ispravno prepoznaje kao Server insajder verzija.

## Verzija 20.07

* Windows 10 verzija 20H2 se ispravno prepoznaje kada se preuzimaju
  informacije o verziji Windowsa (NVDA+Šift+6).
* Pojednostavljena poruka o verziji Windowsa 10 to jest Windows 10 GGMM
  umesto Windows 10 verGGMM kada se pritisne NVDA+Šift+6.

## Verzija 20.06

* Ispravljeni brojni problemi u stilizovanju koda i potencijalne greške uz
  Flake8.

## Verzija 20.04

* Ažurirana psutil biblioteka na 5.7.0.

## Verzija 20.01

* NVDA 2019.3 ili noviji je neophodan zbog značajnog korišćenja Pythona 3.

## Verzija 19.11

* Poboljšano prepoznavanje Windows insajder verzija za testiranje, posebno
  za 20H1 i novije.

## Verzija 19.07

* Ažurirana psutil biblioteka na 5.6.3.
* Interne promene za komandu izgovora statusa baterije.

## Verzija 18.12

* Interne promene kako bi se podržale buduće NVDA verzije.

## Verzija 18.10

* Kod je kompatibilniji za Python 3.
* Ažurirana psutil biblioteka na 5.4.7.
* Kada se preuzima kapacitet diska ili iskorišćenost memorije, NVDA više
  neće izbacivati greške ako se koristi računar ili servis sa više od
  petabajta RAM-a ili veličine diska.
* Vrednosti iskorišćenosti memorije ili diskova se prikazuju sa do dva
  decimalna mesta (na primer 4.00 GB umesto 4.0 GB).
* Poboljšano prepoznavanje Windows insajder verzija za testiranje.

## Verzija 18.04

Verzija 18.04.x je poslednja verzija koja podržava Windows verzije starije
od 7 SP1.

* Poslednja verzija koja podržava Windows Server 2003, Vista i Server 2008.
* Bolje prepoznavanje Windows 10 verzija i razlikovanje između javnih
  verzija i insajder verzija za testiranje.

## Verzija 17.12

* Dodata podrška za 64-bitne ARM procesore na Windowsu 10.

## Verzija 17.09

Važno: Verzija 17.09.x je poslednja verzija koja podržava Windows XP.

* Poslednja verzija koja se pokreće na Windowsu XP.
* Windows 10 podverzija 16278 i novije se prepoznaju kao verzija
  1709. Sitnija revizija za ovaj dodatak će biti objavljena nakon što se
  stabilna verzija 1709 objavi.

## Verzija 17.07.1

* Vraća podršku za Windows XP (neispravna od verzije 17.02).

## Verzija 17.05

* Izgovor vremena rada sistema (vreme koje je proteklo od poslednjeg
  pokretanja računara; NVDA+Šift+7).

## Verzija 17.02

* Ažurirana psutil biblioteka na 5.0.1.
* Kada se proverava iskorišćenost diskova, NVDA više neće prikazivati
  dijalog greške na nekim sistemima kada se disk koji se može ukloniti ne
  prepoznaje ispravno (na primer kada se kartica ne ubaci u čitač kartica).

## Verzija 16.08

Počevši od verzije 16.08, verzije dodatka će biti imenovane kao
godina.mesec.revizija.

* Različite revizije Windowsa 10 se sada ispravno prepoznaju (kao što su
  1607 za podverziju 14393).
* Windows 10 revizije podverzija (nakon što se instaliraju kumulativna
  ažuriranja) se ispravno prepoznaju (kao što su 14393.51).
* Ako se koriste insajder verzije za testiranje, ovo se prepoznaje.

## Promene za 4.5

* Repozitorijum dodatka je premešten na GitHub (može se pronaći na
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 se ispravno prepoznaje.

## Promene za 4.0

* Ažurirana psutil biblioteka na 2.2.1.
* Značajno poboljšane performanse kada se preuzimaju informacije o
  opterećenosti procesora.
* Dodata podrška za prepoznavanje Windowsa 10.
* U Windowsu 10, podverzija Windowsa će se takođe izgovoriti.
* Možete koristiti upravljača dodacima da biste videli pomoć za dodatak.

## Promene za 3.1

* Monitor resursa zvanično podržava Windows 8.1.
* Ažurirani prevodi.

## Promene za 3.0

* Ažurirana psutil biblioteka na 1.2.1.
* Izgovor trenutne verzije Windowsa, arhitekture procesora i servisnog
  paketa ako postoji (NVDA+Šift+6).
* Mogućnost promene prečica dodatka (NVDA 2013.3 ili noviji).
* Mogućnost kopiranja pojedinačnih informacija o resursima u privremenu
  memoriju pritiskanjem komandi za izgovor resursa dva puta.

## Promene za 2.4

* Novi jezici: kineski (pojednostavljeni), ukrajinski.
* Ažurirani prevodi.

## Promene za 2.3

* Dodat bugarski prevod.

## Promene za 2.2

* Dodati sledeći prevodi: arapski, aragonski, hrvatski, holandski, finski,
  francuski, galski, nemački, mađarski, italijanski, japanski, korejski,
  nepalski, poljski, portugalski(Brazil), ruski, slovački, slovenački,
  španski, tamilski i turski.

## Promene za 2.1

* Ažurirana psutil biblioteka na verziju 0.6.1.
* Ispravljeno duže kašnjenje kada se preuzimaju informacije o diskovima.
* Čišćenje koda.

## Promene za 2.0

* dodata podrška za prevođenje i komentari za prevodioce.

## Promene za 1.0

* Prva verzija

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
