# Ressourcen-Monitor

* Autoren: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst und weitere Mitwirkende aus der NVDA-Community

Diese NVDA-Erweiterung enthält Informationen über Prozessor-Auslastung, verwendeten Arbeitsspeicher sowie andere nützliche Ressourcen.

## Tastenkürzel

All commands support speech on demand mode.

* NVDA+Umschalt+E: Zeigt den verbrauchten Arbeitsspeicher, die durchschnittliche Prozessorauslastungen und Akku-Informationen an, falls verfügbar.
* NVDA+Umschalt+1: Zeigt die durchschnittliche Prozessorauslastung (falls mehrere CPUs vorhanden sind, die Auslastung der einzelnen Kerne) an.
* NVDA+Umschalt+2/5: Zeigt den genutzten und den Gesamtspeicher sowohl für den physischen als auch für den virtuellen Arbeitsspeicher an.
* NVDA+Umschalt+3: Zeigt den belegten und gesamten Speicherplatz aller Laufwerke an.
* NVDA+Umschalt+4: Zeigt Informationen über die WLAN-Verbindung, die Stärke des Signals, den Namen und die SSID an, falls vorhanden.
* NVDA+Umschalt+6: Zeigt die CPU-Architektur und die Windows-Versions- und Service-Pack-Nummern an.
* NVDA+Shift+7: Zeigt die Laufzeit des Betriebssystems an.
* Unassigned: presents information about the graphics processing unit (GPU; unavailable in secure mode).
* Unassigned: presents graphics processing unit (GPU memory usage information; unavailable in secure mode).

Sie können diese Tastenkombinationen über das Dialogfeld der Tastenbefehle ändern.

## Nutzungshinweise

Diese Erweiterung ersetzt nicht den Task-Manager von Windows sowie andere Systeminformationsprogramme. Bitte beachten Sie Folgendes:

* Apart from overall resource usage command (NVDA+Shift+E), pressing other commands twice will copy resource usage information to the clipboard.
* Die Ressourcen-Informationen können nicht in die Zwischenablage kopiert werden, wenn die Erweiterung im geschützten Bereich ausgeführt wird.
* Die CPU-Nutzung wird für logische Prozessoren angegeben, nicht für physische Kerne. Dies macht sich bei Prozessoren mit Hyper-Threading bemerkbar, bei denen die Anzahl der CPUs doppelt so hoch ist wie die Anzahl der CPU-Kerne. Auf einigen neueren Computern ist Hyper-Threading nicht für alle CPU-Kerne aktiviert.
* Es kann zu Verzögerungen beim Abrufen von Informationen über die Festplattennutzung kommen, wenn starke Festplattenaktivitäten wie z.B. das Kopieren großer Dateien stattfinden.
* GPU information is given for Nvidia GPU's.
* Bei den Informationen zur Prozessorarchitektur beziehen sich "x86" und "AMD64" auf 32-Bit- bzw. 64-Bit-Prozessoren (x64) von Intel bzw. AMD.
* Die Installation der NVDA-Erweiterung unter Windows 10/11 LTSC wird nicht unterstützt.

For a list of changes made between each add-on releases, refer to [changelogs for add-on releases][1] document.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
