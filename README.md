# Selenium Paytest - Demo Web Shop Test Otomasyonu

Bu proje, [Demo Web Shop](https://demowebshop.tricentis.com/) sitesi üzerinde **Selenium** ve **Pytest** kullanarak geliştirilmiş bir **test otomasyon projesidir**.  
Amaç, kullanıcı kayıt süreçlerini, ana sayfa bileşenlerini ve form doğrulamalarını otomatik test senaryoları ile kontrol etmektir.

---

## 🚀 Özellikler

- Selenium WebDriver ile **UI test otomasyonu**
- Pytest ile **test senaryolarının yönetimi**
- **Sayfa Objesi Modeli (POM)** yapısı ile modülerlik
- Geliştirilebilir, yeni senaryolara uygun test altyapısı

---

## 📂 Proje Yapısı

```bash
selenium-paytest/
│
├── demowebshop/
│   ├── pages/                # Sayfa objeleri
│   │   ├── anasayfa.py
│   │   ├── kayıt_olma_sayfası.py
│   │   └── __init__.py
│   │
│   ├── tests/                # Test senaryoları
│   │   ├── test_ana_sayfa.py
│   │   ├── test_kayıt_olma_sayfası.py
│   │   ├── conftest.py
│   │   └── __init__.py
│   │
│   ├── requirements.txt      # Gerekli Python kütüphaneleri
│   ├── pytest.ini            # Pytest yapılandırma dosyası
│   ├── .gitignore            # Gereksiz dosyaları git'ten hariç tutar
│   └── README.md             # Proje dokümantasyonu
│
└── env/                      # Sanal ortam (git'e dahil edilmez)
