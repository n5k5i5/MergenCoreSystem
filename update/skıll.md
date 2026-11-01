# MergenCoreSystem — Yetenek ve Modül Geliştirme Rehberi (skill.md)

Bu doküman, MergenCoreSystem altyapısına yeni OSINT (Açık Kaynak İstihbaratı) modülleri ekleme, global API anahtarlarını yönetme ve Metasploit tarzı CLI komut tablosunu genişletme standartlarını içerir.

---

## 1. Yeni Modül Ekleme Standartları

Sisteme yeni bir yetenek eklemek için üç adımlı bir entegrasyon takvimi uygulanır.

### Adım 1: Modülün Tanımlanması (`core/shell.py`)
`MergenShell.__init__` metodu içerisindeki `self.modules` sözlüğüne modülün yolunu ve ihtiyaç duyduğu **Zorunlu / Seçmeli** parametreleri ekleyin:

```python
self.modules = {
    # Mevcut Modüller...
    'osint/yeni_yetenek': {
        'TARGET': '',        # Kullanıcının doldurması gereken alan
        'VERBOSE': 'TRUE'    # Varsayılan değere sahip alan
    }
}
```

### Adım 2: Tab-Completion Desteği (`core/completer.py`)
Yeni eklenen parametrelerin ve modül isminin sekme (Tab) tuşuna basıldığında otomatik tamamlanabilmesi için `core/completer.py` motoru otomatik olarak `self.shell.modules.keys()` üzerinden beslenir. Ekstra bir girdi gerekmez.

### Adım 3: Çalıştırma Mantığı (Execution Pipeline)
`core/shell.py` içerisindeki `run` veya `exploit` komut bloğuna modülün asıl işi yapacak olan Python kodunu veya dış kütüphane çağrısını bağlayın:

```python
elif base_cmd in ['run', 'exploit']:
    if self.active_module == 'osint/yeni_yetenek':
        target = self.modules[self.active_module]['TARGET']
        # Buraya gerçek OSINT fonksiyonunuzu (Örn: Shodan API çağrısı) entegre edin
        print(f"[*] {target} üzerinde istihbarat toplama başladı...")
```

---

## 2. API ve Kimlik Bilgisi Havuzu (Keyring)

Projeye ait tüm servis anahtarları tek bir merkezden yönetilir. `core/shell.py` altındaki `self.global_api_registry` sözlüğüne ekleme yaparak yeni servisler tanımlayabilirsiniz:

| API Adı | İlgili Servis | Açıklama |
| :--- | :--- | :--- |
| `SHODAN` | shodan.io | IoT ve Sunucu zafiyet taramaları |
| `GMAP_G` | ://google.com | Coğrafi konum ve haritalandırma |
| `IP_API` | ipapi.com | Toplu IP adres analizi ve Whois |
| `NGROK_AUTH` | ://ngrok.com | Big Brother phishing tünelleme |
| `VIRUSTOTAL_API` | virustotal.com | Subdomain ve zararlı analiz taraması |
| `CMS_DETECT_API` | whatcms.org | Hedef web sitesi içerik yönetim sistemi tespiti |
| `PHONE_APIS` | numverify.com | Telefon numarası doğrulama ve operatör sorgu |

---

## 3. Komut Hiyerarşisi ve Durum Makinesi

MergenCoreSystem, kullanıcının bulunduğu konuma (Küresel veya Modül içi) göre tepki verir.

