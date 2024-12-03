# pages/login_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-form")
    LOGIN_HEADING = (By.CSS_SELECTOR, ".login-form h2")

    def is_login_form_visible(self):
        """Verify if login form is visible"""
        return self.is_visible(*self.LOGIN_FORM)

    def verify_login_heading(self):
        """Verify 'Login to your account' heading"""
        heading = self.get_text(*self.LOGIN_HEADING)
        return "Login to your account" in heading

    def login(self, email, password):
        """Login with email and password"""
        self.type_text(*self.LOGIN_EMAIL, email)
        self.type_text(*self.LOGIN_PASSWORD, password)
        self.click(*self.LOGIN_BUTTON)

    def verify_error_message(self):
        """Verify error message for invalid credentials"""
        error = self.get_text(*self.ERROR_MESSAGE)
        return "Your email or password is incorrect!" in error