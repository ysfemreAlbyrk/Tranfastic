<p align="center">
  <a href="https://github.com/ysfemreAlbyrk/Tranfastic">
    <img src="../assets/icon.png" alt="Tranfastic Icon" width="150">
  </a>
</p>

<h1 align="center">Tranfastic</h1>

<h4 align="center">Hafif Taşınabilir Anlık Çevirmen</h4>

<p align="center">
  <br>
  <a href="#-özellikler" style="color: #0366d6">Özellikler</a>
  ·
  <a href="#-hızlı-başlangıç" style="color: #0366d6">Hızlı Başlangıç</a>
  ·
  <a href="#-nasıl-kullanılır" style="color: #0366d6">Nasıl Kullanılır</a>
  ·
  <a href="#%EF%B8%8F-geliştirme" style="color: #0366d6">Geliştirme</a>
  ·
  <a href="#-katkıda-bulunma" style="color: #0366d6">Katkıda Bulunma</a>
  <br>
</p>

<p align="center">
  <a href="../README.md" style="color: #0366d6">🇺🇸 English</a>
  <br>
</p>

<p align="center">
   <a href="https://www.python.org/downloads/">
      <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python 3.7+" />
   </a>
   <a href="https://www.microsoft.com/windows">
      <img src="https://img.shields.io/badge/Platform-Windows-blue.svg" alt="Windows" />
   </a>
   <a href="https://opensource.org/licenses/MIT">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
   </a>
   <a href="../../releases/latest">
      <img src="https://img.shields.io/badge/İndir-Taşınabilir%20EXE-green.svg" alt="Taşınabilir İndir" />
   </a>
</p>

<div align="center">

![Tranfastic](../assets/app.png)

</div>

Windows için sistem çapında kısayollarla anlık çeviri sağlayan hafif, taşınabilir çeviri uygulaması.

## ✨ Özellikler

- **🔥 Anlık Çeviri**: Global kısayol (`Shift+Alt+D`) ile hızlı çeviri
- **🌐 Çoklu Dil**: İngilizce, Türkçe, Almanca, İspanyolca, Japonca ve daha fazlası
- **📱 Sistem Tepsisi**: Arka planda sessizce çalışır
- **⚡ Hafif**: Tek taşınabilir dosya (~50-80MB)
- **🎨 Modern Arayüz**: Temiz, koyu temalı tasarım
- **📋 Pano Entegrasyonu**: Çeviriyi otomatik yapıştırır
- **🔧 Yapılandırılabilir**: Özelleştirilebilir kısayollar ve diller
- **📝 Günlük**: İsteğe bağlı çeviri geçmişi

## 🚀 Hızlı Başlangıç

### 📥 İndir & Çalıştır

1. [Releases](../../releases/latest) sayfasından `Tranfastic.exe` dosyasını indirin
2. İstediğiniz klasöre kopyalayın (Masaüstü, USB sürücü vb.)
3. Çift tıklayarak çalıştırın
4. Herhangi bir yerde metin seçin ve `Shift+Alt+D` tuşlarına basın

Kurulum gerektirmez! Herhangi bir Windows 10/11 bilgisayarında çalışır.

## 🎯 Nasıl Kullanılır

1. **Uygulamayı Başlatın**: `Tranfastic.exe` dosyasını çalıştırın
2. **Metin Seçin**: Herhangi bir uygulamada metni vurgulayın
3. **Çevirin**: `Shift+Alt+D` tuşlarına basın (veya özel kısayolunuz)
4. **Sonuç Alın**: Çeviri penceresi anında açılır
5. **Otomatik Yapıştır**: Çevrilen metin otomatik olarak yapıştırılır

### Sistem Tepsisi Menüsü

Tepsi simgesine sağ tıklayarak:

- Ayarları açın
- Çeviri geçmişini kontrol edin
- Uygulamadan çıkın

## ⚙️ Yapılandırma

- **Dil Ayarları:** Ayarlar menüsünde tercih ettiğiniz kaynak ve hedef dilleri belirleyin.
- **Kısayol Özelleştirme:** İsteğinize uygun olarak kısayol tuşunu değiştirin.
- **Başlangıçta Çalıştırma (Windows):** İsteğe bağlı olarak Tranfastic'ın bilgisayarınız açıldığında başlamasını etkinleştirin.

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Katkıda bulunmak için:

1. **Depoyu fork edin** ve özelliğiniz veya hata düzeltmeniz için yeni bir dal oluşturun.
2. **Değişikliklerinizi test edin** kararlılığı sağlamak için.
3. **Bir pull request gönderin**, değişiklikleri ve eklenen özellikleri açıklayarak.

