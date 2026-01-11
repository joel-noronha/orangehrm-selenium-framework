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

    def click_save(self):
        self.driver.find_element(*self.save_btn).click()

    def is_employee_created(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.personal_details_header)
        ).is_displayed()

    SUCCESS_TOAST_MESSAGE = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast')]//p[contains(@class,'oxd-text--toast-message')]"
    )

    def get_success_message(self):
        try:
            toast = self.wait.until(
                EC.visibility_of_element_located(self.SUCCESS_TOAST_MESSAGE)
            )
            return toast.text
        except TimeoutException:
            return None

    UPLOAD_PHOTO = (By.XPATH, "//input[@type='file']")
    middle_name = (By.CSS_SELECTOR, "input[placeholder='Middle Name']")
    Emp_ID = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    EMP_ID_SEARCH = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div/input")
    EMP_NAME_SEARCH = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BTN = (By.XPATH, "//button[.=' Search ']")
    RESULT_ROWS = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    NO_RECORDS = (By.XPATH, "//span[text()='No Records Found']")

    def upload_profile_picture(self, image_path):
        upload = self.wait.until(
            EC.presence_of_element_located(self.UPLOAD_PHOTO)
        )
        upload.send_keys(image_path)

    def add_additional_details(self, middle_name, emp_id):
        self.wait.until(
            EC.visibility_of_element_located(self.middle_name)
        ).send_keys(middle_name)

        self.driver.find_element(*self.Emp_ID).send_keys(emp_id)

    def search_by_id(self, emp_id):
        self.wait.until(
            EC.visibility_of_element_located(self.EMP_ID_SEARCH)
        ).send_keys(emp_id)
        self.driver.find_element(*self.SEARCH_BTN).click()

    def search_by_name(self, name):
        self.wait.until(
            EC.visibility_of_element_located(self.EMP_NAME_SEARCH)
        ).send_keys(name)
        self.driver.find_element(*self.SEARCH_BTN).click()

    def is_employee_in_results(self):
        rows = self.wait.until(
            EC.presence_of_all_elements_located(self.RESULT_ROWS)
        )
        return len(rows) > 0

    def is_no_records_found(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NO_RECORDS)
        ).is_displayed()
