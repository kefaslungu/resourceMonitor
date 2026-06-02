# Kaynak İzleme

* Yazarlar: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Ethin Probst ve diğer NVDA katılımcıları

Bu eklenti, CPU yükü, bellek kullanımı ve diğer kaynak kullanımları hakkında bilgi verir.

## Kısayollar

Tüm komutlar isteğe bağlı konuşma modunu destekler.

* NVDA+Shift+E: kullanılan ram, ortalama işlemci yükü ve varsa pil bilgilerini sunar.
* NVDA+Shift+1: ortalama işlemci yükünü ve çok çekirdekli CPU'lar varsa her bir çekirdeğin yükünü gösterir.
* NVDA+Shift+2/5: hem fiziksel hem de sanal ram için kullanılan ve toplam alanı sunar.
* NVDA+Shift+3: statik ve çıkarılabilir sürücülerin kullanılan ve toplam alanını sunar.
* NVDA+Shift+4: pil yüzdesini, şarj durumunu, kalan süreyi (şarjda değilse) ve pil zayıf veya kritikse bir uyarı duyurur.
* NVDA+Shift+6: CPU Mimarisini,  Windows sürümünü ve hizmet paketi numaralarını duyurur.
* NVDA+Shift+7: sistemin çalışma süresini gösterir.
* NVDA+Shift+8: kablosuz bağlantı, ssid adı ve gücü veya yoksa ssid olmadığı konusunda bilgi verir.

Girdi hareketleri iletişim kutusu aracılığıyla bu kısayol tuşlarını değiştirebilirsiniz.

## Kullanım notları

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* Eklenti güvenli ekranlarda çalıştırılıyorsa kaynak bilgileri panoya kopyalanamaz.
* CPU kullanımı fiziksel çekirdekler için değil mantıksal işlemciler için verilmiştir. Bu, CPU sayısının CPU çekirdeği sayısının iki katı olduğu Hyper-Threading kullanan işlemciler için fark edilir. Bazı yeni bilgisayarlarda, tüm CPU çekirdeklerinde hiper iş parçacığı etkin olmayacaktır.
* Büyük dosyaların kopyalanması gibi yoğun disk etkinliği varsa, disk kullanım bilgilerinin alınmasında gecikmeler olabilir.
* İşlemci mimarisi bilgileri açıklanırken "x86" ve "AMD64" sırasıyla 32 bit ve 64 bit (x64) Intel ve AMD işlemcileri ifade eder.
* Bu eklenti Windows 8.1'i (sınırlı destek) desteklese de, Windows 10 22H2 (2022 Güncellemesi/derleme 19045) veya üstü önerilir.
* Eklentinin Windows 10/11 LTSC'ye yüklenmesi desteklenmemektedir.
