from pageobjects.loginpage_locator import LoginpageLocator
from pages.dashboard import Dashboard
from utilities.basepage import BasePage
from testdata.constant import Constant

# @author SPEC INDIA
class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Constant.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Description: Login to account
    # @param username and password
    def do_login(self, username, password):
        self.clear(LoginpageLocator.username)
        self.send_keys(LoginpageLocator.username, username)
        self.clear(LoginpageLocator.password)
        self.send_keys(LoginpageLocator.password, password)
        self.click(LoginpageLocator.submit_button)
        return Dashboard(self.driver)

    # Description: Invalid login attempt error message
    def get_error_message(self):
        return self.get_element_text(LoginpageLocator.loginpage_message)