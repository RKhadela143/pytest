import time
from pageobjects.myrequest_locator import MyrequestLocator
from testdata.constant import Constant
from utilities.basepage import BasePage

 
class MyRequest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Description: Fill up leave request details and Submit
    def open_apply_leave_window(self):
        self.click(MyrequestLocator.add_leave_button)
        self.move_to_element_click(MyrequestLocator.leave_category)
        self.click(MyrequestLocator.personal_leave)
        self.move_to_element_click(MyrequestLocator.leave_type)
        self.click(MyrequestLocator.full_day)
        self.send_keys(MyrequestLocator.leave_status, "Request")

        self.select_start_date(Constant.START_DATE)
        self.select_end_date(Constant.END_DATE)
        if self.is_visible(MyrequestLocator.leave_validation):
            self.get_element_text(MyrequestLocator.leave_validation)

        self.send_keys(MyrequestLocator.leave_reason_input, Constant.REASON)
        self.click(MyrequestLocator.save_button)
        self.click(MyrequestLocator.yes_button)
        print("Leave applied successfully")
        assert self.get_element_text(MyrequestLocator.success_message) == Constant.LEAVE_SUCCESS_MESSAGE

    # Description: To select start date from leave request screen
    def select_start_date(self, date):
        self.click(MyrequestLocator.start_date_input)
        self.click(MyrequestLocator.start_date)
        x = self.get_element_text(MyrequestLocator.start_month_year)

        # readdata.read_date("date", Constant.BOOK_PATH)
        while x not in date:
            self.click(MyrequestLocator.start_date_next)
            x = self.get_element_text(MyrequestLocator.start_month_year)
            time.sleep(2)
            print(x)

        self.click(MyrequestLocator.select_start_date)
        time.sleep(2)

    # Description: To select end date from leave request screen
    def select_end_date(self, date):
        self.click(MyrequestLocator.end_date_input)
        self.click(MyrequestLocator.end_date)
        x = self.get_element_text(MyrequestLocator.end_month_year)

        while x not in date:
            self.click(MyrequestLocator.end_date_next)
            x = self.get_element_text(MyrequestLocator.end_month_year)
            time.sleep(2)

        self.click(MyrequestLocator.select_end_date)
        time.sleep(2)