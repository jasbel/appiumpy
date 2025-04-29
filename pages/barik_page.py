from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class BarikPage(BasePage):
  BOX_TRANSACTION = (AppiumBy.ACCESSIBILITY_ID, "box-transaction")

  def navigate_pestanias(self):
    self.wait_for_element(self.BOX_TRANSACTION)
    self.click(self.BOX_TRANSACTION)