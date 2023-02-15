import time

from pages.HomePage import HomePage
from testcases.test_base import BaseTest
from Utilities.customLog import LogGen

class TestSaveWs(BaseTest):
    logger = LogGen.loggen()

    def test_save_worksheet_after_upload(self):
        home_page = HomePage(self.driver)
        home_page.login()

        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)

        self.create_ws_page.upload_file()

        self.create_ws_page.click_red_save_button()

        self.create_ws_page.input_ws_name()

        self.create_ws_page.click_blue_save_button()


    def test_save_ws_template(self):
        home_page = HomePage(self.driver)
        home_page.login()
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)

        self.create_ws_page.pick_a_template()
        self.logger.info()
        self.create_ws_page.click_red_save_button()

        self.create_ws_page.input_ws_name()

        self.create_ws_page.click_blue_save_button()

    def test_save_blank_ws(self):
        home_page = HomePage(self.driver)
        home_page.login()
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)

        self.create_ws_page.click_red_save_button()

        assert bool(self.create_ws_page.get_the_message_bar())














