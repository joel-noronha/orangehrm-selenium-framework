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
        self.PROFILE_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-name")
        self.side_menu_items = (By.CSS_SELECTOR,"ul[class='oxd-main-menu'] li")

    #Locators

    def is_dasboard_loaded(self):
        return self.wait.until(EC.presence_of_element_located((self.title_text)))

    def get_current_url(self):
        return self.driver.current_url

    def get_dashboard_profiledropdown(self):
        profile = self.wait.until(
            EC.presence_of_element_located(self.PROFILE_DROPDOWN)
        )
        return profile is not None

    def get_side_menu_items(self):
        self.wait.until(EC.presence_of_element_located(self.side_menu_items))
        items = self.driver.find_elements(*self.side_menu_items)
        print(items)
        return items