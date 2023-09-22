# Kaynak izleme #

* Yazarlar: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Ethin
  Probst ve diğer NVDA katılımcıları
* [Kararlı sürümü][1] indir
* NVDA uyumluluğu: 2022.4 ve sonrası

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
* NVDA+Shift+6: CPU Mimarisini,  Windows sürümünü ve hizmet paketi
  numaralarını duyurur.
* NVDA+Shift+7: sistemin çalışma süresini gösterir.
* NVDA+Shift+8: kablosuz bağlantı, ssid adı ve gücü veya yoksa ssid olmadığı
  konusunda bilgi verir.

Girdi hareketleri iletişim kutusu aracılığıyla bu kısayol tuşlarını
değiştirebilirsiniz.

## Kullanım notları

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka
uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* Eklenti güvenli ekranlarda çalıştırılıyorsa kaynak bilgileri panoya
  kopyalanamaz.
* CPU kullanımı fiziksel çekirdekler için değil mantıksal işlemciler için
  verilmiştir. Bu, CPU sayısının CPU çekirdeği sayısının iki katı olduğu
  Hyper-Threading kullanan işlemciler için fark edilir. Bazı yeni
  bilgisayarlarda, tüm CPU çekirdeklerinde hiper iş parçacığı etkin
  olmayacaktır.
* Büyük dosyaların kopyalanması gibi yoğun disk etkinliği varsa, disk
  kullanım bilgilerinin alınmasında gecikmeler olabilir.
* İşlemci mimarisi bilgileri açıklanırken "x86" ve "AMD64" sırasıyla 32 bit
  ve 64 bit (x64) Intel ve AMD işlemcileri ifade eder.
* Bu eklenti, Windows 10 veya üst sürümlerini gerektirir.

Lisansla ilgili not: bu eklenti, GNU Genel Kamu Lisansı ile uyumlu 3 Maddeli
BSD Lisansı kapsamında lisanslanan Psutil'i kullanır.

## Sürüm 23.09

* NVDA, kablosuz özellik modülleri kullanılamadığında artık Windows Server
  sistemlerinde başlatma hata mesajlarını günlüğe kaydetmeyecektir.

## Sürüm 23.06

* Kablosuz bağdaştırıcıların bulunmaması nedeniyle Kaynak İzleyici'nin
  düzgün çalışmaması durumu düzeltildi.

## Sürüm 23.05.1

kablosuz Ağ Bilgilendirici NVDA eklentisi, artık Kaynak İzleyici'nin bir
parçası!

* Kablosuz bağlantıları kontrol etmenin eski yönteminin yerini Kablosuz Ağ
  Bilgilendirici'nin Windows API'si aldı:
  https://github.com/kvark128/WlanReporter/ .

	* SSID adını ve gücünü söyledikten sonra, NVDA şimdi size ağınızın güvenlik
	  türünü de söyleyecektir.
	* NVDA artık kablosuz bir ağa bağlandığınızda ve bağlantıyı kestiğinizde
	  sizi uyaracak.
	* NVDA artık kablosuz bağlantılar açıldığında veya kapatıldığında sizi
	  uyaracak.

## Sürüm 23.05

* bağlı kablosuz ağın durumunu tespit etme ve sunma yeteneği eklendi.

	* Bağlı kablosuz SSID'nin adını duyurur.
	* SSID'nin gücünü duyurur
	* Hiçbir SSID algılanmazsa bulunamadığı konusunda bilgi duyurur.

## Sürüm 23.02

* NVDA 2022.4 veya üstü gereklidir.
* Windows 10 21H2 (Kasım 2021 Güncellemesi/derlemesi 19044) veya üstü
  gereklidir.

## Sürüm 23.01

* NVDA 2022.3 veya üstü gereklidir.
* Ocak 2023 itibariyle Windows 7, 8 ve 8.1 artık Microsoft tarafından
  desteklenmediğinden Windows 10 veya sonraki sürümleri gereklidir.
* Psutil bağımlılığı 5.9.4'e güncellendi.
* NVDA, Windows sürüm bilgilerinin bir parçası olarak gerçek işlemci
  mimarisini (x86/AMD64/ARM64) duyurur.
* Tek çekirdekli sistemlerde, ortalama CPU yükü çekirdek yükü ile aynı
  olduğundan, NVDA artık CPU çekirdek yükünü duyurmayacaktır.

## Sürüm 22.03

Sürüm 22.03, Windows 7 Service Pack 1, 8 ve 8.1'i destekleyen son kararlı
sürümdür.

* NVDA 2021.3 veya üstü gereklidir.
* Eklentiyi Windows 7, 8 ve 8.1'e yüklemeye çalışırken bir uyarı mesajı
  görüntülenecektir.
* Psutil bağımlılığı 5.9.0'a güncellendi.

## Sürüm 22.01

* NVDA 2021.2 veya üstü gereklidir.

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
* Psutil bağımlılığı 5.8.0 olarak güncellendi.
* Kaynak bilgilerini panoya kopyalamak için eklenti komutlarına iki kez
  basıldığında, NVDA kopyalanmakta olan kaynak özetini söyler.

## Sürüm 21.01

* Psutil bağımlılığı 5.7.3 olarak güncellendi.
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

* Psutil bağımlılığı 5.7.0'a güncellendi.

## Sürüm 20.01

* Python 3'ün yoğun kullanımı nedeniyle NVDA 2019.3 veya üstü gereklidir.

## Sürüm 19.11

* Özellikle 20H1 ve sonrası için Windows Insider Preview derlemelerinin
  iyileştirilmiş tespiti.

## Sürüm 19.07

* Psutil bağımlılığı 5.6.3 olarak güncellendi.
* Pil durumu duyuru komutunda dahili değişiklikler.

## Sürüm 18.12

* Gelecekteki NVDA sürümlerini desteklemek için dahili değişiklikler.

## Sürüm 18.10

* Kod Python 3 ile daha uyumlu hale getirildi.
* Ppsutil bağımlılığı 5.4.7 olarak güncellendi.
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

* Psutil bağımlılığı 5.0.1'e güncellendi.
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

* Psutil bağımlılığı 2.2.1'e güncellendi.
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
  kopyalanıyor.

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

* çeviri desteği ve açıklamalar eklendi.

## 1.0 için değişiklikler

* İlk sürüm

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=resourceMonitor
