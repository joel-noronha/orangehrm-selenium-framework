from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    assert "dashboard" in driver.current_url.lower()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin122")
    assert "Invalid credentials" in login_page.error_message()

def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("WrongUser", "admin123")
    assert "Invalid credentials" in login_page.error_message()


def test_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "")
    errors = login_page.get_required_field()
    print(errors)
    assert len(errors) == 2

def test_password_masked(driver):
    login_page = LoginPage(driver)
    login_page.load()
    assert login_page.is_password_masked()

def test_page_title(driver):
    login_page = LoginPage(driver)
    login_page.load()
    assert 'OrangeHRM' == login_page.get_title()



