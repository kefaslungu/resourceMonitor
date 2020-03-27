# Ressourcen-Monitor #

* Autoren: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst
   und andere NVDA-Entwickler
* [Stabile Version herunterladen][1]
* NVDA compatibility: 2019.3 to 2020.1

Diese Erweiterung enthält Informationen über Prozessor-Auslastung,
verwendeten Arbeitsspeicher sowie andere nützliche Ressourcen.

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

Ab NVDA 2013.3 können Sie die Tastenkürzel im Dialog Eingaben ändern.

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
* Für diese Erweiterung ist Windows 7 Service Pack 1 oder höher
  erforderlich.

## Version 20.04

* Updated psutil dependency to 5.7.0.

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

## Änderungen in 4.5 ##

* Der Quellordner der Erweiterung (Repository) wurde nach GitHub
  verschoben. Das Verzeichnis kann hier gefunden werden
  [https://github.com/josephsl/resourcemonitor](https://github.com/josephsl/resourcemonitor).
* Windows-Server 2016 wird nun korrekt erkannt.

## Änderungen in 4.0 ##

* Psutil-Abhängigkeit auf 2.2.1 aktualisiert.
* Erheblich verbesserte Leistung beim Abrufen von Informationen über die
  CPU-Auslastung.
* Unterstützung für die Erkennung von Windows 10 hinzugefügt.
* In Windows 10 wird auch die Build-Nummer von Windows angesagt.
* Sie können den Add-ons-Manager verwenden, um auf die Hilfe zur Erweiterung
  zuzugreifen.

## Änderungen in 3.1 ##

* Der Ressourcen-Monitor unterstützt offiziell Windows 8.1.
* Übersetzungen aktualisiert.

## Änderungen in 3.0 ##

* Psutil-Abhängigkeit auf 1.2.1 aktualisiert.
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

* Psutil auf Version 0.6.1 aktualisiert.
* Größere Zeitverzögerung beim Erhalten von Informationen von Datenträgern
  beseitigt.
* Der Quellcode wurde bereinigt.

## Änderungen in 2.0 ##

* Möglichkeit zur Übersetzung sowie Übersetzungskommentare hinzugefügt.

## Änderungen in 1.0 ##

* Ehrstveröffentlichung

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
