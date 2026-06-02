# Resource Monitor

* Authors: Alex Hall, Joseph Lee, Kefas Lungu, beqa gozalishvili, Tuukka Ojala, Ethin Probst and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## مفاتيح الاختصار

* NVDA+Shift+E يعطي معلومات عن الذاكرة العشوائية المستخدمة, متوسط حمولة المعالج, ومعلومات عن حالة البطارية إذا كان الجهاز به بطارية,
* NVDA+Shift+1 يعطي معلومات عن متوسط حمولة المعالج وعن حمولة كل نواة,
* NVDA+Shift+2/5 يعطي معلومات عن المساحة المستخدمة والمساحة الكلية لكل من الذاكرة الفعلية والذاكرة العشوائية,
* NVDA+Shift+3 يعطي معلومات عن المساحة المستخدمة والمساحة الكلية للأقراص الثابتة والأقراص التي يمكن إزالتها بالحاسوب,
* NVDA+Shift+4 يعطي معلومات عن نسبة شحن البطارية, وحالة الشحن, والوقت المتبقي (إذا لم يتم شحنها), ورسالة تحذير إذا كانت البطارية منخفضة أو أوشك الشحن على النفاذ.
* NVDA+Shift+6 يعلمك بإصدار الويندوز المستخدم حاليا وهندسة وحدة المعالجة المركزية 32 أو 64-bit  ورقم الحزمة.
* NVDA+Shift+7 presents the system's uptime.

If you have NVDA 2013.3 or later installed, you can change these shortcut keys via input gestures dialog.

## ملاحظات الاستخدام

لا تحل هذه الإضافة محل خدمة مدير المهام بويندوز أو أية برامج أخرى تخبر المستخدم بمعلومات النظام. كما ينبغي عليك ملاحظة الآتي:

* يتم الإعلان عن معدل الاستخدام لوحدات المعالجة المركزية للمعالجات المنطقية وليست للنوى المادية. ويلاحظ هذا بشكل واضح للمعالجات التي تستخدم الخيط التشاعبي (Hyper Threading) والتي فيها يكون رقم وحدة المعالجة المركزية هو ضعف رقم نوى وحدة المعالجة المركزية. 
* If there is heavy disk activity such as copying large files, there might be delays when obtaining disk usage information.
* This add-on requires Windows 7 Service Pack 1 or later.
