from appium import webdriver
from appium.options.android import UiAutomator2Options

from drivers.driver_factory import create_driver


def before_all(context):
    context.driver = create_driver()
    context.driver.implicitly_wait(5)


def after_all(context):
    if hasattr(context, "driver"):
        print("🛑 Cerrando sesión...")
        context.driver.quit()