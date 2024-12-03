# pages/contact_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    # Locators
    CONTACT_HEADING = (By.CSS_SELECTOR, ".contact-form h2")
    NAME_INPUT = (By.CSS_SELECTOR, "input[data-qa='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "input[data-qa='subject']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    FILE_UPLOAD = (By.CSS_SELECTOR, "input[name='upload_file']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    HOME_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-success']")

    def verify_contact_heading(self):
        """Verify 'GET IN TOUCH' heading"""
        heading = self.get_text(*self.CONTACT_HEADING)
        return "GET IN TOUCH" in heading

    def fill_contact_form(self, name, email, subject, message):
        """Fill all contact form fields"""
        self.type_text(*self.NAME_INPUT, name)
        self.type_text(*self.EMAIL_INPUT, email)
        self.type_text(*self.SUBJECT_INPUT, subject)
        self.type_text(*self.MESSAGE_INPUT, message)

    def upload_file(self, file_path):
        """Upload file"""
        self.find_element(*self.FILE_UPLOAD).send_keys(file_path)

    def submit_form(self):
        """Submit contact form"""
        self.click(*self.SUBMIT_BUTTON)

    def verify_success_message(self):
        """Verify success message"""
        return self.is_visible(*self.SUCCESS_MESSAGE)

    def click_home(self):
        """Click home button"""
        self.click(*self.HOME_BUTTON)