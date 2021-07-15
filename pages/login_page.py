from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Current page url is not login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME)
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)

    def register_new_user(self, email, password):
        email_address = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_address.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()


