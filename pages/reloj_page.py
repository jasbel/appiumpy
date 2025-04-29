from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class RelojPage(BasePage):
    ALARM = (AppiumBy.ACCESSIBILITY_ID, "Alarm")
    ADD_ALARM = (AppiumBy.ACCESSIBILITY_ID, "Add alarm")
    CONFIRM_ALARM = (AppiumBy.XPATH, "//android.widget.Button[@text='OK']")
    CONFIRM_ALARM = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')

    def abrir_alarma(self):
        self.click(self.ALARM)

    def agregar_alarma(self):
        self.click(self.ADD_ALARM)

    def seleccionar_tiempo(self, tiempo):
        el = f"//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc='{tiempo}']"
        self.click((AppiumBy.XPATH, el))


    def seleccionar_hora(self, hora):
        self.seleccionar_tiempo(hora)

    def seleccionar_minuto(self, minuto):
        self.seleccionar_tiempo(minuto)

    def confirmar_alarma(self):
        self.click(self.CONFIRM_ALARM)

    def verificar_alarma(self, hora, minuto):
        el = f'//android.widget.TextView[@content-desc="{hora}:{minuto} PM"]'
        return self.find_element((AppiumBy.XPATH, el))
