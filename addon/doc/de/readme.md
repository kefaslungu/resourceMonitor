# Resourcen-Monitor #

* Autoren: Alex Hall, Joseph Lee, beqa gozalishvili und andere
  NVDA-Entwickler
* Version: [3.1][1]

This plugin gives information about CPU load, memory usage and other
resource usage information.

Important: Resource Monitor 3.1 is not compatible with NvDA 2013.3 or
earlier. If you use 2013.3 or earlier, please use Resource Monitor 3.0.

# Tastenkürzel #

* NVDA+Shift+E Presents used ram, average processor load, and battery info
  if available.
* NVDA+Shift+1 Presents the average processor load and if multicore CPU's
  are present the load of each core.
* NVDA+Shift+2/5 Presents the used and total space for both physical and
  virtual ram.
* NVDA+Shift+3 Presents the used and total space of the static and removable
  drives.
* NVDA+Shift+4 Presents battery percentage, charging status, remaining time
  (if not charging), and a warning if the battery is low or critical.
* NVDA+Shift+6 Presents CPU Architecture 32/64-bit and Windows version and
  service pack numbers.

If you have NvDA 2013.3 or later installed, you can change these shortcut
keys.

## Nutzungshinweise ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Changes for 3.1 ##

* Resource Monitor officially supports Windows 8.1.
* Übersetzungen aktualisiert.

## Änderungen bis 3.0 ##

* psutil-Abhängigkeit auf 1.2.1 aktualisiert.
* Announcement of current Windows version, CPU architecture and service pack
  if any (NVDA+Shift+6).
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Änderungen bis 2.4 ##

* Neue Sprachen: vereinfachtes chinesisch, ukrainisch.
* Übersetzungen aktualisiert.

## Änderungen bis 2.3 ##

* bulgarische Übersetzung hinzugefügt.

## Änderungen bis 2.2 ##

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish,
  French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali,
  Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil
  and Turkish.

## Änderungen bis 2.1 ##

* psutil auf Version 0.6.1 aktualisiert.
* Größere Zeitverzögerung beim Erhalt von Informationen von Datenträgern
  beseitigt.
* %s in {freundlicheVariableNamen} übersetzt.
* Code cleanup.

## Änderungen bis 2.0 ##

* Möglichkeit zur Übersetzung sowie Übersetzungskommentare hinzugefügt.

## Änderungen bis 1.0 ##

* Ehrstveröffentlichung

[[!tag stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm
