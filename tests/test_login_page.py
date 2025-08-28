from pages.homepage import HomePage
from pages.login_page import LoginPage
import pytest

URL = "https://demowebshop.tricentis.com/"

@pytest.mark.usefixtures("browser")
class TestLoginPage:
    def login_button_click(self):
        self.driver.get(URL)
        homepage = HomePage(self.driver)
        button = homepage.get_login_button()
        assert button is not None
        button.click()

    def test_login_page_verification(self):
        self.driver.get(URL + "login")
        title = self.driver.title
        assert title == "Demo Web Shop. Login"
        print("Login page has been redirected and title is verified.")

    def test_login_with_correct_credentials(self):
        self.driver.get(URL + "login")
        login_page = LoginPage(self.driver)
        login_page.input_email("ahmetyilmaz12345@gmail.com")
        login_page.input_password("Ahmet12345")
        login_page.get_login_button().click()