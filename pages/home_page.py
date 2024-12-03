# pages/home_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage(BasePage):
    # Locators
    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    HOME_SLIDER = (By.ID, "slider")
    LOGGED_IN_USER = (By.CSS_SELECTOR, "a:not(.btn)[href='/logout']")
    
    def is_home_page_visible(self):
        """Verify home page is visible"""
        return self.is_visible(*self.HOME_SLIDER)

    def remove_ads(self):
        """Remove ads that might interfere with clicks"""
        try:
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            for iframe in iframes:
                self.driver.execute_script("""
                    var elem = arguments[0];
                    elem.parentNode.removeChild(elem);
                    """, iframe)
        except:
            pass

    def click_signup_login(self):
        """Click on Signup/Login link with retry mechanism"""
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                # Remove ads first
                self.remove_ads()
                
                # Wait and scroll to element
                element = self.wait.until(EC.element_to_be_clickable(self.SIGNUP_LOGIN_LINK))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(1)
                
                # Try clicking
                element.click()
                return
            except:
                if attempt == max_attempts - 1:
                    raise
                time.sleep(1)

    def is_user_logged_in(self, username):
        """Verify if user is logged in"""
        user_element = self.find_element(*self.LOGGED_IN_USER)
        return f"Logged in as {username}" in user_element.text