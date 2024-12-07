# tests/tc008_verify_products_page.py
import pytest
from pages.home_page import HomePage
from pages.product_page import ProductsPage
from config.config import TestData

class TestVerifyProductsPage:
    def test_verify_all_products_and_search(self, driver):
        """
        Test Case 8: Verify All Products and product detail page
        1. Launch browser
        2. Navigate to url 'http://automationexercise.com'
        3. Verify that home page is visible successfully
        4. Click on 'Products' button
        5. Verify user is navigated to ALL PRODUCTS page successfully
        6. The products list is visible
        7. Click on 'View Product' of first product
        8. User is landed to product detail page
        9. Verify that detail is visible: product name, category, price, availability, condition, brand
        """
        home_page = HomePage(driver)
        products_page = ProductsPage(driver)
        
        # Navigate to home page
        driver.get(TestData.BASE_URL)
        assert home_page.is_home_page_visible(), "Home page not visible"
        
        # Go to Products page
        home_page.click_products()
        assert products_page.is_products_page_visible(), "Products page not visible"
        
        # Verify products list
        assert products_page.is_product_list_visible(), "Products list not visible"
        
        # View first product details
        products_page.click_first_product()
        
        # Verify product details
        assert products_page.verify_product_details(), "Product details not visible"