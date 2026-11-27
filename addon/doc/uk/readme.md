# Resource Monitor (Монітор ресурсів)

* Автори: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst та інші учасники спільноти NVDA

Цей додаток надає інформацію про завантаженість процесора, використання пам’яті та інших ресурсів.

## Гарячі клавіші

Усі команди підтримують режим мовлення на вимогу.

* NVDA+Shift+E: enters the Resource Monitor command layer. There are two modes:
	* Lock: pressing the layer entry command once will keep the layer mode active until the Escape key or a key not defined in the layer mode (see below) is pressed. Keys not defined in the layer mode will be passed to the application.
	* Report: performing a resource usage info command will announce the information and exit the layer mode. Press the layer entry command repeatedly to lock the layer mode.

Для отримання інформації про використання окремих ресурсів доступні такі команди шару:

* Пробіл: загальна інформація про використання ресурсів, включаючи обсяг використаної оперативної пам’яті (фізичної пам’яті) та середнє навантаження на процесор.
* C: ЦП (середнє навантаження на процесор, а також, за наявності багатоядерних процесорів, навантаження на кожне ядро)
* D: диски (зайнятий та загальний обсяг місця на жорстких (вбудованих), знімних та мережевих дисках)
* G (недоступно в безпечному режимі): інформація про графічний процесор (GPU)
* Shift+G (недоступно в безпечному режимі): використання пам'яті графічного процесора
* M: пам'ять (використаний та загальний простір як для фізичної, так і для віртуальної оперативної пам'яті)
* O: операційна система (версія Windows, архітектура процесора та точний номер збірки (build.revision))
* U: час безперебійної роботи системи
* W: wi-fi (назва мережі (SSID), сила сигналу, режим безпеки або відсутність SSID, якщо його немає)

You can also assign shortcuts to announce individual resource information without entering the layer first (go to NvDA menu/Preferences/Input gestures to assign custom commands).

## Примітки про користування

Цей додаток не замінює диспетчера завдань Windows чи інших програм, які надають інформацію про систему.  Також запам’ятайте:

* Pressing resource commands twice or Control+NVDA+X will copy resource usage information to the clipboard (pressing Control+NVDA+X copies the last spoken resource information).
* Інформацію про ресурси тепер неможливо скопіювати в буфер обміну, якщо додаток запущено на захищеному екрані.
* Використання центрального процесора подано для логічних процесорів, а не для фізичних ядер. Це важливо для процесорів, які використовують Hyper-Threading, де кількість процесорів удвічі перевищує кількість ядер процесора. На деяких нових комп'ютерах не всі ядра процесора можуть мати увімкнений hyper-threading.
* При інтенсивних діях на диску, таких як копіювання великих файлів, можливі затримки з отриманням інформації про використання диска.
* NVDA відтворюватиме звук і повідомлятиме про підключення до бездротових мереж або відключення від них. Про те, як змінити цю поведінку, див. у наступному розділі.
* Інформація про графічний процесор надається для графічних процесорів Nvidia.
* Під час оголошення інформації про архітектуру процесора в рамках звітності про версію Windows термін «AMD64» стосується 64-розрядних (x64) процесорів Intel та AMD. Ця інформація не стосується назви фактично використовуваного процесора.
* Встановлення додатка на Windows 10/11 LTSC не підтримується.

## Налаштування

You can configure the following settings from NVDA settings screen under Resource Monitor category:

* Enter resource monitor layer when layer command is performed: select between once (default, lock the layer mode) or repeatedly (pressing once will anounce resource info once, press repeatedly to lock the layer mode).
* Одиниця вимірювання температури графічного процесора: виберіть одиницю вимірювання температури, яка вказується у інформації про графічний процесор (Цельсій або Фаренгейт).
* Сповіщення про підключення/відключення Wi-Fi: виберіть, як NVDA має повідомляти про сповіщення про підключення/відключення Wi-Fi (вимкнено, повідомлення, звук, обидва).
* Позначення обсягу пам'яті та дискового простору: виберіть спосіб показу обсягів оперативної пам'яті (RAM) та одиниць виміру дискового простору, таких як гігабайти та терабайти (початково встановлено альтернативний метод (КБ/МБ/...)).

Перелік змін, внесених між окремими версіями додатка, наведено в документі [журнал змін до версій додатка][1].

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
