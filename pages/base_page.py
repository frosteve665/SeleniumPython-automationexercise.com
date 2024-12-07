# base_page.py
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def type_text(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def is_visible(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            return element.is_displayed()
        except TimeoutException:
            return False

    def get_text(self, by, value):
        element = self.find_element(by, value)
        return element.text

    def get_attribute(self, by, value, attribute):
        element = self.find_element(by, value)
        return element.get_attribute(attribute)

    def is_enabled(self, by, value):
        element = self.find_element(by, value)
        return element.is_enabled()

    def select_dropdown_by_text(self, by, value, text):
        element = self.find_element(by, value)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_dropdown_by_value(self, by, value, val):
        element = self.find_element(by, value)
        select = Select(element)
        select.select_by_value(val)

    def scroll_to_element(self, by, value):
        element = self.find_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def hover_over(self, by, value):
        element = self.find_element(by, value)
        ActionChains(self.driver).move_to_element(element).perform()

    def accept_alert(self):
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, by, value):
        frame = self.find_element(by, value)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def wait_for_url_to_be(self, url):
        return self.wait.until(EC.url_to_be(url))

    def wait_for_url_contains(self, partial_url):
        return self.wait.until(EC.url_contains(partial_url))
    
