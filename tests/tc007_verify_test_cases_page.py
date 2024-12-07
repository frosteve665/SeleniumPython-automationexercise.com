# tests/tc007_verify_test_cases_page.py
import pytest
from pages.home_page import HomePage
from pages.test_cases_page import CasesPage
from config.config import TestData

class TestVerifyTestCasesPage:
    def test_verify_test_cases_page(self, driver):
        """
        Test Case 7: Verify Test Cases Page
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Test Cases' button
        5. Verify user is navigated to test cases page successfully
        """
        home_page = HomePage(driver)
        cases_page = CasesPage(driver)
        
        driver.get(TestData.BASE_URL)
        assert home_page.is_home_page_visible()
        
        home_page.click_test_cases()
        assert cases_page.is_test_cases_page_visible()