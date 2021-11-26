# Kaynak izleme #

* Yazarlar: Alex Hall, Joseph Lee, beqa gozalishvili, Tuukka Ojala, Ethin
  Probst ve diğer NVDA katkıda bulunanlar
* [Kararlı sürümü][1] indir
* NVDA uyumluluğu: 2021.1 ve sonrası

Bu eklenti, CPU yükü, bellek kullanımı ve diğer kaynak kullanımları hakkında
bilgi verir.

# Kısayollar

* NVDA+Shift+E: kullanılan ram, ortalama işlemci yükü ve varsa pil
  bilgilerini sunar.
* NVDA+Shift+1: ortalama işlemci yükünü ve çok çekirdekli CPU'lar varsa her
  bir çekirdeğin yükünü gösterir.
* NVDA+Shift+2/5: hem fiziksel hem de sanal ram için kullanılan ve toplam
  alanı sunar.
* NVDA+Shift+3: statik ve çıkarılabilir sürücülerin kullanılan ve toplam
  alanını sunar.
* NVDA+Shift+4: pil yüzdesini, şarj durumunu, kalan süreyi (şarjda değilse)
  ve pil zayıf veya kritikse bir uyarı gösterir.
* NVDA+Shift+6: CPU Mimarisi 32/64-bit ve Windows sürümünü ve hizmet paketi
  numaralarını sunar.
* NVDA+Shift+7: sistemin çalışma süresini gösterir.

NVDA 2013.3 veya sonraki bir sürümünü yüklediyseniz, bu kısayol tuşlarını
girdi hareketleri iletişim kutusundan değiştirebilirsiniz.

## Kullanım notları

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka
uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* CPU kullanımı fiziksel çekirdekler için değil mantıksal işlemciler için
  verilmiştir. Bu, CPU sayısının CPU çekirdeği sayısının iki katı olduğu
  Hyper-Threading kullanan işlemciler için fark edilebilir.
* Büyük dosyaların kopyalanması gibi yoğun disk etkinliği varsa, disk
  kullanım bilgilerinin alınmasında gecikmeler olabilir.
* Bu eklenti, Windows 7 Service Pack 1 veya sonraki bir sürümünü gerektirir.

Lisansla ilgili not: bu eklenti, GNU Genel Kamu Lisansı ile uyumlu 3 Maddeli
BSD Lisansı kapsamında lisanslanan Psutil'i kullanır.

## Sürüm 21.10

* Bu eklentiyi etkileyen NVDA değişiklikleri nedeniyle NVDA 2021.1 veya üstü
  gereklidir.

## Sürüm 21.08

* Minimum Windows sürüm gereksinimi artık NVDA sürümlerine bağlıdır.
* Windows derlemeleri 20348 ve 22000, sırasıyla Windows Server 2022 ve
  Windows 11 olarak tanınır.
* Insider Preview derlemelerinde, "Windows 10" gibi Windows sürümleri
  kullanılmayacaktır. Bunun yerine NvDA "Windows Insider" duyurusunu yapar.
* 64 bit sistemlerde, işlemci mimarisi (x64 veya ARM64), Windows sürüm
  bilgilerinin bir parçası olarak duyurulacaktır.

## Sürüm 21.04

* NVDA 2020.4 veya üstü gereklidir.
* psutil bağımlılığı 5.8.0 olarak güncellendi.
* Kaynak bilgilerini panoya kopyalamak için eklenti komutlarına iki kez
  basıldığında, NVDA kopyalanmakta olan kaynak özetini söyler.

## Sürüm 21.01

* psutil bağımlılığı 5.7.3 olarak güncellendi.
* Kısaltılmış Windows sürüm mesajı.
* Windows 8.1'de build.revision, Windows 10'a benzer şekilde Windows sürüm
  mesajının bir parçası olarak duyurulacaktır.

## Sürüm 20.09

* Sistem çalışma süresi artık gün, saat, dakika, saniye olarak
  verilmektedir.
* Windows Server Insider Preview derlemesi 20201 veya üstü, bir Server
  Insider derlemesi olarak doğru şekilde tanınır.

## Sürüm 20.07

* Windows 10 Sürüm 20H2, Windows sürüm bilgisi (NVDA+Shift+6) alınırken
  düzgün şekilde tanınır.
* Basitleştirilmiş Windows 10 sürüm mesajı, yani NVDA+Shift+6 tuşlarına
  basıldığında Windows 10verYYAA yerine Windows 10 YYAA.

## Sürüm 20.06

* Flake8 ile birçok kodlama stili sorunu ve olası hatalar çözüldü.

## Sürüm 20.04

* psutil bağımlılığı 5.7.0'a güncellendi.

## Sürüm 20.01

* Python 3'ün yoğun kullanımı nedeniyle NVDA 2019.3 veya üstü gereklidir.

## Sürüm 19.11

* Özellikle 20H1 ve sonrası için Windows Insider Preview derlemelerinin
  iyileştirilmiş tespiti.

## Sürüm 19.07

* psutil bağımlılığı 5.6.3 olarak güncellendi.
* Pil durumu duyuru komutunda dahili değişiklikler.

