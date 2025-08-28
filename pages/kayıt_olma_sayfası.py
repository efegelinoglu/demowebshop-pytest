from selenium.webdriver.common.by import By

class KayıtOlmaSayfası:
    def __init__(self, driver):
        self.driver = driver  

    def kayıt_olma_sayfa_başlıgı(self):
        return self.driver.title
    
    def cinsiyet_radio_button_erkek(self):
        return self.driver.find_element(By.ID, "gender-male")
    
    def cinsiyet_radio_button_kadın(self):
        return self.driver.find_element(By.ID, "gender-female")
    
    def isim_input(self):
        return self.driver.find_element(By.ID, "FirstName")
    
    def soyisim_input(self):
        return self.driver.find_element(By.ID, "LastName")
    
    def email_input(self):
        return self.driver.find_element(By.ID, "Email")
    
    def şifre_input(self):
        return self.driver.find_element(By.ID, "Password")
    
    def şifre_tekrar_input(self):
        return self.driver.find_element(By.ID, "ConfirmPassword")
    
    def kayıt_ol_button(self):
        return self.driver.find_element(By.ID, "register-button")
    
    def kayıt_başarılı_mesajı(self):
        return self.driver.find_element(By.CLASS_NAME, "result")
    def kayıt_olma_başarılı_devam_et_button(self):
        return self.driver.find_element(By.CLASS_NAME, "register-continue-button")
    def belirtilen_email_kullanılıyor_hata_mesajı(self):
        return self.driver.find_element(By.CLASS_NAME, "validation-summary-errors")
