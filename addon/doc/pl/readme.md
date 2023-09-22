# Resource Monitor #

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst and other NVDA contributors
* Pobierz [wersja stabilna][1]
* Zgodność z NVDA: 2022.4 i nowsze

Ta wtyczka podaje informacje o obciążeniu procesora, użyciu pamięci RAM, a
także wykorzystaniu innych zasobów.

# Skróty

* NVDA+Shift+E podaje używaną pamięć, średnie obciążenie procesora,
  informacje o baterii jeśli jest dostępna.
* NVDA+Shift+1: przedstawia średnie obciążenie procesora, a jeśli obecne są
  procesory wielordzeniowe, obciążenie każdego rdzenia.
* NVDA+Shift+2/5 podaje informacje o użyciu fizycznej i wirtualnej pamięci
  RAM.
* NVDA+Shift+3 podaje informacje o używanej i całkowitej przestrzeni dysków
  twardych i wymiennych.
* NVDA+Shift+4 raportuje procent baterii, status ładowania, pozostały czas
  (jeśli nie ładuje), i ostrzeżenie o niskim lub krytycznym poziomie
  baterii.
* NVDA+Shift+6: przedstawia architekturę procesora oraz numer wersji systemu
  Windows i dodatku Service Pack.
* NVDA+Shift+7 Pokazuje czas pracy systemu.
* NVDA+Shift+8: presents information on the wireless connection, ssid name
  and strength, or no ssid if there is none available.

Możesz zmienić te skrótów za pomocą okna dialogowego gestów wprowadzania.

## Uwagi o użytkowaniu

Ten dodatek nie zastępuje Menedżera zadań i innych programów dla Windows,
dostarczających informacji o systemie. Proszę również zwrócić uwagę na
następujące kwestie:

* Informacji o zasobach nie można skopiować do schowka, jeśli dodatek jest
  uruchamiany na bezpiecznych ekranach.
* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores. On some newer computers, not all CPU
  cores will have hyper-threading enabled.
* Jeśli aktywność dysku jest za duża, tak jak na przykład kopiowanie
  wielkich plików, możliwe są opóźnienia w trakcie pobierania informacji.
* Podczas ogłaszania informacji o architekturze procesora "x86" i "AMD64"
  odnoszą się odpowiednio do 32-bitowych i 64-bitowych (x64) procesorów
  Intel i AMD.
* Ten dodatek wymaga systemu Windows 10 lub nowszego.

Uwaga dotycząca licencji: ten dodatek używa Psutil, licencjonowanego na
3-klauzulowej licencji BSD, która jest zgodna z GNU General Public License.

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

## Wersja 23.02

* Wymagana jest NVDA 2022.4 lub nowsza.
* Wymagany jest system Windows 10 21H2 (aktualizacja z listopada 2021
  r./kompilacja 19044) lub nowszy.

## Wersja 23.01

* Wymagana jest NVDA 2022.3 lub nowsza.
* System Windows 10 lub nowszy jest wymagany, ponieważ systemy Windows 7, 8
  i 8.1 nie są już obsługiwane przez firmę Microsoft od stycznia 2023 r.
* Zaktualizowano zależność psutil do wersji 5.9.4.
* NVDA ogłosi rzeczywistą architekturę procesora (x86/AMD64/ARM64) jako
  część informacji o wersji systemu Windows.
* W systemach jednordzeniowych NVDA nie będzie już informować o obciążeniu
  rdzenia procesora, ponieważ średnie obciążenie procesora jest takie samo
  jak obciążenie rdzenia.

## Wersja 22.03

Wersja 22.03 jest ostatnią stabilną wersją obsługującą system Windows 7 z
dodatkiem Service Pack 1, 8 i 8.1.

* Wymagana jest nvda 2021.3 lub nowsza.
* Podczas próby zainstalowania dodatku w systemie Windows 7, 8 i 8.1
  zostanie wyświetlony komunikat ostrzegawczy.
* Zaktualizowano zależność psutil do wersji 5.9.0.

