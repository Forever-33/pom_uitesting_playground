import allure

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AjaxDataPage(BasePage):

    PAGE_URL = Links.AJAX_DATA_PAGE

    BUTTON_TRIGGERING_AJAX_REQUEST = (By.XPATH, "//button[@id='ajaxButton']")
    LOADED_DATA_AJAX = (By.XPATH, "(//p[@class='bg-success'])[1]")
    SPINNER = (By.XPATH, "//i[@id='spinner']")

    @allure.step("Нажать на кнопку 'Button Triggering AJAX Request'")
    def click_triggering_ajax_button(self):
        self.be_clickable(*self.BUTTON_TRIGGERING_AJAX_REQUEST).click()

    @allure.step("Появление данных на стороне клиента")
    def data_success(self):
        self.element_is_invisible(*self.SPINNER)
        self.find_the_element(*self.LOADED_DATA_AJAX)

    @allure.step("Кликнуть на текст загруженного элемента")
    def click_loaded_data(self):
        self.be_clickable(*self.LOADED_DATA_AJAX).click()




