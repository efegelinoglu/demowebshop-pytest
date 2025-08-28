import pytest
from pages.anasayfa import Anasayfa

URL = "https://demowebshop.tricentis.com/"  

@pytest.mark.usefixtures("browser")
class TestAnaSayfa:

    def test_kayıt_ol_click(self):
        self.driver.get(URL)
        

        driver = Anasayfa(self.driver)
        button = driver.kayıt_ol_button()
        assert button is not None

        button.click()
        


