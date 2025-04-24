from appium.webdriver.common.appiumby import AppiumBy

class RelojPage:
    def __init__(self, driver):
        self.driver = driver

    def abrir_alarma(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alarm").click()

    def agregar_alarma(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add alarm").click()

    def seleccionar_hora(self, hora):
        el = f"//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='{hora}']"
        self.driver.find_element(AppiumBy.XPATH, el).click()

    def seleccionar_minuto(self, minuto):
        el = f"//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='{minuto}']"
        self.driver.find_element(AppiumBy.XPATH, el).click()

    def confirmar_alarma(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()
        # self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='OK']").click()

    def verificar_alarma(self, hora, minuto):
        el = f'//android.widget.TextView[@content-desc="{hora}:{minuto} PM"]'
        return self.driver.find_element(AppiumBy.XPATH, el)
