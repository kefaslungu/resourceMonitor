# श्रोत अनुगामी (resourceMonitor) #

* लेखकहरु: अलेक्स हल, जोसेफ लि, बिका गोजालिस्भीलि र अन्य नेत्रवाणी योगदान
  कर्ताहरू ।
* Download [stable version][1]

This plugin gives information about CPU load, memory usage and other
resource usage information.

महत्त्वपूर्ण: श्रोत अनुगामी ३.१ नेत्रवाणी २०१३.३ अघिका संस्करणमा चल्दैन ।
यदी तपाइ यस्ता संस्करण चलाउनु हुन्छ भने श्रोत अनुगामी ३.० चलाउनु होला ।

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

यदि चालू नेत्रवाणी २०१३.३ अथवा यस पछीको संस्करण छ भने तपाइले यी द्रुतमार्ग
कुञ्जी बदल्न सक्नु हुन्छ ।

## टिप्पणिको प्रयोग ##

यो उप-कर्मीले कार्य व्यबस्थापक र अरू विन्डोज सम्बन्धी सूचना कार्यक्रम
प्रणालीलाई   विस्थापन गर्दैन । यो पनि ध्यान दिनु होला:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper-Threading where number of CPU's
  is twice the number of CPU cores.
* प्रोसेसरको प्रयोग सम्बन्धी जानकारी दिदा केही ढिलो हुन सक्छ ।

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

[1]: http://addons.nvda-project.org/files/get.php?file=rm [2]:
http://addons.nvda-project.org/files/get.php?file=rm-next
