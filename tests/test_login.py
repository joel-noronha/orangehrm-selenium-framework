import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


def test_valid_login():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    time.sleep(2)


