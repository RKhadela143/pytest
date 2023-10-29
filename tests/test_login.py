import pytest
from pageobjects.dashboard_locator import DashboardLocator
from pages.loginpage import LoginPage
from testdata.constant import Constant
from utilities.readdata import readdata
from utilities.baseclass import BaseClass

 
class TestLogin(BaseClass):

    # Description: Invalid login credentials scenarios

    @pytest.mark.parametrize("username1, password1", readdata("test_login", Constant.BOOK_PATH))
    def test_invalid_login(self, username1, password1):

        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(username1, password1)

        msg = self.loginpage.get_error_message()
        assert msg == Constant.LOGINPAGE_MESSAGE

    # Description: Valid login credentials scenario

    @pytest.mark.parametrize("username2, password2", readdata("test_leave", Constant.BOOK_PATH))
    def test_valid_login(self, username2, password2):

        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(username2, password2)

        msg = homepage.get_element_text(DashboardLocator.dashboard)
        assert msg == "Dashboard"

        homepage.get_logout()