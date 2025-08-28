import pytest
from pages.homepage import HomePage
from pages.registration_page import RegistrationPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://demowebshop.tricentis.com/"

@pytest.mark.usefixtures("browser")
class TestRegistrationPage:
    def test_register_button_click(self):
        self.driver.get(URL)
        homepage = HomePage(self.driver)
        button = homepage.get_register_button()
        assert button is not None
        button.click()

    def test_registration_page_verification(self):
        self.driver.get(URL + "register")
        registration_page = RegistrationPage(self.driver)
        title = registration_page.get_page_title()
        assert title == "Demo Web Shop. Register"
        print("Redirected to the registration page and title is verified.")

    @pytest.mark.parametrize("gender, first_name, last_name, email, password", [
        ("male", "Ahmet", "Yilmaz", "ahmetyilmaz12345@gmail.com", "Ahmet12345"),
        ("female", "Ayse", "Demir", "aysedemir@gmail.com", "Ayse12345")
    ])
    def test_register_with_correct_credentials(self, gender, first_name, last_name, email, password):
        self.driver.get(URL + "register")
        registration_page = RegistrationPage(self.driver)

        # Fill the form
        if gender == "male":
            registration_page.get_male_radio_button().click()
        else:
            registration_page.get_female_radio_button().click()
        
        registration_page.get_first_name_input().send_keys(first_name)
        registration_page.get_last_name_input().send_keys(last_name)
        registration_page.get_email_input().send_keys(email)
        registration_page.get_password_input().send_keys(password)
        registration_page.get_confirm_password_input().send_keys(password)
        registration_page.get_register_button().click()

        # Check for email existence error
        try:
            error_message = registration_page.get_email_exists_error_message().text
            if "The specified email already exists" in error_message:
                print(f"This email '{email}' already exists. Please try a different email.")
                return
        except NoSuchElementException:
            pass

        # Wait for the successful registration message
        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of(registration_page.get_success_message())
        ).text

        assert message == "Your registration completed"
        registration_page.get_success_continue_button().click()
        print(f"{gender.capitalize()} user registered successfully.")