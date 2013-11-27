# resource Monitor #

* Geliştiriciler: Alex Hall, Joseph Lee, beqa gozalishvili and other NVDA
  contributors
* Kararlı sürüm: [version 2.4][1]
* Geliştirme sürümü: [version 3.0-dev][2]

Bu eklenti, işlemci yükü, kullanılan ram, harddiskte kullanılan alanı ve pil
bilgisini verir.

# Kısayollar #

* NVDA+Shift+E kullanılan ram, ortalama işlemci yükü, ve mevcutsa batarya
  bilgisini  seslendirir.
* NVDA+Shift+1 ortalama işlemci yükünü söyler ve bu bilgiyi her bir çekirdek
  için sunar
* NVDA+Shift+2/5 Fiziksel ve sanal ram için toplam ram ve kullanılan ram
  miktarını söyler,
* NVDA+Shift+3 bilgisayara bağlı sabit ve çıkarılabilir diskler için toplam
  alan ve kullanılan alan bilgisini seslendirir
* NVDA+Shift+4 batarya yüzdesini, şarj durumunu, kalan zamanı  (eğer şarj
  edilmiyorsa), batarya düşük ya da kritik seviyede uyarısını seslendirir,
* NVDA+Shift+6 mevcut windows sürümünü, varsa service pack versiyonunu ve 32
  ya da 64 bit olup olmadığını söyler (version 3.0-dev).

## Kullanım notları ##

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka
uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* CPU kullanımı fiziksel çekirdekler için değil mantıksal (logical)
  işlemciler için verilir. Bu CPU sayısı CPU çekirdeklerinin iki katı olan
  Hyper Threading kullanan işlemciler için belirgindir.
* There might be a short delay when getting processor usage information.

## 3.0-dev için değişiklikler ##

* Updated psutil dependency to 1.2.1.
* Windows sürümünü ve hizmet paketleri varsa, bildirim için bir komut (NVDA
  + Shift +6) eklendi.
* Kısayol tuşları, NVDA 2013.3 sürümüyle birlikte değiştirilebilir.
* Ability to copy individual resource information to clipboard by pressing
  resource commands two times.

## 2.4 için değişiklikler ##

* Yeni diller: Çince (basitleştirilmiş), Ukrayna.
* Çeviriler güncellendi.

## 2.3 için değişiklikler ##

* Bulgarca çeviri eklendi.

## 2.2 için değişiklikler ##

* Aşağıdaki çeviriler eklendi: Arabic, Aragonese, Croatian, Dutch, Finnish,
  French, Galatian, German, Hungarian, Italian, Japanese, Korean, Nepali,
  Polish, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil
  and Turkish.

## 2.1 için değişiklikler ##

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Replaced %s-es into {friendlyVariableNames}.
* kod temizliği

## 2.0 için değişiklikler ##

* çeviri desteği ve açıklamalar eklendi

## 1.0 için değişiklikler ##

* ilk sürüm

[[!tag stable dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=rm

[2]: http://addons.nvda-project.org/files/get.php?file=rm-dev
