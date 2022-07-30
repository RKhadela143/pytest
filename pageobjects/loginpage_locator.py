from selenium.webdriver.common.by import By

# @author SPEC INDIA
# Description: Login screen locators

class LoginpageLocator:
    username = (By.ID, 'UserId')
    password = (By.ID, 'Password')
    submit_button = (By.ID, 'btnSubmit')
    loginpage_message = (By.CLASS_NAME, 'orderClass3')