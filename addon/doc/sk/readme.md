# Monitor prostriedkov #

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst and other NVDA contributors
* Stiahnuť [stabilnú verziu][1]
* NVDA compatibility: 2022.4 and later

Poskytuje informácie o zaťažení procesora, stave pamäte a o iných zdrojoch.

# Klávesové skratky

* NVDA+Shift+E: oznámy využitie pamäte ram, priemerné zaťaženie procesora a
  stav batérie, ak je dostupná.
* NVDA+Shift+1: oznámy vyťaženie procesora a jednotlivých jadier.
* NVDA+Shift+2/5: Oznámi využitú a celkovú fyzickú a virtuálnu pamäť.
* NVDA+Shift+3: Oznámi využité a celkové miesto pre pevné a pamäťové disky
  pripojené k počítaču.
* NVDA+Shift+4: oznámy stav batérie v percentách, stav napájania,
  zostávajúci čas (ak sa vybíja) a prípadne upozornenie ak je batéria vybytá
  alebo v kritickom stave.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service
  pack numbers.
* Nvda+shift+7: Oznámi čas behu systému od posledného reštartu.
* NVDA+Shift+8: presents information on the wireless connection, ssid name
  and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Všimnite si

Tento doplnok nie je náhradou za správcu úloh a iné programy na zisťovanie
informácií v systéme Windows. Vezmite preto navedomie tieto skutočnosti:

* Resource information cannot be copied to clipboard if running the add-on
  in secure screens.
* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores. On some newer computers, not all CPU
  cores will have hyper-threading enabled.
* Ak práve kopírujete veľké súbory, zistenie informácie o využití disku môže
  chvíľu trvať.
* When announcing processor architecture information, "x86" and "AMD64"
  refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

Note on license: this add-on uses Psutil, licensed under 3-Clause BSD
License which is compatible with GNU General Public License.

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

## Version 23.05

* added the ability to detect and present the state of the connected
  wireless network.

	* Announces the name of the connected wireless SSID.
	* Announces the strength of the ssid
	* Announce SSID not found if None is detected.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.
* Updated psutil dependency to 5.9.4.
* NVDA will announce actual processor architecture (x86/AMD64/ARM64) as part
  of Windows version information.
* On single-core systems, NVDA will no longer announce CPU core load as
  average CPU load is the same as core load.

## Version 22.03

Version 22.03 is the last stable version to support Windows 7 Service Pack
1, 8, and 8.1.

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.
* Updated psutil dependency to 5.9.0.

## Version 22.01

* NVDA 2021.2 or later is required.

## Version 21.10

* NVDA 2021.1 or later is required due to changes to NVDA that affects this
  add-on.

## Version 21.08

* Minimum Windows release requirement is now tied to NVDA releases.
* Windows builds 20348 and 22000 are recognized as Windows Server 2022 and
  Windows 11, respectively.
* On Insider Preview builds, Windows release such as "Windows 10" will not
  be used. Instead NvDA will announce "Windows Insider".
* On 64-bit systems, processor architecture (x64 or ARM64) will be announced
  as part of Windows version information.

## Version 21.04

* NVDA 2020.4 or later is required.
* Updated psutil dependency to 5.8.0.
* When pressing add-on commands twice to copy resource information to
  clipboard, NVDA will announce resource summary that is being copied.

## Version 21.01

* Updated psutil dependency to 5.7.3.
* Shortened Windows version message.
* On Windows 8.1, build.revision will be announced as part of Windows
  version message, similar to Windows 10.

## Verzia 20.09

* Čas od posledného reštartovania je hlásený v tvare dni, hodiny, minúty,
  sekundy.
* Odteraz sú správne rozpoznané náhľady verzie Windows server insider.

## Verzia 20.07

* Pri zisťovaní verzie Windows (NVDA+Shift+6) je správne rozpoznaná verzia
  Windows 10 20H2.
* Skrátené zobrazenie verzie Windows.

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

## Zmeny vo verzii 4.5

* Doplnok presunutý na GitHub (https://github.com/josephsl/resourcemonitor).
* Správne je rozpoznávaný Windows server 2016.

## Zmeny vo verzii 4.0

* Aktualizovaná knižnica psutil na verziu 2.2.1.
* Upravené zisťovanie zaťaženia procesora.
* Pridaná podpora pre rozpoznávanie Windows 10.
* V systéme Windows 10 je oznamované aj číslo zostavi.
* Pomocníka k doplnku nájdete v správcovi doplnkov.

## Zmeny vo verzii 3.1

* Resource monitor oficiálne podporuje Windows 8.1
* Aktualizované preklady.

## Zmeny vo verzii 3.0

* Aktualizovaná knižnica psutil na verziu 1.2.1.
* Oznamovanie architektúri procesora (32 alebo 64 bit), verzie windows a
  Service Packu ((NVDA+Shift+6).
* Možnosť zmeniť klávesové skratky (NVDA 2013 a vyššie).
* Možnosť kopírovať údaje do schránky dvojitým stlačením danej skratky.

## Zmeny vo verzii 2.4

* Nové jazyky: Ukrajinčina, zjednodušená Čínština
* Aktualizované preklady.

## Zmeny vo verzii 2.3

* pridaný preklad do bulharčiny

## Zmeny vo verzii 2.2

* Pridané preklady: Arabčina, Aragónčina, chorvátčina, holandčina, fínčina,
  francúzština, Galijcíjčina, nemčina, maďarčina, taliančina, japončina,
  kórejčina, nepálčina, poľština, brazílska portugalčina, ruština,
  slovenčina, slovinčina, španielčina, Tamilčina a turečtina.

## Zmeny vo verzii 2.1

* Aktualizovaná knižnica psutil na verziu 0.6.1.
* Skrátený čas na zistenie kapacity a miesta na diskoch.
* drobné úpravy v kóde.

## Zmeny vo verzii 2.0

* Podpora pre preklady vrátane komentárov pre prekladateľov.

## Zmeny vo verzii 1.0

* prvé vydanie

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
