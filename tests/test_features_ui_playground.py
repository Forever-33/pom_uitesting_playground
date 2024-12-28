import time

import allure
from base.base_test import BaseTest


@allure.feature('feature_ui_playground')
class TestFeaturesUiPlayground(BaseTest):

    @allure.title("Client Side Delay")
    @allure.severity("Minor")
    def test_client_side_delay_page(self):
        self.client_side_delay_page.open()
        self.client_side_delay_page.is_opened()
        self.client_side_delay_page.click_triggering_client_button()
        self.client_side_delay_page.data_success()
        self.client_side_delay_page.do_screenshot("Пройден")

    @allure.title("Mouse Over")
    @allure.severity("Minor")
    def test_mouse_page(self):
        self.mouse_over_page.open()
        self.mouse_over_page.is_opened()
        self.mouse_over_page.hover_over_button()
        self.mouse_over_page.double_click_button()
        self.mouse_over_page.verify_double_click()
        self.mouse_over_page.do_screenshot("Пройден")

    @allure.title("Progress Bar 75%")
    @allure.severity("Minor")
    def test_progress_bar(self):
        self.progress_bar_page.open()
        self.progress_bar_page.is_opened()
        self.progress_bar_page.click_button_start()
        self.progress_bar_page.get_progress_bar_value()
        self.progress_bar_page.wait_for_progress_bar_to_reach_75()
        self.progress_bar_page.click_button_stop()
        self.progress_bar_page.do_screenshot("Пройден")

    @allure.title("AJAX data")
    @allure.severity("Minor")
    def test_ajax_data(self):
        self.ajax_data_page.open()
        self.ajax_data_page.is_opened()
        self.ajax_data_page.click_triggering_ajax_button()
        self.ajax_data_page.data_success()
        self.ajax_data_page.click_loaded_data()
        self.ajax_data_page.do_screenshot("Пройден")

    @allure.title("Shadow DOM")
    @allure.severity("Major")
    def test_shadow_dom(self):
        self.shadow_dom_page.open()
        self.shadow_dom_page.is_opened()
        self.shadow_dom_page.click_button_generate()
        self.shadow_dom_page.click_button_copy()
        self.shadow_dom_page.get_clipboard_value()
        self.shadow_dom_page.assert_clipboard_value()
        self.shadow_dom_page.do_screenshot("Пройден")




