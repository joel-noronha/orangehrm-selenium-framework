from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_employee_page_loads(driver):
    login_page = LoginPage(driver)
    login_page.load()
    dashboard = login_page.login("Admin", "admin123")
    dashboard.is_dasboard_loaded()
    employee_page = EmployeePage(driver)
    employee_page.click_on_pim_menu()
    assert employee_page.is_page_loaded() == 'PIM'

def test_add_new_employee(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    employee_page = EmployeePage(driver)
    employee_page.click_on_pim_menu()
    employee_page.click_add_employee()
    empid = employee_page.get_employee_id()
    print(empid)
    employee_page.add_employee_mandatory('test123','emplast')
    assert employee_page.is_employee_created()



