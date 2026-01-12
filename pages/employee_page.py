from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
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
        self.save_btn = (By.XPATH, "(//button[@type='submit'])[1]")
        self.employee_id = (By.XPATH,"//label[text()= 'Employee Id']/../following-sibling::div/input")
        self.personal_details_header = (By.XPATH, "//h6[text()='Personal Details']")
        self.EDIT_FIRST_NAME = (By.CSS_SELECTOR, "input[placeholder='First Name']")
        self.EDIT_LAST_NAME = (By.NAME, "lastName")
        self.EDIT_SAVE_BTN = (
    By.XPATH,
    "//h6[text()='Personal Details']/parent::div//button[@type='submit']"
)


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

    FIRST_RESULT_EDIT = (
        By.XPATH,
        "(//div[@class='oxd-table-body']//div[@role='row'])[1]//button[last()]"
    )

    def open_first_employee(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FIRST_RESULT_EDIT)
        ).click()

    def click_edit_save(self):
        save_btn = self.wait.until(
            EC.presence_of_element_located(self.EDIT_SAVE_BTN)
        )

        # Scroll into view
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            save_btn
        )

        # Wait for UI to settle (overlay disappears)
        self.wait.until(
            lambda d: save_btn.is_displayed()
        )

        try:
            save_btn.click()
        except ElementClickInterceptedException:
            # Reliable fallback
            self.driver.execute_script(
                "arguments[0].click();",
                save_btn
            )



    def edit_employee_name(self, new_first, new_last):
        first = self.wait.until(
            EC.presence_of_element_located(self.EDIT_FIRST_NAME)
        )
        last = self.wait.until(
            EC.presence_of_element_located(self.EDIT_LAST_NAME)
        )

        # 2. Wait until existing values are loaded
        self.wait.until(lambda d: first.get_attribute("value") != "")
        self.wait.until(lambda d: last.get_attribute("value") != "")

        # 3. Proper clear (SPA-safe)
        first.send_keys(Keys.CONTROL, "a")
        first.send_keys(Keys.DELETE)
        first.send_keys(new_first)

        last.send_keys(Keys.CONTROL, "a")
        last.send_keys(Keys.DELETE)
        last.send_keys(new_last)

        # 4. Save
        self.click_edit_save()

    def get_first_name_value(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.EDIT_FIRST_NAME)
        ).get_attribute("value")

