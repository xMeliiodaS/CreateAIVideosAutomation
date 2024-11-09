import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class InvideoSignupPage:
    EMAIL_INPUT = '//input[@name="email_id"]'
    CODE_INPUT = '//input[@name="code"]'
    CREATE_ACCOUNT_BEFORE_CODE_BUTTON = '//button[contains(text(), "Create account")]'

    def __init__(self, driver):
        """
        Initializes the FakeEmailCreation with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        self.driver = driver

    def fill_email_input(self, email_text):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT))
        ).send_keys(email_text)

    def click_create_account_button(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_ACCOUNT_BEFORE_CODE_BUTTON))
        )

    def fill_verification_code_input(self, verification_code):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.CODE_INPUT))
        ).send_keys(verification_code)
