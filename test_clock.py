from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

# Configuración usando AppiumOptions
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android GoogleAPI Emulator"  # o el nombre de tu dispositivo
options.platform_version = "11.0"
options.app_package = "com.google.android.deskclock"
options.app_activity = "com.android.deskclock.DeskClock"

driver = webdriver.Remote("http://localhost:4723", options=options)

driver.implicitly_wait(5)
# sleep(5)

try:
    hora = 10
    minuto = 20

    print("⏰ Abriendo la app de reloj...")
    sleep(2)

    print("🕐 Navegando a la pestaña de alarmas...")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alarm").click()
    sleep(2)

    print("➕ Agregando nueva alarma...")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add alarm").click()
    sleep(2)

    print(f"🕙 Seleccionando la hora: {hora}")
    driver.find_element(
        AppiumBy.XPATH,
        f'//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="{hora}"]'
    ).click()
    sleep(2)

    print(f"🕧 Seleccionando los minutos: {minuto}")
    driver.find_element(
        AppiumBy.XPATH,
        f'//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="{minuto}"]'
    ).click()
    sleep(2)

    print("✅ Confirmando alarma...")
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()
    sleep(2)

    print("🔍 Verificando alarma creada...")
    resultado = driver.find_element(
        AppiumBy.XPATH,
        f'//android.widget.TextView[@content-desc="{hora}:{minuto} PM"]'
    )
    assert resultado.is_displayed()
    print("🎉 Alarma creada correctamente!")

except Exception as e:
    print(f"❌ Error durante la prueba: {e}")

finally:
    print("🛑 Cerrando sesión...")
    sleep(2)
    driver.quit()
