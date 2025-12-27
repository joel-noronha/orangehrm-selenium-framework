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

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self,username,password):
        self.wait.until(EC.visibility_of_element_located(self.UserName)).send_keys(username)
        self.driver.find_element(*self.Password).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()