# tests/tc003_incorrect_login_user.py
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config.config import TestData

class TestIncorrectLogin:
    def test_login_with_incorrect_credentials(self, driver):
        """
        Test Case 3: Login User with incorrect email and password
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'Login to your account' is visible
        6. Enter incorrect email address and password
        7. Click 'login' button
        8. Verify error 'Your email or password is incorrect!' is visible
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
        
        # Enter incorrect email and password
        login_page.login("wrong@email.com", "wrongpassword")
        
        # Verify error message is visible
        assert login_page.is_visible(*login_page.LOGIN_ERROR), \
            "Error message 'Your email or password is incorrect!' not visible"