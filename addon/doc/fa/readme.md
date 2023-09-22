# دیده‌بان منابع (Resource Monitor) #

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Tuukka
  Ojala, Ethin Probst and other NVDA contributors
* دانلود [نسخه‌ی پایدار][1]
* NVDA compatibility: 2022.4 and later

این افزونه، اطلاعاتی درباره‌ی عملکرد CPU، میزان استفاده از حافظه، و دیگر
اطلاعات مربوط به استفاده از منابع سیستم را در اختیارتان میگذارد.

# کلیدهای میانبر

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

## تذکراتی در مورد استفاده از افزونه

این افزونه جای task manager و دیگر برنامه‌های اطلاعات سیستم که برای ویندوز
طراحی شده‌اند را نمیگیرد. همچنین، نکات زیر را نیز به یاد داشته باشید:

* Resource information cannot be copied to clipboard if running the add-on
  in secure screens.
* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores. On some newer computers, not all CPU
  cores will have hyper-threading enabled.
* چنانچه دیسک‌ها درگیر فعالیت سنگینی مانند کپی فایل‌های بزرگ باشند، ممکن است
  هنگام به‌دست‌آوردن اطلاعات میزان استفاده از دیسک، تأخیرهایی به وجود بیاید.
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

## Version 18.10

* Code has been made more compatible with Python 3.
* Updated psutil dependency to 5.4.7.
* When obtaining disk capacity and memory usage, NVDA will no longer give
  errors if using a computer or a service with more than a petabyte of RAM
  or disk size.
* Values for memory and disk usage are shown with up to two decimal places
  (e.g. 4.00 GB instead of 4.0 GB).
* Improved detection of Windows Insider Preview builds.

## نسخه‌ی 18.04

نسخه‌ی 18.04.x آخرین نسخه‌ایست که از ویندوزهای قدیمیتر از ویندوز 7 SP1
پشتیبانی میکند.

* آخرین انتشاری است که ویندوز سرور 2003، ویستا و سرور 2008 را پشتیبانی
  میکند.
* شناسایی بهتر انتشارهای ویندوز ۱۰ و تشخیص دادن ساخت‌های پیش‌نمایش عمومی
  (public) و داخلی (insider).

## نسخه‌ی 17.12

* پشتیبانی از پردازشگرهای ۶۴ بیتی ARM در ویندوز ۱۰.

## نسخه‌ی 17.09

مهم: نسخه‌ی 17.09.x، آخرین نسخه‌ایست که از ویندوز XP پشتیبانی میکند.

* آخرین نسخه‌ای که روی ویندوز XP اجرا میشود.
* ویندوز ۱۰ ساخت 16278 و بعد از آن به عنوان نسخه‌ی 1709 شناسایی
  میشوند. بازبینی کوچکی از افزونه، وقتی نسخه‌ی پایدار ساخت 1709 منتشر شود،
  در دسترس قرار خواهد گرفت.

## نسخه‌ی 17.07.1

* پشتیبانی مجدد از ویندوز XP که در نسخه‌ی 17.02 قطع شده بود.

## نسخه‌ی 17.05

* اعلام زمان بالا بودن سیستم؛ زمانی که از آخرین بوت سیستم سپری شده است؛
  NVDA+Shift+7).

## نسخه‌ی 17.02

* متعلقات psutil به نسخه‌ی 5.0.1 به‌روز شد.
* در زمان بررسی میزان استفاده از دیسک، NVDA دیگر در بعضی سیستم‌ها، هنگامی که
  یک رسانه‌ی قابل حمل به‌درستی توسط سیستم شناسایی نشده، مثلا کارتی داخل
  کارت‌خوان قرار ندارد، پنجره‌ی خطا نشان نمیدهد.

## نسخه‌ی 16.08

با آغاز به انتشار نسخه‌ی 16.08، انتشارهای افزونه به صورت سال.ماه.بازبینی
نشان داده میشوند.

* نسخه‌های گوناگونی از ویندوز ۱۰ حالا به‌درستی شناسایی میشوند (مانند 1607
  برای بیلد 14393).
* نسخه بیلدهای ویندوز ۱۰ (بعد از نصب به‌روزرسانی‌ها) به‌درستی شناخته میشوند
  (مثل 14393.51).
* چنانچه در حال استفاده از نسخه‌های پیش‌نمایش داخلی (Insider Preview) باشید،
  این مورد توسط افزونه شناسایی میشود.

## تغییرات در نسخه‌ی 4.5

* منبع فایل‌های افزونه به GitHub منتقل شده است. میتوانید آنرا در این نشانی
  بیابید: https://github.com/josephsl/resourcemonitor.
* ویندوز سرور 2016 به‌درستی شناسایی میشود.

## تغییرات در نسخه‌ی 4.0

* متعلقات psutil به نسخه‌ی 2.2.1 به‌روز شد.
* عملکرد افزونه، هنگام دریافت اطلاعات مربوط به بار CPU، به مقدار زیادی بهبود
  یافت.
* پشتیبانی از شناسایی ویندوز ۱۰ افزوده شد.
* در ویندوز ۱۰، شماره‌ی ساخت ویندوز (build number) هم اعلام خواهد شد.
* میتوانید برای دسترسی به راهنمای افزونه، از مدیر افزونه‌ها استفاده کنید.

## تغییرات در نسخه‌ی 3.1

* دیده‌بان منابع بطور رسمی از ویندوز 8.1 پشتیبانی میکند.
* ترجمه‌ها به‌روز شد.

## تغییرات در نسخه‌ی 3.0

* متعلقات psutil به نسخه‌ی 1.2.1 به‌روز شد.
* اعلام نسخه‌ی جاری ویندوز، معماری CPU و در صورت موجود بودن، بسته‌ی خدماتی
  (service pack) (NVDA+Shift+6).
* توانایی تغییر کلیدهای میانبر افزونه (NVDA 2013.3 یا بالاتر).
* توانایی کپی اطلاعات هرکدام از منابع در کلیپ‌برد با فشردن فرمان مربوط، دو
  بار پشت سر هم.

## تغییرات در نسخه‌ی 2.4

* زبان‌های جدید: چینی (ساده‌شده)، اوکراینی.
* ترجمه‌ها به‌روز شد.

## تغییرات نسخه‌ی 2.3

* ترجمه‌ی بلغاری افزوده شد.

## تغییرات در نسخه‌ی 2.2

* افزونه به این زبان‌ها ترجمه شد: آراگونیایی، آلمانی، اسلوواکیایی،
  اسلوونیایی، اسپانیولی، ایتالیایی، پرتغالی برزیلی، تامیل، ترکیه‌ای، روسی،
  ژاپنی، عربی، فرانسوی، فنلاندی، کره‌ای، کرواتی، گالیسیایی، لهستانی،
  مجارستانی، نپالی و هلندی.

## تغییرات در نسخه‌ی 2.1

* Psutil dependency به نسخه‌ی 0.6.1 به‌روز شد.
* تأخیر طولانی در زمان به‌دست آوردن اطلاعات درایوها برطرف شد.
* پاکسازیِ کد.

## تغییرات در نسخه‌ی 2.0

* پشتیبانی از ترجمه و توضیحات ترجمه افزوده شد.

## تغییرات در نسخه‌ی 1.0

* انتشار اولیه

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
