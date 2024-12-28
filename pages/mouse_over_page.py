import allure

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class MouseOverPage(BasePage):

    PAGE_URL = Links.MOUSE_OVER_PAGE

    HOVER_LINKED_BUTTON = (By.XPATH, "//a[@onmouseenter='linkButtonActive(this)']")
    OVER_LINKED_BUTTON = (By.XPATH, "//a[@onclick='linkButtonClicked(this)']")
    CLICKED_NUM_COUNT = (By.XPATH, "//span[@id='clickButtonCount']")

    @allure.step("Навестись на кнопку 'Click me'")
    def hover_over_button(self):
        button = self.be_clickable(*self.HOVER_LINKED_BUTTON)
        AC(self.driver).move_to_element(button).perform()

    @allure.step("Двойное нажатие на кнопку 'Click me'")
    def double_click_button(self):
        button = self.be_clickable(*self.OVER_LINKED_BUTTON)
        AC(self.driver).double_click(button).perform()

    @allure.step("Кнопка была нажата два раза")
    def verify_double_click(self):
        count_element = self.find_the_element(*self.CLICKED_NUM_COUNT)
        count_text = count_element.text
        assert count_text == "2", f"Ожидали '2', но получили '{count_text}'"
