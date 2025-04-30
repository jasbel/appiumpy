from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def _get_locator_tuple(self, locator: Tuple[str, str]) -> Tuple[str, str]:
        """
        Helper method to convert locator string to a tuple (AppiumBy, value).

        Args:
            locator (Tuple[str, str]): A locator tuple (AppiumBy, value).

        Returns:
            Tuple[str, str]: The locator as a tuple (AppiumBy, value).

        Raises:
            ValueError: If the locator type is invalid.
        """
        if isinstance(locator, tuple) and len(locator) == 2:
            return locator
        else:
            raise ValueError(
                "Invalid locator format. Please provide a tuple (AppiumBy, value)."
            )

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def is_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def get_text_with_wait(self, locator, expected_title, timeout = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.TITLE, expected_title)
        )

        return self.find_element(locator).text
    def get_text(self, locator):
        return self.find_element(locator).text

    def swipe_up(self, duracion=800):
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duracion)
    def swipe_right(self, duration: int = 500):
        """
        Swipes right on the screen.

        Args:
            duration (int, optional): The duration of the swipe in milliseconds. Defaults to 500.
        """
        size = self.driver.get_window_size()
        start_x = size["width"] * 0.8
        start_y = size["height"] / 2
        end_x = size["width"] * 0.2
        self.driver.swipe(start_x, start_y, end_x, start_y, duration)

    def swipe_down(self, duration: int = 800):
        """
        Swipes down on the screen.

        Args:
            duration (int, optional): The duration of the swipe in milliseconds. Defaults to 800.
        """
        size = self.driver.get_window_size()
        start_x = size["width"] / 2
        start_y = size["height"] * 0.2
        end_y = size["height"] * 0.8
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_left(self, duration: int = 500):
        """
        Swipes left on the screen.

        Args:
            duration (int, optional): The duration of the swipe in milliseconds. Defaults to 500.
        """
        size = self.driver.get_window_size()
        start_x = size["width"] * 0.2
        start_y = size["height"] / 2
        end_x = size["width"] * 0.8
        self.driver.swipe(start_x, start_y, end_x, start_y, duration)

    def wait_for_element(self, locator, timeout=None):
        WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def is_clickable(self, locator: Tuple[str, str], timeout: int = None) -> bool:
        """
        Check if an element is clickable.

        Args:
            locator (Tuple[str, str]): Locator of the element to be checked
            timeout (int): The timeout. Defaults to None

        Returns:
            bool: True if the element is clickable, otherwise false.
        """
        locator_tuple = self._get_locator_tuple(locator)
        try:
            WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.element_to_be_clickable(locator_tuple)
            )
            return True
        except TimeoutException:
            return False
