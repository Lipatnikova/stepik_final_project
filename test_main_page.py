from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.click_button_see_basket()
        page_basket = BasketPage(browser, browser.current_url)
        page_basket.is_basket_empty()
        page_basket.message_basket_is_empty_is_present()
        page_basket.message_basket_is_empty_text_en()

    def test_guest_cant_see_product_items_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.click_button_see_basket()
        page_basket = BasketPage(browser, browser.current_url)
        page_basket.items_in_basket_is_not_present()
