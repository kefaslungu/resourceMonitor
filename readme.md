# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst, Kevin Derome and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## Shortcuts

All commands support speech on demand mode.

* NVDA+Shift+E: presents used RAM (pyysical memory) and average processor load.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's are present the load of each core.
* NVDA+Shift+2/5: presents the used and total space for both physical and virtual ram.
* NVDA+Shift+3: presents the used and total space of the static and removable drives.
* NVDA+Shift+4: presents information on the wireless connection, ssid name and strength, or no ssid if there is none available.
* NVDA+Shift+6: presents  CPU Architecture and Windows version and service pack numbers.
* NVDA+Shift+7: presents the system's uptime.
* Unassigned: presents information about the graphics processing unit (GPU; unavailable in secure mode).

You can change these shortcut keys via input gestures dialog.

## Usage notes

This add-on does not replace task manager and other system information programs for Windows. Also note the following:

* Resource information cannot be copied to the clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* If there is heavy disk activity such as copying large files, there might be delays when obtaining disk usage information.
* When announcing processor architecture information, "x86" and "AMD64" refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* Installing the add-on on Windows 10/11 LTSC is not supported.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
