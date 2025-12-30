import os
import sys

from pages.dashboard_page import DashboardPage

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #Locators
    UserName = (By.CSS_SELECTOR, "input[name='username']")
    Password = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.XPATH,"//button[@type='submit']")
    Error_message = (By.XPATH,"//p[contains(@class, 'oxd-alert-content-text')]")
    Required_message = (By.XPATH,"//span[text()='Required']")


    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self,username,password):
        self.wait.until(EC.visibility_of_element_located(self.UserName)).send_keys(username)
        self.driver.find_element(*self.Password).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        dashboard = DashboardPage(self.driver)
        return dashboard

    def error_message(self):
        return self.wait.until(EC.presence_of_element_located(self.Error_message)).text

    def get_required_field(self):
        return self.driver.find_elements(*self.Required_message)

    def is_password_masked(self):
        password = self.wait.until(EC.presence_of_element_located(self.Password))
        return password.get_attribute("type") == "password"

    def get_title(self):
        return self.driver.title
