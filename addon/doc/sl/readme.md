# Nadzornik porabe #

* Avtorji: Alex Hall, Joseph Lee, beqa gozalishvili in drugi NVDA sodelujoči
* Končnana različica: [različica 2.4][1]
* Razvojna različica: [različica 3.0-razvojna][2]

This plugin gives information about CPU load, memory usage, battery and disk
usage status.

# Bližnjice #

* NVDA+Shift+E Presents used ram, average processor load, and battery info
  if available,
* NVDA+Shift+1 Presents the average processor load and the load of each
  core,
* NVDA+Shift+2/5 Presents the used and total space for both physical and
  virtual ram,
* NVDA+Shift+3 Presents the used and total space of the static and removable
  drives on this computer,
* NVDA+Shift+4 Presents battery percentage, charging status, remaining time
  (if not charging), and a warning if the battery is low or critical,
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or
  64-bit) and service pack if any (version 3.0-dev).

## Opombe k uporabi ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Spremembe v 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Spremembe v 2.4 ##

* New languages: Chinese (simplified), Ukrainian.
* Updated translations.

## Changes for 2.3 ##

* Added Bulgarian translation.

## Changes for 2.2 ##

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish,
  French, Galatian, German, Hungarian, Italian, Japanese, Korean, Nepali,
  Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil
  and Turkish.

## Spremembe v 2.1 ##

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Replaced %s-es into {friendlyVariableNames}.
* Manjše čiščenje v kodi

## Spremembe v 2.0 ##

* Dodani podpora prevodom in komentarji v datoteki s prevodi

## Spremembe v 1.0 ##

* Osnovna izdaja

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
