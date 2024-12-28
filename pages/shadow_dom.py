import time

import allure
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ShadowDomPage(BasePage):

    PAGE_URL = Links.SHADOW_DOM_PAGE

    BUTTON_GENERATE = (By.CSS_SELECTOR, "#buttonGenerate")
    BUTTON_COPY = (By.CSS_SELECTOR, "#buttonCopy")
    INPUT_EDIT_FIELD = (By.CSS_SELECTOR, "#editField")
    SHADOW_HOST = (By.CSS_SELECTOR, ".container guid-generator")

    @allure.step("Нажать на кнопку генерации Shadow DOM и Получить значение из поля ввода")
    def click_button_generate(self):
        shadow_host = self.find_the_element(*self.SHADOW_HOST)
        shadow_root = shadow_host.shadow_root
        button_generate = shadow_root.find_element(*self.BUTTON_GENERATE)
        shadow_input = shadow_root.find_element(*self.INPUT_EDIT_FIELD)
        button_generate.click()
        self.wait.until(EC.visibility_of(shadow_input))
        return shadow_input.get_property('value')

    @allure.step("Нажать на кнопку генерации 'Скопировать'")
    def click_button_copy(self):
        shadow_host = self.find_the_element(*self.SHADOW_HOST)
        shadow_root = shadow_host.shadow_root
        button_copy = shadow_root.find_element(*self.BUTTON_COPY)
        button_copy.click()

    @allure.step("Получить значение из буфера обмена")
    def get_clipboard_value(self):
        shadow_root = self.find_the_element(*self.SHADOW_HOST).shadow_root
        input_field = shadow_root.find_element(*self.INPUT_EDIT_FIELD)
        time.sleep(1)
        input_field.clear()
        time.sleep(1)
        input_field.click()
        time.sleep(1)
        input_field.send_keys(Keys.COMMAND + "v")
        time.sleep(1)
        return input_field.get_property('value')

    @allure.step("Сравнить значения из буфера обмена и поля ввода")
    def assert_clipboard_value(self):
        input_value = self.click_button_generate()
        clipboard_value = self.get_clipboard_value()
        print(f"Сравниваем значения: {input_value} и {clipboard_value}")
        assert input_value != clipboard_value, f"Значения совпадают: {input_value} != {clipboard_value}"
