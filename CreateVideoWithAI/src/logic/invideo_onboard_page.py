import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from infra.ai_generate import generate_random_name_ai
from src.utils import generate_random_number



class InvideoOnboardPage:
    NAME_TEXT_INPUT = '//input[@id="userFullName"]'
    CONTINUE_BUTTON = '//button[@type="submit"]'
    DISCOVERY_SOURCE_DROPDOWN = '//div[@type="button"]'
    DISCOVERY_SOURCE_OPTIONS = '//DIV[@role="menuitem"]'  # Random 1 - 6
    WAYS_TO_USE_INVIDEO_LIST_BUTTONS = '//div[@class="c-PJLV c-cQJzLy"]'  # Random 1 - 6

    def __init__(self, driver):
        """
        Initializes the FakeEmailCreation with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        self.driver = driver

    def fill_name_input(self):
        """
        Fills the name input field with a randomly generated name using AI.
        """
        name = generate_random_name_ai()

        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.NAME_TEXT_INPUT))
        ).send_keys(name)

    def click_continue_button(self):
        """
        Waits for the "Continue" button to be clickable and clicks it.
        """
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON))
        ).click()

    def click_discovery_source_dropdown(self):
        """
        Clicks the dropdown button to reveal discovery source options.
        """
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.DISCOVERY_SOURCE_DROPDOWN))
        ).click()

    def select_random_discovery_source_option(self):
        """
        Clicks the discovery source dropdown and selects an option based on the provided text.
        """
        random_index = generate_random_number(0, 5)

        options = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.DISCOVERY_SOURCE_OPTIONS))
        )

        options[random_index].click()

    def select_random_method_to_use_invideo(self):
        """
        Selects a random option from the 'Ways to Use InVideo' list by
         clicking on one of the available options.
        """
        random_index = generate_random_number(0, 4)

        options = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.WAYS_TO_USE_INVIDEO_LIST_BUTTONS))
        )

        options[random_index].click()


    def onboard_setup_workflow(self):
        self.fill_name_input()
        time.sleep(1)

        self.click_continue_button()
        self.click_discovery_source_dropdown()
        time.sleep(1)

        self.select_random_discovery_source_option()
        time.sleep(1)

        self.click_continue_button()
        self.select_random_method_to_use_invideo()