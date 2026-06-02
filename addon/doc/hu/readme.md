# Erőforrás-kilistázó

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## Billentyűparancsok

* NVDA+Shift+E: presents used ram, average processor load, and battery info if available.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's are present the load of each core.
* NVDA+Shift+2/5: presents the used and total space for both physical and virtual ram.
* NVDA+Shift+3: presents the used and total space of the static and removable drives.
* NVDA+Shift+4: presents battery percentage, charging status, remaining time (if not charging), and a warning if the battery is low or critical.
* NVDA+Shift+6: presents CPU Architecture 32/64-bit and Windows version and service pack numbers.
* NVDA+Shift+7: presents the system's uptime.

If you have NvDA 2013.3 or later installed, you can change these shortcut keys via input gestures dialog.

## Használati megjegyzések

Ez a kiegészítő nem helyettesíti a feladatkezelőt és a többi rendszerfigyelő Windows-os programot. Fontos megjegyezni a következőket:

* A processzor használata logikai processzorok alapján történik, nem a fizikai magok szerint. Ez azoknál a processzoroknál észrevehető, amelyek a Hyper Threading technológiát használják, ahol a processzorok száma kétszerese a magszámnak.
* If there is heavy disk activity such as copying large files, there might be delays when obtaining disk usage information.
* This add-on requires Windows 7 Service Pack 1 or later.
