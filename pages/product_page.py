from .base_page import BasePage
from .locators import ProductPageLocators as locator


class ProductPage(BasePage):

    def click_button_add_to_basket(self):
        self.browser.find_element(*locator.BUTTON_ADD_TO_BASKET).click()

    def should_be_message_about_adding(self):
        self.should_be_message_about_adding_is_present()
        self.should_be_message_about_adding_correct_text()

    def should_be_message_about_adding_is_present(self):
        assert self.is_element_present(*locator.MESSAGE_SUCCESS), \
            "The success message is not presented."

    def should_be_message_about_adding_correct_text(self):
        actual_result = self.browser.find_element(*locator.MESSAGE_SUCCESS).text
        expected_result = self.browser.find_element(*locator.PRODUCT_NAME).text
        assert expected_result in actual_result, \
            "The success message contains the name of the product name"

    def should_be_message_about_adding_with_price(self):
        self.should_be_message_about_adding_with_price_is_present()
        self.should_be_message_about_adding_with_price_text()

    def should_be_message_about_adding_with_price_is_present(self):
        assert self.is_element_present(*locator.MESSAGE_SUCCESS_PRICE_BASKET), \
            "The success message with price item is not presented."

    def should_be_message_about_adding_with_price_text(self):
        actual_result = self.browser.find_element(*locator.PRICE_IN_MESSAGE).text
        expected_result = self.browser.find_element(*locator.PRODUCT_PRICE).text
        assert actual_result == expected_result, \
            "The success message contains the product price"

