# Monitor zasobów

* Autorzy: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst, Kevin Derome i inni współtwórcy NVDA

Ten dodatek podaje informacje o obciążeniu procesora, wykorzystaniu pamięci i innych zasobów systemowych.

## Skróty

Wszystkie polecenia obsługują tryb mowy „Na żądanie”.

* NVDA+Shift+E: włącza warstwę poleceń Monitora zasobów.

W warstwie dostępne są następujące polecenia odczytujące informacje o poszczególnych zasobach:

* Spacja: ogólne informacje o wykorzystaniu zasobów, w tym pamięci RAM (pamięci fizycznej) i średnim obciążeniu procesora.
* C: procesor (średnie obciążenie procesora, a w przypadku procesorów wielordzeniowych także obciążenie każdego rdzenia).
* D: dyski (ilość zajętego i całkowitego miejsca na dyskach stałych — wbudowanych — oraz dyskach wymiennych i sieciowych).
* G (niedostępne w trybie bezpiecznym): informacje o procesorze graficznym (GPU).
* Shift+G (niedostępne w trybie bezpiecznym): wykorzystanie pamięci procesora graficznego.
* M: pamięć (ilość używanej i całkowitej pamięci fizycznej oraz wirtualnej).
* O: system operacyjny (wersja systemu Windows, architektura procesora i dokładny numer kompilacji w formacie kompilacja.rewizja).
* U: czas działania systemu.
* W: Wi-Fi (nazwa sieci — SSID, siła sygnału i typ zabezpieczeń albo informacja o braku połączenia).

Polecenia odczytujące informacje o zasobach pozostawiają warstwę aktywną, dzięki czemu można je powtarzać. Aby wyjść z warstwy, naciśnij Escape. Naciśnięcie klawisza bez przypisanego polecenia również wyłącza warstwę i przekazuje ten klawisz do aktywnej aplikacji.

Dla zachowania ograniczonej zgodności wstecznej nadal dostępne są wcześniejsze skróty od NVDA+Shift+1 do NVDA+Shift+7. Ich usunięcie jest planowane w przyszłej wersji dodatku:

* NVDA+Shift+1: procesor.
* NVDA+Shift+2/5: pamięć (NVDA+Shift+5 jest alternatywą dla NVDA+Shift+2, jeśli nie można wykonać tej drugiej kombinacji).
* NVDA+Shift+3: dyski.
* NVDA+Shift+4: Wi-Fi.
* NVDA+Shift+6: system operacyjny.
* NVDA+Shift+7: czas działania systemu.

Skróty można zmienić w oknie „Zdarzenia wejścia”.

## Uwagi dotyczące użytkowania

Ten dodatek nie zastępuje Menedżera zadań ani innych programów udostępniających informacje o systemie Windows. Należy również pamiętać o następujących kwestiach:

* Dwukrotne wywołanie polecenia odczytującego informacje o zasobach kopiuje te informacje do schowka.
* Informacji o zasobach nie można kopiować do schowka, gdy dodatek działa na bezpiecznych ekranach.
* Obciążenie procesora jest podawane dla procesorów logicznych, a nie fizycznych rdzeni. Jest to zauważalne w procesorach z technologią Hyper-Threading, w których liczba procesorów logicznych jest dwukrotnie większa od liczby fizycznych rdzeni. W niektórych nowszych komputerach Hyper-Threading może być włączony tylko dla części rdzeni.
* Podczas intensywnej aktywności dysku, np. kopiowania dużych plików, lub wyszukiwania dysków sieciowych odczytywanie informacji o zajętości dysków może być opóźnione.
* NVDA odtwarza dźwięk i odczytuje komunikat przy połączeniu z siecią bezprzewodową lub rozłączeniu z nią. Sposób zmiany tego zachowania opisano w następnej sekcji.
* Informacje o procesorze graficznym są dostępne dla układów NVIDIA.
* W informacjach o wersji systemu Windows oznaczenie architektury „AMD64” odnosi się do 64-bitowych (x64) procesorów firm Intel i AMD. Nie jest to nazwa używanego procesora.
* Instalowanie dodatku w systemach Windows 10/11 LTSC nie jest obsługiwane.

## Ustawienia

W oknie ustawień NVDA, w kategorii „Monitor zasobów”, można skonfigurować następujące opcje:

* Jednostka temperatury GPU: wybór jednostki, w której podawana jest temperatura procesora graficznego — „Stopnie Celsjusza” lub „Stopnie Fahrenheita”.
* Powiadomienia o połączeniu z siecią Wi-Fi i rozłączeniu: wybór sposobu powiadamiania przez NVDA — „Wyłączone”, „Komunikat”, „Dźwięk” lub „Komunikat i dźwięk”.
* Sposób zapisu rozmiarów pamięci i dysków: wybór sposobu zapisu jednostek, np. gigabajtów i terabajtów, w informacjach o wykorzystaniu pamięci RAM i zajętości dysków. Domyślnie wybrany jest zapis „Alternatywny” (KB, MB, GB).

Listę zmian w poszczególnych wersjach dodatku można znaleźć w [historii zmian][1].

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
