from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from locators.accessibility_ids import AX

class TabBottomComponent(BasePage):
    HOME = (AppiumBy.ACCESSIBILITY_ID, AX.TabBottom.HOME)
    TEMPORARY = (AppiumBy.ACCESSIBILITY_ID, AX.TabBottom.TEMPORARY)
    TRANSACTIONS = (AppiumBy.ACCESSIBILITY_ID, AX.TabBottom.TRANSACTIONS)
    OPTIONS = (AppiumBy.ACCESSIBILITY_ID, AX.TabBottom.OPTIONS)

    def go_to_home(self):
        self.click(self.HOME)

    def go_to_temporary(self):
        self.click(self.TEMPORARY)

    def go_to_transactions(self):
        self.click(self.TRANSACTIONS)

    def go_to_options(self):
        self.click(self.OPTIONS)