Hata raporları için lütfen şunlarla birlikte bir issue açın:

- Sorunun net bir açıklaması.
- Sorunu yeniden üretme adımları.
- Mümkünse `logs/[date].log` dosyasının içeriği (uygulamanın dizininde bulunur).

## 🛠️ Geliştirme Yol Haritası

**Mevcut özellikler ve gelecek güncellemeler fazara göre düzenlenmiştir:**

### ✅ Faz 1: Temel Altyapı (Tamamlandı)

- [x] Kısayol tuşu ve günlük kaydı uygulaması
- [x] Sistem tepsisi entegrasyonu (özel ikon ve menü)
- [x] Minimalist, modern, başlıksız çeviri penceresi
- [x] Dil ve kısayol ayarlarının özelleştirilebilmesi
- [x] Lokal çeviri geçmişi (günlük dosya, opsiyonel)
- [x] Koyu tema ve özel font entegrasyonu
- [x] Çevirinin odaklanılan inputa otomatik yapıştırılması
- [x] Ayarlar içinde Hakkında bölümü
- [ ] Windows başlangıcında çalıştırma seçeneği

### 🔄 Faz 2: Kullanıcı Deneyimi İyileştirmeleri (Devam Ediyor)

- [ ] İlk açılışta odak çalınmasını önleme
- [ ] Seçili alanlardan doğrudan metin yakalama
- [ ] Çeviriler için kullanıcı bildirimleri ekleme
- [ ] Tepsi menüsünde hızlı dil değiştirici
- [ ] Pencere boyutu ve şeffaflığının özelleştirilebilmesi
- [ ] Tüm arayüz için klavye ile gezinme
- [ ] Panodaki içeriği otomatik algılayıp çevirme
- [ ] **Çeviri Geçmişi Yönetimi:**
  - [ ] Çeviri geçmişini görüntüleme, arama ve yönetme için modern arayüz
  - [ ] Meta verilerle (zaman damgası, dil çiftleri, sıklık) veritabanı yapısı
  - [ ] Önemli çevirileri hızlı erişim için yıldızlama/favoriler
  - [ ] Metin, tarih veya dil çiftlerine göre arama ve filtreleme
  - [ ] Organizasyon için kategoriler ve etiketler
  - [ ] Toplu işlemler (silme, dışa aktarma, kategorilendirme)
  - [ ] Yedekleme ve senkronizasyon yetenekleri

### 🚀 Faz 3: Gelişmiş Özellikler

- [ ] Otomatik güncelleme sistemi (GitHub releases üzerinden)
- [ ] OCR ile görselden metin çevirisi
- [ ] Sesli giriş ve çeviri
- [ ] Çoklu API desteği (Google, DeepL, Yandex, vs.)
- [ ] Çeviri geçmişini dışa/içe aktarabilme
- [ ] Tema desteği (açık/koyu/özel)
- [ ] Uygulama içi geri bildirim ve hata bildirimi

### 🤖 Faz 4: Yapay Zeka ve Makine Öğrenmesi

- [ ] Offline çeviri (yerel ML modeli)
- [ ] Makine öğrenmesi ile çeviri iyileştirmeleri
- [ ] Ollama entegrasyonu ile yerel AI destekli çeviri
- [ ] Bağlam farkında çeviriler

### 🌍 Faz 5: Platform Genişletme

- [ ] Çoklu platform desteği (Linux, macOS)

**Senin de bir fikrin mi var? Issue veya pull request açabilirsin!**

## 🙏 Açık Kaynak Bağımlılıkları

Tranfastic, bu harika açık kaynak projeler olmadan mümkün olmazdı:

- **[googletrans](https://github.com/ssut/py-googletrans)** - Çeviri motorumuzu güçlendiren Google Translate API wrapper'ı
- **[PyQt5](https://www.riverbankcomputing.com/software/pyqt/)** - Modern, duyarlı arayüzümüz için çok platformlu GUI framework'ü
- **[pystray](https://github.com/moses-palmer/pystray)** - Tranfastic'ı arka planda sessizce çalıştıran sistem tepsisi entegrasyonu
- **[keyboard](https://github.com/boppreh/keyboard)** - Anlık çeviri penceresi aktivasyonu için global kısayol tuşu algılama
- **[Inter Font](https://github.com/rsms/inter)** - Temiz arayüzümüz için güzel, modern font ailesi
- **[Material Symbols](https://fonts.google.com/icons)** - UI öğeleri için Google'ın Material Design ikonları
- **[pywin32](https://github.com/mhammond/pywin32)** - Sorunsuz Windows entegrasyonu için Windows'a özel API'ler

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.
