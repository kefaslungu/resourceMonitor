[[!meta title="resourceMonitor"]]

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili and other NVDA contributors
* Stable version: [version 2.4][1]
* Development version: [version 3.0-dev][2]

This plugin gives information about CPU load, memory usage and other resource usage information.

# Shortcuts #

* NVDA+Shift+E Presents used ram, average processor load, and battery info if available,
* NVDA+Shift+1 Presents the average processor load and the load of each core (if multicore CPU's are present),
* NVDA+Shift+2/5 Presents the used and total space for both physical and virtual ram,
* NVDA+Shift+3 Presents the used and total space of the static and removable drives on this computer,
* NVDA+Shift+4 Presents battery percentage, charging status, remaining time (if not charging), and a warning if the battery is low or critical,
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit of Windows (32 or 64-bit) and service pack if any.

If you have NvDA 2013.3 or later installed, you can change these shortcut keys.

## Usage notes ##

This add-on does not replace task manager and other system information programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper Threading where number of CPU's is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Changes for 3.0-dev ##

* Updated psutil dependency to 1.0.1.
* Announcement of current Windows version, CPU bit and service pack if any (NVDA+Shift+6).
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing resource commands two times.

## Changes for 2.4 ##

* New languages: Chinese (simplified), Ukrainian.
* Updated translations.

## Changes for 2.3 ##

* Added Bulgarian translation.

## Changes for 2.2 ##

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish, French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali, Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil and Turkish.

## Changes for 2.1 ##

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Replaced %s-es into {friendlyVariableNames}.
* Code cleanup.

## Changes for 2.0 ##

* added translation support and translation comments.

## Changes for 1.0 ##

* Initial Release

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
