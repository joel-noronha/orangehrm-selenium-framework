from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.pim_header_text = (By.XPATH,"//h6[text()='PIM']")
        self.add_employee_button = (By.XPATH, "//a[text()='Add Employee']")
        self.first_name = (By.XPATH,"//input[@placeholder='First Name']")
        self.last_name = (By.NAME, "lastName")
        self.save_btn = (By.XPATH, "//button[@type='submit']")
        self.employee_id = (By.XPATH,"//label[text()= 'Employee Id']/../following-sibling::div/input")
        self.personal_details_header = (By.XPATH, "//h6[text()='Personal Details']")

    def click_on_pim_menu(self):
        self.wait.until(EC.element_to_be_clickable((self.pim_menu))).click()

    def is_page_loaded(self):
        self.wait.until(EC.presence_of_element_located((self.pim_header_text)))
        header_text = self.driver.find_element(*self.pim_header_text).text
        print(header_text)
        return header_text

    def click_add_employee(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_employee_button)
        ).click()

    def get_employee_id(self):
        emp_id = self.wait.until(
            EC.presence_of_element_located(self.employee_id)
        )
        return emp_id.get_attribute("value")

    def add_employee_mandatory(self, first_name, last_name):
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.save_btn).click()

    def is_employee_created(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.personal_details_header)
        ).is_displayed()