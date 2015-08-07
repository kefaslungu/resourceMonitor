# Resourcen-Monitor #

* Autoren: Alex Hall, Joseph Lee, beqa gozalishvili und andere
  NVDA-Entwickler
* [stabile version][1] herunterladen

Diese Erweiterung gibt Informationen über Prozessor-Auslastung, verwendeten
Arbeitsspeicher sowie andere nützliche Resourcen.

Wichtig: Resourcenmonitor 3.1 ist nicht zu NVDA 2013.3 und älter
kompatibel. Fals Sie die Version 2013.3 oder älter verwenden, verwenden Sie
bitte  Resourcenmonitor 3.0.

# Tastenkürzel #

* NVDA+Umschalt+E gibt den verwendeten Arbeitsspeicher, die ungefähre
  Prozessor-Auslastung und sofern vorhanden Informationen über den Akku aus
* NVDA+Umschalt+1 gibt den  ungefähre Prozessor-Auslastung und die
  Auslastung für jeden Kern aus.
* NVDA+Umschalt+2/5 gibt den verwendeten und verfügbaren Speicherplatz des
  virtuellen und physikalischen Arbeitsspeichers aus.
* NVDA+Umschalt+3 gibt den verwendeten und verfügbaren Speicherplatz aller
  angeschlossenen Datenträger am Computer aus.
* NVDA+Umschalt+4 gibt den Ladezustand des Akkus und die verbleibende Zeit
  (sofern das Netzteil nicht angeschlossen ist), und eine Warnung bei
  geringem oder kritischem Ladezustand aus.
* NVDA+Shift+6 Gibt die Windows-Version, die verwendete
  Prozessor-Architektur  sowie verwendete Service Packs aus

Fals Sie NVDA 2013.3 oder neuer installiert haben, können Sie die
Tastenkürzel ändern.

## Nutzungshinweise ##

Diese Erweiterung ersetzt den Task-Manager von Windows sowie andere
Systeminformationsprogramme nicht. Bitte beachten Sie folgendes:

* Die Prozessor-Auslastung wird für logische Prozessoren, jedoch nicht für
  physische Kerne ausgegeben. Dies ist bei Prozessoren bemerkbar, welche
  Hyper Threading verwenden. Bei diesen Prozessoren ist die Anzahl der
  Prozessoren das doppelte der Prozessorkerne.
* Möglicherweise gibt es eine kurze Verzögerung, während die
  Prozessor-Auslastung ermittelt wird.

## Änderungen bis 4.0 ##

* psutil-Abhängigkeit auf 2.2.1 aktualisiert.
* Erheblich verbesserte Leistung beim Abrufen von Informationen über die
  CPU-Auslastung.
* Unterstützung für die Erkennung von Windows 10 hinzugefügt.
* In Windows 10 wird auch die Build-Nummer von Windows angesagt.
* Sie können den Add-ons-Manager verwenden, um auf die Hilfe zur Erweiterung
  zuzugreifen.

## Änderungen bis 3.1 ##

* Resourcenmonitor unterstützt offiziell Windows 8.1
* Übersetzungen aktualisiert.

## Änderungen bis 3.0 ##

* psutil-Abhängigkeit auf 1.2.1 aktualisiert.
* NVDA+Shift+6 Gibt die Windows-Version, die verwendete
  Prozessor-Architektur sowie verwendete Service Packs aus
* Tastenkürzel der Erweiterung sind ab NVDA 2013.3 änderbar.
* Nun besteht die Möglichkeit, einzelne Ressourceninformationen durch
  zweimaliges Drücken der Tastenkombination in die Zwischenablage zu
  kopieren.

## Änderungen bis 2.4 ##

* Neue Sprachen: vereinfachtes chinesisch, ukrainisch.
* Übersetzungen aktualisiert.

## Änderungen bis 2.3 ##

* bulgarische Übersetzung hinzugefügt.

## Änderungen bis 2.2 ##

* Folgende Übersetzungen hinzugefügt: arabisch, Aragonesisch, Kroatisch,
  Niederländisch, Finnisch, Französisch, Galizisch, Deutsch, Ungarisch,
  Italienisch, japanisch, Koreanisch, Nepalesisch, polisch, Portugisisch
  (Brasilianisch), Russisch, Slovakisch, Slovenisch, Spanisch, Tamil und
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

[1]: http://addons.nvda-project.org/files/get.php?file=rm [2]:
http://addons.nvda-project.org/files/get.php?file=rm-next
