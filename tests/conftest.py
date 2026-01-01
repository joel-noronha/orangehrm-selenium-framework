from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    #options.add_argument('--start-maximized')
    options.add_argument('--incognito')
    #options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    #driver.implicitly_wait(5)
    yield driver
    driver.quit()