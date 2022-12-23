# Ressourcen-Monitor #

* Autoren: Alex Hall, Joseph Lee, Beqa Gozalishvili, Tuukka Ojala, Ethin
  Probst und weitere NVDA-Mitwirkende
* [Stabile Version herunterladen][1]
* NVDA compatibility: 2022.3 and later

Diese Erweiterung enthält Informationen über Prozessor-Auslastung,
verwendeten Arbeitsspeicher sowie andere nützliche Ressourcen.

# Tastenkürzel

* NVDA+Umschalt+E: Zeigt den verbrauchten Arbeitsspeicher, die
  durchschnittliche Prozessorauslastungen und Akku-Informationen an, falls
  verfügbar.
* NVDA+Umschalt+1: Zeigt die durchschnittliche Prozessorauslastung (falls
  mehrere CPUs vorhanden sind, die Auslastung der einzelnen Kerne) an.
* NVDA+Umschalt+2/5: Zeigt den genutzten und den Gesamtspeicher sowohl für
  den physischen als auch für den virtuellen Arbeitsspeicher an.
* NVDA+Umschalt+3: Zeigt den belegten und gesamten Speicherplatz aller
  Laufwerke an.
* NVDA+Umschalt+4: Zeigt den Akku-Status in Prozent und den Ladestatus, die
  verbleibende Zeit (falls nicht aufgeladen) an und gibt eine Warnung aus,
  sobald der Akku schwach oder kritisch ist.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service
  pack numbers.
* NVDA+Shift+7: Zeigt die Laufzeit des Betriebssystems an.

You can change these shortcut keys via input gestures dialog.

## Nutzungshinweise

Diese Erweiterung ersetzt nicht den Task-Manager von Windows sowie andere
Systeminformationsprogramme. Bitte beachten Sie Folgendes:

* Die Ressourcen-Informationen können nicht in die Zwischenablage kopiert
  werden, wenn die Erweiterung im geschützten Bereich ausgeführt wird.
* Die Prozessor-Auslastung wird für logische Prozessoren, jedoch nicht für
  physische Kerne ausgegeben. Dies ist bei Prozessoren bemerkbar, welche
  Hyper Threading verwenden. Bei diesen Prozessoren ist die Anzahl der
  Prozessoren das doppelte der Prozessorkerne.
* Es kann zu Verzögerungen beim Abrufen von Informationen über die
  Festplattennutzung kommen, wenn starke Festplattenaktivitäten wie z.B. das
  Kopieren großer Dateien stattfinden.
* When announcing processor architecture information, "x86" and "AMD64"
  refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

Hinweis zur Lizensierung: Diese Erweiterung verwendet Psutil, welches  mit
der 3-Clause BSD Lizenz veröffentlicht wurd. Diese ist mit der General
Public Lizenz kompatibel.

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

Version 22.03 ist die letzte Version, die Windows 7 Service Pack 1 und
Windows 8/8.1 unterstützt.

* NVDA 2021.3 oder neuer wird benötigt.
* Beim Versuch, die Erweiterung unter Windows 7, 8 und 8.1 zu installieren,
  wird eine Warnung angezeigt.
* Die Python-Abhängigkeit "psutil" wurde auf 5.9.0 aktualisiert.

## Version 22.01

* NVDA 2021.2 oder neuer wird benötigt.

## Version 21.10

* NVDA 2021.2 oder neuer ist erforderlich, da die Änderungen diese
  Erweiterung betreffen.

## Version 21.08

* Die Mindestanforderungen für Windows-Versionen sind jetzt an
  NVDA-Versionen gebunden.
* Windows Builds 20348 und 22000 werden als Windows Server 2022 und Windows
  11 erkannt.
* In Windows Insider-Vorabversionen wird nicht mehr Windows Version 10 oder
  ähnliches angesagt. Stattdessen wird "Windows Insider" gesagt.
