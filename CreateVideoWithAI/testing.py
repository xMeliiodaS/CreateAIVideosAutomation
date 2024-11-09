from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from src.logic.fake_email_creation import FakeEmailCreation
from src.logic.invideo_signup_page import InvideoSignupPage


def main():
    # Load configuration
    config = ConfigProvider.load_config_json()

    # Initialize the browser using the Chrome profile if needed
    browser = BrowserWrapper()
    driver = browser.get_driver(config["invideo_signup_url"])

    try:

        # Create an instance for InVideo signup and fill in the form
        signup_page = InvideoSignupPage(driver)
        signup_page.submit_email_signup_flow("sfgfdgfdgfdgdfgdfg")


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        browser.close_browser()

if __name__ == "__main__":
    main()
