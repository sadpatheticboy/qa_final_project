from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, f"Expected 'login' to be substring of {url!r}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_label = self.browser.find_element(*LoginPageLocators.EMAIL_LABEL)
        password_label = self.browser.find_element(*LoginPageLocators.PASSWORD_LABEL)
        same_password_label = self.browser.find_element(*LoginPageLocators.SAME_PASSWORD_LABEL)

        email_label.send_keys(email)
        password_label.send_keys(password)
        same_password_label.send_keys(password)

        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
