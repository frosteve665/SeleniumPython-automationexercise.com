from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class TestCasesPage(BasePage):
    #Locator  
    TEST_CASES_HEADING = (By.CSS_SELECTOR, ".title.text-center")

    def is_test_cases_page_visible(self):
        """Verify if Test Cases page is visible"""
        return self.is_visible(*self.TEST_CASES_HEADING)

class TestCasesPage(BasePage):
    #Locator  
    TEST_CASES_HEADING = (By.CSS_SELECTOR, ".title.text-center")

    def is_test_cases_page_visible(self):
        """Verify if Test Cases page is visible"""
        return self.is_visible(*self.TEST_CASES_HEADING)