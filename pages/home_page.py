from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from locators.accessibility_ids import AX

class HomePage(BasePage):
    TAB_NFC = (AppiumBy.ACCESSIBILITY_ID, AX.Home.TAB_NFC)
    TAB_MOBILE = (AppiumBy.ACCESSIBILITY_ID, AX.Home.TAB_MOBILE)
    BOX_TRANSACTIONS = (AppiumBy.ACCESSIBILITY_ID, AX.Home.BOX_TRANSACTIONS)

    def navigate_pestanias(self):
        self.wait_for_element(self.BOX_TRANSACTIONS)
        self.click(self.BOX_TRANSACTIONS)

    def verify_home_buttons(self):
        assert self.is_visible(self.TAB_NFC)
        assert self.is_visible(self.TAB_MOBILE)

    def verify_home_card(self):
        assert self.is_visible(self.BOX_TRANSACTIONS)
