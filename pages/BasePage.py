from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def is_page_loaded(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )
        return bool(element)

    def do_lick(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element.click()

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return bool(element)

    def escape(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE)
        actions.perform()

    def get_location(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.location

    def is_correct_location(self, location, actual_location):
        tolerance = 20
        if actual_location['x'] - tolerance <= location['x'] <= actual_location['x'] + tolerance and actual_location['y'] - tolerance <= location['y'] <= actual_location['y'] + tolerance:
            return True
        else:
            return False

    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def drag_to_location(self, element, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x, y).perform()












