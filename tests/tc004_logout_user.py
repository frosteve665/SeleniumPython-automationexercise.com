# tests/tc004_logout_user.py
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config.config import TestData

class TestLogout:
    def test_user_logout(self, driver):
        """
        Test Case 4: Logout User
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter correct email and password
        7. Click 'login' button
        8. Verify that 'Logged in as username' is visible
        9. Click 'Logout' button
        10. Verify that user is navigated to login page
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
        
        # Enter correct email and password
        login_page.login(TestData.TEST_USER_EMAIL, TestData.TEST_USER_PASSWORD)
        
        # Verify logged in as username is visible
        assert home_page.is_visible(*home_page.LOGGED_IN_USERNAME), \
            f"'Logged in as {TestData.TEST_USER_NAME}' message not visible"
        
        # Click logout button
        home_page.click_logout()
        
        # Verify user is navigated to login page
        assert login_page.verify_login_heading(), "Not redirected to login page after logout"