<p align="center">
  <a href="https://github.com/ysfemreAlbyrk/Tranfastic">
    <img src="../assets/icon.png" alt="Tranfastic Icon" width="150">
  </a>
</p>

<h1 align="center">Tranfastic</h1>

<h4 align="center">Hafif Anlık Çevirmen</h4>

<p align="center">
  <br>
  <a href="#-özellikler" style="color: #0366d6">Özellikler</a>
  .
  <a href="#-hızlı-başlangıç" style="color: #0366d6">Hızlı Başlangıç</a>
  .
  <a href="#%EF%B8%8F-geliştirme" style="color: #0366d6">Geliştirme</a>
  .
  <a href="#-katkıda-bulunma" style="color: #0366d6">Katkıda Bulunma</a>
  .
  <a href="LEGAL.md" style="color: #0366d6">Hukuki</a>
  .
  <a href="TROUBLESHOOTING.md" style="color: #0366d6">Sorun Giderme</a>
  .
  <a href="ROADMAP.md" style="color: #0366d6">Yol Haritası</a>
  .
  <a href="#-lisans" style="color: #0366d6">Lisans</a>
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

![Tranfastic](../assets/howto.gif)

</div>

Tranfastic, çalışırken anlık, gerçek zamanlı çeviri için tasarlanmış hafif bir Python uygulamasıdır. Sistem tepsisinde gizlice durur ve hızlı bir kısayol tuşu metin girişi için bir pencere açar, çevrilmiş metni kopyalama veya yerleştirme için hazır hale getirir.

## ✨ Özellikler

- **🔥 Anlık Çeviri**: Global kısayol (`Shift+Alt+D`) ile hızlı çeviri
- **⚡ Kısayol Aktivasyonu:** Özelleştirilebilir klavye kısayolu ile çeviri pop-up'ını anında açar.
- **🌐 Çoklu Dil**: _İngilizce_, _Türkçe_, _Almanca_, _İspanyolca_, _Japonca_ ve daha fazlası desteği.
- **📱 Sistem Tepsisi**: Arka planda sessizce çalışır.
- **📋 Pano Entegrasyonu**: Çevrilmiş metni otomatik yapıştırır
- **🔧 Yapılandırılabilir**: Özelleştirilebilir kısayollar ve diller
- **🔒 Gizlilik Odaklı:** Herhangi bir çeviri geçmişi veya hassas bilgi saklamaz.
- **🎨 Temiz Arayüz:** Çalışmanızı bölmeyen minimalist tasarım.

## 🚀 Hızlı Başlangıç

### 📥 İndir & Çalıştır

1. [**Releases**](../../releases/latest) sayfasından `Tranfastic.exe` dosyasını indirin
2. İstediğiniz klasöre kopyalayın (Masaüstü, USB sürücü vb.)
3. Çift tıklayarak çalıştırın

Kurulum gerektirmez! Herhangi bir Windows 10/11 bilgisayarında çalışır.

### 🎯 Nasıl Kullanılır

1. **Kısayolu Kullanarak:**
   - `Shift+Alt+D` tuşlarına basın (varsayılan) veya ayarlarda tercih ettiğiniz kısayolu belirleyin.
2. **Giriş ve Çeviri:**

   - Pop-up penceresine metin yazın veya yapıştırın ve çevirinizi almak için Enter tuşuna basın.

3. **Kolayca Kapatın:**
   - Pop-up penceresini hızlıca kapatmak için `Esc` tuşuna basın.

## 🛠️ Geliştirme

### 📦 Kurulum

1. **Önce, depoyu klonlayın:**

```bash
git clone https://github.com/your-username/Tranfastic.git
cd Tranfastic
```

2. **Sanal ortam kurun**

```bash

python -m venv venv

# Sanal ortamı etkinleştirin
./venv/Script/activate
```

3. **Bağımlılıkları yükleyin:**

```bash
pip install -r requirements.txt
```

### 🏃 Uygulamayı Çalıştırın

1. **Tranfastic'ı başlatın:**

```bash
python main.py
```

Tranfastic simgesi sistem tepsisinde görünecektir.

### 🔨 Taşınabilir Çalıştırılabilir Dosya Oluşturun

```bash
# Depoyu klonlayın
git clone https://github.com/ysfemreAlbyrk/Tranfastic.git
cd Tranfastic

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Taşınabilir çalıştırılabilir dosya oluşturun
./build_portable.bat
```

Çalıştırılabilir dosya `dist/Tranfastic.exe` konumunda oluşturulacaktır.

## 🐛 Yardıma mı İhtiyacınız Var?

Sorun mu yaşıyorsunuz? Yaygın sorunların çözümleri için kapsamlı [Sorun Giderme Rehberimizi](TROUBLESHOOTING.md) kontrol edin.

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

Planlanan özellikler, zaman çizelgeleri ve Tranfastic'ın geleceğine nasıl katkıda bulunabileceğiniz için detaylı [Geliştirme Yol Haritamızı](ROADMAP.md) inceleyin.

**Hızlı öne çıkanlar:**

- 🔄 **Faz 2 (Devam Ediyor)**: Kullanıcı deneyimi iyileştirmeleri ve çeviri geçmişi yönetimi
- 🚀 **Faz 3**: OCR, sesli giriş ve çoklu API desteği dahil gelişmiş özellikler
- 🤖 **Faz 4**: AI ve makine öğrenmesi entegrasyonu (ollama aracılığıyla)
- 🌍 **Faz 5**: Çapraz platform genişletme

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
