from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



def test_browser_launch():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://google.com")
    time.sleep(2)
    driver.quit()

