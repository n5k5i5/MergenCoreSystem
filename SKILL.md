---
name: mergencore
description: MergenCoreSystem Framework — açık kaynak istihbarat (OSINT) aracı. IP/Domain analizi, telefon numarası sorgulama, metadata çıkarma, yüz tanıma, Shodan araması, kullanıcı adı tarama, Android Debug Bridge (ADB) ve sosyal mühendislik (phishing/geolocation) modüllerini içerir.
---

# MergenCoreSystem Framework

Ücretsiz ve açık kaynaklı OSINT (Open Source Intelligence) framework'üdür. İnternet kullanıcılarını deanonimize etmek ve hedef hakkında kapsamlı bilgi toplamak amacıyla geliştirilmiştir. **Parrot OS** ve **Kali Linux** üzerinde çalışacak şekilde optimize edilmiştir.

> **Geliştirici:** MergenCoreSystem  
> **Web:** MergenCoreSystem  
> **Telegram:** MergenCoreSystem

---

## Proje Yapısı

```
MergenCoreSystem/
├── mergencore.py                # Ana giriş noktası — API anahtarlarını ve lisansı yönetir
├── licence.json                 # Lisans durumu ({"licence": true})
├── requirements.txt             # Python bağımlılıkları (~70 paket)
├── README.md                    # Proje açıklaması (Rusça)
│
├── core/
│   ├── __init__.py
│   └── core.py                  # Ana menü ve modül yönlendirme (osint() fonksiyonu)
│
├── module/
│   ├── __init__.py
│   ├── domain.py                # Domain analiz modülü (16 alt fonksiyon)
│   ├── host.py                  # Geolocation & Big Brother (ngrok + phishing sayfaları)
│   ├── phonenumber.py           # Telefon numarası sorgulama (numverify API)
│   ├── macaddress.py            # MAC adres sorgulama
│   ├── metadata.py              # EXIF metadata çıkarma (fotoğraf + PDF)
│   ├── reverseimagesearch.py    # Ters görsel arama (Google + Yandex)
│   ├── chmodan.py               # Shodan arama motoru entegrasyonu
│   ├── wizard.py                # Kullanıcı adı tarama (Maigret kütüphanesi)
│   ├── android.py               # Android Debug Bridge (ADB) modülü (30 komut)
│   ├── Information_services.py  # Bilgi servisleri menüsü (49 kategori)
│   ├── cookies.txt              # Çerez dosyası
│   ├── setup.cfg                # Modül yapılandırması
│   │
│   ├── db/                      # Veritabanı ve phishing şablonları
│   ├── maigret/                 # Maigret veri kaynakları
│   └── utils/
│       ├── __init__.py          # COLORS modülünü import eder
│       ├── COLORS.py            # Terminal renk kodları (ANSI escape)
│       ├── ban.py               # ASCII banner ve menü şablonları
│       ├── banner.py            # Banner gösterim fonksiyonu
│       ├── identity.py          # Sahte kimlik üreteci (Faker)
│       ├── information_services_data.py  # 49 kategoriye ait veri sayfaları
│       ├── killing.py           # Süreç sonlandırma ve yeniden başlatma
│       ├── licensysi.py         # Lisans doğrulama sistemi
│       ├── mergencore.png       # Logo görseli
│       └── user_agent.txt       # User-Agent listesi
│
└── report/                      # Çıktı ve raporların kaydedildiği klasör
```

---

## Modüller ve Yetenekler

### 1. IP Whois Sorgulama (`core.py` — Opsiyon 1)
- IP adresi için WHOIS bilgisi çeker (`ipwhois` kütüphanesi)
- Reverse DNS lookup yapar (`sonar.omnisint.io` API)

### 2. Domain Analiz (`module/domain.py` — Opsiyon 2)
16 alt fonksiyonu barındırır:
- DNS Dumpster ile subdomain keşfi
- HTTP header analizi
- DNS Lookup, Reverse DNS
- Reverse WHOIS (Selenium + ViewDNS)
- Shared DNS bulma
- Zone Transfer testi
- WHOIS sorgusu
- GeoIP konum belirleme
- Reverse IP lookup
- Nmap port tarama (HackerTarget API)
- Subnet hesaplama
- HTTP headers çekme
- Sayfa bağlantılarını çıkarma
- VirusTotal ile subdomain tarama (API gerektirir)
- CMS tespiti — WhatCMS API

### 3. Telefon Numarası Sorgulama (`module/phonenumber.py` — Opsiyon 3)
- Numverify API ile numara doğrulama
- Ülke, operatör, hat tipi, konum bilgisi

### 4. Metadata Çıkarma (`module/metadata.py` — Opsiyon 4)
- **Fotoğraf EXIF:** GPS koordinatları, lens bilgisi, tarih/saat, yükseklik, yön
- **PDF metadata:** Oluşturma tarihi, yazar, yazılım bilgisi (`pikepdf`)
- Google Earth'te koordinatları açma desteği

### 5. Ters Görsel Arama (`module/reverseimagesearch.py` — Opsiyon 5)
- Google Images ve Yandex Images'a otomatik yükleme
- search4faces, FindClone, TinEye, PimEyes, Carnet.AI bağlantıları

### 6. MAC Adres Sorgulama (`module/macaddress.py` — Opsiyon 6)
- macvendors.co API ile üretici, adres, ülke bilgisi

