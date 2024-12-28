import pytest

from config.data import Data

from pages.client_side_delay_page import ClientSideDelayPage
from pages.mouse_over_page import MouseOverPage
from pages.progress_bar import ProgressBarPage
from pages.ajax_data_page import AjaxDataPage
from pages.shadow_dom import ShadowDomPage


class BaseTest:

    data: Data

    client_side_delay_page = ClientSideDelayPage
    mouse_over_page = MouseOverPage
    progress_bar_page = ProgressBarPage
    ajax_data_page = AjaxDataPage
    shadow_dom_page: ShadowDomPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.client_side_delay_page = ClientSideDelayPage(driver)
        request.cls.mouse_over_page = MouseOverPage(driver)
        request.cls.progress_bar_page = ProgressBarPage(driver)
        request.cls.ajax_data_page = AjaxDataPage(driver)
        request.cls.shadow_dom_page = ShadowDomPage(driver)
