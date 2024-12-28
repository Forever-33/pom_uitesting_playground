import allure

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ClientSideDelayPage(BasePage):

    PAGE_URL = Links.CLIENT_SIDE_DELAY_PAGE

    BUTTON_TRIGGERING_CLIENT_SIDE_LOGIC = (By.XPATH, "//button[@id='ajaxButton']")
    LOADED_LABEL = (By.XPATH, "(//p[@class='bg-success'])[1]")
    SPINNER = (By.XPATH, "//i[@id='spinner']")

    @allure.step("Нажать на кнопку 'Button Triggering Client Side Logic'")
    def click_triggering_client_button(self):
        self.be_clickable(*self.BUTTON_TRIGGERING_CLIENT_SIDE_LOGIC).click()

    @allure.step("Появление данных на стороне клиента")
    def data_success(self):
        self.element_is_invisible(*self.SPINNER)
        self.find_the_element(*self.LOADED_LABEL)





