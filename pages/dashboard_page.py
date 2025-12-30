import os
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




class DashboardPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.title_text = (By.XPATH, "//h6[text()='Dashboard']")

    #Locators

    def is_dasboard_loaded(self):
        return self.wait.until(EC.presence_of_element_located((self.title_text)))

    def get_current_url(self):
        return self.driver.current_url
