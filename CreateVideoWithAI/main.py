from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from src.logic.fake_email_creation import FakeEmailCreation
from src.logic.invideo_signup_page import InvideoSignupPage


def main():
    # Load configuration
    config = ConfigProvider.load_config_json()

    # Initialize the browser using the Chrome profile if needed
    browser = BrowserWrapper()
    driver = browser.get_driver(config["temp_mail_url"])

    try:
        # Create an instance of the page logic
        email_page = FakeEmailCreation(driver)
        copied_email = email_page.copy_email_flow()
        print(f"Copied Email: {copied_email}")

        # Open a new tab for the InVideo signup page
        browser.open_new_tab(config["invideo_signup_url"])  # Use the helper function

        # Switch to the second tab
        browser.switch_to_tab(1)

        # Create an instance for InVideo signup and fill in the form
        signup_page = InvideoSignupPage(driver)
        signup_page.submit_email_signup_flow(copied_email)


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        browser.close_browser()

if __name__ == "__main__":
    main()
