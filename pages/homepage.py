from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_register_button(self):
        return self.driver.find_element(By.CLASS_NAME, "ico-register")

    def get_login_button(self):
        return self.driver.find_element(By.CLASS_NAME, "ico-login")