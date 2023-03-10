# Resource Monitor #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst and other NVDA contributors
* Загрузить [стабильную версию][1]
* NVDA compatibility: 2022.4 and later

Этот плагин предоставляет информацию о загрузке процессора, используемой
памяти и  других используемых ресурсах.

# Горячие клавиши

* NVDA+Shift+E: presents used ram, average processor load, and battery info
  if available.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's
  are present the load of each core.
* NVDA+Shift+2/5: presents the used and total space for both physical and
  virtual ram.
* NVDA+Shift+3: presents the used and total space of the static and
  removable drives.
* NVDA+Shift+4: presents battery percentage, charging status, remaining time
  (if not charging), and a warning if the battery is low or critical.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service
  pack numbers.
* NVDA+Shift+7: presents the system's uptime.

You can change these shortcut keys via input gestures dialog.

## Замечания по использованию

Это дополнение не заменяет диспетчер задач и другие информационные программы
системы Windows. Также обратите внимание на следующее:

* Resource information cannot be copied to clipboard if running the add-on
  in secure screens.
* Использование процессора предоставляется для логических процессоров, а не
  физических ядер. Это касается процессоров, которые использует Hyper
  Threading, где количество процессоров в два раза превышает количество
  процессорных ядер.
* Если есть тяжелые дисковые операции, такие как копирование больших файлов,
  возникают задержки при получении информации об использовании диска.
* When announcing processor architecture information, "x86" and "AMD64"
  refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

Note on license: this add-on uses Psutil, licensed under 3-Clause BSD
License which is compatible with GNU General Public License.

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

## Version 20.09

* System uptime is now given as days, hours, minutes, seconds.
* Windows Server Insider Preview build 20201 or later is properly recognized
  as a Server Insider build.

## Version 20.07

* Windows 10 Version 20H2 is properly recognized when obtaining Windows
  version information (NVDA+Shift+6).
* Simplified Windows 10 version message i.e. Windows 10 YYMM instead of
  Windows 10verYYMM when pressing NVDA+Shift+6.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Updated psutil dependency to 5.7.0.

## Version 20.01

* NVDA 2019.3 or later is required due to extensive use of Python 3.

## Version 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1
  and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## Версия 18.04

Version 18.04.x is the last release to support Windows releases earlier than
7 SP1.

* Last release to support Windows Server 2003, Vista and Server 2008.
* Better detection of Windows 10 releases and distinguishing between public
  and Insider Preview builds.

## Версия 17.12

* Added support for 64-bit ARM processors on Windows 10.

## Версия 17.09

Important: Version 17.09.x is the last version to support Windows XP.

* Last version to run on Windows XP.
* Windows 10 build 16278 and later is recognized as Version 1709. A minor
  revision for this add-on will be released once Version 1709 stable build
  is released.

## Версия 17.07.1

* Reintroduce support for Windows XP (broken since version 17.02).

## Версия 17.05

* Announcement of system uptime (time passed since last boot; NVDA+Shift+7).

## Версия 17.02

* Обновлён пакет psutil до версии 5.0.1.
* При проверке использования диска, NVDA больше не будет предоставлять
  диалог ошибки на некоторых системах, где съемный носитель не распознаётся
  (например, если карта не вставлена в устройство чтения карт памяти).)

## Версия 16.08

Начиная с версии 16.08, выпуски ревизий дополнения будут показаны в
год.месяц.

* Различные ревизии системы Windows 10 теперь правильно распознаются
  (например, 1607 для сборки 14393).
* Ревизии сборок Windows 10 (после установки накопительных обновлений)
  теперь правильно распознаются (например, 14393.51).
* Распознаётся факт использования сборок Insider Preview.

## Изменения в версии 4.5

* Репозиторий дополнения перемещён на github (находится на
  https://github.com/josephsl/resourcemonitor).
* Правильно распознаётся Windows Server 2016.

## Изменения в версии 4.0

* Обновлён пакет psutil до версии 2.2.1.
* Значительно улучшена производительность при получении информации о
  загрузке процессора.
* Добавлена поддержка для распознавания Windows 10.
* В Windows 10, также будет объявляться номер сборки Windows.
* Вы можете использовать Менеджер дополнений для доступа к справке
  дополнения.

## Изменения в версии 3.1

* Resource Monitor официально поддерживает Windows, 8.1.
* Обновлены переводы.

## Изменения в версии 3.0

* Обновлён пакет psutil до версии 1.2.1.
* Предоставляется установленная версия Windows, разрядность процессора (32
  или 64-разрядный) и пакет обновления, если есть (NVDA+Shift+6).
* Возможность изменения сочетания клавиш дополнения (NVDA 2013.3 или выше).
* Возможность копирования индивидуальной информации о ресурсах в буфер,
  нажимая команды дважды.

## Изменения в версии 2.4

* Новые языки: китайский (упрощённый), украинский.
* Обновлены переводы.

## Изменения в версии 2.3

* Добавлен болгарский перевод.

## Изменения в версии 2.2

* Добавлены следующие переводы: Арабский, арагонский, хорватский,
  голландский, финский, французский, галисийский, немецкий, венгерский,
  итальянский, японский, корейский, непальский, польский, португальский
  (Бразилия), русский, словацкий, словенский, испанский, тамильский и
  турецкий.

## Изменения в версии 2.1

* Обновлен пакет psutil до версии 0.6.1.
* Исправлена ​​большая задержка при получении информации о дисках.
* Немного очищен код

## Изменения в версии 2.0

* добавлена ​​поддержка Переводов и коментариев для переводчиков.

## Изменения в версии 1.0

* Первый публичный релиз

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=resourceMonitor
