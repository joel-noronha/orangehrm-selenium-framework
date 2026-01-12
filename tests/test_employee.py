import os


import pytest

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
    employee_page.click_save()
    assert employee_page.is_employee_created()


def test_add_employee_full_details(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")

    employee_page = EmployeePage(driver)
    employee_page.click_on_pim_menu()
    employee_page.click_add_employee()

    employee_page.add_employee_mandatory("Joel", "Doe")

    image_path = os.path.abspath("test_data/profile.jpg")
    employee_page.upload_profile_picture(image_path)

    employee_page.add_additional_details("Mid","6830")
    employee_page.click_save()
    assert employee_page.is_employee_created()

def test_search_employee_by_id(driver):
    login = LoginPage(driver)
    login.load()
    login.login("Admin", "admin123")

    employee = EmployeePage(driver)
    employee.click_on_pim_menu()

    employee.search_by_id("8705")
    assert employee.is_employee_in_results()


def test_search_employee_invalid(driver):
    login = LoginPage(driver)
    login.load()
    login.login("Admin", "admin123")

    employee = EmployeePage(driver)
    employee.click_on_pim_menu()

    employee.search_by_id("99999")
    assert employee.is_no_records_found()


@pytest.mark.smoke
def test_edit_employee_details(driver):
    login = LoginPage(driver)
    login.load()
    login.login("Admin", "admin123")

    employee = EmployeePage(driver)
    employee.click_on_pim_menu()

    # Assumes at least one employee exists
    #employee.search_by_name("kljsd")
    #assert employee.is_employee_in_results()

    # Open first employee
    employee.open_first_employee()

    employee.edit_employee_name("JoelUpdated", "DoeUpdated")
    assert employee.get_first_name_value() == "JoelUpdated"






