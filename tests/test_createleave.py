import pytest
from pages.loginpage import LoginPage
from testdata.constant import Constant
from utilities.baseclass import BaseClass
from utilities.readdata import readdata

 
class TestCreateLeave(BaseClass):

    # Description: Create leave scenario

    @pytest.mark.sanity
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username, password", readdata("test_leave", Constant.BOOK_PATH))
    def test_createleave(self, username, password):

        loginpage = LoginPage(self.driver)
        dashboard = loginpage.do_login(username, password)
        myrequest = dashboard.open_myrequest()
        myrequest.open_apply_leave_window()
        dashboard.get_logout()

