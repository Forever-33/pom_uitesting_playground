import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.shadowroot import ShadowRoot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1)

    """
    Открыть страницу
    """
    def open(self):
        with allure.step(f'Открыть страницу {self.PAGE_URL}'):
            self.driver.get(self.PAGE_URL)

    """
    Проверить, что страница открыта
    """
    def is_opened(self):
        with allure.step(f'Страница {self.PAGE_URL} открыта'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    """
    Сделать скриншот
    """
    def do_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    """
    Элемент предназначен для нажатия
    """
    def be_clickable(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable((by, value)),
                               message=f'Элемент {by, value} не найден')

    """
    Проверить, что элемент есть
    """
    def find_the_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    """
    Проверить, что элементы есть
    """
    def find_the_elements(self, by: By or int, value: str) -> [WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located((by, value)),
                               message=f'Элементы {by, value} не найдены')

    """
    Проверить, что элемента нет
    """
    def element_is_invisible(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(EC.invisibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')


