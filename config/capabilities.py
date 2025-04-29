from appium.options.android import UiAutomator2Options

def get_android_options(app_name="barik"):
    if app_name == "clock":
        capabilities = {
            "platformName": "Android",
            "deviceName": "Android GoogleAPI Emulator",
            "platformVersion": "11.0",
            "automationName": "UiAutomator2",
            "appPackage": "com.google.android.deskclock",
            "appActivity": "com.android.deskclock.DeskClock",
            # "noReset": True,
            # "newCommandTimeout": 300
        }
    elif app_name == "barik":
        capabilities = {
            "platformName": "Android",
            "deviceName": "Android GoogleAPI Emulator",
            "platformVersion": "11.0",
            "automationName": "UiAutomator2",
            "appPackage": "net.develoop.barik",
            "appActivity": "net.develoop.barik.MainActivity",
        }
    else:
        raise ValueError(f"No se reconoce la app_name: {app_name}")

    options = UiAutomator2Options().load_capabilities(capabilities)
    return options
