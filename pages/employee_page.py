from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.pim_header_text = (By.XPATH,"//h6[text()='PIM']")

    def click_on_pim_menu(self):
        self.wait.until(EC.element_to_be_clickable((self.pim_menu))).click()

    def is_page_loaded(self):
        self.wait.until(EC.presence_of_element_located((self.pim_header_text)))
        header_text = self.driver.find_element(*self.pim_header_text).text
        print(header_text)
        return header_text