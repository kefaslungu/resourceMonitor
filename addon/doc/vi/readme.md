# Theo dõi tài nguyên

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

Add-on này cung cấp các thông tin về tải CPU, sử dụng bộ nhớ và các nguồn tài nguyên khác.

## Các phím tắt

All commands support speech on demand mode.

* NVDA+Shift+E: presents used ram, average processor load, and battery info if available.
* NVDA+Shift+1: presents the average processor load and if multicore CPU's are present the load of each core.
* NVDA+Shift+2/5: presents the used and total space for both physical and virtual ram.
* NVDA+Shift+3: presents the used and total space of the static and removable drives.
* NVDA+Shift+4: presents battery percentage, charging status, remaining time (if not charging), and a warning if the battery is low or critical.
* NVDA+Shift+6: presents CPU Architecture and Windows version and service pack numbers.
* NVDA+Shift+7: presents the system's uptime.
* NVDA+Shift+8: presents information on the wireless connection, ssid name and strength, or no ssid if there is none available.

You can change these shortcut keys via input gestures dialog.

## Các lưu ý sử dụng

Add-on này không thay thế cho task manager và các trình kiểm tra thông tin hệ thống khác của Windows. Cũng lưu ý những điểm sau:

* Resource information cannot be copied to clipboard if running the add-on in secure screens.
* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores. On some newer computers, not all CPU cores will have hyper-threading enabled.
* Nếu có một hoạt động làm nặng ổ đĩa như sao chép các tập tin lớn, có thể phải chờ trong khi lấy thông tin về mức độ sử dụng ô đĩa.
* When announcing processor architecture information, "x86" and "AMD64" refer to 32-bit and 64-bit (x64) Intel and AMD processors, respectively.
* This add-on requires Windows 10 22H2 (2022 Update/build 19045) or later.
* Installing the add-on on Windows 10/11 LTSC is not supported.
