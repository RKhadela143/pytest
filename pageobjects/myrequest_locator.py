from selenium.webdriver.common.by import By
from testdata.constant import Constant

# @author SPEC INDIA
# Description: My request screen locators

class MyrequestLocator:
    add_leave_button = (By.ID, 'createAddLeave')
    leave_category = (By.XPATH, '//body/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/span[1]/span[1]/span[2]/span[1]')
    personal_leave = (By.XPATH, "//li[contains(text(),'Personal Leave')]")
    leave_type = (By.XPATH, '//body/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[3]/span[1]/span[1]/span[2]')
    full_day = (By.XPATH, "//li[contains(text(),'Full Day')]")
    leave_status = (By.XPATH, '//body/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[2]/span[1]/span[1]/input[1]')
    request_status = (By.ID, "247a177c-3b74-438d-81ec-95aeb6316840")

    start_date_input = (By.XPATH, '//body/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/span[1]/span[1]/input[1]')
    start_date = (By.XPATH, "//body/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[2]/span[1]/span[1]/span[1]")
    start_month_year = (By.XPATH, '//body/div[18]/div[1]/div[1]/div[1]/a[2]')
    calender = (By.ID, 'f5829533-4b10-48f2-aeb7-4b51597c136b')
    start_date_next = (By.XPATH, '//body[1]/div[18]/div[1]/div[1]/div[1]/a[3]/span[1]')
    leave_date = (By.XPATH, '//tbody/tr[1]/td[1]/a[1]')
    select_start_date = (By.LINK_TEXT, Constant.START_DATE.split()[0])

    end_date_input = (By.XPATH, '//body/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[3]/span[1]/span[1]/input[1]')
    end_date = (By.XPATH, '//body/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[3]/span[1]/span[1]/span[1]')
    end_month_year = (By.XPATH, '//body/div[19]/div[1]/div[1]/div[1]/a[2]')
    end_date_next = (By.XPATH, '//body/div[19]/div[1]/div[1]/div[1]/a[3]/span[1]')
    select_end_date = (By.LINK_TEXT, Constant.END_DATE.split()[0])

    leave_validation = (By.CLASS_NAME, 'ng-binding')

    leave_reason_input = (By.XPATH, '//body/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/textarea[1]')
    save_button = (By.XPATH, '//body[1]/div[2]/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/div[1]/button[1]')
    yes_button = (By.XPATH, "//button[contains(text(),'Yes')]")

    success_message = (By.CLASS_NAME, 'notificationText')
