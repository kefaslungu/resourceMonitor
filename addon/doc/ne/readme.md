# श्रोत अनुगामी (resourceMonitor) #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala and other
  NVDA contributors
* Download [stable version][1]
* NVDA compatibility: 2017.4 to 2019.2

This add-on gives information about CPU load, memory usage and other
resource usage information.

# द्रुतमार्ग #

* NVDA+Shift+E Presents used ram, average processor load, and battery info
  if available.
* नेत्रवानी +Shift+१ ले प्रोसेसरको औसत भार र यदी बहुकोर CPU's भएमा यि
  कोरहरुको भार समेत प्रस्तुत गर्ने छ ।
* NVDA+Shift+2/5 Presents the used and total space for both physical and
  virtual ram.
* NVDA+Shift+3 Presents the used and total space of the static and removable
  drives.
* NVDA+Shift+4 Presents battery percentage, charging status, remaining time
  (if not charging), and a warning if the battery is low or critical.
* नेत्रवाणी+Shift+6 चालु विन्डोजको संस्करण, CPU बीट (३२ वा ६४-विट) र सर्भिस
  प्याक  सङ्ख्या बताउने छ ।
* NVDA+Shift+7 presents the system's uptime.

यदि चालू नेत्रवाणी २०१३.३ अथवा यस पछीको संस्करण छ भने तपाइले यी द्रुतमार्ग
कुञ्जी बदल्न सक्नु हुन्छ ।

## टिप्पणिको प्रयोग ##

यो उप-कर्मीले कार्य व्यबस्थापक र अरू विन्डोज सम्बन्धी सूचना कार्यक्रम
प्रणालीलाई   विस्थापन गर्दैन । यो पनि ध्यान दिनु होला:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores.
* If there is heavy disk activity such as copying large files, there might
  be delays when obtaining disk usage information.
* Support for Windows XP from this add-on ended on December 31,
  2017. Support for Windows Server 2003, Vista and Server 2008 ended on June
  30, 2018.

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## Version 18.04

Version 18.04.x is the last release to support Windows releases earlier than
7 SP1.

* Last release to support Windows Server 2003, Vista and Server 2008.
* Better detection of Windows 10 releases and distinguishing between public
  and Insider Preview builds.

## Version 17.12

* Added support for 64-bit ARM processors on Windows 10.

## Version 17.09

Important: Version 17.09.x is the last version to support Windows XP.

* Last version to run on Windows XP.
* Windows 10 build 16278 and later is recognized as Version 1709. A minor
  revision for this add-on will be released once Version 1709 stable build
  is released.

## Version 17.07.1

* Reintroduce support for Windows XP (broken since version 17.02).

## Version 17.05

* Announcement of system uptime (time passed since last boot; NVDA+Shift+7).

## Version 17.02

* Updated psutil dependency to 5.0.1.
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

## Changes for 4.5 ##

* Add-on repository has moved to GitHub (can be found at
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 is properly recognized.

## Changes for 4.0 ##

* Updated psutil dependency to 2.2.1.
* Vastly improved performance when obtaining information on CPU load.
* Added support for recognition of Windows 10.
* In Windows 10, the build number of Windows will also be announced.
* You can use Add-ons Manager to access add-on help.

## ३.1 संस्करणमा गरिएका परिवर्तनहरू । ##

* श्रोत अनुगामीले आधिकारीक रुपमा नै विन्डोज ८.१ लाइ समर्थन गर्छ ।
* अनुवादलाई अद्यावधिक गरियो 

## ३.० संस्करणमा गरिएका परिवर्तनहरू । ##

* psutil आधारितलाई १.२.१ मा अद्यावधिक गरियो ।.
* नेत्रवाणी+Shift+6 चालु विन्डोजको संस्करण, CPU बीट (३२ वा ६४-विट) र सर्भिस
  प्याक सङ्ख्या बताउने छ ।
* २०१३.३ वा यस पछिका नेत्रवाणीमा लागु हुने गरी उप-कर्मीको द्रुतमार्ग बदल्ने
  क्षमता थप गरियो ।
* स्रोत आदेसहरूलाई दुई पटक दबाएर क्लिपपाटीमा स्रोतहरू सम्बन्धी वैयक्तिक
  सुचनालाई सञ्चय गर्ने सुविदा थप गरियो ।

## २.४ मा गरिएका परिवर्तनहरू ##

* नयाँ भाषाहरू: सरलीकृत चिनिया, युक्रेनी
* अनुवादलाई अद्यावधिक गरियो 

## २.३ मा गरिएका परिवर्तनहरू ##

* बुल्गेरियाली अनुवाद थपियो ।

## २.१ संस्करणमा गरिएका परिवर्तनहरू । ##

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish,
  French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali,
  Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil
  and Turkish.

## २.१ संस्करणमा गरिएका परिवर्तनहरू । ##

* psutil आधारितलाई ०.६.१ मा अद्यावधिक गरियो ।.
* भकारि सम्बन्धी जानकारी लिदा लामो समय लाग्ने समस्या हल गरियो ।
* Code cleanup.

## २.० संस्करणमा गरिएका परिवर्तनहरू । ##

* अनुवाद टिप्पणी र अनुवाद सहयोग थप गरियो ।.

## १.० संस्करणमा गरिएका परिवर्तनहरू । ##

* पहिलो सार्वजनिकीकरण

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
