# tests/tc002_correct_user.py
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config.config import TestData

class TestLoginUser:
    def test_login_with_correct_credentials(self, driver):
        """
        Test Case 2: Login User with correct email and password
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email address and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        """
        # Initialize pages
        home_page = HomePage(driver)
        login_page = LoginPage(driver)
        
        # Navigate to website
        driver.get(TestData.BASE_URL)
        
        # Verify home page is visible
        assert home_page.is_home_page_visible(), "Home page is not visible"
        
        # Click on Signup/Login button
        home_page.click_signup_login()
        
        # Verify 'Login to your account' is visible
        assert login_page.verify_login_heading(), "Login heading is not visible"
        
        # Enter correct email and password and click login
        login_page.login(TestData.TEST_USER_EMAIL, TestData.TEST_USER_PASSWORD)
        
        # Verify logged in as username is visible
        assert home_page.is_visible(*home_page.LOGGED_IN_USERNAME), \
    f"'Logged in as {TestData.TEST_USER_NAME}' message not visible"