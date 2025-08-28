from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def input_email(self, email):
        email_input = self.driver.find_element(By.ID, "Email")
        email_input.clear()
        email_input.send_keys(email)

    def input_password(self, password):
        password_input = self.driver.find_element(By.ID, "Password")
        password_input.clear()
        password_input.send_keys(password)

    def check_remember_me(self):
        remember_me_checkbox = self.driver.find_element(By.ID, "RememberMe")
        if not remember_me_checkbox.is_selected():
            remember_me_checkbox.click()

    def get_login_button(self):
        return self.driver.find_element(By.CLASS_NAME, "login-button")

    def get_forgot_password_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Forgot password?")