* Auf 64-bit-Systemen, wird die Prozessorarchitektur (x64 oder ARM64) mit
  der Windows Version ausgegeben.

## Version 21.04

* NVDA 2020.4 oder neuer ist erforderlich.
* Die psutil-Abhängigkeit wurde auf 5.8.0 aktualisiert.
* Wenn Sie zweimal die Tastenbefehle der Erweiterung drücken, um
  Ressourcen-Informationen in die Zwischenablage zu kopieren, werden diese
  von NVDA gleichzeitig vorgelesen.

## Version 21.01

* Die psutil-Abhängigkeit wurde auf 5.7.3 aktualisiert.
* Verkürzte Windows-Versionsmeldung.
* Unter Windows 8.1 wird build.revision als Teil der
  Windows-Versionsnachricht angekündigt, ähnlich wie bei Windows 10.

## Version 20.09

* Die Systemlaufzeit wird nun in Tagen, Stunden, Minuten und Sekunden
  angegeben.
* Windows Server Insider Preview Build 20201 oder neuer wird ordnungsgemäß
  als Server-Insider-Build erkannt.

## Version 20.07

* Windows 10 Version 20H2 wird beim Abrufen von Informationen zur
  Windows-Version (NVDA+Umschalt+6) korrekt erkannt.
* Vereinfachte Windows 10-Versionsmeldung, d. h. Windows 10 JJMM statt
  Windows 10VerJJMM beim Drücken von NVDA+Umschalt+6.

## Version 20.06

* Mit Flake8 wurden viele Code-Probleme und potenzielle Fehler behoben.

## Version 20.04

* Die "psutil"-Abhängigkeit wurde auf 5.7.0 aktualisiert.

## Version 20.01

* NVDA 2019.3 oder höher ist aufgrund des umfangreichen Einsatzes von Python
  3 erforderlich.

## Version 19.11

* Verbesserte Erkennung von Windows Insider Preview-Builds, insbesondere für
  20H1 und darüber hinaus.

## Version 19.07

* Die Paket-Abhängigkeit "psutil" wurde auf 5.6.3 aktualisiert.
* Interne Änderungen am Befehl "Akku-Status ankündigen".

## Version 18.12

* Interne Änderungen zur Unterstützung zukünftiger NVDA-Versionen.

## Version 18.10

* Der Code wurde mit Python 3 besser kompatibel gemacht.
* Die Paket-Abhängigkeit "psutil" wurde auf 5.4.7. aktualisiert.
* Bei der Ermittlung der Speicher- und Medienkapazität und -auslastung
  verursacht NVDA keinen Fehler mehr, wenn ein Computer oder ein Dienst mit
  mehr als einem Petabyte Speichergröße verwendet werden.
* Werte für Speicher- und Mediennutzung werden mit bis zu zwei
  Dezimalstellen angezeigt (z. B. 4,00 GB statt 4,0 GB).
* Verbesserte Erkennung von Windows Insider Preview Builds.

## Version 18.04

Wichtig: Version 18.04.x ist die letzte Version, die auf Windows-Versionen
vor Windows 7 Service-pack 1 ausgeführt werden kann.

* Dies ist die letzte Version der Erweiterung, die Windows Server 2003,
  Vista und Server 2008 unterstützt.
* Die Identifikation der Windows-10-Version funktioniert
  zuverlässiger. Außerdem wird nun zwischen Windows-Insider-Versionen und
  veröffentlichten Windows-Versionen unterschieden.

## Version 17.12

* Unterstützung für 64-Bit-Arm-Prozessoren auf Windows 10 hinzugefügt.

## Version 17.09

Wichtig: Version 17.09.x ist die letzte Version, die auf Windows XP
ausgeführt werden kann.

* Dies ist die letzte Version, welche Windows XP unterstützt.
* Windows 10 Build 16278 und höher wird als Version 1709 erkannt. Eine
  kleinere Revision für diese Erweiterung wird veröffentlicht, sobald
  Version 1709 stable build veröffentlicht wird.

