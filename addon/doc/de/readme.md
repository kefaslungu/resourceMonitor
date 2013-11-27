# resourcen-Monitor #

* Autoren: Alex Hall, Joseph Lee, beqa gozalishvili und andere
  NVDA-Entwickler
* stabile Version: [version 2.4][1]
* Entwicklerversion: [version 3.0-dev][2]

Diese Erweiterung gibt Informationen über Prozessor-Auslastung, verwendeten
Arbeitsspeicher sowie Akku- und Datenträgerkapazität.

# Tastenkürzel #

* NVDA+Umschalt+E gibt den verwendeten Arbeitsspeicher, die ungefähre
  Prozessor-Auslastung und sofern vorhanden Informationen über den Akku aus
* NVDA+Umschalt+1 gibt den  ungefähre Prozessor-Auslastung und die
  Auslastung für jeden Kern aus.
* NVDA+Umschalt+2/5 gibt den verwendeten und verfügbaren Speicherplatz des
  virtuellen und physikalischen Arbeitsspeichers aus.
* NVDA+Umschalt+3 gibt den verwendeten und verfügbaren Speicherplatz aller
  Datenträger am Computer aus.
* NVDA+Umschalt+4 gibt den Ladezustand des Akkus und die verbleibende Zeit
  (sofern das Netzteil nicht angeschlossen ist), und eine Warnung bei
  geringem oder kritischem Ladezustand aus.
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or
  64-bit) and service pack if any (version 3.0-dev).

## Nutzungshinweise ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Änderungen bis 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

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
* %s in {freundlicheVariableNamen} übersetzt.
* Der Quellcode wurde ein bisschen bereinigt.

## Änderungen bis 2.0 ##

* Möglichkeit zur Übersetzung sowie Übersetzungskommentare hinzugefügt.

## Änderungen bis 1.0 ##

* Ehrstveröffentlichung

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
