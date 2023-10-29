import time
from selenium.webdriver.common.by import By
from pageobjects.myapproval_locator import MyapprovalLocator
from testdata.constant import Constant
from utilities.basepage import BasePage


 
class MyApproval(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Description: To approve leaves listed on screen
    def approve_leave(self):
        self.click(MyapprovalLocator.leave_button)
        self.is_all_visible(MyapprovalLocator.approve_buttons)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(MyapprovalLocator.approve_buttons))
        buttons = self.driver.find_elements(By.CLASS_NAME, 'fa-check')

        print(len(buttons))
        i = 0
        for i in range(len(buttons)):
            self.driver.find_element(By.CLASS_NAME, 'fa-check').click()
            time.sleep(2)
            i+=1

        print("Leave has been approved successfully")
        assert self.get_element_text(MyapprovalLocator.approve_success_message) == Constant.LEAVE_APPROVE_SUCCESS_MESSAGE

