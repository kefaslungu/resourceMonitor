# Ressourcen-Monitor #

* Autoren: Alex Hall, Joseph Lee, beqa gozalishvili und andere
  NVDA-Entwickler
* [stabile version][1] herunterladen

Diese Erweiterung gibt Informationen über Prozessor-Auslastung, verwendeten
Arbeitsspeicher sowie andere nützliche Ressourcen.

# Tastenkürzel #

* NVDA+Umschalt+E gibt den verwendeten Arbeitsspeicher, die ungefähre
  Prozessor-Auslastung und sofern vorhanden Informationen über den Akkustand
  aus.
* NVDA+Umschalt+1 gibt den  ungefähre Prozessor-Auslastung und die
  Auslastung für jeden Kern aus.
* NVDA+Umschalt+2/5 gibt den verwendeten und verfügbaren Speicherplatz des
  virtuellen und physikalischen Arbeitsspeichers aus.
* NVDA+Umschalt+3 gibt den verwendeten und verfügbaren Speicherplatz aller
  angeschlossenen Datenträger am Computer aus.
* NVDA+Umschalt+4 gibt den Ladezustand des Akkus und die verbleibende Zeit
  (sofern das Netzteil nicht angeschlossen ist), und eine Warnung bei
  geringem oder kritischem Ladezustand aus.
* NVDA+Umschalt+6 gibt die Windows-Version, die verwendete
  Prozessor-Architektur sowie eventuell installierte Service Packs aus.

Wenn Sie NVDA 2013.3 oder neuer installiert haben, können Sie die
Tastenkürzel ändern.

## Nutzungshinweise ##

Diese Erweiterung ersetzt nicht den Task-Manager von Windows sowie andere
Systeminformationsprogramme. Bitte beachten Sie Folgendes:

* Die Prozessor-Auslastung wird für logische Prozessoren, jedoch nicht für
  physische Kerne ausgegeben. Dies ist bei Prozessoren bemerkbar, welche
  Hyper Threading verwenden. Bei diesen Prozessoren ist die Anzahl der
  Prozessoren das doppelte der Prozessorkerne.
* If there is heavy disk activity such as copying large files, there might
  be delays when obtaining disk usage information.

## Version 17.02

* psutil-Abhängigkeit auf 5.0.1 aktualisiert.
* When checking disk usage, NVDA will no longer present an error dialog on
  some systems where a removable media is not properly recognized (such as
  when a card isn't inserted into a card reader).)

## Version 16.08

Starting with version 16.08, add-on releases will be shown as
year.month.revision.

* Various revisions of Windows 10 are now properly recognized (such as 1607
  for build 14393).
* Windows 10 build revisions (after installing cumulative updates) are
  properly recognized (such as 14393.51).
* If using Insider Preview builds, this fact is recognized.

## Änderungen bis 4.5 ##

* Add-on repository has moved to GitHub (can be found at
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 is properly recognized.

## Änderungen bis 4.0 ##

* psutil-Abhängigkeit auf 2.2.1 aktualisiert.
* Erheblich verbesserte Leistung beim Abrufen von Informationen über die
  CPU-Auslastung.
* Unterstützung für die Erkennung von Windows 10 hinzugefügt.
* In Windows 10 wird auch die Build-Nummer von Windows angesagt.
* Sie können den Add-ons-Manager verwenden, um auf die Hilfe zur Erweiterung
  zuzugreifen.

## Änderungen bis 3.1 ##

* Der Ressourcen-Monitor unterstützt offiziell Windows 8.1
* Übersetzungen aktualisiert.

## Änderungen bis 3.0 ##

* psutil-Abhängigkeit auf 1.2.1 aktualisiert.
* NVDA+Umschalt+6 gibt die Windows-Version, die verwendete
  Prozessor-Architektur sowie verwendete Service Packs aus.
* Tastenkürzel der Erweiterung sind ab NVDA 2013.3 änderbar.
* Nun besteht die Möglichkeit, einzelne Ressourceninformationen durch
  zweimaliges Drücken der Tastenkombination in die Zwischenablage zu
  kopieren.

## Änderungen bis 2.4 ##

* Neue Sprachen: Chinesisch (vereinfacht), Ukrainisch.
* Übersetzungen aktualisiert.

## Änderungen bis 2.3 ##

* Übersetzung für Bulgarisch hinzugefügt.

## Änderungen bis 2.2 ##

* Folgende Übersetzungen hinzugefügt: Arabisch, Aragonesisch, Kroatisch,
  Niederländisch, Finnisch, Französisch, Galiesisch, Deutsch, Ungarisch,
  Italienisch, Japanisch, Koreanisch, Nepalesisch, Polnisch, Portugiesisch
  (Brasilien), Russisch, Slovakisch, Slovenisch, Spanisch, Tamil und
  Türkisch.

## Änderungen bis 2.1 ##

* psutil auf Version 0.6.1 aktualisiert.
* Größere Zeitverzögerung beim Erhalt von Informationen von Datenträgern
  beseitigt.
* Der Quellcode wurde bereinigt.

## Änderungen bis 2.0 ##

* Möglichkeit zur Übersetzung sowie Übersetzungskommentare hinzugefügt.

## Änderungen bis 1.0 ##

* Ehrstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
