from appium import webdriver
from config.capabilities import get_android_options

def create_driver(context):
    app_name = context.config.userdata.get("app", "clock") 
    return webdriver.Remote("http://localhost:4723", options=get_android_options(app_name))
