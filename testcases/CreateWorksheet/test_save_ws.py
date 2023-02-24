import time

import pytest

from pages.HomePage import HomePage
from testcases.test_base import BaseTest
from Utilities.customLog import LogGen

class TestSaveWs(BaseTest):
    logger = LogGen.loggen()

    def test_save_worksheet_after_upload(self):
        try:
            self.home_page = HomePage(self.driver)
            self.home_page.login()
            assert self.home_page.is_page_loaded()
            self.logger.info("********* Open home page ***********")
        except Exception as e:
            self.logger.error(f'{e}')
            pytest.fail("******** Test failed *********")

        self.create_ws_page = self.home_page.get_started()
        self.logger.info("******** Open create ws page **********")
        self.create_ws_page.switchTab(1)
        self.create_ws_page.upload_file()
        self.logger.info("********* File uploaded ********")
        self.create_ws_page.click_red_save_button()

        try:
            assert bool(self.create_ws_page.get_save_pop_up())
        except Exception:
            self.logger.error("******** Save pop up not found ********")
            pytest.fail("******** Test failed *********")

        self.create_ws_page.input_ws_name()
        self.logger.info("******* Fill save pop up ************")

        self.create_ws_page.click_blue_save_button()
        try:
            self.create_ws_page.get_shared_popup()
        except Exception:
            self.logger.error("********** Shared popup not found *******")
            pytest.fail("******** Test failed *********")
        self.logger.info("******* Test pass *******")


    def test_save_ws_template(self):
        home_page = HomePage(self.driver)
        self.logger.info("****** Homepage ********")
        home_page.login()
        self.logger.info("******** Login **********")

        self.create_ws_page = home_page.get_started()
        self.logger.info("*******  Create Ws Page **********")
        self.create_ws_page.switchTab(1)

        self.create_ws_page.pick_a_template()
        self.logger.info("****** Pick a template *******")

        self.create_ws_page.click_red_save_button()
        self.logger.info("********** Save ********")
        ##
        try:
            assert bool(self.create_ws_page.get_save_pop_up())
        except AssertionError:
            self.logger.error("******** Save pop up not found ********")
            pytest.fail("******** Test failed *********")

        self.create_ws_page.input_ws_name()
        self.logger.info("******* Fill pop up ********")

        self.create_ws_page.click_blue_save_button()
        self.logger.info("******* Save ******")
        # Test
        try:
            self.create_ws_page.get_shared_popup()
        except Exception:
            self.logger.error("********** Shared popup not found *******")
            pytest.fail("******** Test failed *********")
        self.logger.info("******* Test pass *******")
    def test_save_blank_ws(self):
        home_page = HomePage(self.driver)
        self.logger.info("******* HomePage *********")
        home_page.login()
        self.logger.info("******* Login ********")

        self.create_ws_page = home_page.get_started()
        self.logger.info("******* CreatePage ********")
        self.create_ws_page.switchTab(1)

        self.create_ws_page.click_red_save_button()
        self.logger.info("******** Save ********")
        try:
            assert bool(self.create_ws_page.get_the_message_bar())
        except Exception:
            self.logger.error("Upload or select template Message ")
            pytest.fail("******** Test failed *******")
        self.logger.info("*******Test pass ********")














