from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    CONFIRM_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_MAIN = (By.CSS_SELECTOR, "div.page_inner a.btn-default")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages")