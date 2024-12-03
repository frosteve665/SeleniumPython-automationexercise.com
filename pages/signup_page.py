# pages/signup_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
import time

class SignupPage(BasePage):
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    
    # Account Information elements
    TITLE_MR = (By.ID, "id_gender1")
    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    
    # Address Information elements
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-qa='create-account']")
    
    ACCOUNT_CREATED_MESSAGE = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    
    def enter_signup_details(self, name, email):
        self.type_text(*self.NAME_INPUT, name)
        self.type_text(*self.EMAIL_INPUT, email)
        self.click(*self.SIGNUP_BUTTON)
    
    def fill_account_details(self, password):
        self.click(*self.TITLE_MR)
        self.type_text(*self.PASSWORD, password)
        self.select_dropdown_by_value(*self.DAYS, "1")
        self.select_dropdown_by_value(*self.MONTHS, "1")
        self.select_dropdown_by_value(*self.YEARS, "2000")
    
    def fill_address_details(self, first_name, last_name, address, country, state, city, zipcode, mobile):
        self.type_text(*self.FIRST_NAME, first_name)
        self.type_text(*self.LAST_NAME, last_name)
        self.type_text(*self.ADDRESS, address)
        self.select_dropdown_by_value(*self.COUNTRY, country)
        self.type_text(*self.STATE, state)
        self.type_text(*self.CITY, city)
        self.type_text(*self.ZIPCODE, zipcode)
        self.type_text(*self.MOBILE, mobile)
        self.click(*self.CREATE_ACCOUNT_BUTTON)
        time.sleep(5)
