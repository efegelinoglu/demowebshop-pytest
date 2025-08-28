import pytest
from pages.anasayfa import Anasayfa
from pages.kayıt_olma_sayfası import KayıtOlmaSayfası
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = "https://demowebshop.tricentis.com/"  

@pytest.mark.usefixtures("browser")
class TestKayıtOlmaSayfası:

    def test_kayıt_ol_click(self):
        self.driver.get(URL)
        
        anasayfa = Anasayfa(self.driver)
        button = anasayfa.kayıt_ol_button()
        assert button is not None

        button.click()
        
    def test_kayıt_olma_sayfa_dogrulama(self):
        self.driver.get(URL + "register")
        
        kayıt_sayfası = KayıtOlmaSayfası(self.driver)
        başlık = kayıt_sayfası.kayıt_olma_sayfa_başlıgı()
        assert başlık == "Demo Web Shop. Register"
        print("Kayıt olma sayfasına yönlendirildi ve başlık doğrulandı.")
        
    def test_dogru_bilgilerle_kayıt_olma_erkek(self):
        self.driver.get(URL + "register")
        
        kayıt_sayfası = KayıtOlmaSayfası(self.driver)
        
        # Formu doldur
        kayıt_sayfası.cinsiyet_radio_button_erkek().click()
        kayıt_sayfası.isim_input().send_keys("Ahmet")
        kayıt_sayfası.soyisim_input().send_keys("Yılmaz")
        kayıt_sayfası.email_input().send_keys("ahmetyılmaz12345@gmail.com")
        kayıt_sayfası.şifre_input().send_keys("Ahmet12345")
        kayıt_sayfası.şifre_tekrar_input().send_keys("Ahmet12345")
        kayıt_sayfası.kayıt_ol_button().click()
        
        # Email hatasını kontrol et
        try:
            hata_mesajı = kayıt_sayfası.belirtilen_email_kullanılıyor_hata_mesajı().text
            if hata_mesajı == "The specified email already exists":
                print("Bu email zaten kullanılıyor, lütfen farklı bir email deneyin.")
                return
        except NoSuchElementException:
            # Hata mesajı yok → email kullanılmıyor
            pass
        
        # Başarılı kayıt mesajını bekle
        mesaj = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(kayıt_sayfası.kayıt_başarılı_mesajı())
        ).text
        
        assert mesaj == "Your registration completed"
        kayıt_sayfası.kayıt_olma_başarılı_devam_et_button().click()
        print("Erkek kullanıcı başarıyla kayıt oldu.")

    def test_dogru_bilgilerle_kayıt_olma_kadın(self):
            self.driver.get(URL + "register")
            
            kayıt_sayfası = KayıtOlmaSayfası(self.driver)
            
            # Formu doldur
            kayıt_sayfası.cinsiyet_radio_button_kadın().click()
            kayıt_sayfası.isim_input().send_keys("Ayşe")
            kayıt_sayfası.soyisim_input().send_keys("Demir")
            kayıt_sayfası.email_input().send_keys("ayşedemir@gmail.com")
            kayıt_sayfası.şifre_input().send_keys("Ayşe12345")
            kayıt_sayfası.şifre_tekrar_input().send_keys("Ayşe12345")
            kayıt_sayfası.kayıt_ol_button().click()
            try:
                hata_mesajı = kayıt_sayfası.belirtilen_email_kullanılıyor_hata_mesajı().text
                if hata_mesajı == "The specified email already exists":
                    print("Bu email zaten kullanılıyor, lütfen farklı bir email deneyin.")
                    return
            except NoSuchElementException:
                # Hata mesajı yok → email kullanılmıyor
                pass
            
            # Başarılı kayıt mesajını bekle
            mesaj = WebDriverWait(self.driver, 10).until(
                EC.visibility_of(kayıt_sayfası.kayıt_başarılı_mesajı())
            ).text
            
            assert mesaj == "Your registration completed"
            kayıt_sayfası.kayıt_olma_başarılı_devam_et_button().click()
            print("Erkek kullanıcı başarıyla kayıt oldu.")
            