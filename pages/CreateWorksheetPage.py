import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Config.config import TestData
from pages.BasePage import BasePage


class CreateWorksheetPage(BasePage):
    # Locators
    EDIT_WORKSHEET_BUTTON = (By.CSS_SELECTOR, "div.list-action-button > div:nth-child(1)")
    MAKE_INTERACTIVE_BUTTON = (By.CSS_SELECTOR, "div.list-action-button > div:nth-child(2)")
    TRY_IT_OUT_BUTTON = (By.CSS_SELECTOR, "div.list-action-button > div:nth-child(3)")
    RED_SAVE_BUTTON = ((By.CSS_SELECTOR, "div.list-action-button > div:nth-child(4)"))
    UPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, "div.canvas-pages > div:nth-child(2) > div > label > input[type=file]")

    EXAMPLE_TEMPLATE = (By.CSS_SELECTOR, ".template-resource-item:nth-child(1)")
    MESSAGE_BAR = (By.CSS_SELECTOR, "#app > div.MuiSnackbar-root.MuiSnackbar-anchorOriginBottomCenter.css-1ozswge")


    # SAVE_POPUP_CONTAINER
    WS_NAME = (By.CSS_SELECTOR, "input#ws-name")
    BLUE_SAVE_BUTTON = (By.CSS_SELECTOR, ".save-btn")

    SHARE_POPUP_CONTAINER = (By.CSS_SELECTOR, ".shared-popup-container")

    # # Login
    USER = (By.CSS_SELECTOR, ".user")

    def __init__(self, driver):
        super().__init__(driver)
        self.open_browser()

    def open_browser(self):
        self.driver.get(TestData.CREATE_WORKSHEET_URL)

    def click_make_interactive_button(self):
        self.do_lick(self.MAKE_INTERACTIVE_BUTTON)

    def upload_file(self):
        upload_button = self.driver.find_element(*self.UPLOAD_IMAGE_BUTTON)
        upload_button.send_keys(TestData.PATH_TO_TEST_FILE)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".switch-button-eraser"))
        )

    def get_red_save_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.RED_SAVE_BUTTON)
        )

    def click_red_save_button(self):
        self.get_red_save_button().click()

    def input_ws_name(self):
        name_input_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.WS_NAME)
        )
        name_input_box.send_keys("name")

    def click_blue_save_button(self):
        self.driver.find_element(*self.BLUE_SAVE_BUTTON).click()

    def pick_a_template(self):
        self.driver.find_element(*self.EXAMPLE_TEMPLATE).click()

    def get_the_message_bar(self):
        return self.driver.find_element(*self.MESSAGE_BAR)







