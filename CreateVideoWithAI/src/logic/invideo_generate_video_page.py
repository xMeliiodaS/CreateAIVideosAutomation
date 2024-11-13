import logging
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.ai_generate import generate_random_name_ai


class InvideoGenerateVideoPage:
    TITLE_INPUT = '//p/following-sibling::div'
    AUDIENCE_OPTIONS = '//div[text()="Audience"]/following-sibling::div//button'
    LOOK_AND_FEEL_OPTIONS = '//div[text()="Look and Feel"]/following-sibling::div//button'
    YOUTUBE_SHORTS_BUTTON = '//div[text() ="YouTube shorts"]'
    GENERATE_VIDEO_BUTTON = '//div[text() = "Generate a video"]'
    CONTINUE_BUTTON = '//div[text() = "Continue"]'

    def __init__(self, driver):
        """
        Initializes the FakeEmailCreation with the provided WebDriver instance.

        :param driver: The WebDriver instance to use for browser interactions.
        """
        self.driver = driver

    def get_text_from_audience_options(self):
        """
        Waits for the 'Audience' option elements, then retrieves their text.

        Returns:
            list: A list of text values for each 'Audience' option button.
        """
        audience_buttons = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.AUDIENCE_OPTIONS)))

        # Extract and return the text from each button in the list
        return [button.text for button in audience_buttons]

    def get_text_from_look_feel_options(self):
        """
        Waits for the 'Look and Feel' option elements, then retrieves their text.

        Returns:
            list: A list of text values for each 'Look and Feel' option button.
        """
        look_and_feel_buttons = WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.XPATH, self.LOOK_AND_FEEL_OPTIONS)))

        # Extract and return the text from each button in the list
        return [button.text for button in look_and_feel_buttons]

    def get_text_from_title(self):
        """
        Waits for the 'title' option elements, then retrieves their text.

        Returns:
            str: The title's text.
        """
        return WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, self.TITLE_INPUT))
        ).text


    def click_generate_video_button(self):
        """
        Waits for the "Generate" button to be clickable and clicks it.
        """
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.GENERATE_VIDEO_BUTTON))
        ).click()

    def click_continue_button(self):
        """
        Waits for the "continue" button to be clickable and clicks it.
        """
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.CONTINUE_BUTTON))
        ).click()
