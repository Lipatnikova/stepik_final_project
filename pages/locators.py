from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