## Sürüm 18.12

* Gelecekteki NVDA sürümlerini desteklemek için dahili değişiklikler.

## Sürüm 18.10

* Kod Python 3 ile daha uyumlu hale getirildi.
* psutil bağımlılığı 5.4.7 olarak güncellendi.
* Disk kapasitesi ve bellek kullanımı elde edilirken, NVDA, bir petabayttan
  fazla RAM veya disk boyutuna sahip bir bilgisayar veya hizmet
  kullanıldığında artık hata vermeyecektir.
* Bellek ve disk kullanımına ilişkin değerler en fazla iki ondalık basamakla
  gösterilir (ör. 4.0 GB yerine 4.00 GB).
* Windows Insider Preview derlemelerinin algılanması iyileştirildi.

## Sürüm 18.04

Sürüm 18.04.x, 7 SP1'den önceki Windows sürümlerini destekleyen son
sürümdür.

* Windows Server 2003, Vista ve Server 2008'i destekleyen son sürüm.
* Windows 10 sürümlerinin daha iyi algılanması ve genel ve Insider Preview
  derlemeleri arasında ayrım yapılması.

## Sürüm 17.12

* Windows 10'da 64 bit ARM işlemciler için destek eklendi.

## Sürüm 17.09

Önemli: Sürüm 17.09.x, Windows XP'yi destekleyen son sürümdür.

* Windows XP'de çalışacak son sürüm.
* Windows 10 build 16278 ve sonraki sürümleri Sürüm 1709 olarak
  tanınır. Sürüm 1709 kararlı yapı yayınlandığında bu eklenti için küçük bir
  revizyon yayınlanacaktır.

## Sürüm 17.07.1

* Windows XP desteğini yeniden verildi (17.02 sürümünden beri bozulmuştu).

## Sürüm 17.05

* Sistem çalışma süresinin duyurusu (son önyüklemeden bu yana geçen süre;
  NVDA+Shift+7).

## Sürüm 17.02

* psutil bağımlılığı 5.0.1'e güncellendi.
* Disk kullanımını kontrol ederken, NVDA, çıkarılabilir medyanın düzgün
  tanınmadığı bazı sistemlerde (örneğin, bir kart okuyucuya bir kart
  takılmadığında) artık bir hata iletişim kutusu göstermeyecektir.)

## Sürüm 16.08

16.08 sürümünden itibaren, eklenti sürümleri yıl.ay.revizyonu olarak
gösterilecektir.

* Windows 10'un çeşitli revizyonları artık düzgün bir şekilde tanınmaktadır
  (derleme 14393 için 1607 gibi).
* Windows 10 derleme revizyonları (kümülatif güncellemeleri yükledikten
  sonra) düzgün bir şekilde tanınır (14393.51 gibi).
* Insider Preview derlemelerini kullanıyorsanız, bu gerçek kabul edilir.

## 4.5 için değişiklikler

* Eklenti deposu GitHub'a taşındı
  (https://github.com/josephsl/resourcemonitor adresinde bulunabilir).
* Windows Server 2016 düzgün bir şekilde tanındı.

## 4.0 için değişiklikler

* psutil bağımlılığı 2.2.1'e güncellendi.
* CPU yükü hakkında bilgi alırken büyük ölçüde geliştirilmiş performans.
* Windows 10'un tanınması için destek eklendi.
* Windows 10'da Windows'un derleme numarası da duyurulacak.
* Eklenti yardımına erişmek için Eklenti Yöneticisi'ni kullanabilirsiniz.

## 3.1 için değişiklikler

* Kaynak İzleyicisi resmi olarak Windows 8.1'i destekler.
* Çeviriler güncellendi.

## 3.0 için değişiklikler

* 1.2.1 için psutil bağımlılık güncellendi.
* Mevcut Windows sürümünün, CPU mimarisinin ve varsa hizmet paketinin
  duyurusu (NVDA+Shift+6).
* Kısayol tuşları, NVDA 2013.3 sürümüyle birlikte değiştirilebilir.
* Kaynak bilgisi öğrenme komutlarına iki kez basıldığında bilgi panoya
  kopyalanıyor

## 2.4 için değişiklikler

* Yeni diller: Çince (basitleştirilmiş), Ukrayna.
* Çeviriler güncellendi.

## 2.3 için değişiklikler

* Bulgarca çeviri eklendi.

## 2.2 için değişiklikler

* Şu çeviriler eklendi: Arapça, Aragonca, Hırvatça, Felemenkçe, Fince,
  Fransızca, Galiçyaca, Almanca, Macarca, İtalyanca, Japonca, Korece,
  Nepalce, Lehçe, Portekizce (Brezilya), Rusça, Slovakça, Slovence,
  İspanyolca, Tamilce ve Türkçe.

## 2.1 için değişiklikler

* Updated psutil dependency to version 0.6.1.
* Fixed long delay when getting information of drives.
* Kod temizlendi.

## 2.0 için değişiklikler

* çeviri desteği ve açıklamalar eklendi

## 1.0 için değişiklikler

* ilk sürüm

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=rm
