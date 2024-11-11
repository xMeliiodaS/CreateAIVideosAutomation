from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from src.logic.fake_email_creation import FakeEmailCreation
from src.logic.invideo_signup_page import InvideoSignupPage
from src.logic.invideo_onboard_page import InvideoOnboardPage


class VideoSignupAutomation:
    def __init__(self):
        self.config = None
        self.browser = None
        self.driver = None

    def get_driver_and_config(self):
        try:
            # Load configuration and initialize the browser
            self.config = ConfigProvider.load_config_json()
            self.browser = BrowserWrapper()
            self.driver = self.browser.get_driver(self.config["temp_mail_url"])
        except Exception as e:
            print(f"Error in get_driver_and_config: {e}")
            raise

    def run(self):
        try:
            # Create an instance of the page logic for email creation
            email_page = FakeEmailCreation(self.driver)
            copied_email = email_page.copy_email_flow()
            print(f"Copied Email: {copied_email}")

            # Open a new tab for the InVideo signup page
            self.browser.open_new_tab(self.config["invideo_signup_url"])
            self.browser.switch_to_tab(1)

            # Create an instance for InVideo signup and fill in the form
            invideo_signup_page = InvideoSignupPage(self.driver)
            invideo_signup_page.submit_email_signup_flow(copied_email)

            self.browser.switch_to_tab(0)

            verification_code = ''
            if email_page.wait_for_mail(retries=5, wait_time=5):
                verification_code = email_page.extract_code_from_mail()  # Extract the code

            self.browser.switch_to_tab(1)

            invideo_signup_page.submit_code_signup_flow(verification_code)

            invideo_onboard_page = InvideoOnboardPage(self.driver)

            invideo_onboard_page.onboard_setup_workflow()

        except Exception as e:
            print(f"An error occurred during execution: {e}")
            raise

        finally:
            # Ensure browser is closed even if an error occurs
            self.browser.close_browser()


def main():
    automation = VideoSignupAutomation()
    automation.get_driver_and_config()
    automation.run()


if __name__ == "__main__":
    main()
