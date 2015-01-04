# Kaynak izleme #

* Geliştiriciler: Alex Hall, Joseph Lee, beqa gozalishvili and other NVDA
  contributors
* Download [stable version][1]
* Download [development version][2]

This plugin gives information about CPU load, memory usage and other
resource usage information.

Important: Resource Monitor 3.1 is not compatible with NvDA 2013.3 or
earlier. If you use 2013.3 or earlier, please use Resource Monitor 3.0.

# Kısayollar #

* NVDA+Shift+E Presents used ram, average processor load, and battery info
  if available.
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

If you have NvDA 2013.3 or later installed, you can change these shortcut
keys.

## Kullanım notları ##

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka
uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* CPU kullanımı fiziksel çekirdekler için değil mantıksal (logical)
  işlemciler için verilir. Bu CPU sayısı CPU çekirdeklerinin iki katı olan
  Hyper Threading kullanan işlemciler için belirgindir.
* Işlemci kullanım bilgilerini alırken kısa bir gecikme olabilir.

## Changes for 3.1 ##

* Resource Monitor officially supports Windows 8.1.
* Çeviriler güncellendi.

## 3.0 için değişiklikler ##

* 1.2.1 için psutil bağımlılık güncellendi.
* Announcement of current Windows version, CPU architecture and service pack
  if any (NVDA+Shift+6).
* Kısayol tuşları, NVDA 2013.3 sürümüyle birlikte değiştirilebilir.
* Kaynak bilgisi öğrenme komutlarına iki kez basıldığında bilgi panoya
  kopyalanıyor

## 2.4 için değişiklikler ##

* Yeni diller: Çince (basitleştirilmiş), Ukrayna.
* Çeviriler güncellendi.

## 2.3 için değişiklikler ##

* Bulgarca çeviri eklendi.

## 2.2 için değişiklikler ##

* Added following translations: Arabic, Aragonese, Croatian, Dutch, Finnish,
  French, Galician, German, Hungarian, Italian, Japanese, Korean, Nepali,
  Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil
  and Turkish.

## 2.1 için değişiklikler ##

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Replaced %s-es into {friendlyVariableNames}.
* Code cleanup.

## 2.0 için değişiklikler ##

* çeviri desteği ve açıklamalar eklendi

## 1.0 için değişiklikler ##

* ilk sürüm

[[!tag stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
