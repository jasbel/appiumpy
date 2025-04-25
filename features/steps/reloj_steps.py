from behave import given, when, then
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from pages.reloj_page import RelojPage

@given("que abro la aplicación de reloj")
def step_impl(context):
    sleep(2)
    context.reloj = RelojPage(context.driver)

@when("navego a la pestaña de alarmas")
def step_impl(context):
    context.reloj.abrir_alarma()

@when("presiono el botón para agregar una nueva alarma")
def step_impl(context):
    context.reloj.agregar_alarma()

@when('selecciono la hora "{hora}"')
def step_impl(context, hora):
    context.reloj.seleccionar_hora(hora)

@when('selecciono los minutos "{minutos}"')
def step_impl(context, minutos):
    context.reloj.seleccionar_minuto(minutos)

@then('confirmo la alarma de la "{hora}" horas con "{minuto}" minutos')
def step_impl(context, hora, minuto):
    context.reloj.confirmar_alarma()

    sleep(2)
    assert context.reloj.verificar_alarma(hora, minuto).is_displayed()
