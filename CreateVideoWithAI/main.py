import logging

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from src.logic.fake_email_creation import FakeEmailCreation
from src.logic.invideo_signup_page import InvideoSignupPage
from src.logic.invideo_onboard_page import InvideoOnboardPage
from git_automation import pull_prompts_repo
#

class VideoSignupAutomation:
    def __init__(self):
        self.config = None
        self.browser = None
        self.driver = None


    def get_driver_and_config(self):
        """
        Loads the configuration and initializes the browser and driver.
        """
        try:
            self.config = ConfigProvider.load_config_json()
            self.browser = BrowserWrapper()
            self.driver = self.browser.get_driver(self.config["temp_mail_url"])
        except Exception as e:
            print(f"Error in get_driver_and_config: {e}")
            raise

    def get_copied_email(self):
        """
        Creates an instance for email creation and copies the generated email.
        """
        email_page = FakeEmailCreation(self.driver)
        copied_email = email_page.copy_email_flow()
        return copied_email

    def open_invideo_signup_page(self):
        """
        Opens the InVideo signup page in a new tab.
        """
        self.browser.open_new_tab(self.config["invideo_signup_url"])
        self.browser.switch_to_tab(1)

    def submit_email_for_signup(self, copied_email):
        """
        Submits the copied email to the InVideo signup form.
        """
        invideo_signup_page = InvideoSignupPage(self.driver)
        invideo_signup_page.submit_email_signup_flow(copied_email)

    def handle_verification(self):
        """
        Waits for the email verification code and returns it.
        """
        email_page = FakeEmailCreation(self.driver)
        verification_code = ''
        if email_page.wait_for_mail(retries=5, wait_time=5):
            verification_code = email_page.extract_code_from_mail()
        return verification_code

    def submit_verification_code(self, verification_code):
        """
        Submits the extracted verification code to complete the signup process.
        """
        invideo_signup_page = InvideoSignupPage(self.driver)
        invideo_signup_page.submit_code_signup_flow(verification_code)

    def complete_onboarding(self):
        """
        Completes the onboarding process on the InVideo platform.
        """
        invideo_onboard_page = InvideoOnboardPage(self.driver)
        invideo_onboard_page.onboard_setup_workflow()

    def run(self):
        """
        Orchestrates the entire signup and onboarding process.
        """
        try:
            copied_email = self.get_copied_email()

            self.open_invideo_signup_page()
            self.submit_email_for_signup(copied_email)

            self.browser.switch_to_tab(0)
            verification_code = self.handle_verification()

            self.browser.switch_to_tab(1)
            self.submit_verification_code(verification_code)

            self.complete_onboarding()

            pull_prompts_repo()

        except Exception as e:
            print(f"An error occurred during execution: {e}")
            raise

        finally:
            # Ensure browser is closed even if an error occurs
            self.browser.close_browser()


def main():
    logging.info("------------------------------SETUP------------------------------")
    automation = VideoSignupAutomation()
    automation.get_driver_and_config()
    automation.run()


if __name__ == "__main__":
    main()
