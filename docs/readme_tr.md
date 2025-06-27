<p align="center">
  <a href="https://github.com/your-username/Tranfastic">
    <img src="../assets/icon.png" alt="Tranfastic Icon" width="150">
  </a>
</p>

<h1 align="center">Tranfastic</h1>

---

<h4 align="center">Anlık Çeviri Uygulaması (GUI ile)</h3>

<p align="center">
  <br>
  <a href="#-özellikler">Özellikler</a>
  .
  <a href="#-başlangıç">Başlangıç</a>
  .
  <a href="#%EF%B8%8F-yapılandırma">Yapılandırma</a>
  .
  <a href="#-katkıda-bulunma">Katkıda Bulunma</a>
  .
  <a href="#%EF%B8%8F-geliştirme-yol-haritası">Geliştirme</a>
  .
  <a href="#-lisans">Lisans</a>
  <br>
  <br>
</p>

<p align="center">
   <a href="https://www.python.org/downloads/">
      <image src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+" />
   </a>
   <a href="https://www.microsoft.com/windows">
      <image src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-blue.svg" alt="Windows | Linux" />
   </a>
   <a href="https://opensource.org/licenses/MIT">
      <image src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" />
   </a>
</p>

<div align="center">

![Uygulama Önizlemesi](../docs/app_withoutbg.png)

</div>

## ⚠️ Şu anda sadece **Windows** için mevcuttur. Linux ve Mac için yakında yayınlanacaktır.

## 📖 Hakkında

Tranfastic, çalışırken anlık, gerçek zamanlı çeviri için tasarlanmış hafif bir Python uygulamasıdır. Sistem tepsisinde sessizce çalışır ve hızlı bir kısayol tuşu metin girişi için bir pencere açar, çevrilen metni kopyalama veya ekleme için hazır hale getirir.

## ✨ Özellikler

- **🌐 Gerçek Zamanlı Çeviri:** Yazarken anında çeviri sağlar.
- **⚡ Kısayol Tuşu Aktivasyonu:** Özelleştirilebilir klavye kısayolu ile çeviri penceresini anında açar.
- **🖥️ Sistem Tepsisi Entegrasyonu:** Karmaşıklığı en aza indirmek için arka planda sessizce çalışır.
- **⚙️ Özelleştirilebilir Ayarlar:** Kaynak ve hedef dilleri yapılandırmanıza olanak tanır.
- **🔒 Gizlilik Odaklı:** Hiçbir çeviri geçmişi veya hassas bilgi saklamaz.
- **📋 Tek Tıkla Kopyalama:** Çevrilen metni tek tıkla kopyalayın.
- **🎨 Temiz Arayüz:** Çalışmanızı rahatsız etmeyen minimalist tasarım.
- **🔧 Kolay Yapılandırma:** Dil tercihleri için basit ayarlar menüsü.

## 🚀 Başlangıç

### Kurulum

1. **Depoyu klonlayın:**
   ```bash
   git clone https://github.com/your-username/Tranfastic.git
   cd Tranfastic
   ```
2. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

### Uygulamayı Çalıştırma

1. **Tranfastic'ı başlatın:**

   ```bash
   python main.py
   ```

   Tranfastic simgesi sistem tepsinizde görünecektir.

2. **Kısayol Tuşunu Kullanma:**
   - `Shift+Alt+D` (varsayılan) tuşlarına basın veya ayarlarda tercih ettiğiniz kısayolu belirleyin.
3. **Giriş ve Çeviri:**

   - Açılan pencereye metin yazın veya yapıştırın ve çevirinizi almak için Enter'a basın.

4. **Kolay Kapatma:**
   - Açılan pencereyi hızlıca kapatmak için `Esc` tuşuna basın.

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
- Mümkünse `app.log` dosyasının içeriği (uygulamanın dizininde bulunur).

## 🛠️ Geliştirme Yol Haritası

**Mevcut özellikler ve gelecek güncellemeler:**

- [x] Kısayol tuşu ve günlük kaydı uygulaması
- [ ] İlk açılışta odak çalınmasını önleme
- [ ] Seçili alanlardan doğrudan metin yakalama
- [ ] Çeviriler için kullanıcı bildirimleri ekleme
- [ ] Windows başlangıcında çalıştırmayı etkinleştirme

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.
