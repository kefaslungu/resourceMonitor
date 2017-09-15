# Monitor zasobów / Resource Monitor #

* Autorzy: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala i inni
  współtwórcy NVDA
* Pobierz [wersja stabilna][1]

Ta wtyczka podaje informacje o obciąrzeniu procesora, użyciu pamięci RAM, a
także wykorzystaniu innych zasobów.

# Skróty #

* NVDA+Shift+E raportuje używaną pamięć, średnie obciążenie procesora,
  informacje o baterii jeśli dostępna.
* nvda+szift+1 podaje średnie obciążenie procesora i obciąrzenie każdego z
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
* NVDA+Shift+7 Pokazuje czas pracy systemu.

Jeśli masz zainstalowane NVDA 2013.3 lub nowsze, możesz zmienić te skróty
klawiszowe.

## Uwagi o użytkowaniu ##

Ten dodatek nie zastępuje Menedżera zadań i innych programów dla Windows,
dostarczających informacji o systemie. Proszę również zwrócić uwagę na
następujące kwestie:

* Użycie CPU jest podawane dla procesorów logicznych, nie fizycznych
  rdzeni. Jest to zauważalne dla procesorów używających technologii Hyper
  Threading gdzie liczba CPU jest dwukrotnie większa od liczby rdzeni.
* Jeśli aktywność dysku jest za duża, tak jak na przykład kopiowanie
  wielkich plików, możliwe są opóźnienia przy pobieraniu informacji.
* Wsparcie dla Windows XP do tego dodatku skończy się 31 grudnia,
  2017. Wsparcie dla Windows Server 2003 i Windows Vista skończy się
  30. czerwca, 2018.

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
  dialog o błędzie na niektórymi systemami na którymi dyski wymienne nie są
  rospoznane prawidłowo (Tak jak naprzykład, kiedy karta SD nie jest włożona
  do karty pamięci).)

## Wersja 16.08

Zaczynając od wersji 16.08, wersje dodatku będą wyświetlane jako
rok.miesiąc.rewizja.

* Różne wydania Windowsa 10 teraz są rozpoznawane, (tak jak 1607, dla
  kompilacji 14393). 
* Wydania kompilacji windowsa 10 (po instalacji aktualizacji zbiorczych) są
  rozpoznawane poprawnie (tak jak 14393.51).
* Jeżeli są używane kompilacje Insider Preview, ten stan jest rospoznany.

## zmiany dla wersji 4.5 ##

* Repozytorium tego dodatku został przeniesiony do GitHuba (można go znaleźć
  pod adresem https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 jest rozpoznawany poprawnie.

## zmiany dla wersji 4.0 ##

* zaktualizowano bibliotekę psutil do wersji 2.2.1.
* Znacznie ulepszona zawodność przy pobieraniu informacji o użyciu
  procesora.
* Dodano wsparcie dla rospoznawania Windows 10.
* W Windowsie 10, numer kompilacji także będzie oznajmiany. 
* Teraz państwo może użyć menedżera dodatków, aby dostać się do pomocy
  dodatku.

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

[1]: https://addons.nvda-project.org/files/get.php?file=rm
