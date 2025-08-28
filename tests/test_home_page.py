import pytest
from pages.homepage import HomePage

URL = "https://demowebshop.tricentis.com/"

@pytest.mark.usefixtures("browser")
class TestHomePage:
    def test_register_button_click(self):
        self.driver.get(URL)
        homepage = HomePage(self.driver)
        button = homepage.get_register_button()
        assert button is not None
        button.click()