from pages.product_page import ProductPage


class TestProductPage:

    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.click_button_add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_about_adding_with_price()