## Wersja 22.01

* Wymagana jest nvda 2021.2 lub nowsza.

## Wersja 21.10

* NVDA 2021.1 lub nowsza jest wymagana ze względu na zmiany w NVDA, które
  mają wpływ na ten dodatek.

## Wersja 21.08

* Minimalne wymagania dotyczące wersji systemu Windows są teraz powiązane z
  wersjami NVDA.
* Kompilacje systemu Windows 20348 i 22000 są rozpoznawane odpowiednio jako
  Windows Server 2022 i Windows 11.
* W kompilacjach Insider Preview wersja systemu Windows, taka jak "Windows
  10", nie będzie używana. Zamiast tego NvDA ogłosi "Windows Insider".
* W systemach 64-bitowych architektura procesora (x64 lub ARM64) zostanie
  ogłoszona jako część informacji o wersji systemu Windows.

## Wersja 21.04

* Wymagana jest wersja NVDA 2020.4 lub nowsza.
* Zaktualizowano zależność psutil do wersji 5.8.0.
* Po dwukrotnym naciśnięciu poleceń dodatków w celu skopiowania informacji o
  zasobach do schowka, NVDA ogłosi kopiowane podsumowanie zasobów.

## Wersja 21.01

* Zaktualizowano zależność psutil do wersji 5.7.3.
* Komunikat o skróconej wersji systemu Windows.
* W systemie Windows 8.1 wersja build.revision zostanie ogłoszona jako część
  komunikatu o wersji systemu Windows, podobnie jak w systemie Windows 10.

## Wersja 20.09

* Czas pracy systemu od teraz jest podawany jako wartość w dniach,
  godzinach, minutach, sekundach.
* Windows Server kompilacja Insider Preview 20201 lub nowsze są teraz
  prawidłowo rozpoznawane jako kompilacje insider preview.

## Wersja 20.04

* Windows 10 wersja 20H2 jest poprawnie rozpoznawana przy dostarczaniu
  informacji o wersji za pomocą skrótu (NVDA+Shift+6).
* Uproszczony komunikato o werji Windows Na przykład: Windows 10 YYMM
  instead of Windows 10verYYMM when pressing NVDA+Shift+6.

## Wersja 20.06

* Naprawiono błędy związane z stylem kodu oraz linterem flake8.

## Wersja 20.04

* Zaktualizowano zależność psutil dependency to 5.7.0.

## Wersja 20.01

* NVDA 2019.3 lub nowsza jest wymagana ze względu na szerokie wykorzystanie
  Pythona 3.

## Wersja19.11

* Ulepszone wykrywanie kompilacji insider preview, dla wersji 20H1 i
  nowszej.

## Wersja 19.07

* Zaktualizowano zależność psutil do wersji 5.6.3.
* Zmiany wewnętrzne do polecenia baterii.

## Wersja 18.12

* Zmiany wewnętrzne do wspierania przyszłych wersji NVDA.

## Wersja 18.10

* Poprawiona została zgodność kodu źródłowego z Pythonem 3.
* Zaktualizowano zależność psutil do wersji 5.4.7.
* Podczas wyświetlania pojemności dysku i użycia pamięci, NVDA nie będzie
  już wyrzucać błędów, dla komputerów lub usług używających więcej niż
  petabajt pamięci RAM lub dysku.
* Wartości użycia pamięci i dysku wyświetlane są do dwóch miejsc po
  przecinku, np. 4.00 GB zamiast 4.0 GB).
* Ulepszone wykrywanie kompilacji Windows insider preview.

## Wersja 18.04

Wersja 18.04.x jest ostatnim wydaniem wspierającym wydania windows wcześniej
niż 7 SP1.

* Ostatnia wersjawspierająca Windows Server 2003, Vista i Server 2008.
* Lepsze wykrywanie wydań Windowsa 10, a także rozróżnianie między wydaniami
  publicznymi i wydaniami niejawnego programu testów.

## Wersja 17.12

