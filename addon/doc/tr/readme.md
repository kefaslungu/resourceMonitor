# Kaynak İzleme

* Yazarlar: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Ethin Probst, Kevin Derome ve NVDA'ya katkıda bulunan diğer kişiler

Bu eklenti, CPU yükü, bellek kullanımı ve diğer kaynak kullanımları hakkında bilgi verir.

## Kısayollar

Tüm komutlar isteğe bağlı konuşma modunu destekler.

* NVDA+Shift+E: kullanılan ram, ortalama işlemci yükü ve varsa pil bilgilerini sunar.
* NVDA+Shift+1: ortalama işlemci yükünü ve çok çekirdekli CPU'lar varsa her bir çekirdeğin yükünü gösterir.
* NVDA+Shift+2/5: hem fiziksel hem de sanal ram için kullanılan ve toplam alanı sunar.
* NVDA+Shift+3: presents the used and total space of the fixed (built-in), removable, and network drives.
* NVDA+Shift+4: pil yüzdesini, şarj durumunu, kalan süreyi (şarjda değilse) ve pil zayıf veya kritikse bir uyarı duyurur.
* NVDA+Shift+6: CPU Mimarisini,  Windows sürümünü ve hizmet paketi numaralarını duyurur.
* NVDA+Shift+7: sistemin çalışma süresini gösterir.
* Atanmamış: grafik işlem birimi (GPU; güvenli modda kullanılamaz) hakkındaki bilgileri sunar.
* Unassigned: presents graphics processing unit (GPU memory usage information; unavailable in secure mode).

Girdi hareketleri iletişim kutusu aracılığıyla bu kısayol tuşlarını değiştirebilirsiniz.

## Kullanım notları

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* Genel kaynak kullanım komutunun (NVDA+Shift+E) dışında, diğer komutlara iki kez basıldığında kaynak kullanım bilgileri panoya kopyalanır.
* Eklenti güvenli ekranlarda çalıştırılıyorsa kaynak bilgileri panoya kopyalanamaz.
* CPU kullanımı fiziksel çekirdekler için değil mantıksal işlemciler için verilmiştir. Bu, CPU sayısının CPU çekirdeği sayısının iki katı olduğu Hyper-Threading kullanan işlemciler için fark edilir. Bazı yeni bilgisayarlarda, tüm CPU çekirdeklerinde hiper iş parçacığı etkin olmayacaktır.
* If there is heavy disk activity such as copying large files or while locating network drives, there might be delays when obtaining disk usage information.
* GPU information is given for Nvidia GPU's.
* İşlemci mimarisi bilgileri açıklanırken "x86" ve "AMD64" sırasıyla 32 bit ve 64 bit (x64) Intel ve AMD işlemcileri ifade eder.
* Eklentinin Windows 10/11 LTSC'ye yüklenmesi desteklenmemektedir.

Her eklenti sürümü arasında yapılan değişikliklerin listesi için [eklenti sürümleri için changelogs][1] belgesine bakın.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
