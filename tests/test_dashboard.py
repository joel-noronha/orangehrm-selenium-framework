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

def test_profile_dropdown_visible(driver):
    login_page = LoginPage(driver)
    login_page.load()
    dashboard = login_page.login("Admin", "admin123")
    assert dashboard.get_dashboard_profiledropdown()

def test_dashboard_sidemenu(driver):
    login_page = LoginPage(driver)
    login_page.load()
    dashboard = login_page.login("Admin", "admin123")
    assert len(dashboard.get_side_menu_items()) > 0