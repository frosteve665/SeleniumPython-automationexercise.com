# pages/products_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class ProductsPage(BasePage):
    # Locators
    ALL_PRODUCTS_HEADING = (By.CSS_SELECTOR, ".title.text-center")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".features_items")
    FIRST_PRODUCT_VIEW = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, ".product-information p:nth-child(3)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-information span span")
    PRODUCT_AVAILABILITY = (By.CSS_SELECTOR, ".product-information p:nth-child(6)")
    PRODUCT_CONDITION = (By.CSS_SELECTOR, ".product-information p:nth-child(7)")
    PRODUCT_BRAND = (By.CSS_SELECTOR, ".product-information p:nth-child(8)")
    OVERLAY = (By.ID, "overlay")  # Overlay for product details

    def is_products_page_visible(self):
        return self.is_visible(*self.ALL_PRODUCTS_HEADING)
    
    def is_product_list_visible(self):
        return self.is_visible(*self.PRODUCT_LIST)
    
    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT_VIEW)
    
    def verify_product_details(self):
        """Verify all product details are visible"""
        return all([
            self.is_visible(*self.PRODUCT_NAME),
            self.is_visible(*self.PRODUCT_CATEGORY),
            self.is_visible(*self.PRODUCT_PRICE),
            self.is_visible(*self.PRODUCT_AVAILABILITY),
            self.is_visible(*self.PRODUCT_CONDITION),
            self.is_visible(*self.PRODUCT_BRAND)
        ])
    
    def click_first_product(self):
        """Click first product with waits and scroll"""
        try:
            # Wait for overlay to disappear if present
            self.wait.until_not(EC.presence_of_element_located(self.OVERLAY))
        except:
            pass
            
        # Get product element
        product = self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT_VIEW))
        
        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
        time.sleep(1)  # Small pause after scroll
        
        # Click with retry
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                product.click()
                return
            except:
                if attempt == max_attempts - 1:
                    raise
                time.sleep(1)