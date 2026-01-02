from pages.employee_page import EmployeePage
from pages.login_page import LoginPage


def test_employee_page_loads(driver):
    login_page = LoginPage(driver)
    login_page.load()
    dashboard = login_page.login("Admin", "admin123")
    dashboard.is_dasboard_loaded()
    employee_page = EmployeePage(driver)
    employee_page.click_on_pim_menu()
    assert employee_page.is_page_loaded().lower() == 'PIM'
