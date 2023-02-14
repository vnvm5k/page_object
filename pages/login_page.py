from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        current_url = self.browser.current_url
        assert "login" in current_url, "it is not login link"


    def should_be_login_form(self):
    	assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        confirm_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_field.send_keys(password)
        register_button.click()