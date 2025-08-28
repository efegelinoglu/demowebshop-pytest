import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def browser(request):
    options = Options()
    # options.add_argument("--headless")  # Headless modu istenirse aktif edilir
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver  
    yield
    driver.quit()
