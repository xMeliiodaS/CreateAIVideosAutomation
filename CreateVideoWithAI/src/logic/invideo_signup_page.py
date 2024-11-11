from infra.logger_setup import logger_setup
import logging
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InvideoSignupPage:
    EMAIL_INPUT = '//input[@name="email_id"]'
    CODE_INPUT = '//input[@name="code"]'
    CREATE_ACCOUNT_BUTTON = '//button[contains(text(), "Create account")]'

    def __init__(self, driver):
        """
        Initializes the FakeEmailCreation with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        self.driver = driver

    def fill_email_input(self, email_text):
        """
        Enters the provided email address into the email input field.
        :param email_text: The email address to be entered.
        """
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.EMAIL_INPUT))
        ).send_keys(email_text)

    def click_create_account_button(self):
        """
        Waits for the "Create account" button to be clickable and clicks it.
        """
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_ACCOUNT_BUTTON))
        ).click()

    def fill_verification_code_input(self, verification_code):
        """
        Enters the provided verification code into the code input field.
        :param verification_code: The verification code to be entered.
        """
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.CODE_INPUT))
        ).send_keys(verification_code)

    def submit_email_signup_flow(self, email_text):
        """
        Completes the signup flow by entering the email and clicking the "Create account" button.
        :param email_text: The email address to be entered into the email input field.
        """
        self.fill_email_input(email_text)  # Fill in the email
        time.sleep(1)


        self.click_create_account_button()  # Click the "Create account" button
        logging.info("Entered email on InVideo signup page and proceeded")

    def submit_code_signup_flow(self, verification_code):
        """
        Completes the signup flow by entering the email and clicking the "Create account" button.
        :param verification_code: The code which has been sent to the email.
        """
        self.fill_verification_code_input(verification_code)  # Fill in the email
        time.sleep(1)

        self.click_create_account_button()  # Click the "Create account" button
        logging.info("Filled verification code in InVideo signup page and proceeded")
