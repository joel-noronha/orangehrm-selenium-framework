from pages.login_page import LoginPage


def test_dashboard_loads(driver):
    login_page = LoginPage(driver)
    login_page.load()
    dashboard = login_page.login("Admin", "admin123")
    assert dashboard.is_dasboard_loaded()

def test_dashboard_url_check(driver):
    login_page = LoginPage(driver)
    login_page.load()
    dashboard = login_page.login("Admin", "admin123")
    assert "dashboard" in dashboard.get_current_url().lower()