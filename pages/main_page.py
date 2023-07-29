from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        self.button_click(MainPageLocators.LOGIN_LINK)
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
