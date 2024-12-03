# pages/login_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Locators
    # Login form elements
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-form")
    LOGIN_HEADING = (By.CSS_SELECTOR, ".login-form h2")
    LOGIN_ERROR = (By.CSS_SELECTOR, "p[style='color: red;']")

    # Signup form elements
    SIGNUP_HEADING = (By.XPATH, "//div[@class='signup-form']/h2")  # More specific selector
    SIGNUP_NAME = (By.NAME, "name")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='signup-password']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def verify_signup_heading(self):
        heading = self.get_text(*self.LOGIN_HEADING)
        return "New User Signup!" in heading

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

    def verify_signup_heading(self):
        heading = self.get_text(*self.SINGUP_HEADING)
        return "New User Signup!" in heading

    def signup(self, name, password):
        """Signup with email and password"""
        self.type_text(*self.SIGNUP_NAME, name)
        self.type_text(*self.SIGNUP_EMAIL, password)
        self.click(*self.SIGNUP_BUTTON)

