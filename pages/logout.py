from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Logout:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.profile_dropdown = (By.CLASS_NAME,"oxd-userdropdown-name")
        self.logout_dropdown = (By.XPATH,"//a[text()='Logout']")

    def logout(self):
        self.wait.until(EC.visibility_of_element_located((self.profile_dropdown)))
        self.driver.find_element(*self.profile_dropdown).click()
        self.wait.until(EC.visibility_of_element_located((self.logout_dropdown)))
        self.driver.find_element(*self.logout_dropdown).click()
