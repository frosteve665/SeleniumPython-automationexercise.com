# utilities/driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser.lower() == "chrome":
            service = Service(r"C:\Program Files (x86)\chromedriver-win64\chromedriver.exe")
            driver = webdriver.Chrome(service=service)
        # Add more browsers as needed
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver