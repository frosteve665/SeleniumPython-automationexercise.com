# tests/test_login.py
import pytest
from pages.home_page import HomePage
from pages.signup_page import SignupPage
import random

class TestUserRegistration:
    @pytest.fixture
    def random_email(self):
        return f"test{random.randint(1000,9999)}@test.com"
    
    def test_register_user(self, driver, random_email):
        """
        Test Case 1: Register User
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Signup / Login' button
        5. Verify 'New User Signup!' is visible
        6. Enter name and email address
        7. Click 'Signup' button
        8. Fill account details
        9. Click 'Create Account' button
        10. Verify 'ACCOUNT CREATED!' is visible
        11. Click 'Continue' button
        """
        # Initialize pages
        home_page = HomePage(driver)
        signup_page = SignupPage(driver)
        
        # Navigate to website
        driver.get("https://automationexercise.com")
        
        # Click signup/login
        home_page.click_signup_login()
        
        # Fill signup details
        signup_page.enter_signup_details("Test User", random_email)
        
        # Fill account information
        signup_page.fill_account_details("password123")
        
        # Fill address information
        signup_page.fill_address_details(
            first_name="Test",
            last_name="User",
            address="123 Test St",
            country="United States",
            state="Test State",
            city="Test City",
            zipcode="12345",
            mobile="1234567890"
        )
        
        # Verify account created
        assert signup_page.is_visible(*signup_page.ACCOUNT_CREATED_MESSAGE)
        
        # Click continue
        signup_page.click(*signup_page.CONTINUE_BUTTON)