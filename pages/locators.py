from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")