## Version 17.07.1

* Unterstützung für Windows XP wurde wieder eingeführt.

## Version 17.05

* Ansage der Betriebszeit des Systems (vergangene Zeit seit dem letzten
  Booten; NVDA+Umschalt+7).

## Version 17.02

* Psutil-Abhängigkeit auf 5.0.1 aktualisiert.
* Bei der Überprüfung der Festplattennutzung zeigt NVDA keinen Fehlerdialog
  mehr auf einigen Systemen an. Dies gilt nur auf Systemen, auf denen ein
  Wechselmedium nicht richtig erkannt wird (z.B. wenn eine Karte nicht in
  einen Kartenleser eingelegt ist).

## Version 16.08

Ab version 16.08 werden neue Versionen dieser Erweiterung mit Jahr.Monat
angezeigt.

* Verschiedene Korrekturen für Windows10-Versionen werden richtig erkannt
  (z.B. 1607 für build 14393).
* Korrekturen der Buildnummer (z.B. 14393.51) wird jetzt auch nach
  kummulativen Aktualisierungen erkannt.
* Es wird nun auch erkannt, ob die aktive Windowsversion ein Build des
  Insiderprogramms ist.

## Änderungen in 4.5

* Der Quellordner der Erweiterung (Repository) wurde nach GitHub
  verschoben. Das Verzeichnis kann hier gefunden werden
  [https://github.com/josephsl/resourcemonitor](https://github.com/josephsl/resourcemonitor).
* Windows-Server 2016 wird nun korrekt erkannt.

## Änderungen in 4.0

* Psutil-Abhängigkeit auf 2.2.1 aktualisiert.
* Erheblich verbesserte Leistung beim Abrufen von Informationen über die
  CPU-Auslastung.
* Unterstützung für die Erkennung von Windows 10 hinzugefügt.
* In Windows 10 wird auch die Build-Nummer von Windows angesagt.
* Sie können den Add-ons-Manager verwenden, um auf die Hilfe zur Erweiterung
  zuzugreifen.

## Änderungen in 3.1

* Der Ressourcen-Monitor unterstützt offiziell Windows 8.1.
* Übersetzungen aktualisiert.

## Änderungen in 3.0

* Psutil-Abhängigkeit auf 1.2.1 aktualisiert.
* NVDA+Umschalt+6 gibt die Windows-Version, die verwendete
  Prozessor-Architektur sowie verwendete Service Packs aus.
* Tastenkürzel der Erweiterung sind ab NVDA 2013.3 änderbar.
* Es besteht die Möglichkeit, einzelne Ressourceninformationen durch
  zweimaliges Drücken der Tastenkombination in die Zwischenablage zu
  kopieren.

## Änderungen in 2.4

* Neue Sprachen: Chinesisch (vereinfacht), Ukrainisch.
* Übersetzungen aktualisiert.

## Änderungen in 2.3

* Übersetzung für Bulgarisch hinzugefügt.

## Änderungen in 2.2

* Folgende Übersetzungen hinzugefügt: Arabisch, Aragonesisch, Kroatisch,
  Niederländisch, Finnisch, Französisch, Galiesisch, Deutsch, Ungarisch,
  Italienisch, Japanisch, Koreanisch, Nepalesisch, Polnisch, Portugiesisch
  (Brasilien), Russisch, Slovakisch, Slovenisch, Spanisch, Tamil und
  Türkisch.

## Änderungen in 2.1

* Psutil auf Version 0.6.1 aktualisiert.
* Größere Zeitverzögerung beim Erhalten von Informationen von Datenträgern
  beseitigt.
* Der Quellcode wurde bereinigt.

## Änderungen in 2.0

* Möglichkeit zur Übersetzung sowie Übersetzungskommentare hinzugefügt.

## Änderungen in 1.0

* Ehrstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
