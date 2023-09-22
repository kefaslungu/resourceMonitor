# Theo dõi tài nguyên #

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst and other NVDA contributors
* Tải về [phiên bản chính thức][1]
* NVDA compatibility: 2022.4 and later

Add-on này cung cấp các thông tin về tải CPU, sử dụng bộ nhớ và các nguồn
tài nguyên khác.

# Các phím tắt

* NVDA+Shift+E: presents used ram, average processor load, and battery info
  if available.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's
  are present the load of each core.
* NVDA+Shift+2/5: presents the used and total space for both physical and
  virtual ram.
* NVDA+Shift+3: presents the used and total space of the static and
  removable drives.
* NVDA+Shift+4: presents battery percentage, charging status, remaining time
  (if not charging), and a warning if the battery is low or critical.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service
  pack numbers.
* NVDA+Shift+7: presents the system's uptime.
* NVDA+Shift+8: presents information on the wireless connection, ssid name
  and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Các lưu ý sử dụng

Add-on này không thay thế cho task manager và các trình kiểm tra thông tin
hệ thống khác của Windows. Cũng lưu ý những điểm sau:

* Resource information cannot be copied to clipboard if running the add-on
  in secure screens.
* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores. On some newer computers, not all CPU
  cores will have hyper-threading enabled.
* Nếu có một hoạt động làm nặng ổ đĩa như sao chép các tập tin lớn, có thể
  phải chờ trong khi lấy thông tin về mức độ sử dụng ô đĩa.
* When announcing processor architecture information, "x86" and "AMD64"
  refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 or later.

Note on license: this add-on uses Psutil, licensed under 3-Clause BSD
License which is compatible with GNU General Public License.

## Version 23.09

* NVDA will no longer log startup error messages on Windows Server systems
  when wireless capability modules are unavailable.

## Version 23.06

* Situation where resourceMonitor doesn't work properly due to
  unavailability of wireless adapters has been fixed.

## Version 23.05.1

wlanReporter NVDA-addon is now part of resourceMonitor!

* The old way of checking for wireless connections has been replaced by the
  windows API from wlanReporter: https://github.com/kvark128/WlanReporter/ .

	* After speaking SSID name and strength, NVDA will also now tell you the
	  security type of your network.
	* NVDA will now alert you when you connect and disconnect from a wireless
	  network.
	* NVDA will now alert you when wireless connections is turned on or off.

## Version 23.05

* added the ability to detect and present the state of the connected
  wireless network.

	* Announces the name of the connected wireless SSID.
	* Announces the strength of the ssid
	* Announce SSID not found if None is detected.

## Version 23.02

* NVDA 2022.4 or later is required.
* Windows 10 21H2 (November 2021 Update/build 19044) or later is required.

## Version 23.01

* NVDA 2022.3 or later is required.
* Windows 10 or later is required as Windows 7, 8, and 8.1 are no longer
  supported by Microsoft as of January 2023.
* Updated psutil dependency to 5.9.4.
* NVDA will announce actual processor architecture (x86/AMD64/ARM64) as part
  of Windows version information.
* On single-core systems, NVDA will no longer announce CPU core load as
  average CPU load is the same as core load.

## Version 22.03

Version 22.03 is the last stable version to support Windows 7 Service Pack
1, 8, and 8.1.

* NVDA 2021.3 or later is required.
* A warning message will be displayed when attempting to install the add-on
  on Windows 7, 8, and 8.1.
* Updated psutil dependency to 5.9.0.

## Version 22.01

* NVDA 2021.2 or later is required.

## Version 21.10

* NVDA 2021.1 or later is required due to changes to NVDA that affects this
  add-on.

## Version 21.08

* Minimum Windows release requirement is now tied to NVDA releases.
* Windows builds 20348 and 22000 are recognized as Windows Server 2022 and
  Windows 11, respectively.
* On Insider Preview builds, Windows release such as "Windows 10" will not
  be used. Instead NvDA will announce "Windows Insider".
* On 64-bit systems, processor architecture (x64 or ARM64) will be announced
  as part of Windows version information.

## Version 21.04

* NVDA 2020.4 or later is required.
* Updated psutil dependency to 5.8.0.
* When pressing add-on commands twice to copy resource information to
  clipboard, NVDA will announce resource summary that is being copied.

## Version 21.01

* Updated psutil dependency to 5.7.3.
* Shortened Windows version message.
* On Windows 8.1, build.revision will be announced as part of Windows
  version message, similar to Windows 10.

## Version 20.09

* System uptime is now given as days, hours, minutes, seconds.
* Windows Server Insider Preview build 20201 or later is properly recognized
  as a Server Insider build.

## Version 20.07

* Windows 10 Version 20H2 is properly recognized when obtaining Windows
  version information (NVDA+Shift+6).
* Simplified Windows 10 version message i.e. Windows 10 YYMM instead of
  Windows 10verYYMM when pressing NVDA+Shift+6.

## Version 20.06

* Resolved many coding style issues and potential bugs with Flake8.

## Version 20.04

* Updated psutil dependency to 5.7.0.

## Version 20.01

* NVDA 2019.3 or later is required due to extensive use of Python 3.

## Version 19.11

* Improved detection of Windows Insider Preview builds, especially for 20H1
  and beyond.

## Version 19.07

* Updated psutil dependency to 5.6.3.
* Internal changes to battery status announcement command.

## Version 18.12

* Internal changes to support future NVDA releases.

## Phiên bản 18.10

