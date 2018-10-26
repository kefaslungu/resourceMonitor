# Resource Monitor #

* Tác giả: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala và các
  cộng tác viên khác của NVDA
* Tải về [phiên bản chính thức][1]

Add-on này cung cấp các thông tin về tải CPU, sử dụng bộ nhớ và các nguồn
tài nguyên khác.

# Các phím tắt #

* NVDA+Shift+E thể hiện mức độ sử dụng ram, tốc độ tải trung bình của vi xử
  lý và pin nếu có.
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
* NVDA+Shift+7 presents the system's uptime.

If you have NvDA 2013.3 or later installed, you can change these shortcut
keys.

## Các lưu ý sử dụng ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores.
* If there is heavy disk activity such as copying large files, there might
  be delays when obtaining disk usage information.
* Support for Windows XP from this add-on ended on December 31,
  2017. Support for Windows Server 2003, Vista and Server 2008 ended on June
  30, 2018.

## Phiên bản 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## Phiên bản 18.04

Version 18.04.x is the last release to support Windows releases earlier than
7 SP1.

* Last release to support Windows Server 2003, Vista and Server 2008.
* Better detection of Windows 10 releases and distinguishing between public
  and Insider Preview builds.

## Phiên bản 17.12

* Added support for 64-bit ARM processors on Windows 10.

## Phiên bản 17.09

Important: Version 17.09.x is the last version to support Windows XP.

* Phiên bản cuối cùng chạy trên Windows XP.
* Windows 10 build 16278 and later is recognized as Version 1709. A minor
  revision for this add-on will be released once Version 1709 stable build
  is released.

## Phiên bản 17.07.1

* Reintroduce support for Windows XP (broken since version 17.02).

## Phiên bản 17.05

* Announcement of system uptime (time passed since last boot; NVDA+Shift+7).

## Phiên bản 17.02

* Updated psutil dependency to 5.0.1.
* When checking disk usage, NVDA will no longer present an error dialog on
  some systems where a removable media is not properly recognized (such as
  when a card isn't inserted into a card reader).)

## Phiên bản 16.08

Starting with version 16.08, add-on releases will be shown as
year.month.revision.

* Various revisions of Windows 10 are now properly recognized (such as 1607
  for build 14393).
* Windows 10 build revisions (after installing cumulative updates) are
  properly recognized (such as 14393.51).
* If using Insider Preview builds, this fact is recognized.

## Các thay đổi cho phiên bản 4.5 ##

* Add-on repository has moved to GitHub (can be found at
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 is properly recognized.

## Các thay đổi cho phiên bản 4.0 ##

* Updated psutil dependency to 2.2.1.
* Vastly improved performance when obtaining information on CPU load.
* Added support for recognition of Windows 10.
* In Windows 10, the build number of Windows will also be announced.
* You can use Add-ons Manager to access add-on help.

## Các thay đổi cho phiên bản 3.1 ##

* Resource Monitor officially supports Windows 8.1.
* Cập nhật các bản phiên dịch.

## Các thay đổi cho phiên bản 3.0 ##

* Updated psutil dependency to 1.2.1.
* Announcement of current Windows version, CPU architecture and service pack
  if any (NVDA+Shift+6).
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## Các thay đổi cho phiên bản 2.4 ##

* Các ngôn ngữ mới: Chinese (simplified), Ukrainian.
* Cập nhật các bản phiên dịch.

## Các thay đổi cho phiên bản 2.3 ##

* Added Bulgarian translation.

## Các thay đổi cho phiên bản 2.2 ##

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish,
  French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali,
  Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil
  and Turkish.

## Các thay đổi cho phiên bản 2.1 ##

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Dọn dẹp mã nguồn.

## Các thay đổi cho phiên bản 2.0 ##

* added translation support and translation comments.

## Các thay đổi cho phiên bản 1.0 ##

* Bản phát hành đầu tiên

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
