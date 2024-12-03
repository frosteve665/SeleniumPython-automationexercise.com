import pytest
import os
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from config.config import TestData

class TestContactUs:
    def test_contact_us_form(self, driver):
        """
        Test Case 6: Contact Us Form
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Contact Us' button
        5. Verify 'GET IN TOUCH' is visible
        6. Enter name, email, subject and message
        7. Upload file
        8. Click 'Submit' button
        9. Click OK button
        10. Verify success message 'Success! Your details have been submitted successfully.' is visible
        11. Click 'Home' button and verify that landed to home page successfully
        """
         # Initialize pages
        home_page = HomePage(driver)
        
        # Navigate to website
        driver.get(TestData.BASE_URL)

        # Verify home page is visible
        assert home_page.is_home_page_visible(), "Home page is not visible"

        # Click on Contact Us button
        home_page.click_contact_us()
        
        # Initialize contact page
        contact_page = ContactPage(driver)
        
        # Click Contact Us and verify heading
        home_page.click_contact_us()
        assert contact_page.verify_contact_heading(), "Contact heading not visible"

        # Fill contact form with test data
        contact_page.fill_contact_form(
            name=TestData.TEST_USER_NAME,
            email=TestData.TEST_USER_EMAIL,
            subject="Test Contact",
            message="This is a test message"
        )
        
        # Upload test file
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                 "utilities", 
                                 "Image.png")
        contact_page.upload_file(image_path)
        
        # Submit form and handle alert
        contact_page.submit_form()
        alert = driver.switch_to.alert
        alert.accept()
        
        # Verify success message
        assert contact_page.verify_success_message(), "Success message not visible"
        
        # Return to home page
        contact_page.click_home()
        assert home_page.is_home_page_visible(), "Home page not visible after return"
