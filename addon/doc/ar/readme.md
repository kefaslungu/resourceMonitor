# Resource Monitor #

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala and other
  NVDA contributors
* تحميل [الإصدار النهائي][1]

This add-on gives information about CPU load, memory usage and other
resource usage information.

# مفاتيح الاختصار #

* NVDA+Shift+E يعطي معلومات عن الذاكرة العشوائية المستخدمة, متوسط حمولة
  المعالج, ومعلومات عن حالة البطارية إذا كان الجهاز به بطارية,
* NVDA+Shift+1 يعطي معلومات عن متوسط حمولة المعالج وعن حمولة كل نواة,
* NVDA+Shift+2/5 يعطي معلومات عن المساحة المستخدمة والمساحة الكلية لكل من
  الذاكرة الفعلية والذاكرة العشوائية,
* NVDA+Shift+3 يعطي معلومات عن المساحة المستخدمة والمساحة الكلية للأقراص
  الثابتة والأقراص التي يمكن إزالتها بالحاسوب,
* NVDA+Shift+4 يعطي معلومات عن نسبة شحن البطارية, وحالة الشحن, والوقت
  المتبقي (إذا لم يتم شحنها), ورسالة تحذير إذا كانت البطارية منخفضة أو أوشك
  الشحن على النفاذ.
* NVDA+Shift+6 يعلمك بإصدار الويندوز المستخدم حاليا وهندسة وحدة المعالجة
  المركزية 32 أو 64-bit  ورقم الحزمة.
* NVDA+Shift+7 presents the system's uptime.

إذا كان مثبت على حاسوبك الإصدار 2013.3 أو ما بعده, يمكنك تغيير الاختصارات
الخاصة بالإضافة.

## ملاحظات الاستخدام ##

لا تحل هذه الإضافة محل خدمة مدير المهام بويندوز أو أية برامج أخرى تخبر
المستخدم بمعلومات النظام. كما ينبغي عليك ملاحظة الآتي:

* يتم الإعلان عن معدل الاستخدام لوحدات المعالجة المركزية للمعالجات المنطقية
  وليست للنوى المادية. ويلاحظ هذا بشكل واضح للمعالجات التي تستخدم الخيط
  التشاعبي (Hyper Threading) والتي فيها يكون رقم وحدة المعالجة المركزية هو
  ضعف رقم نوى وحدة المعالجة المركزية. 
* If there is heavy disk activity such as copying large files, there might
  be delays when obtaining disk usage information.
* Support for Windows XP from this add-on ended on December 31,
  2017. Support for Windows Server 2003, Vista and Server 2008 ended on June
  30, 2018.

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

## مستجدات الإصدار 4.0 ##

* تحديث توابع psutil حتى الإصدار 2.2.1.
* تحسين الأداء بشكل كبير عند الحصول على معلومات عن تحميل المعالج.
* إضافة دعم للتعرف على ويندوز 10
* سيتم الإعلان عن رقم بناء الويندوز أيضا في ويندوز 10
* يمكنك استخدام مدير الإضافات البرمجية للوصول لملف المساعدة.

## مستجدات الإصدار 3.1 ##

* تدعم الإضافة نظام التشغيل ويندوز 8.1 رسميا.
* تحديث ترجمة الإضافة

## مستجدات الإصدار 3.0 ##

* تحديث توابع psutil حتى الإصدار 1.2.1.
* للاستعلام عن إصدار الويندوز المستخدم حاليا وهندسة وحدة المعالجة المركزية
  وإصدار الحزمة إن وجد (NVDA+Shift+6).
* إمكانية تغيير اختصارات الإضافة (NVDA2013.3 وما بعده).
* إمكانية نسخ معلومة النظام بالضغط على الأمر المنوط بالإخبار عنها مرتين
  متعاقبتين.

## مستجدات الإصدار 2.4 ##

* ترجمة الإضافة إلى: الصينية (المبسطة) والأوكرانية.
* تحديث ترجمة الإضافة

## مستجدات الإصدار 2.3 ##

* ترجمة الإضافة للغة البلغارية.

## مستجدات الإصدار 2.2 ##

* ترجمة الإضافة إلى اللغات: العربية, والأرجانيزية, والكرواتية, والهولندية,
  والفنلندية, والفرنسية, والغالية, والألمانية, والمجرية, والإيطالية,
  واليابانية, والكورية, والنيبالية, والبولندية, والبرتغالية (برازيلي),
  والروسية, والسلوفاكية, والسلوفينية, والإسبانية, وتامل والتركية.

## مستجدات الإصدار 2.1 ##

* تحديث psutil dependency للإصدار 0.6.1.
* معالجة التأخر الذي يحدث عند استحضار معلومات عن الأقراص.
* قليل من الترتيب لكود الإضافة.

## مستجدات الإصدار 2.0 ##

* إضافة إمكانية ترجمة الإضافة مع وضع تعليقات عن كل رسالة

## مستجدات الإصدار 1.0 ##

* إصدار أولي

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
