from selenium.webdriver.common.by import By

 
# Description: Dashboard screen locators

class DashboardLocator:
    dashboard = (By.ID, 'childMenu')
    logout_dropdown = (By.CLASS_NAME, 'role_caret')
    logout_button = (By.ID, 'logout')
    menu = (By.CLASS_NAME, 'cd-dropdown-trigger')
    mydesk = (By.CLASS_NAME, 'nav_My_Desk')
    myrequest = (By.LINK_TEXT, 'My Request')
    myapproval = (By.LINK_TEXT, 'My Approval')