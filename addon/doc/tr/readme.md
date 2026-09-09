# Kaynak İzleme

* Yazarlar: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Ethin Probst, Kevin Derome ve NVDA'ya katkıda bulunan diğer kişiler

Bu eklenti, CPU yükü, bellek kullanımı ve diğer kaynak kullanımları hakkında bilgi verir.

## Kısayollar

Tüm komutlar isteğe bağlı konuşma modunu destekler.

* NVDA+Shift+E: Kaynak İzleme komut katmanına girer.

Aşağıdaki katman komutları, bireysel kaynak kullanım bilgilerini elde etmek için kullanılabilir:

* Aralık: Kullanılan RAM (fiziksel bellek) ve ortalama işlemci yükü de dahil olmak üzere genel kaynak kullanım bilgileri.
* C: CPU (ortalama işlemci yükü ve çok çekirdekli CPU'lar varsa her bir çekirdeğin yükü)
* D: diskler (sabit (dahili), çıkarılabilir ve ağ sürücülerinin kullanılan ve toplam alanı)
* G (güvenli modda kullanılamaz): grafik işlem birimi (GPU) bilgileri
* Shift+G (güvenli modda kullanılamaz): GPU bellek kullanımı
* M: Bellek (hem fiziksel hem de sanal RAM için kullanılan ve toplam alan (NVDA+Shift+2 tuş kombinasyonu kullanılamadığında NVDA+Shift+5 alternatifi kullanılabilir))
* O: işletim sistemi (Windows sürümü, CPU mimarisi ve tam derleme numarası (build.revision))
* U: sistem çalışma süresi
* W: Wi-Fi (ağ adı (SSID), sinyal gücü, güvenlik modu veya mevcut değilse SSID yok)

Kaynak komutları, katmanı aktif tutar; böylece bu komutlar tekrar edilebilir. Katmandan çıkmak için Escape tuşuna basın; atanmamış bir tuş, aktif uygulamadan geçirilerek çıkışı sağlar.

Sınırlı geriye dönük uyumluluk amacıyla, önceki NVDA+Shift+1 ile NVDA+Shift+7 arasındaki kaynak kısayolları hâlâ kullanılabilir durumdadır:

* NVDA+Shift+1: CPU
* NVDA+Shift+2/5: bellek
* NVDA+Shift+3: diskler
* NVDA+Shift+4: wi-fi
* NVDA+Shift+6: işletim sistemi
* NVDA+Shift+7: sistem çalışma süresi

Bu hareketleri girdi hareketleri iletişim kutusu aracılığıyla değiştirebilirsiniz.

## Kullanım notları

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* Kaynak komutlarına iki kez basmak, kaynak kullanım bilgilerini panoya kopyalayacaktır.
* Eklenti güvenli ekranlarda çalıştırılıyorsa kaynak bilgileri panoya kopyalanamaz.
* CPU kullanımı, fiziksel çekirdekler için değil, mantıksal işlemciler için verilmektedir. Bu durum, CPU sayısının CPU çekirdek sayısının iki katı olduğu Hyper-Threading özelliğine sahip işlemcilerde fark edilir. Bazı yeni bilgisayarlarda, tüm CPU çekirdeklerinde Hyper-Threading etkinleştirilmemiş olabilir.
* Büyük dosyaların kopyalanması veya ağ sürücülerinin bulunması gibi yoğun disk etkinliği söz konusu olduğunda, disk kullanım bilgilerinin alınmasında gecikmeler yaşanabilir.
* Nvidia GPU'larına ait GPU bilgileri verilmiştir.
* Windows sürüm raporlamasında işlemci mimarisi bilgisi açıklanırken, "AMD64" 64-bit (x64) Intel ve AMD işlemcilerini ifade eder. Bu bilgi, kullanılan gerçek işlemcinin adını ifade etmez.
* Eklentinin Windows 10/11 LTSC'ye yüklenmesi desteklenmemektedir.

Her eklenti sürümü arasında yapılan değişikliklerin listesi için [eklenti sürümleri için changelogs][1] belgesine bakın.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