* Mã nguồn đã được làm cho tương thích hơn với Python 3.
* Cập nhật psutil dependency lên 5.4.7.
* Khi lấy thông tin về tổng dung lượng ổ đĩa và mức sử dụng bộ nhớ, NVDA sẽ
  không còn báo lỗi nếu dùng một máy tính hay dịch vụ với nhiều hơn một
  petabyte dung lượng am hay ổ đĩa.
* Các giá trị của việc sử dụng bộ nhớ và ổ đĩa được hiển thị tới hai chữ số
  thập phân (ví dụ: 4.00 GB thay vì 4.0 GB).
* Cải thiện khả năng phát hiện cho Windows Insider Preview builds.

## Phiên bản 18.04

Phiên bản 18.04.x là bản phát hành cuối cùng hỗ trợ các bản Windows phát
hành trước 7 SP1.

* Phiên bản cuối cùng hỗ trợ Windows Server 2003, Vista và Server 2008.
* Phát hiện tốt hơn với các bản phát hành Windows 10 và sự khác nhau giữa
  các bản chính thức và Insider Preview.

## Phiên bản 17.12

* Đã hỗ trợ cho 64-bit ARM processors trên Windows 10.

## Phiên bản 17.09

Quan trọng: phiên bản 17.09.x là phiên bản cuối cùng hỗ trợ Windows XP.

* Phiên bản cuối cùng chạy trên Windows XP.
* Windows 10 build 16278 trở lên được nhận dạng là phiên bản 1709. Một bản
  chỉnh sửa chính cho add-on này sẽ được phát hành khi phiên bản 1709 chính
  thức được phát hành.

## Phiên bản 17.07.1

* Hỗ trợ lại cho Windows XP (đã bị bỏ từ phiên bản 17.02).

## Phiên bản 17.05

* Thông báo thời gian hoạt động của hệ thống (thời gian trôi qua kể từ lần
  khởi động cuối cùng; NVDA + Shift + 7).

## Phiên bản 17.02

* Cập nhật psutil dependency lên 5.0.1.
* Khi kiểm tra mức độ sử dụng đĩa, NVDA sẽ không còn tình trạng hiển thị hộp
  thoại báo lỗi trên vài hệ thống có ổ đĩa di động không được nhận dạng
  chính xác (như khi thẻ nhớ không được gắn vào ổ đọc thẻ).)

## Phiên bản 16.08

Từ phiên bản 16.08, các bản phát hành của add-on sẽ được hiển thị tên là
năm.tháng.bản chỉnh sửa.

* Nhiều bản chỉnh sửa của Windows 10 giờ đã được nhận dạng chính xác (như
  1607 cho số hiệu 14393).
* Windows 10 bản sửa đổi (sau khi cài các bản cập nhật tích lũy) đã được
  nhận dạng chính xác (ví dụ 14393.51).
* Nếu đang dùng bản Insider Preview, trường hợp này cũng được nhận dạng.

## Các thay đổi cho phiên bản 4.5

* Kho add-on đã được chuyển sang GitHub (có thể tìm thấy tại
  https://github.com/josephsl/resourcemonitor).
* Windows Server 2016 đã được nhận dạng chính xác.

## Các thay đổi cho phiên bản 4.0

* Cập nhật psutil dependency lên 2.2.1.
* Cải thiện lớn cho hiệu xuất vận hành khi lấy thông tin về tải CPU.
* Đã hỗ trợ tính năng nhận dạng của Windows 10.
* Trong Windows 10, số hiệu (build number) của Windows cũng sẽ được thông
  báo.
* Bạn có thể truy cập hỗ trợ cho add-on thông qua trình quản lý add-on.

## Các thay đổi cho phiên bản 3.1

* Theo dõi tài nguyên chính thức hỗ trợ Windows 8.1.
* Cập nhật các bản phiên dịch.

## Các thay đổi cho phiên bản 3.0

* Cập nhật psutil dependency lên 1.2.1.
* Thông báo phiên bản Windows hiện tại, kiểu CPU và gói dịch vụ nếu có
  (NVDA+Shift+6).
* Khả năng thay đổi phím tắt cho add-on (NVDA 2013.3 trở lên).
* Khả năng sao chép  thông tin tài nguyên cụ thể vào bộ nhớ tạm bằng cách
  bấm lệnh xem thông tin hai lần.

## Các thay đổi cho phiên bản 2.4

* Các ngôn ngữ mới: tiếng Trung Quốc (giản thể), tiếng Ukraina.
* Cập nhật các bản phiên dịch.

## Các thay đổi cho phiên bản 2.3

* Đã thêm bản dịch tiếng Bungari.

## Các thay đổi cho phiên bản 2.2

* Đã thêm các bản dịch sau: tiếng Ả Rập, Aragonese, Croatia, Hà Lan, Phần
  Lan, Pháp, Galicia, Đức, Hungary, Ý, Nhật Bản, Hàn Quốc, Nepal, Ba Lan, Bồ
  Đào Nha (Brazil), Nga, Slovak, Slovenia, Tây Ban Nha, Tamil và Thổ Nhĩ Kỳ.

## Các thay đổi cho phiên bản 2.1

* Cập nhật psutil dependency lên phiên bản 0.6.1.
* Sửa lỗi đợi lâu khi lấy thông tin ổ đĩa.
* Dọn dẹp mã nguồn.

## Các thay đổi cho phiên bản 2.0

* thêm các hỗ trợ và chú thích phiên dịch.

## Các thay đổi cho phiên bản 1.0

* Bản phát hành đầu tiên

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
