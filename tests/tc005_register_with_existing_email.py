# tests/tc005_register_with_existing_email.py
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from config.config import TestData

class TestExistingEmail:
    def test_register_with_existing_email(self, driver):
        """
        Test Case 5: Register User with existing email
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'New User Signup!' is visible
        6. Enter name and already registered email address
        7. Click 'Signup' button
        8. Verify error 'Email Address already exist!' is visible
        """
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
class TestExistingEmail:
    def test_register_with_existing_email(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Navigate and verify home page
        driver.get(TestData.BASE_URL)
        assert home_page.is_home_page_visible(), "Home page is not visible"
        
        # Click signup/login and verify signup form
        home_page.click_signup_login()
        assert login_page.is_visible(*login_page.SIGNUP_HEADING), "Signup heading not visible"
        
        # Try to register with existing email
        login_page.signup("Lucius Norris", TestData.TEST_USER_EMAIL)
        
        # Verify error message
        assert login_page.is_visible(*login_page.LOGIN_ERROR), \
            "Email already exists error message not visible"