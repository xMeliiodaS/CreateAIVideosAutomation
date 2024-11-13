import logging
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from infra.ai_generate import generate_random_name_ai
from src.utils import generate_random_number


class InvideoGenerateVideoPage:
    GENERATE_VIDEO_BUTTON = '//div[text() = "Generate a video"]'
    AUDIENCE_OPTIONS = '//div[text()="Audience"]/following-sibling::div//button'
    LOOK_AND_FEEL_OPTIONS = '//div[text()="Look and Feel"]/following-sibling::div//button'
    YOUTUBE_SHORTS_BUTTON = '//div[text() ="YouTube shorts"]'

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
            EC.visibility_of_element_located((By.XPATH,))
        ).send_keys(name)

    def click_generate_video_button(self):
        """
        Waits for the "Continue" button to be clickable and clicks it.
        """
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.GENERATE_VIDEO_BUTTON))
        ).click()
