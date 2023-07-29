from .base_page import BasePage
from .locators import MainPageLocators as locator


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def click_button_see_basket(self):
        self.button_click(locator.BUTTON_SEE_BASKET)
