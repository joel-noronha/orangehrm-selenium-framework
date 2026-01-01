from pages.login_page import LoginPage
from pages.logout import Logout


def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    logout = Logout(driver)
    logout.logout()
    assert "login" in driver.current_url.lower()

