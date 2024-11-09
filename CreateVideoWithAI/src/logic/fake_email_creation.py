import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from infra.utils import stop_page_load
import pyperclip


class FakeEmailCreation:
    COPY_MAIL_BUTTON = '(//button[@data-clipboard-action="copy"])[3]'
    VERIFIED_MAIL_CODE = '(//span[@class="inboxSubject subject-title"])[2]//a'

    def __init__(self, driver):
        """
        Initializes the FakeEmailCreation with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        self.driver = driver

    def wait_for_mail(self, retries=5, wait_time=5):
        """
        Waits for the verification mail to appear in the inbox.

        :param retries: Maximum number of retry attempts.
        :param wait_time: Time in seconds to wait between retries.
        :return: True if mail is found, False if timed out.
        """
        try:
            attempts = 0
            while attempts < retries:
                try:
                    # Wait for the mail to be present in the inbox
                    WebDriverWait(self.driver, wait_time).until(
                        EC.presence_of_element_located((By.XPATH, self.VERIFIED_MAIL_CODE))
                    )
                    print("Verification mail received.")
                    return True  # Exit if mail is found
                except TimeoutException:
                    print(f"Attempt {attempts + 1} failed. Retrying...")
                    attempts += 1
                    if attempts >= retries:
                        print("Max retries reached. Verification mail not found.")
                        return False  # Return False after max retries
                    time.sleep(wait_time)  # Wait before retrying
        except Exception as e:
            print(f"Error during mail waiting: {e}")
            return False

    def copy_mail(self):
        """
        Clicks the button to copy the generated email address.

        :return: None
        """
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, self.COPY_MAIL_BUTTON))
            ).click()

            time.sleep(1)  # Wait a moment to ensure the copy action completes
            copied_email = pyperclip.paste()

            if copied_email:
                return copied_email

        except NoSuchElementException:
            print("Failed to find the copy button.")

    def check_mail_inbox(self):
        """
        Checks if the verification email is present in the inbox.

        :return: True if the email is found, False otherwise.
        """
        try:
            self.driver.find_element(*self.VERIFIED_MAIL_CODE)
            print("Verification email is present in the inbox.")
            return True
        except NoSuchElementException:
            print("Verification email not found.")
            return False

    def is_mail_empty(self):
        """
        Checks if the inbox is empty by trying to find the verification mail.

        :return: True if the inbox is empty, False otherwise.
        """
        is_empty = not self.check_mail_inbox()
        print("Inbox is empty." if is_empty else "Inbox has mail.")
        return is_empty

    def extract_code_from_mail(self):
        """
        Opens the verification email and extracts the code from its content.

        :return: The extracted code as a string, or None if not found.
        """
        try:
            # Locate and click the email link that contains the login code
            email_link = self.driver.find_element(By.XPATH, self.VERIFIED_MAIL_CODE)
            email_link_text = email_link.text.strip()  # Get the visible text of the email link

            # Extract the code using string operations or a regular expression
            code = None
            if email_link_text:
                # Assuming the code is the first 6-digit number in the text
                import re
                match = re.search(r'\b\d{6}\b', email_link_text)
                if match:
                    code = match.group(0)
                    print(f"Extracted code: {code}")
                else:
                    print("No 6-digit code found in the email link text.")

            return code
        except (NoSuchElementException, TimeoutException):
            print("Failed to extract the code from the email.")
            return None

    def copy_email_flow(self):
        """
        Complete workflow to wait for the page to load and copy the temporary email address.

        :return: True if the email was successfully copied, False otherwise.
        """
        stop_page_load(self.driver)
        return self.copy_mail()
