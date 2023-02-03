from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import TestData
from Utilities.customLog import LogGen
from pages.BasePage import BasePage


class CreateWorksheetPage(BasePage):
    # Locators
    EDIT_WORKSHEET_BUTTON = (By.CSS_SELECTOR, "div.list-action-button > div:nth-child(1)")
    MAKE_INTERACTIVE_BUTTON = (By.CSS_SELECTOR, "div.list-action-button > div:nth-child(2)")
    TRY_IT_OUT_BUTTON = (By.CSS_SELECTOR, "div.list-action-button > div:nth-child(3)")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.INPUT_GAME_URL)

    def click_make_interactive_button(self):
        self.do_lick(self.MAKE_INTERACTIVE_BUTTON)


