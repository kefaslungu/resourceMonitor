# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

Ta wtyczka podaje informacje o obciążeniu procesora, użyciu pamięci RAM, a także wykorzystaniu innych zasobów.

## Skróty

All commands support speech on demand mode.

* NVDA+Shift+E podaje używaną pamięć, średnie obciążenie procesora, informacje o baterii jeśli jest dostępna.
* NVDA+Shift+1: przedstawia średnie obciążenie procesora, a jeśli obecne są procesory wielordzeniowe, obciążenie każdego rdzenia.
* NVDA+Shift+2/5 podaje informacje o użyciu fizycznej i wirtualnej pamięci RAM.
* NVDA+Shift+3 podaje informacje o używanej i całkowitej przestrzeni dysków twardych i wymiennych.
* NVDA+Shift+4 raportuje procent baterii, status ładowania, pozostały czas (jeśli nie ładuje), i ostrzeżenie o niskim lub krytycznym poziomie baterii.
* NVDA+Shift+6: przedstawia architekturę procesora oraz numer wersji systemu Windows i dodatku Service Pack.
* NVDA+Shift+7 Pokazuje czas pracy systemu.
* NVDA+Shift+8: presents information on the wireless connection, ssid name and strength, or no ssid if there is none available.

Możesz zmienić te skrótów za pomocą okna dialogowego gestów wprowadzania.

## Uwagi o użytkowaniu

Ten dodatek nie zastępuje Menedżera zadań i innych programów dla Windows, dostarczających informacji o systemie. Proszę również zwrócić uwagę na następujące kwestie:

* Informacji o zasobach nie można skopiować do schowka, jeśli dodatek jest uruchamiany na bezpiecznych ekranach.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* Jeśli aktywność dysku jest za duża, tak jak na przykład kopiowanie wielkich plików, możliwe są opóźnienia w trakcie pobierania informacji.
* Podczas ogłaszania informacji o architekturze procesora "x86" i "AMD64" odnoszą się odpowiednio do 32-bitowych i 64-bitowych (x64) procesorów Intel i AMD.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.