### 7. Big Brother — Geolocation (`module/host.py` — Opsiyon 7)
- **Sosyal mühendislik aracı:** Phishing sayfaları ile hedefin tarayıcı bilgilerini ve GPS koordinatlarını toplar
- Ngrok ile tünel oluşturma
- 24+ farklı phishing şablonu (near you, weather, hotel, youtube, telegram, tinder, vb.)
- Cihaz bilgileri: IP, OS, tarayıcı, ekran çözünürlüğü, saat dilimi, dil
- GPS koordinatlarını Google Maps ve Google Earth'te açma

### 8. Bilgi Servisleri (`module/Information_services.py` — Opsiyon 8)
49 kategoride OSINT kaynak koleksiyonu:
- Kullanıcı adı araştırma, e-posta, telefon numarası
- Telegram, VK, Instagram, Facebook, Twitter, Reddit OSINT
- Askeri istihbarat, devlet kaynakları (RU/BR/KZ/UZ/PL/Kırgızistan)
- Yüz tanıma, geolocation, güneş hesaplayıcı
- Cryptocurrency araştırma, araç plaka sorgulama
- Uçuş takibi, deniz kargo takibi
- Forum ve ilan sitesi araştırma
- Shodan rehberi, arama motorları, belge arama

### 9. Sahte Kimlik Üreteci (`utils/identity.py` — Opsiyon 9)
- Faker kütüphanesi ile rastgele kimlik bilgisi üretir
- thispersondoesnotexist.com ve generated.photos bağlantıları

### 10. Kullanıcı Adı Tarama (`module/wizard.py` — Opsiyon 12)
- **Maigret** kütüphanesi entegrasyonu
- 2500+ web sitesinde kullanıcı adı arama
- Paralel isteklerle hızlı tarama

### 11. Cryptocurrency Araştırma (Opsiyon 13)
- Bitcoin blok zinciri analiz araçları bağlantıları
- BTC explorer'lar, cüzdan analizi, AML araçları

### 12. Shodan Arama (`module/chmodan.py` — Opsiyon 14)
- Shodan API ile IoT cihaz ve sunucu tarama
- IP, port, organizasyon, konum, domain bilgisi
- Sonuçları `report/` klasörüne kaydetme

### 13. Android Debug Bridge (`module/android.py` — Opsiyon 16)
30 komut içeren ADB modülü:
- Cihaz bağlama/bağlantıyı kesme
- Shell erişimi
- APK yükleme/çıkarma/silme
- Ekran kaydı ve ekran görüntüsü
- Dosya aktarımı (push/pull)
- WiFi açma/kapama
- Parola silme (root gerekli)
- Tuş emülasyonu (84 tuş kodu)
- Sistem dump, logcat, batarya durumu
- WPA supplicant çıkarma
- Port forwarding
- Toplu cihaz bağlama (IP listesinden)

---

## API Anahtarları

API anahtarları `mergencore.py` dosyasındaki `api` sözlüğünde tanımlanır:

| Anahtar | Kaynak | Kullanıldığı Modül |
|---------|--------|-------------------|
| `Shodan` | https://www.shodan.io | `chmodan.py` — IoT tarama |
| `Gmap_g` | Google Maps API | Harita işlemleri |
| `IP_api` | https://ipapi.com | IP toplu tarama |
| `ngrok.set_auth_token` | https://ngrok.com | `host.py` — Tünel oluşturma |
| `virustotal_api` | https://virustotal.com | `domain.py` — Subdomain tarama |
| `cms_detect_api` | https://whatcms.org | `domain.py` — CMS tespiti |
| `phone_apis` | https://numverify.com | `phonenumber.py` — Numara doğrulama |

---

## Kurulum ve Çalıştırma

```bash
# Bağımlılıkları yükle
sudo pip3 install -r requirements.txt

# Framework'ü başlat
python3 mergencore.py
```

### Ön Koşullar
- Python 3.x
- Parrot OS veya Kali Linux (önerilen)
- PHP (Big Brother modülü için)
- ADB (Android Debug Bridge modülü için)
- Selenium + Firefox GeckoDriver (Reverse WHOIS için)

---

## Mimari Notlar

### Akış Yapısı
1. `mergencore.py` → Lisans kontrolü (`licensysi.py`) → `osint()` fonksiyonu (`core.py`)
2. `core.py` → Ana menü döngüsü → Kullanıcı seçimine göre ilgili modülü çağırır
3. Her modül bağımsız çalışır ve gerekli API anahtarlarını `mergencore.api` sözlüğünden alır

### Renk Sistemi
Terminal çıktıları ANSI escape kodları ile renklendirilir (`COLORS.py`):
- `REDL` — Kırmızı (uyarı/hata)
- `GNSL` — Mavi (bilgi)
- `WHSL` — Varsayılan (metin)
- `FIOL` — Mor (vurgu)
- `OKNL` — Cyan (başarı)

### Menü Navigasyonu
- `99` → Bir üst menüye dön
- `66` → Konsolu temizle
- `00` → Programı kapat

---

## Geliştirme Rehberi

### Yeni Modül Ekleme
1. `module/` altında yeni bir `.py` dosyası oluşturun
2. API gerekiyorsa `mergencore.py`'deki `api` sözlüğüne ekleyin
3. `core/core.py`'deki `osint()` fonksiyonuna yeni bir `elif choice ==` bloğu ekleyin
4. Gerekirse `module/utils/ban.py`'ye yeni menü banner'ı ekleyin

### Dikkat Edilecekler
- Modüller lazy import kullanır (fonksiyon içinde import)
- Bazı modüller `os.system('clear')` kullanır — Windows uyumluluğu sınırlıdır
- Hata yönetimi çoğunlukla bare `except` kullanır — iyileştirme fırsatı
- `domain.py`'deki bazı fonksiyonlar recursive çağrı yapar (sonsuz döngü riski)
