from pageobjects.dashboard_locator import DashboardLocator
from pages.myapproval import MyApproval
from pages.myrequest import MyRequest
from utilities.basepage import BasePage

 

class Dashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Description: Click on logout button
    def get_logout(self):
        self.click(DashboardLocator.logout_dropdown)
        self.click(DashboardLocator.logout_button)

    # Description: To open my request screen
    def open_myrequest(self):
        self.do_hover(DashboardLocator.menu)
        self.do_hover(DashboardLocator.mydesk)
        self.click(DashboardLocator.myrequest)
        return MyRequest(self.driver)

    # Description: To open my approval screen
    def open_myapproval(self):
        self.do_hover(DashboardLocator.menu)
        self.do_hover(DashboardLocator.mydesk)
        self.click(DashboardLocator.myapproval)
        return MyApproval(self.driver)
