import time

import pytest

from pages.CreateWorksheetPage import CreateWorksheetPage
from pages.HomePage import HomePage
from testcases.test_base import BaseTest
from Utilities.customLog import LogGen


class TestCreateWs(BaseTest):
    logger = LogGen.loggen()

    def test_save_worksheet_after_upload(self):
        try:
            self.logger.info("*************")
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
            self.logger.error("***** Save pop up not found ********")
            pytest.fail("******** Test failed *********")

        self.create_ws_page.input_ws_name()
        self.logger.info("******* Fill save pop up **********")

        self.create_ws_page.click_blue_save_button()
        try:
            self.create_ws_page.get_shared_popup()
        except Exception:
            self.logger.error("********** Shared popup not found *******")
            pytest.fail("******** Test failed *********")
        self.logger.info("******* Test passed *******")

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

    def test_undo_redo(self):
        self.logger.info("********** Test 004, 005 *********")
        home_page = HomePage(self.driver)
        self.logger.info("********** Home Page*********")
        home_page.login()
        self.logger.info("********** Login *********")
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)

        self.create_ws_page.pick_a_template()
        self.logger.info("********** Pick a template *********")

        self.create_ws_page.undo_redo_btn("hover", "undo")
        self.create_ws_page.undo_redo_btn("click", "undo")
        self.logger.info("********** Undo *********")

        self.create_ws_page.undo_redo_btn("hover", "redo")
        self.create_ws_page.undo_redo_btn("click", "redo")
        self.logger.info("********** Redo *********")

    def test_zoom(self):
        home_page = HomePage(self.driver)
        home_page.login()
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)

        self.create_ws_page.change_ws_size(45)
        self.create_ws_page.change_ws_size(200)

    def test_feed_back_pop_up_1(self):
        self.logger.info("****** Test 008 ******")
        pytest.skip()
        home_page = HomePage(self.driver)
        # home_page.login()
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)

        time.sleep(15)

    def test_feed_back_pop_up_2(self):
        self.logger.info("****** Test 009 ******")
        pytest.skip()
        home_page = HomePage(self.driver)
        # home_page.login()
        self.create_ws_page = home_page.get_started()
        self.create_ws_page.switchTab(1)
        time.sleep(15)

    def test_add_page(self):
        home_page = HomePage(self.driver)
        preview_page = home_page.select_worksheet()
        create_ws_page = preview_page.click_customize_button()
        time.sleep(3)
        create_ws_page.switchTab(1)
        time.sleep(3)
        create_ws_page.add_page()
        time.sleep(3)

    def test_add_page_with_icon(self):
        home_page = HomePage(self.driver)
        preview_page = home_page.select_worksheet()
        create_ws_page = preview_page.click_customize_button()
        create_ws_page.switchTab(1)

        create_ws_page.add_page_with_icon()
        time.sleep(3)

    #      Test 018
    def test_duplicate_page(self):
        pass

    #   Test 019
    def test_move_up_down(self):
        pass

    #     Test 020
    def test_scroll_to_top(self):
        create_page = CreateWorksheetPage(self.driver)
        create_page.open_browser()
        create_page.scroll_to_bottom()
        time.sleep(5)
        create_page.click_scroll_to_top_button()
        time.sleep(5)




