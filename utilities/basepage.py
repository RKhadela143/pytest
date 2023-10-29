from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

 
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Description: To get element text
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    # Description: To enter value to field
    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Description: To click button
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # Description: To clear value from field
    def clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).clear()

    # Description: To check visibility of element
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_all_visible(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))

    # Description: To switch frame
    def do_switch_frame(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(by_locator))

    # Description: To perform hover over on element
    def do_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ActionChains(self.driver).move_to_element(element).perform()

    # Description: To press down arrow key
    def press_down(self, by_locator, num_of_click):
        element = WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(by_locator)))
        for i in range(num_of_click):
            element.send_keys(Keys.ARROW_DOWN)
        element.click()

    # Description: To move to particular element
    def move_to_element_click(self, by_locator):
        element = ActionChains(self.driver).move_to_element(WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(by_locator))))
        element.click().perform()

    # Description: To press ENTER key
    def press_enter(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)
