# श्रोत अनुगामी (resourceMonitor)

* Authors: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala and other NVDA contributors

This add-on gives information about CPU load, memory usage and other resource usage information.

## द्रुतमार्ग

* NVDA+Shift+E Presents used ram, average processor load, and battery info if available.
* नेत्रवानी +Shift+१ ले प्रोसेसरको औसत भार र यदी बहुकोर CPU's भएमा यि कोरहरुको भार समेत प्रस्तुत गर्ने छ ।
* NVDA+Shift+2/5 Presents the used and total space for both physical and virtual ram.
* NVDA+Shift+3 Presents the used and total space of the static and removable drives.
* NVDA+Shift+4 Presents battery percentage, charging status, remaining time (if not charging), and a warning if the battery is low or critical.
* नेत्रवाणी+Shift+6 चालु विन्डोजको संस्करण, CPU बीट (३२ वा ६४-विट) र सर्भिस प्याक  सङ्ख्या बताउने छ ।
* NVDA+Shift+7 presents the system's uptime.

यदि चालू नेत्रवाणी २०१३.३ अथवा यस पछीको संस्करण छ भने तपाइले यी द्रुतमार्ग कुञ्जी बदल्न सक्नु हुन्छ ।

## टिप्पणिको प्रयोग

यो उप-कर्मीले कार्य व्यबस्थापक र अरू विन्डोज सम्बन्धी सूचना कार्यक्रम प्रणालीलाई   विस्थापन गर्दैन । यो पनि ध्यान दिनु होला:

* CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores.
* If there is heavy disk activity such as copying large files, there might be delays when obtaining disk usage information.
* Support for Windows XP from this add-on ended on December 31, 2017. Support for Windows Server 2003, Vista and Server 2008 ended on June 30, 2018.
