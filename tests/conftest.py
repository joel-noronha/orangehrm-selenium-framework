from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    # options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()