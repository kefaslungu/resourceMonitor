# Monitor zasobów / Resource Monitor #

* Autorzy: Alex Hall, Joseph Lee, beqa gozalishvili i inni
* Pobierz [wersja stabilna][1]

wtyczka podaje informacje o obciąrzeniu procesora, użyciu pamięci RAM,
wykorzystaniu innych zasobów.

# skróty #

* NVDA+Shift+E raportuje używaną pamięć, średnie obciążenie procesora,
  informacje o baterii jeśli dostępna.
* nvda+shift+1 podaje średnie obciążenie procesora i obciąrzenie każdego z
  rdzeni, jeśli używany jest procesor wielordzeniowy.
* NVDA+Shift+2/5 podaje informacje o użyciu fizycznej i wirtualnej pamięci
  RAM.
* NVDA+Shift+3 podaje informacje o używanej i całkowitej przestrzeni dysków
  twardych i wymiennych.
* NVDA+Shift+4 raportuje procent baterii, status ładowania, pozostały czas
  (jeśli nie ładuje), i ostrzeżenie o niskim lub krytycznym poziomie
  baterii.
* NVDA+Shift+6 odczytuje wersję i servicepack systemu Windows, oraz bity
  procesora (32 lub 64 bity).

Jeśli masz zainstalowane NVDA 2013.3 lub nowsze, możesz zmienić te skróty
klawiszowe.

## Uwagi o użytkowaniu ##

Ten dodatek nie zastępuje Menedżera zadań i innych programów dla Windows,
dostarczających informacji o systemie. Proszę również zwrócić uwagę na
następujące kwestie:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores.
* Może pojawiać się krótkie opóźnienie przy pobieraniu informacji o użyciu
  procesora.

## Version 16.08

Starting with version 16.08, add-on releases will be shown as
year.month.revision.

* Various revisions of Windows 10 are now properly recognized (such as 1607
  for build 14393).
* Windows 10 build revisions (after installing cumulative updates) are
  properly recognized (such as 14393.51).
* If using Insider Preview builds, this fact is recognized.

## Changes for 4.5 ##

* Add-on repository has moved to GitHub (can be found at
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 is properly recognized.

## Changes for 4.0 ##

* Updated psutil dependency to 2.2.1.
* Vastly improved performance when obtaining information on CPU load.
* Added support for recognition of Windows 10.
* In Windows 10, the build number of Windows will also be announced.
* You can use Add-ons Manager to access add-on help.

## zmiany dla wersji 3.1 ##

* Monitor zasobów oficjalnie obsługuje Windows 8.1.
* Zaktualizowano tłumaczenia.

## zmiany dla wersji 3.0 ##

* zaktualizowano bibliotekę psutil do wersji 1.2.1.
* NVDA+Shift+6 odczytuje wersję i servicepack systemu Windows, oraz bity
  procesora (32 lub 64 bity).
* Możliwość zmiany klawiszy skrótu dodatku (NVDA 2013.3 lub nowsza).
* Możliwość skopiowania do schowka pojedynczych informacji o zasobach, przez
  naciśnięcie dwukrotnie klawisza polecenia wypowiadającego daną informację.

## zmiany dla wersji 2.4 ##

* Nowe języki: chiński (uproszczony), ukraiński.
* Zaktualizowano tłumaczenia.

## zmiany dla wersji 2.3 ##

* Dodano tłumaczenie na bułgarski.

## zmiany dla wersji 2.2 ##

* Dodano następujące języki: arabski, aragoński, chorwacki, holenderski,
  fiński, francuski, galicyjski, niemiecki, węgierski, włoski, japoński,
  koreański, nepalski, polski, portugalski(brazylijski), rosyjski, słowacki,
  słoweński, hiszpański, tamilski i turecki.

## zmiany dla wersji 2.1 ##

* zaktualizowano psutil do wersji 0.6.1.
* poprawiono opóźnienie przy uzyskiwaniu informacji o dyskach
* porządki w kodzie.

## zmiany dla wersji 2.0 ##

* wsparcie dla wielojęzyczności

## zmiany dla wersji 1.0 ##

* wydanie wstępne

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm
