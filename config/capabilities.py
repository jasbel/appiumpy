from appium.options.android import UiAutomator2Options

def get_android_options():
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
    return options
