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