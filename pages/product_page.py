from .base_page import BasePage
from .locators import ProductPageLocators as locator


class ProductPage(BasePage):

    def click_button_add_to_basket(self):
        self.button_click(locator.BUTTON_ADD_TO_BASKET)

    def should_be_message_about_adding(self):
        self.should_be_message_about_adding_is_present()
        self.should_be_message_about_adding_correct_text()

    def should_be_message_about_adding_is_present(self):
        assert self.is_element_present(*locator.MESSAGE_SUCCESS), \
            "The success message is not presented."

    def should_be_message_about_adding_correct_text(self):
        actual_result = self.get_element_text(locator.MESSAGE_SUCCESS)
        expected_result = self.get_element_text(locator.PRODUCT_NAME)
        assert expected_result in actual_result, \
            "The success message contains the name of the product name"

    def should_be_message_about_adding_with_price(self):
        self.should_be_message_about_adding_with_price_is_present()
        self.should_be_message_about_adding_with_price_text()

    def should_be_message_about_adding_with_price_is_present(self):
        assert self.is_element_present(*locator.MESSAGE_SUCCESS_PRICE_BASKET), \
            "The success message with price item is not presented."

    def should_be_message_about_adding_with_price_text(self):
        actual_result = self.get_element_text(locator.PRICE_IN_MESSAGE)
        expected_result = self.get_element_text(locator.PRODUCT_PRICE)
        assert actual_result == expected_result, \
            "The success message contains the product price"

