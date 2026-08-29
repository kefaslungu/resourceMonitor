# Kaynak İzleme

* Yazarlar: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Ethin Probst, Kevin Derome ve NVDA'ya katkıda bulunan diğer kişiler

Bu eklenti, CPU yükü, bellek kullanımı ve diğer kaynak kullanımları hakkında bilgi verir.

## Kısayollar

Tüm komutlar isteğe bağlı konuşma modunu destekler.

* NVDA+Shift+E: Kullanılan RAM (fiziksel bellek) ve ortalama işlemci yükünü seslendirir.
* NVDA+Shift+1: ortalama işlemci yükünü ve çok çekirdekli CPU'lar varsa her bir çekirdeğin yükünü gösterir.
* NVDA+Shift+2/5: hem fiziksel hem de sanal ram için kullanılan ve toplam alanı sunar.
* NVDA+Shift+3: Sabit (dahili), çıkarılabilir ve ağ sürücülerinin kullanılan ve toplam alanını seslendirir.
* NVDA+Shift+4: pil yüzdesini, şarj durumunu, kalan süreyi (şarjda değilse) ve pil zayıf veya kritikse bir uyarı duyurur.
* NVDA+Shift+6: presents  Windows version, CPU architecture (AMD64 (x64), ARM64), and exact build number (build.revision).
* NVDA+Shift+7: sistemin çalışma süresini gösterir.
* Atanmamış: grafik işlem birimi (GPU; güvenli modda kullanılamaz) hakkındaki bilgileri sunar.
* Atanmamış: Grafik işlem birimini (GPU bellek kullanım bilgilerini) seslendirir (güvenli modda kullanılamaz).

Girdi hareketleri iletişim kutusu aracılığıyla bu kısayol tuşlarını değiştirebilirsiniz.

## Kullanım notları

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* Genel kaynak kullanım komutunun (NVDA+Shift+E) dışında, diğer komutlara iki kez basıldığında kaynak kullanım bilgileri panoya kopyalanır.
* Eklenti güvenli ekranlarda çalıştırılıyorsa kaynak bilgileri panoya kopyalanamaz.
* CPU kullanımı, fiziksel çekirdekler için değil, mantıksal işlemciler için verilmektedir. Bu durum, CPU sayısının CPU çekirdek sayısının iki katı olduğu Hyper-Threading özelliğine sahip işlemcilerde fark edilir. Bazı yeni bilgisayarlarda, tüm CPU çekirdeklerinde Hyper-Threading etkinleştirilmemiş olabilir.
* Büyük dosyaların kopyalanması veya ağ sürücülerinin bulunması gibi yoğun disk etkinliği söz konusu olduğunda, disk kullanım bilgilerinin alınmasında gecikmeler yaşanabilir.
* Nvidia GPU'larına ait GPU bilgileri verilmiştir.
* When announcing processor architecture information as part of Windows version reporting, "AMD64" refer to 64-bit (x64) Intel and AMD processors. This information does not refer to the name of the actual processor in use.
* Eklentinin Windows 10/11 LTSC'ye yüklenmesi desteklenmemektedir.

Her eklenti sürümü arasında yapılan değişikliklerin listesi için [eklenti sürümleri için changelogs][1] belgesine bakın.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
