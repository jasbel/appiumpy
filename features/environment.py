from appium import webdriver
from appium.options.android import UiAutomator2Options

def before_all(context):
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "deviceName": "Android GoogleAPI Emulator",
        "platformVersion": "11.0",
        "automationName": "UiAutomator2",
        "appPackage": "com.google.android.deskclock",
        "appActivity": "com.android.deskclock.DeskClock",
        # "noReset": True,
        # "newCommandTimeout": 300
    })
    context.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    context.driver.implicitly_wait(5)


def after_all(context):
    if hasattr(context, "driver"):
        print("🛑 Cerrando sesión...")
        context.driver.quit()