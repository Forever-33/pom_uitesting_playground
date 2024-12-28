import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function", autouse=True, params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920x1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.instance.driver
        if driver:
            allure.attach(
                name='Скриншот',
                body=driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
        else:
            print(f"Driver not found in test {node.name}")


"""
ФИКСТУРА ТОЛЬКО ДЛЯ CHROME
"""

# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--window-size=1920x1080")
#     driver = webdriver.Chrome(options=options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()

"""
ХУК ДЛЯ ЗАПУСКА СКРИПТА УПАВШИХ С ПОСЛЕДНЕГО ПРОГОНА ТЕСТОВ
"""

# def pytest_sessionfinish(exitstatus):
#     if exitstatus != 0:
#         print("Некоторые тесты не прошли, запускаем скрипт упавших с последнего прогона тестов...")
#         command = [
#             "python", "run_failed_tests.py"
#         ]
#         try:
#             subprocess.run(command, check=True)
#             print("Повторное выполнение тестов завершено.")
#         except subprocess.CalledProcessError as e:
#             print(f"Ошибка при запуске повторных тестов: {e}")

