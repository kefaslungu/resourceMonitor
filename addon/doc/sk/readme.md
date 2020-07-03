# Monitor prostriedkov #

* Autori: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst a ďalší.
* Stiahnuť [stabilnú verziu][1]
* NVDA compatibility: 2019.3 to 2020.2

Poskytuje informácie o zaťažení procesora, stave pamäte a o iných zdrojoch.

# Klávesové skratky #

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

## Všimnite si ##

Tento doplnok nie je náhradou za správcu úloh a iné programy na zisťovanie
informácií v systéme Windows. Vezmite preto navedomie tieto skutočnosti:

* Využitie procesora je vypočítané pre logické procesory, nie pre fyzické
  jadrá. Toto je dôležité pri procesoroch, ktoré používajú viacero vláken,
  kde počet procesorov je dvojnásobný, ako počet jadier.
* Ak práve kopírujete veľké súbory, zistenie informácie o využití disku môže
  chvíľu trvať.
* Tento doplnok funguje na systémoch Windows od verzie 7 Servicepack 1.

## Version 20.07

* Windows 10 Version 20H2 is properly recognized when obtaining Windows
  version information (NVDA+Shift+6).
* Simplified Windows 10 version message i.e. Windows 10 YYMM instead of
  Windows 10verYYMM when pressing NVDA+Shift+6.

## Verzia 20.06

* Opravené drobné chyby v kóde.

## Verzia 20.04

* Aktualizované knižnice psutil na verziu 5.7.0.

## Verzia 20.01

* Keďže doplnok vyžaduje Python 3, Vyžaduje sa NVDA od verzie2019.3

## Verzia 19.11

* Vylepšená detekcia verzii Windows insider, hlavne od verzie 20H1.

## Verzia 19.07

* Aktualizované knižnice psutil na verziu 5.6.3.
* Interné zmeny oznamovania stavu batérie.

## Verzia 18.12

* Interné zmeny ako príprava na nové verzie NVDA.

## Verzia 18.10

* Kód upravený na Python 3.
* Aktualizovaná knižnica psutil na verziu 5.4.7.
* NVDA viac nevypíše chybu, ak sa pokúsite zistiť využitie disku a máte viac
  ako petabitový disk.
* Hodnoty pre kapacitu disku a pamäť sú interpretované s presnosťou na dve
  miesta (nie 4,0 ale 4,00).
* Zlepšené zisťovanie verzii Windows insider.

## Verzia 18.04

Verzia 18.04.x je posledná, ktorá podporuje systémy staršie ako Windows 7
Servicepack1.

* Posledná verzia, ktorá podporuje Windows Server 2003, Vista a Server 2008.
* Vylepšená detekcia verzií Windows 10 vrátane rozlišovania medzi verejnými
  a testovacími verziami.

## Verzia 17.12

* Pridaná podpora pre 64-bitové ARM procesory v systéme Windows 10.

## Version 17.09

Dôležité: Verzia 17.09.x je posledná, ktorá podporuje Windows XP.

* Posledná verzia, ktorá funguje so systémom Windows XP.
* Windows 10 od verzie 16278 je rozpoznaný ako Verzia 1709. Mierne upravená
  verzia tohto doplnku bude vydaná po vydaní verejnej stabilnej verzie
  Windowsu 1709.

## Verzia 17.07.1

* Obnovená podpora pre Windows XP (nebola dostupná od verzie 17.02)

## Verzia 17.05

* Pridaná možnosť zistiť čas behu  systému od posledného reštartu
  (nvda+shift+7).

## Verzia 17.02

* Aktualizovaná knižnica psutil na verziu 5.0.1.
* NVDA viac nezobrazí chybu, ak pri kontrole kapacity disku nie je možné
  načítať všetky externé disky (napríklad pamäťovú kartu, ktorá aktuálne nie
  je vložená).

## Verzia 16.08

Od verzie 16.08 používame na číslovanie verzii systém rok.mesiac.

* Doplnok dokáže rozpoznať rôzne verzie Windows 10 (napríklad 1607 pre
  zostavu 14393).
* Správne sú rozpoznané zostavy Windows 10 po inštalácii kumulatívnych
  aktualizácii (napríklad 14393.51).
* Doplnok upozorňuje, ak používate vývojové verzie Windows (program
  Insider).

## Zmeny vo verzii 4.5 ##

* Doplnok presunutý na GitHub (https://github.com/josephsl/resourcemonitor).
* Správne je rozpoznávaný Windows server 2016.

## Zmeny vo verzii 4.0 ##

* Aktualizovaná knižnica psutil na verziu 2.2.1.
* Upravené zisťovanie zaťaženia procesora.
* Pridaná podpora pre rozpoznávanie Windows 10.
* V systéme Windows 10 je oznamované aj číslo zostavi.
* Pomocníka k doplnku nájdete v správcovi doplnkov.

## Zmeny vo verzii 3.1 ##

* Resource monitor oficiálne podporuje Windows 8.1
* Aktualizované preklady.

## Zmeny vo verzii 3.0 ##

* Aktualizovaná knižnica psutil na verziu 1.2.1.
* Oznamovanie architektúri procesora (32 alebo 64 bit), verzie windows a
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
