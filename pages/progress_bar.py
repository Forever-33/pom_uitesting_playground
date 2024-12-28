import allure

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProgressBarPage(BasePage):

    PAGE_URL = Links.PROGRESS_BAR_PAGE

    BUTTON_START = (By.XPATH, "//button[@id='startButton']")
    BUTTON_STOP = (By.XPATH, "//button[@id='stopButton']")
    PROGRESS_BAR = (By.XPATH, "//div[@id='progressBar']")

    PROGRESS_ATTRIBUTE = "aria-valuenow"
    TARGET_VALUE = 75

    @allure.step("Нажать на кнопку 'Start'")
    def click_button_start(self):
        self.be_clickable(*self.BUTTON_START).click()

    @allure.step("Нажать на кнопку 'Stop'")
    def click_button_stop(self):
        self.be_clickable(*self.BUTTON_STOP).click()

    @allure.step("Получить текущее значение индикатора выполнения")
    def get_progress_bar_value(self):
        progress_bar = self.wait.until(EC.presence_of_element_located(self.PROGRESS_BAR))
        return int(progress_bar.get_attribute(self.PROGRESS_ATTRIBUTE))

    @allure.step("Ждать, пока индикатор выполнения достигнет 75%")
    def wait_for_progress_bar_to_reach_75(self):
        self.wait.until(
            lambda driver: self.get_progress_bar_value() >= self.TARGET_VALUE
        )

