from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from locators.accessibility_ids import AX

class TabTopComponent(BasePage):
    TITLE = (AppiumBy.ACCESSIBILITY_ID, AX.TabTop.TITLE)

    def get_title_text(self, expected_title):
        return self.get_text_with_wait(self.TITLE, expected_title)
