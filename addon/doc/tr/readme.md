# Kaynak İzleme

* Yazarlar: Alex Hall, Joseph Lee, Kefas Lungu, Beqa Gozalishvili, Ethin Probst, Kevin Derome ve NVDA'ya katkıda bulunan diğer kişiler

Bu eklenti, CPU yükü, bellek kullanımı ve diğer kaynak kullanımları hakkında bilgi verir.

## Komutlar ve Girdi Hareketleri

Tüm komutlar isteğe bağlı konuşma modunu destekler.

Bu sürümde varsayılan kısayol veya sabit tuşlu komut katmanı bulunmaz.
NVDA menüsü > Tercihler > Girdi Hareketleri > Kaynak İzleme bölümünü açın,
istediğiniz komutu seçip kendi tuşunuzu ekleyin. Kaynak komutlarına daha önce
Girdi Hareketleri üzerinden kaydettiğiniz kullanıcı atamaları korunur.

Kullanılabilir komutlar:

* Genel kaynak kullanımı: RAM kullanım yüzdesi ve ortalama CPU yükü.
* İşlemci bilgileri: ortalama CPU kullanım yüzdesi ve mantıksal işlemcilerin yükü.
* İşlemci kullanımı ve sıcaklığı: ortalama CPU kullanım yüzdesi ve CPU paket sıcaklığı (güvenli modda kullanılamaz).
* Bellek: fiziksel ve sanal RAM'in kullanılan ve toplam miktarı.
* Diskler: sabit, çıkarılabilir ve ağ sürücülerinin kullanılan ve toplam alanı.
* GPU bilgileri: kullanım yüzdesi ve sıcaklık (güvenli modda kullanılamaz).
* GPU belleği: kullanılan ve toplam GPU belleği (güvenli modda kullanılamaz).
* Wi-Fi: ağ adı, sinyal gücü ve güvenlik türü.
* İşletim sistemi: Windows sürümü, mimari ve derleme numarası.
* Sistemin açık kalma süresi.

Bu iki işlemci komutundan istediğiniz birine veya ikisine ayrı tuş atayabilirsiniz.
Eski işlemci bilgileri komutu sıcaklık sorgulamaz ve sensör okuyucusunu başlatmaz.
Yeni kullanım ve sıcaklık komutunun ilk sorgusunda paketle gelen sensör okuyucusu için Windows yönetici
onayı istenir. NVDA normal yetkileriyle çalışır. Sıcaklık için çalışan bir PawnIO
sürücüsü gerekir; eksik veya geçersiz değerler sıcaklık olarak bildirilmez.

## Kullanım notları

Bu eklenti görev yöneticisi ya da sistem bilgisiyle ilgili başka uygulamaların yerine geçmez. Yanısıra, aşağıdakileri de not edin:

* Kaynak komutlarına iki kez basmak, kaynak kullanım bilgilerini panoya kopyalayacaktır.
* Eklenti güvenli ekranlarda çalıştırılıyorsa kaynak bilgileri panoya kopyalanamaz.
* CPU kullanımı, fiziksel çekirdekler için değil, mantıksal işlemciler için verilmektedir. Bu durum, CPU sayısının CPU çekirdek sayısının iki katı olduğu Hyper-Threading özelliğine sahip işlemcilerde fark edilir. Bazı yeni bilgisayarlarda, tüm CPU çekirdeklerinde Hyper-Threading etkinleştirilmemiş olabilir.
* Büyük dosyaların kopyalanması veya ağ sürücülerinin bulunması gibi yoğun disk etkinliği söz konusu olduğunda, disk kullanım bilgilerinin alınmasında gecikmeler yaşanabilir.
* NVDA, kablosuz ağlara bağlanırken veya bağlantıyı keserken bir ses çıkaracak ve bir mesaj bildirecektir. Bu davranışı nasıl değiştireceğinizi bir sonraki bölümde görebilirsiniz.
* Nvidia GPU'larına ait GPU bilgileri verilmiştir.
* Windows sürüm raporlamasında işlemci mimarisi bilgisi açıklanırken, "AMD64" 64-bit (x64) Intel ve AMD işlemcilerini ifade eder. Bu bilgi, kullanılan gerçek işlemcinin adını ifade etmez.
* Eklentinin Windows 10/11 LTSC'ye yüklenmesi desteklenmemektedir.

## Ayarlar

NVDA Menüsü/Tercihler/Ayarlar iletişim kutusunda Kaynak İzleme kategorisi altında aşağıdaki kaynak kullanım bildirme seçeneklerini yapılandırabilirsiniz:

* CPU/GPU sıcaklık birimi: CPU ve GPU sıcaklıklarının Santigrat veya Fahrenheit olarak bildirilmesini seçin.
* Wi-Fi bağlanma/kesilme bildirimi: NVDA'nın Wi-Fi bağlantı/kesme bildirimlerini nasıl bildirmesi gerektiğini seçin (kapalı, mesaj, ses, hem mesaj hem ses).
* Bellek ve disk boyutu gösterimi: RAM ve disk kullanım birimleri (gigabayt ve terabayt gibi) için bellek boyutlarının nasıl seslendirileceğini seçin (varsayılan olarak alternatif yöntem (KB/MB/...) kullanılır).

Her eklenti sürümü arasında yapılan değişikliklerin listesi için [eklenti sürümleri için changelogs][1] belgesine bakın.

[1]: https://github.com/kefaslungu/resourceMonitor/blob/main/changes.md
