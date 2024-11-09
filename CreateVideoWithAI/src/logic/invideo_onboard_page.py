import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class InvideoSignupPage:
    NAME_TEXT_INPUT = '//input[@id="userFullName"]'
    CONTINUE_BUTTON = '//button[@type="submit"]'
    SELECT_REASON_BUTTON = '//div[@type="button"]'
    SELECTION_LIST = '//DIV[@role="menuitem"]' # Random 1 - 6
    WAYS_TO_USE_INVIDEO_LIST_BUTTONS = '//div[@class="c-PJLV c-cQJzLy"]'

    def __init__(self, driver):
        """
        Initializes the FakeEmailCreation with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        self.driver = driver

