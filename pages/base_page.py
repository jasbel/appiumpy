from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

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
    
    def wait_for_element(self, locator, timeout=None):
        WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
