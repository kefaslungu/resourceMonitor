# resource Monitor #

* سازندگان: Alex Hall, Joseph Lee, beqa gozalishvili و دیگر حامیان NVDA
* Stable version: [version 2.4][1]
* Development version: [version 3.0-dev][2]

This plugin gives information about CPU load, memory usage, battery and disk
usage status.

# کلیدهای میانبر #

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

## Usage notes ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## Changes for 3.0-dev ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## تغییرات داده شده در نسخه 2.4 ##

* زبانهای جدید: چینی (ساده شده) ، اوکراینی.
* برگردانها روزآمدسازی شد

## تغییرات داده شده در نسخه 2.3 ##

* زبان بلغاری اضافه گردید.

## تغییرات داده شده در نسخه 2.2 ##

* زبانهای زیر اضافه گردید: عربی، آراگونی ، کرواتی، هلندی ، فنلاندی، فرانسوی،
  غلاطیه ، آلمانی ، مجارستانی ، ایتالیایی ، ژاپنی ، کره ای ، نپالی ، لهستانی
  ، پرتغالی (برزیل) ، روسی، اسلواکی ، اسلوونیایی ، اسپانیایی ، تامیل و ترکی
  .

## تغییرات داده شده در نسخه 2.1 ##

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Replaced %s-es into {friendlyVariableNames}.
* a bit code cleanup

## تغییرات داده شده در نسخه 2.0 ##

* پشتیبانی برگردان و بیش گویه های برگردان اضافه گردید.

## تغییرات داده شده در نسخه 1.0 ##

* انتشار اولیه

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
