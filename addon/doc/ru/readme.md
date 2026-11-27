# Монитор Ресурсов

* Авторы: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst и другие участники NVDA

Это дополнение предоставляет информацию о загрузке процессора, используемой памяти и  других используемых ресурсах.

## Горячие клавиши

Все команды поддерживают режим речи по требованию.

* NVDA+Shift+E: enters the Resource Monitor command layer. There are two modes:
	* Lock: pressing the layer entry command once will keep the layer mode active until the Escape key or a key not defined in the layer mode (see below) is pressed. Keys not defined in the layer mode will be passed to the application.
	* Report: performing a resource usage info command will announce the information and exit the layer mode. Press the layer entry command repeatedly to lock the layer mode.

Для получения информации об использовании отдельных ресурсов доступны следующие команды уровня:

* Пробел: Общая информация об использовании ресурсов, включая используемую оперативную память (физическую память) и среднюю загрузку процессора.
* C: ЦП (средняя загрузка процессора, а при наличии многоядерных процессоров — загрузка каждого ядра).
* D: диски (используемое и общее пространство стационарных (встроенных), съёмных и сетевых накопителей)
* G (недоступно в защищённом режиме): информация о графическом процессоре (GPU)
* Shift+G(недоступно в защищённом режиме): использование памяти графического процессора
* M: память (используемое и общее пространство для физической и виртуальной оперативной памяти)
* O: Операционная система (версия Windows, архитектура процессора и точный номер сборки (build.revision))
* U: время безотказной работы системы
* W: Wi-Fi (название сети (SSID), уровень сигнала, режим безопасности или отсутствие SSID, если таковой отсутствует)

You can also assign shortcuts to announce individual resource information without entering the layer first (go to NvDA menu/Preferences/Input gestures to assign custom commands).

## Замечания по использованию

Это дополнение не заменяет диспетчер задач и другие информационные программы системы Windows. Также обратите внимание на следующее:

* Pressing resource commands twice or Control+NVDA+X will copy resource usage information to the clipboard (pressing Control+NVDA+X copies the last spoken resource information).
* Информацию о ресурсах невозможно скопировать в буфер обмена при запуске дополнения на защищённых экранах.
* Загрузка ЦП указана для логических процессоров, а не для физических ядер. Это особенно заметно на процессорах с технологией Hyper-Threading, где количество ядер ЦП вдвое превышает их общее число. На некоторых новых компьютерах технология Hyper-Threading может быть включена не для всех ядер ЦП.
* При интенсивной работе с диском, например, при копировании больших файлов или поиске сетевых дисков, могут возникать задержки при получении информации об использовании диска.
* NVDA будет воспроизводить звук и выдавать сообщение при каждом подключении к беспроводной сети или отключении от неё. Инструкции по изменению этого поведения см. в следующем разделе.
* Информация о графических процессорах представлена ​​для видеокарт Nvidia.
* При указании информации об архитектуре процессора в отчётах о версиях Windows, "AMD64" обозначает 64-битные (x64) процессоры Intel и AMD. Эта информация не относится к названию используемого процессора.
* Установка дополнения в Windows 10/11 LTSC не поддерживается.

## Настройки

You can configure the following settings from NVDA settings screen under Resource Monitor category:

* Enter resource monitor layer when layer command is performed: select between once (default, lock the layer mode) or repeatedly (pressing once will anounce resource info once, press repeatedly to lock the layer mode).
* Единица измерения температуры графического процессора: выберите единицу измерения температуры, отображаемую в информации о графическом процессоре (Цельсий или Фаренгейт).
* Уведомления о подключении/отключении Wi-Fi: выберите способ, которым NVDA должна сообщать об уведомлениях о подключении/отключении Wi-Fi (выключено, сообщение, звук, сообщение и звук).
* Обозначения размера памяти и диска: выбрать способ отображения размеров оперативной памяти и объема используемого дискового пространства в единицах гигабайт и терабайт (по умолчанию используется альтернативный метод (КБ/МБ/...)).

Список изменений, вносимых между выпусками каждого дополнения, см. в документе [списки изменений для выпусков дополнения][1].

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
