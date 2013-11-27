# श्रोत अनुगामी (resourceMonitor) #

* लेखकहरु: अलेक्स हल, जोसेफ लि, बिका गोजालिस्भीलि र अन्य नेत्रवाणी योगदान
  कर्ताहरू ।
* स्थिर संस्करण: [version 2.4][1]
* Development version: [version 3.0-dev][2]

यो चुकुलले हामीलाई CPU को भारको बारेमा, प्रयोगमा आएको भण्डार, ब्याट्री तथा
भकारिको प्रयोग भएको अवस्था बताउने छ ।

# द्रुतमार्ग #

* नेत्रवाणी+Shift+E ले प्रयोग भएको र्‍याम, औसत प्रोसेसर भार, र ब्याट्री
  सम्बन्धि जानकारी बताउनेछ ।
* नेत्रवाणी+Shift+1 ले औसत प्रोसेसरको भार र हरेक कोरको भार बताउने छ ।
* नेत्रवाणी+Shift+2/५ ले भोतिक र अवास्तविक र्‍यामको प्रयोग भएको र जम्मा
  क्षमता बताउने छ ।
* नेत्रवाणी+Shift+3 ले यो कल्पयन्त्र्मा भएका स्थिर र हटाउन मिल्ने भकारीहरूको
  प्रयोग भएको र जम्मा क्षमता बताउने छ । 
* नेत्रवाणी +Shift+4 ले ब्याट्री प्रतिशत, चार्जको अवस्था, बाकि समय (चार्ज भई
  रहेको छैन भने) र ब्रयाट्री कम वा नाजुक छ भने सो को चेतावणी समेत बताउने छ ।
* NVDA+Shift+6 Presents currently installed Windows version, CPU bit (32 or
  64-bit) and service pack if any (version 3.0-dev).

## Usage notes ##

This add-on does not replace task manager and other system information
programs for Windows. Also note the following:

* CPU usage is given for logical processors, not physical cores. This is
  noticeable for processors which uses Hyper Threading where number of CPU's
  is twice the number of CPU cores.
* There might be a short delay when getting processor usage information.

## विकास-३.० मा गरिएका परिवर्तनहरु ##

* Updated psutil dependency to 1.2.1.
* Added a command (NVDA+Shift+6) to report the version of Windows you are
  using, CPU bit and service packs if any.
* Ability to change add-on shortcut keys (NVDA 2013.3 or later).
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## २.४ मा गरिएका परिवर्तनहरू ##

* नयाँ भाषाहरू: सरलीकृत चिनिया, युक्रेनी
* अनुवादलाई अद्यावधिक गरियो 

## २.३ मा गरिएका परिवर्तनहरू ##

* बुल्गेरियाली अनुवाद थपियो ।

## २.१ संस्करणमा गरिएका परिवर्तनहरू । ##

* निम्न भाषाहरूमा अनुवाद गरियो: अरबी, अर्गानिज, क्रोएसीयाली, डच, फिनिस,
  फ्रान्सेली, ग्यालेसियन, जर्मनी, हङ्गेरियाली, इटालियन, कोरियाली, नेपाली,
  पुर्तगाली(ब्राजिल), रुसी, स्लोभाक, स्लोभिनियन, स्पेनी, तामिल र तुर्कि ।

## २.१ संस्करणमा गरिएका परिवर्तनहरू । ##

* psutil आधारितलाई ०.६.१ मा अद्यावधिक गरियो ।.
* भकारि सम्बन्धी जानकारी लिदा लामो समय लाग्ने समस्या हल गरियो ।
* %s लाई {friendlyVariableNames} मा प्रतिस्थापन गर ।
* एउटा संहिता साफ करता

## २.० संस्करणमा गरिएका परिवर्तनहरू । ##

* अनुवाद टिप्पणी र अनुवाद सहयोग थप गरियो ।.

## १.० संस्करणमा गरिएका परिवर्तनहरू । ##

* पहिलो सार्वजनिकीकरण

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
