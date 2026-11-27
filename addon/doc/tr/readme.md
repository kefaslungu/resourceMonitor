# Kaynak İzleme

* Yazarlar: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Ethin Probst, Kevin Derome ve NVDA'ya katkıda bulunan diğer kişiler

Bu eklenti, CPU yükü, bellek kullanımı ve diğer kaynak kullanımları hakkında bilgi verir.

## Kısayollar

Tüm komutlar isteğe bağlı konuşma modunu destekler.

* NVDA+Shift+E: enters the Resource Monitor command layer. There are two modes:
	* Lock: pressing the layer entry command once will keep the layer mode active until the Escape key or a key not defined in the layer mode (see below) is pressed. Keys not defined in the layer mode will be passed to the application.
	* Report: performing a resource usage info command will announce the information and exit the layer mode. Press the layer entry command repeatedly to lock the layer mode.

Aşağıdaki katman komutları, bireysel kaynak kullanım bilgilerini elde etmek için kullanılabilir:

* Aralık: Kullanılan RAM (fiziksel bellek) ve ortalama işlemci yükü de dahil olmak üzere genel kaynak kullanım bilgileri.
* C: CPU (ortalama işlemci yükü ve çok çekirdekli CPU'lar varsa her bir çekirdeğin yükü)
* D: diskler (sabit (dahili), çıkarılabilir ve ağ sürücülerinin kullanılan ve toplam alanı)
* G (güvenli modda kullanılamaz): grafik işlem birimi (GPU) bilgileri
* Shift+G (güvenli modda kullanılamaz): GPU bellek kullanımı
* M: Bellek (hem fiziksel hem de sanal RAM için kullanılan ve toplam alan)
* O: işletim sistemi (Windows sürümü, CPU mimarisi ve tam derleme numarası (build.revision))
* U: sistem çalışma süresi
* W: Wi-Fi (ağ adı (SSID), sinyal gücü, güvenlik modu veya mevcut değilse SSID yok)

You can also assign shortcuts to announce individual resource information without entering the layer first (go to NvDA menu/Preferences/Input gestures to assign custom commands).

## Kullanım notları

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* Pressing resource commands twice or Control+NVDA+X will copy resource usage information to the clipboard (pressing Control+NVDA+X copies the last spoken resource information).
* Eklenti güvenli ekranlarda çalıştırılıyorsa kaynak bilgileri panoya kopyalanamaz.
* CPU kullanımı, fiziksel çekirdekler için değil, mantıksal işlemciler için verilmektedir. Bu durum, CPU sayısının CPU çekirdek sayısının iki katı olduğu Hyper-Threading özelliğine sahip işlemcilerde fark edilir. Bazı yeni bilgisayarlarda, tüm CPU çekirdeklerinde Hyper-Threading etkinleştirilmemiş olabilir.
* Büyük dosyaların kopyalanması veya ağ sürücülerinin bulunması gibi yoğun disk etkinliği söz konusu olduğunda, disk kullanım bilgilerinin alınmasında gecikmeler yaşanabilir.
* NVDA, kablosuz ağlara bağlanırken veya bağlantıyı keserken bir ses çıkaracak ve bir mesaj bildirecektir. Bu davranışı nasıl değiştireceğinizi bir sonraki bölümde görebilirsiniz.
* Nvidia GPU'larına ait GPU bilgileri verilmiştir.
* Windows sürüm raporlamasında işlemci mimarisi bilgisi açıklanırken, "AMD64" 64-bit (x64) Intel ve AMD işlemcilerini ifade eder. Bu bilgi, kullanılan gerçek işlemcinin adını ifade etmez.
* Eklentinin Windows 10/11 LTSC'ye yüklenmesi desteklenmemektedir.

## Ayarlar

You can configure the following settings from NVDA settings screen under Resource Monitor category:

* Enter resource monitor layer when layer command is performed: select between once (default, lock the layer mode) or repeatedly (pressing once will anounce resource info once, press repeatedly to lock the layer mode).
* GPU sıcaklık birimi: GPU bilgileri kapsamında bildirilen sıcaklık birimini seçin (Santigrat veya Fahrenheit).
* Wi-Fi bağlanma/kesilme bildirimi: NVDA'nın Wi-Fi bağlantı/kesme bildirimlerini nasıl bildirmesi gerektiğini seçin (kapalı, mesaj, ses, hem mesaj hem ses).
* Bellek ve disk boyutu gösterimi: RAM ve disk kullanım birimleri (gigabayt ve terabayt gibi) için bellek boyutlarının nasıl seslendirileceğini seçin (varsayılan olarak alternatif yöntem (KB/MB/...) kullanılır).

Her eklenti sürümü arasında yapılan değişikliklerin listesi için [eklenti sürümleri için changelogs][1] belgesine bakın.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
