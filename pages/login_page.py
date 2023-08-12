from .base_page import BasePage
from .locators import LoginPageLocators as locator


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url is invalid."

    def should_be_login_form(self):
        assert self.is_element_present(*locator.FORM_LOGIN), "Form login is not presented on the page."

    def should_be_register_form(self):
        assert self.is_element_present(*locator.FORM_REGISTRATION), "Form registration is not presented on the page."

    def register_new_user(self, email, password):
        self.send_keys_to_input(locator.EMAIL, email)
        self.send_keys_to_input(locator.PASSWORD, password)
        self.send_keys_to_input(locator.CONFIRM_PASSWORD, password)
        self.button_click(locator.BUTTON_REGISTER)
