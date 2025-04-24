from behave import given, when, then
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

@given("que abro la aplicación de reloj")
def step_impl(context):
    sleep(2)

@when("navego a la pestaña de alarmas")
def step_impl(context):
    context.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alarm").click()

@when("presiono el botón para agregar una nueva alarma")
def step_impl(context):
    context.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add alarm").click()

@when('selecciono la hora "{hora}"')
def step_impl(context, hora):
    context.driver.find_element(
        AppiumBy.XPATH,
        f'//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="{hora}"]'
    ).click()

@when('selecciono los minutos "{minutos}"')
def step_impl(context, minutos):
    context.driver.find_element(
        AppiumBy.XPATH,
        f'//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="{minutos}"]'
    ).click()

@then('confirmo la alarma de la "{hora}" horas con "{minuto}" minutos')
def step_impl(context, hora, minuto):
    context.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")').click()
    resultado = context.driver.find_element(
        AppiumBy.XPATH,
        f'//android.widget.TextView[@content-desc="{hora}:{minuto} PM"]'
    )
    assert resultado.is_displayed()
