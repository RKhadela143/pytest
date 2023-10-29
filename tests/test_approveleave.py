import pytest
from pages.loginpage import LoginPage
from testdata.constant import Constant
from utilities.baseclass import BaseClass
from utilities.readdata import readdata


 
class TestApproveLeave(BaseClass):

    # Description: Approve leave scenario

    @pytest.mark.sanity
    @pytest.mark.order(after="test_createleave.py::TestCreateLeave::test_createleave")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("username, password", readdata("test_leaveapprove", Constant.BOOK_PATH))
    def test_approveleave(self, username, password):

        loginpage = LoginPage(self.driver)
        dashboard = loginpage.do_login(username, password)
        myapproval = dashboard.open_myapproval()
        myapproval.approve_leave()
