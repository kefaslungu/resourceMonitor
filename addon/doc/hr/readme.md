# Prikaz Resursa #

* Autori: Alex Hall, Joseph Lee, Beqa Gozalishvili, Tuukka Ojala I drugi
  NVDA doprinositelji
* Preuzmi [stabilnu inačicu][1]

Ovaj dodatak daje informacije o učitavanju procesora, korištenju memorije i
druge informacije o korištenju resursa.

# Kratice #

* NVDA+Shift+E Prikazuje korištenje ram memorije, prosječno opterećenje
  procesora i informacije o stanju baterije ako su dostupne.
* NVDA+Shift+1 Prikazuje prosječno opterećenje procesora i ako postoje
  višejezgreni procesori, prikazuje opterećenje svake jezgre.
* NVDA+shift+2/5 Prikazuje iskorišten i ukupni kapacitet fizičke I virtualne
  ram memorije.
* NVDA+Shift+3 Prikazuje iskorišten i ukupni prostor na statičnim i
  prenosivim diskovima.
* NVDA+Shift+4 Prikazuje postotak baterije, status punjenja, preostalo
  vrijeme (ako se ne puni), te upozorenje ako je baterija prazna ili
  kritična.
* NVDA+Shift+6 Prikazuje strukturu procesora (32-64-bitni), inačicu Windowsa
  i broj service packa.
* NVDA+Shift+7: Prikazuje ažuriranost sustava.

Ako imate instaliranu NVDA inačicu 2013.3 ili noviju, možete izmijeniti ove
tipkovničke kratice.

## Upute za korištenje  ##

Ovaj dodatak ne zamjenjuje upravitelj zadacima i druge programe za
informacije o sustavu Windows. Također upamtite sljedeće:

* Informacije o korištenju procesora dane su za logičke procesore, ne za
  fizičke jezgre. To se može primijetiti kod procesora koji koriste
  Hyper-Threading gdje je broj procesora dvostruko veći od broja jezgri.
* Ako je u tijeku velika aktivnost diska, kao što je kopiranje velikih
  datoteka, moguća su kašnjenja prilikom dobivanja informacija o korištenju
  diska.
* Podrška ovog dodatka za Windows XP završila je 31. prosinca 2017. Podrška
  za Windows Server 2003, Vistu i 2008. završit će 30. lipnja 2018.

## Inačica 18.04

Inačica 18.04.x je posljednje izdanje koje će podržavati inačice Windowsa
starije od Windowsa 7 SP1. 

* Posljednje izdanje koje podržava Windows Server 2003, Vistu i Server 2008.
* Poboljšana detekcija za izdanja Windowsa 10 i bolje razlikovanje između
  javnih i Insider Preview izdanja.

## Inačica 17.12

* Dodana podrška za 64-bitne ARM procesore na Windowsima 10.

## Inačica 17.09

Važno: Inačica 17.09 je posljednje izdanje koje podržava Windows XP.

* Zadnja inačica koja radi na Windowsima XP.
* Windows 10 inačica 16278 i novija prepoznata je kao Inačica 17.09. Manje
  izdanje ovog dodatka bit će objavljeno nakon objave stabilne inačice
  2017.9.

## Inačica 17.07.1

* Ponovno uvedena podrška za Windows XP (prekinuta od inačice 17.02).

## Inačica 17.05

* Izgovor vremena rada sustava (vrijeme proteklo od zadnjeg pokretanja
  računala); NVDA+Shift+7).

## Inačica 17.02

* Ažurirana je psutil zavisnost na 5.0.1.
* Tijekom provjere upotrebljivosti diska, NVDA više neće prikazivati
  dijaloški okvir pogreške na nekim sustavima gdje izmjenjivi medij nije
  ispravno prepoznat (primjerice kada kartica nije umetnuta u čitač
  kartica.) 

## Inačica 16.08

Počevši od inačice 16.08, izdanja ovog dodatka prikazivat će se u formatu
godina.mjesec.izdanje.

* Različite inačice Windowsa 10 sada su ispravno prepoznate (kao što je 1607
  za inačicu 14393).
* Izmjene u Windowsima 10 (nakon instalacije kumulativnih ažuriranja)
  ispravno su prepoznate (kao što je 14.393.51).
* Ako koristite Insider Preview inačice, to je također prepoznato.

## Promjene u inačici 4.5 ##

* Repozitorij dodatka premješten je na GitHub (možete ga pronaći na
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016. ispravno je prepoznat.

## Promjene u inačici 4.0 ##

* Ažurirana je opsutil zavisnost na 2.2.1.
* Izrazito poboljšana učinkovitost pri dobivanju informacija o opterećenosti
  procesora.
* Dodana podrška za prepoznavanje Windowsa 10.
* U Windowsima 10, broj inačice Windowsa također će biti izgovoren.
* Možete koristiti Upravitelj Dodacima za pristup pomoći.

## Promjene u inačici 3.1 ##

* Resource Monitor službeno podržava Windows 8.1.
* Ažurirani prijevodi.

## Promjene u inačici 3.0 ##

* Ažurirana psutil zavisnost na 1.2.1.
* Izgovor trenutne inačice Windowsa, arhitekture procesora i servisnog
  paketa ako postoji (NVDA+Shift+6).
* Mogućnost promjene tipkovnih prečica (NVDA inačica 2013.3 ili novija).
* Mogućnost kopiranja pojedinačnih informacija o resursima u međuspremnik
  pritiskom naredbi resursa dva puta.

## Promjene u inačici 2.4 ##

* Novi jezici: kineski (pojednostavljeni), ukrajinski.
* Ažurirani prijevodi.

## Promjene u inačici 2.3 ##

* Dodan prijevod na bugarski jezik.

## Promjene u inačici 2.2 ##

* Dodani prijevodi na sljedeće jezike: arapski, aragonski, hrvatski,
  nizozemski, finski, francuski, galicijski, njemački, mađarski, talijanski,
  Japanski, Korejski, Nepaljski, Poljski, portugalski (Grazil), ruski,
  slovački, slovenski, španjolski, tamilski i turski.

## Promjene u inačici 2.1 ##

* Ažurirana psutil zavisnost na inačicu 0.6.1.
* Riješen problem velikog kašnjenja pri dobivanju informacija o particijama.
* Čišćenje koda.

## Promjene u inačici 2.0 ##

* Dodana podrška za prijevode i komentari.

## Promjene u inačici 1.0 ##

* Prvo izdanje

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
