from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.json_utils import load_json
import os
import pytest
import pytest_html
from datetime import datetime

data = load_json("employee.json")
@pytest.fixture
def driver():
    options = Options()
    #options.add_argument('--headless')
    #options.add_argument("--window-size=1920,1080")
    #options.add_argument('--start-maximized')
    options.add_argument('--incognito')
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    #driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(params=data["employees"])
def employee_data(request):
    return request.param

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # 1️⃣ Physical save location
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"

            full_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(full_path)

            # 2️⃣ Path RELATIVE to report.html
            relative_path = os.path.join("screenshots", file_name)

            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(relative_path))
                report.extra = extra