* Dodano wsparcie dla 64-bitowych ARM procesorów w Windowsie 10.

## Wersja 17.09

Ważne: Wersja 17.09.x jest ostatnią wersją wspierającą Windows XP.

* Ostatnia wersja, którą będzie można uruchomić na Windowsie XP.
* Windows 10 kompilacja 16278 i nowsze są rozpoznawane jako 1709. Pomniejsza
  aktualizacja tego dodatku będzie wydana po wydaniu wersji 1709 stabilnej
  kompilacji.

## Wersja 17.07.1

* Ponowne wsparcie Windowsa XP (uszkodzone od wersji 17.02).

## Wersja 17.05

* Wymawianie czasu pracy systemu (czas od ostatniego rozruchu;
  NVDA+Shift+7).

## Wersja 17.02

* Zaktualizowano zależność psutil do wersji 5.0.1.
* Podczas sprawdzania użycia dysku NVDA nie będzie już wyświetlać okna
  dialogowego błędu w niektórych systemach, w których nośnik wymienny nie
  jest prawidłowo rozpoznawany (na przykład gdy karta nie jest włożona do
  czytnika kart).)

## Wersja 16.08

Zaczynając od wersji 16.08, wersje dodatku będą wyświetlane jako
rok.miesiąc.rewizja.

* Różne wersje systemu Windows 10 są teraz poprawnie rozpoznawane (takie jak
  1607 dla kompilacji 14393).
* Wydania kompilacji windowsa 10 (po instalacji aktualizacji zbiorczych) są
  rozpoznawane poprawnie (tak jak 14393.51).
* Jeżeli są używane kompilacje Insider Preview, ten stan jest rospoznany.

## Zmiany w wersji 4.5

* Repozytorium tego dodatku został przeniesiony do GitHuba (można go znaleźć
  pod adresem https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 jest rozpoznawany poprawnie.

## Zmiany w wersji 4.0

* Zaktualizowano zależność psutil do wersji 2.2.1.
* Znacznie ulepszona zawodność przy pobieraniu informacji o użyciu
  procesora.
* Dodano wsparcie dla rospoznawania Windows 10.
* W systemie Windows 10 zostanie również ogłoszony numer kompilacji systemu
  Windows.
* Teraz państwo może użyć menedżera dodatków, aby dostać się do pomocy
  dodatku.

## Zmiany dla wersji 3.1

* Monitor zasobów oficjalnie obsługuje Windows 8.1.
* Zaktualizowano tłumaczenia.

## Zmiany dla wersji 3.0

* Zaktualizowano zależność psutil do wersji 1.2.1.
* NVDA+Shift+6 odczytuje wersję i servicepack systemu Windows, oraz bity
  procesora (32 lub 64 bity).
* Możliwość zmiany klawiszy skrótu dodatku (NVDA 2013.3 lub nowsza).
* Możliwość skopiowania do schowka pojedynczych informacji o zasobach, przez
  naciśnięcie dwukrotnie klawisza polecenia wypowiadającego daną informację.

## Zmiany w wersji 2.4

* Nowe języki: chiński (uproszczony), ukraiński.
* Zaktualizowano tłumaczenia.

## Zmiany dla 2.3

* Dodano tłumaczenie bułgarskie.

## Zmiany w wersji 2.2

* Dodano następujące języki: arabski, aragoński, chorwacki, holenderski,
  fiński, francuski, galicyjski, niemiecki, węgierski, włoski, japoński,
  koreański, nepalski, polski, portugalski(brazylijski), rosyjski, słowacki,
  słoweński, hiszpański, tamilski i turecki.

## Zmiany dla wersji 2.1

* Zaktualizowano zależność psutil do wersji 0.6.1.
* Naprawiono duże opóźnienie podczas uzyskiwania informacji o dyskach.
* Czyszczenie kodu.

## Zmiany dla wersji 2.0

* dodano wsparcie tłumaczeniowe i komentarze do tłumaczeń.

## Zmiany dla wersji 1.0

* Wstępne wydanie

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
