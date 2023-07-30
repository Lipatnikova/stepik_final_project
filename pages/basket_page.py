from .base_page import BasePage
from .locators import BasketPageLocators as locator


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*locator.BASKET_ITEMS), \
            "Shopping cart must be empty"

    def is_basket_full(self):
        assert self.is_element_present(*locator.BASKET_ITEMS), \
            "Shopping cart must be full"

    def message_basket_is_empty_is_present(self):
        assert self.is_element_present(*locator.MESSAGE_BASKET_IS_EMPTY), \
            "The message basket is empty is not present"

    def message_basket_is_empty_text_en(self):
        assert self.get_element_text(locator.MESSAGE_BASKET_IS_EMPTY) == "Your basket is empty. Continue shopping", \
            "The message basket is empty contains invalid content"

    def item_in_basket_is_not_present(self):
        assert self.is_not_element_present(*locator.BASKET_ITEMS), \
            "The basket contains a item, but expected empty basket"

    def item_in_basket_is_present(self):
        assert self.is_element_present(*locator.BASKET_ITEMS), \
            "The basket does not contains a item"
