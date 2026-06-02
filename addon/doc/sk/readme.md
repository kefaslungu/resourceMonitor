# Monitor prostriedkov

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

Poskytuje informácie o zaťažení procesora, stave pamäte a o iných zdrojoch.

## Klávesové skratky

All commands support speech on demand mode.

* NVDA+Shift+E: oznámy využitie pamäte ram, priemerné zaťaženie procesora a stav batérie, ak je dostupná.
* NVDA+Shift+1: oznámy vyťaženie procesora a jednotlivých jadier.
* NVDA+Shift+2/5: Oznámi využitú a celkovú fyzickú a virtuálnu pamäť.
* NVDA+Shift+3: Oznámi využité a celkové miesto pre pevné a pamäťové disky pripojené k počítaču.
* NVDA+Shift+4: oznámy stav batérie v percentách, stav napájania, zostávajúci čas (ak sa vybíja) a prípadne upozornenie ak je batéria vybytá alebo v kritickom stave.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service pack numbers.
* Nvda+shift+7: Oznámi čas behu systému od posledného reštartu.
* NVDA+Shift+8: presents information on the wireless connection, ssid name and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Všimnite si

Tento doplnok nie je náhradou za správcu úloh a iné programy na zisťovanie informácií v systéme Windows. Vezmite preto navedomie tieto skutočnosti:

* Resource information cannot be copied to clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* Ak práve kopírujete veľké súbory, zistenie informácie o využití disku môže chvíľu trvať.
* When announcing processor architecture information, "x86" and "AMD64" refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.
