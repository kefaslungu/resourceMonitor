# Resource Monitor #

* Autorzy: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst i inni współtwórcy
* Pobierz [wersja stabilna][1]
* NVDA compatibility: 2020.4 to 2021.1

Ta wtyczka podaje informacje o obciążeniu procesora, użyciu pamięci RAM, a
także wykorzystaniu innych zasobów.

# Skróty

* NVDA+Shift+E podaje używaną pamięć, średnie obciążenie procesora,
  informacje o baterii jeśli jest dostępna.
* nvda+shift+1 podaje średnie obciążenie procesora i obciążenie każdego z
  rdzeni, jeśli używany jest procesor wielordzeniowy.
* NVDA+Shift+2/5 podaje informacje o użyciu fizycznej i wirtualnej pamięci
  RAM.
* NVDA+Shift+3 podaje informacje o używanej i całkowitej przestrzeni dysków
  twardych i wymiennych.
* NVDA+Shift+4 raportuje procent baterii, status ładowania, pozostały czas
  (jeśli nie ładuje), i ostrzeżenie o niskim lub krytycznym poziomie
  baterii.
* NVDA+Shift+6 odczytuje wersję i pakiet serwisowy systemu Windows, oraz
  bity procesora (32 lub 64 bity).
* NVDA+Shift+7 Pokazuje czas pracy systemu.

Jeśli posiadasz NVDA 2013.3 lub nowszą, możesz mienić te skróty klawiszowe w
dialogu zdarzeń wejścia.

## Uwagi o użytkowaniu

Ten dodatek nie zastępuje Menedżera zadań i innych programów dla Windows,
dostarczających informacji o systemie. Proszę również zwrócić uwagę na
następujące kwestie:

* Użycie CPU jest podawane dla procesorów logicznych, nie fizycznych
  rdzeni. Jest to zauważalne w przypadku procesorów używających technologii
  Hyper Threading gdzie liczba CPU jest dwukrotnie większa od liczby rdzeni.
* Jeśli aktywność dysku jest za duża, tak jak na przykład kopiowanie
  wielkich plików, możliwe są opóźnienia w trakcie pobierania informacji.
* Ten dodatek wygląda Windows 7 Service Pack 1 lub nowszy.

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

* Wymagana jest nowsza wersja NVDA 2019.3, z powodu dużego używania składni
  języka python 3

## Wersja19.11

* Ulepszone wykrywanie kompilacji insider preview, dla wersji 20H1 i
  nowszej.

## Wersja 19.07

* Zaktualizowano zależność psutil do wersji 5.6.3.
* Zmiany wewnętrzne do polecenia baterii.

## wersja 18.12

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

* zaktualizowano bibliotekę psutil do wersji 5.0.1.
* przy sprawdzaniu użycia dysku, NVDA nigdy więcej nie będzie pokazywał
  dialogu o błędzie na niektórych systemach na których dyski wymienne nie są
  rospoznane prawidłowo (Tak jak na przykład, kiedy karta SD nie jest
  włożona doslotu karty pamięci).)

## Wersja 16.08

Zaczynając od wersji 16.08, wersje dodatku będą wyświetlane jako
rok.miesiąc.rewizja.

* Różne wydania Windowsa 10 teraz są rozpoznawane, (tak jak 1607, dla
  kompilacji 14393). 
* Wydania kompilacji windowsa 10 (po instalacji aktualizacji zbiorczych) są
  rozpoznawane poprawnie (tak jak 14393.51).
* Jeżeli są używane kompilacje Insider Preview, ten stan jest rospoznany.

## zmiany dla wersji 4.5

* Repozytorium tego dodatku został przeniesiony do GitHuba (można go znaleźć
  pod adresem https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 jest rozpoznawany poprawnie.

## zmiany dla wersji 4.0

* zaktualizowano bibliotekę psutil do wersji 2.2.1.
* Znacznie ulepszona zawodność przy pobieraniu informacji o użyciu
  procesora.
* Dodano wsparcie dla rospoznawania Windows 10.
* W Windowsie 10, numer kompilacji także będzie oznajmiany. 
* Teraz państwo może użyć menedżera dodatków, aby dostać się do pomocy
  dodatku.

## zmiany dla wersji 3.1

* Monitor zasobów oficjalnie obsługuje Windows 8.1.
* Zaktualizowano tłumaczenia.

## zmiany dla wersji 3.0

* zaktualizowano bibliotekę psutil do wersji 1.2.1.
* NVDA+Shift+6 odczytuje wersję i servicepack systemu Windows, oraz bity
  procesora (32 lub 64 bity).
* Możliwość zmiany klawiszy skrótu dodatku (NVDA 2013.3 lub nowsza).
* Możliwość skopiowania do schowka pojedynczych informacji o zasobach, przez
  naciśnięcie dwukrotnie klawisza polecenia wypowiadającego daną informację.

## zmiany dla wersji 2.4

* Nowe języki: chiński (uproszczony), ukraiński.
* Zaktualizowano tłumaczenia.

## zmiany dla wersji 2.3

* Dodano tłumaczenie bułgarskie.

## zmiany dla wersji 2.2

* Dodano następujące języki: arabski, aragoński, chorwacki, holenderski,
  fiński, francuski, galicyjski, niemiecki, węgierski, włoski, japoński,
  koreański, nepalski, polski, portugalski(brazylijski), rosyjski, słowacki,
  słoweński, hiszpański, tamilski i turecki.

## zmiany dla wersji 2.1

* zaktualizowano psutil do wersji 0.6.1.
* poprawiono opóźnienie przy uzyskiwaniu informacji o dyskach
* porządki w kodzie.

## zmiany dla wersji 2.0

* wsparcie wielojęzyczności

## zmiany dla wersji 1.0

* wydanie wstępne

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
