from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def get_male_radio_button(self):
        return self.driver.find_element(By.ID, "gender-male")

    def get_female_radio_button(self):
        return self.driver.find_element(By.ID, "gender-female")

    def get_first_name_input(self):
        return self.driver.find_element(By.ID, "FirstName")

    def get_last_name_input(self):
        return self.driver.find_element(By.ID, "LastName")

    def get_email_input(self):
        return self.driver.find_element(By.ID, "Email")

    def get_password_input(self):
        return self.driver.find_element(By.ID, "Password")

    def get_confirm_password_input(self):
        return self.driver.find_element(By.ID, "ConfirmPassword")

    def get_register_button(self):
        return self.driver.find_element(By.ID, "register-button")

    def get_success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "result")

    def get_success_continue_button(self):
        return self.driver.find_element(By.CLASS_NAME, "register-continue-button")

    def get_email_exists_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "validation-summary-errors")