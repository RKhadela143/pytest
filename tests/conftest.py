from datetime import datetime
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from testdata.constant import Constant
from utilities.readdata import readbrowser

driver = None

# @author SPEC INDIA
# Description: Fixture file setup and tear down method
@pytest.fixture(params=readbrowser("test_browser", Constant.BOOK_PATH), scope="class")
def setup(request):

    global driver

    if request.param == "chrome":
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    if request.param == "firefox":
        s = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    if request.param == "edge":
        s = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=s)

    request.cls.driver = driver
    yield
    driver.close()

# Description: To get screenshot on tests fail
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f'{item.nodeid}_{datetime.today().strftime("%Y-%m-%d")}'.replace("/", "_").replace("::", "_") + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png" _%H:%M
            filedir = "../screenshots/" + file_name
            driver.get_screenshot_as_file(filedir)
            _capture_screenshot(filedir)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '  'onclick="window.open(this.src)" align="right"/></div>' %file_name

                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(name):
    driver.save_screenshot(name)