# Monitor zasobów / resource Monitor #

* Autorzy: Alex Hall, Joseph Lee, beqa gozalishvili i inni
* Wersja stabilna: [wersja 2.4][1]
* Wersja rozwojowa: [wersja 3.0-dev][2]

wtyczka podaje informacje o obciąrzeniu procesora, użyciu pamięci RAM,
statusie wykorzystania baterii i dysku twardego.

# skróty #

* NVDA+Shift+E raportuje używaną pamięć, średnie obciążenie procesora,
  informacje o baterii jeśli dostępna,
* nvda+shift+1 podaje średnie obciążenie procesora i obciąrzenie każdego z
  rdzeni,
* NVDA+Shift+2/5 podaje informacje o użyciu fizycznej i wirtualnej pamięci
  RAM,
* NVDA+Shift+3 podaje informacje o zasobach dyskowych na komputerze,
  włączając dyski wymienne
* NVDA+Shift+4 raportuje procent baterii, status ładowania, pozostały czas
  (jeśli nie ładuje), i ostrzeżenie o niskim lub krytycznym poziomie
  baterii,
* NVDA+Shift+6 odczytuje wersję i servicepack systemu Windows, oraz bity
  procesora (32 lub 64 bity)  (wersja 3.0-dev).

## Uwagi o używaniu ##

Ten dodatek nie zastępuje Menedżera zadań i innych programów dla Windows,
dostarczających informacji o systemie. Proszę również zwrócić uwagę na
następujące kwestie:

* Użycie CPU jest podawane dla procesorów logicznych, nie fizycznych
  rdzeni. Jest to zauważalne dla procesorów, które używają technologii Hyper
  Threading gdzie liczba CPU jest dwukrotnie większa od liczby rdzeni.
* Może pojawiać się krótkie opóźnienie przy pobieraniu informacji o użyciu
  procesora.

## Zmiany dla wersji 3.0-dev ##

* zaktualizowano bibliotekę psutil do wersji 1.2.1.
* Dodano polecenie (NVDA+Shift+6) zgłaszające używaną wersję Windows, liczbę
  bitów procesora i ewentualny service pack.
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
* bardziej zrozumiałe nazwy zmiennych
* porządki w kodzie

## zmiany dla wersji 2.0 ##

* wsparcie dla wielojęzyczności

## zmiany dla wersji 1.0 ##

* wydanie wstępne

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
