from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def tap_on_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_added_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        confirm_message = self.browser.find_element(*ProductPageLocators.CONFIRM_MESSAGE)
        assert product_name.text == confirm_message.text, "Product not found"

    def should_be_increased_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        confirm_price = self.browser.find_element(*ProductPageLocators.CONFIRM_PRICE)
        assert price.text == confirm_price.text, "Basket price was not changed"


    def should_not_be_success_message_after_adding_product(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_after_openning_page(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_not_be_success_message_after_some_time(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"