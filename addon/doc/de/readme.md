# Ressourcen-Monitor #

* Autoren: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala und andere
  NVDA-Entwickler
* [stabile version][1] herunterladen

Diese Erweiterung gibt Informationen über Prozessor-Auslastung, verwendeten
Arbeitsspeicher sowie andere nützliche Ressourcen.

# Tastenkürzel #

* NVDA+Umschalt+E gibt den verwendeten Arbeitsspeicher, die ungefähre
  Prozessor-Auslastung und - sofern vorhanden - Informationen über den
  Akkustand aus.
* NVDA+Umschalt+1 gibt den  ungefähre Prozessor-Auslastung und die
  Auslastung für jeden Kern aus.
* NVDA+Umschalt+2/5 gibt den verwendeten und verfügbaren Speicherplatz des
  virtuellen und physikalischen Arbeitsspeichers aus.
* NVDA+Umschalt+3 gibt den verwendeten und verfügbaren Speicherplatz aller
  integrierten Festplatten und angeschlossenen Datenträger aus.
* NVDA+Umschalt+4 gibt den Ladezustand des Akkus und die verbleibende Zeit
  (sofern das Netzteil nicht angeschlossen ist), und eine Warnung bei
  geringem oder kritischem Ladezustand aus.
* NVDA+Umschalt+6 gibt die Windows-Version, die verwendete
  Prozessor-Architektur sowie eventuell installierte Service Packs aus.
* NVDA+Umschalt+7 gibt die Betriebszeit des Systems aus.

Ab NVDA 2013.3 können Sie die Tastenkürzel ändern.

## Nutzungshinweise ##

Diese Erweiterung ersetzt nicht den Task-Manager von Windows sowie andere
Systeminformationsprogramme. Bitte beachten Sie Folgendes:

* Die Prozessor-Auslastung wird für logische Prozessoren, jedoch nicht für
  physische Kerne ausgegeben. Dies ist bei Prozessoren bemerkbar, welche
  Hyper Threading verwenden. Bei diesen Prozessoren ist die Anzahl der
  Prozessoren das doppelte der Prozessorkerne.
* Es kann zu Verzögerungen beim Abrufen von Informationen über die
  Festplattennutzung kommen, wenn starke Festplattenaktivitäten wie z.B. das
  Kopieren großer Dateien stattfinden.
* Support for Windows XP from this add-on ended on December 31,
  2017. Support for Windows Server 2003, Vista and Server 2008 will end on
  June 30, 2018.

## Version 18.04

Version 18.04.x is the last release to support Windows releases earlier than
7 SP1.

* Last release to support Windows Server 2003, Vista and Server 2008.
* Better detection of Windows 10 releases and distinguishing between public
  and Insider Preview builds.

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

* psutil-Abhängigkeit auf 5.0.1 aktualisiert.
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

## Änderungen in 4.5 ##

* Der Quellordner der Erweiterung (Repository) wurde nach GitHub
  verschoben. Das Verzeichnis kann hier gefunden werden
  [https://github.com/josephsl/resourcemonitor](https://github.com/josephsl/resourcemonitor).
* Windows-Server 2016 wird nun korrekt erkannt.

## Änderungen in 4.0 ##

* psutil-Abhängigkeit auf 2.2.1 aktualisiert.
* Erheblich verbesserte Leistung beim Abrufen von Informationen über die
  CPU-Auslastung.
* Unterstützung für die Erkennung von Windows 10 hinzugefügt.
* In Windows 10 wird auch die Build-Nummer von Windows angesagt.
* Sie können den Add-ons-Manager verwenden, um auf die Hilfe zur Erweiterung
  zuzugreifen.

## Änderungen in 3.1 ##

* Der Ressourcen-Monitor unterstützt offiziell Windows 8.1
* Übersetzungen aktualisiert.

## Änderungen in 3.0 ##

* psutil-Abhängigkeit auf 1.2.1 aktualisiert.
* NVDA+Umschalt+6 gibt die Windows-Version, die verwendete
  Prozessor-Architektur sowie verwendete Service Packs aus.
* Tastenkürzel der Erweiterung sind ab NVDA 2013.3 änderbar.
* Es besteht die Möglichkeit, einzelne Ressourceninformationen durch
  zweimaliges Drücken der Tastenkombination in die Zwischenablage zu
  kopieren.

## Änderungen in 2.4 ##

* Neue Sprachen: Chinesisch (vereinfacht), Ukrainisch.
* Übersetzungen aktualisiert.

## Änderungen in 2.3 ##

* Übersetzung für Bulgarisch hinzugefügt.

## Änderungen in 2.2 ##

* Folgende Übersetzungen hinzugefügt: Arabisch, Aragonesisch, Kroatisch,
  Niederländisch, Finnisch, Französisch, Galiesisch, Deutsch, Ungarisch,
  Italienisch, Japanisch, Koreanisch, Nepalesisch, Polnisch, Portugiesisch
  (Brasilien), Russisch, Slovakisch, Slovenisch, Spanisch, Tamil und
  Türkisch.

## Änderungen in 2.1 ##

* psutil auf Version 0.6.1 aktualisiert.
* Größere Zeitverzögerung beim Erhalten von Informationen von Datenträgern
  beseitigt.
* Der Quellcode wurde bereinigt.

## Änderungen in 2.0 ##

* Möglichkeit zur Übersetzung sowie Übersetzungskommentare hinzugefügt.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
