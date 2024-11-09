import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

class BrowserWrapper:
    """
    Wrapper class for managing browser interactions using Selenium WebDriver.
    """

    def __init__(self):
        self._driver = None

    def get_driver(self, url, load_strategy='normal'):
        """
        Initialize the WebDriver and navigate to the specified URL.
        """
        try:
            options = uc.ChromeOptions()
            options.page_load_strategy = 'eager'
            options.add_argument("--disable-blink-features=AutomationControlled")
            self._driver = uc.Chrome(options=options)
            self._driver.get(url)
            self._driver.maximize_window()
            return self._driver

        except Exception as e:
            print(f"Error initializing driver: {e}")
            return None

    def get_driver_with_real_email(self, url, profile_path, profile_name):
        """
        Initialize WebDriver using a real email account, loading the Chrome profile.
        """
        try:
            options = Options()
            options.add_argument(f"user-data-dir={profile_path}")
            options.add_argument(f"profile-directory={profile_name}")
            self._driver = uc.Chrome(options=options)
            self._driver.get(url)
            self._driver.maximize_window()
            return self._driver

        except Exception as e:
            print(f"Error using real email profile: {e}")
            return None

    def open_new_tab(self, url):
        """
        Opens a new tab and loads the specified URL.
        """
        self._driver.execute_script("window.open('');")  # Open a new tab
        self.switch_to_tab(len(self._driver.window_handles) - 1)  # Switch to the new tab
        self._driver.get(url)  # Load the URL in the new tab

    def switch_to_tab(self, tab_index):
        """
        Switches to a specific tab by its index.
        """
        self._driver.switch_to.window(self._driver.window_handles[tab_index])


    def close_browser(self):
        if self._driver:
            self._driver.quit()
