# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors
* Download [stable version][1]
* NVDA compatibility: 2022.4 and later

This add-on gives information about CPU load, memory usage and other resource usage information.

# Shortcuts

* NVDA+Shift+E: presents used ram, average processor load, and battery info if available.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's are present the load of each core.
* NVDA+Shift+2/5: presents the used and total space for both physical and virtual ram.
* NVDA+Shift+3: presents the used and total space of the static and removable drives.
* NVDA+Shift+4: presents battery percentage, charging status, remaining time (if not charging), and a warning if the battery is low or critical.
* NVDA+Shift+6: presents  CPU Architecture and Windows version and service pack numbers.
* NVDA+Shift+7: presents the system's uptime.
* NVDA+Shift+8: presents information on the wireless connection, ssid name and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Usage notes

This add-on does not replace task manager and other system information programs for Windows. Also note the following:

* Resource information cannot be copied to clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* If there is heavy disk activity such as copying large files, there might be delays when obtaining disk usage information.
* When announcing processor architecture information, "x86" and "AMD64" refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

Note on license: this add-on uses Psutil, licensed under 3-Clause BSD License which is compatible with GNU General Public License.

## Version 23.11

* Downgraded psutil dependency to 5.9.4 due to problems with memory usage announcements.

## Version 23.10

* Updated psutil dependency to 5.9.5.

## Version 23.09

* NVDA will no longer log startup error messages on Windows Server systems when wireless capability modules are unavailable.

## Version 23.06

* Situation where resourceMonitor doesn't work properly due to unavailability of wireless adapters has been fixed.

## Version 23.05.1

wlanReporter NVDA-addon is now part of resourceMonitor!

* The old way of checking for wireless connections has been replaced by the windows API from wlanReporter: https://github.com/kvark128/WlanReporter/ .
  * After speaking SSID name and strength, NVDA will also now tell you the security type of your network.
  * NVDA will now alert you when you connect and disconnect from a wireless network.
  * NVDA will now alert you when wireless connections is turned on or off.

## Version 23.05

* added the ability to detect and present the state of the connected wireless network.
  * Announces the name of the connected wireless SSID.
  * Announces the strength of the ssid
  * Announce SSID not found if None is detected.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer supported by Microsoft as of January 2023.
* Updated psutil dependency to 5.9.4.
* NVDA will announce actual processor architecture (x86/AMD64/ARM64) as part of Windows version information.
* On single-core systems, NVDA will no longer announce CPU core load as average CPU load is the same as core load.

## Version 22.03

Version 22.03 is the last stable version to support Windows 7 Service Pack 1, 8, and 8.1.

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on on Windows 7, 8, and 8.1.
* Updated psutil dependency to 5.9.0.

## Version 22.01

* NVDA 2021.2 or later is required.

## Version 21.10

* NVDA 2021.1 or later is required due to changes to NVDA that affects this add-on.

## Version 21.08

* Minimum Windows release requirement is now tied to NVDA releases.
* Windows builds 20348 and 22000 are recognized as Windows Server 2022 and Windows 11, respectively.
* On Insider Preview builds, Windows release such as "Windows 10" will not be used. Instead NvDA will announce "Windows Insider".
* On 64-bit systems, processor architecture (x64 or ARM64) will be announced as part of Windows version information.

## Version 21.04

* NVDA 2020.4 or later is required.
* Updated psutil dependency to 5.8.0.
* When pressing add-on commands twice to copy resource information to clipboard, NVDA will announce resource summary that is being copied.

## Version 21.01

* Updated psutil dependency to 5.7.3.
* Shortened Windows version message.
* On Windows 8.1, build.revision will be announced as part of Windows version message, similar to Windows 10.

## Version 20.09

* System uptime is now given as days, hours, minutes, seconds.
* Windows Server Insider Preview build 20201 or later is properly recognized as a Server Insider build.

## Version 20.07

* Windows 10 Version 20H2 is properly recognized when obtaining Windows version information (NVDA+Shift+6).
* Simplified Windows 10 version message i.e. Windows 10 YYMM instead of Windows 10verYYMM when pressing NVDA+Shift+6.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Updated psutil dependency to 5.7.0.

## Version 20.01

* NVDA 2019.3 or later is required due to extensive use of Python 3.

## Version 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1 and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give errors if using a computer or a service with more than a petabyte of RAM or disk size.
* Values for memory and disk usage are shown with up to two decimal places (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## Version 18.04

Version 18.04.x is the last release to support Windows releases earlier than 7 SP1.

* Last release to support Windows Server 2003, Vista and Server 2008.
* Better detection of Windows 10 releases and distinguishing between public and Insider Preview builds.

## Version 17.12

* Added support for 64-bit ARM processors on Windows 10.

## Version 17.09

Important: Version 17.09.x is the last version to support Windows XP.

* Last version to run on Windows XP.
* Windows 10 build 16278 and later is recognized as Version 1709. A minor revision for this add-on will be released once Version 1709 stable build is released.

## Version 17.07.1

* Reintroduce support for Windows XP (broken since version 17.02).

## Version 17.05

* Announcement of system uptime (time passed since last boot; NVDA+Shift+7).

## Version 17.02

* Updated psutil dependency to 5.0.1.
* When checking disk usage, NVDA will no longer present an error dialog on some systems where a removable media is not properly recognized (such as when a card isn't inserted into a card reader).)

## Version 16.08

Starting with version 16.08, add-on releases will be shown as year.month.revision.

* Various revisions of Windows 10 are now properly recognized (such as 1607 for build 14393).
* Windows 10 build revisions (after installing cumulative updates) are properly recognized (such as 14393.51).
* If using Insider Preview builds, this fact is recognized.

## Changes for 4.5

* Add-on repository has moved to GitHub (can be found at https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 is properly recognized.

## Changes for 4.0

* Updated psutil dependency to 2.2.1.
* Vastly improved performance when obtaining information on CPU load.
* Added support for recognition of Windows 10.
* In Windows 10, the build number of Windows will also be announced.
* You can use Add-ons Manager to access add-on help.

## Changes for 3.1

* Resource Monitor officially supports Windows 8.1.
* Updated translations.

## Changes for 3.0

* Updated psutil dependency to 1.2.1.
* Announcement of current Windows version, CPU architecture and service pack if any (NVDA+Shift+6).
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing resource commands two times.

## Changes for 2.4

* New languages: Chinese (simplified), Ukrainian.
* Updated translations.

## Changes for 2.3

* Added Bulgarian translation.

## Changes for 2.2

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish, French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali, Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil and Turkish.

## Changes for 2.1

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Code cleanup.

## Changes for 2.0

* added translation support and translation comments.

## Changes for 1.0

* Initial Release

[1]: http://addons.nvda-project.org/files/get.php?file=resourceMonitor
