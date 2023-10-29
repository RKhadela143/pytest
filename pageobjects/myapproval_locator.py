from selenium.webdriver.common.by import By

 
# Description: My approval screen locators

class MyapprovalLocator:
    leave_button = (By.ID, 'hyper_LeaveApproval')
    approve_buttons = (By.CLASS_NAME, 'fa-check')
    approve_success_message = (By.CLASS_NAME, 'notificationText')
