from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_SEE_BASKET = (By.CSS_SELECTOR, ".hidden-xs > span > a")


class MainPageLocators:
    pass


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSAGE_SUCCESS_PRICE_BASKET = (By.CSS_SELECTOR, ".in > div > p:nth-child(1)")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".in > div > p:nth-child(1) > strong")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")