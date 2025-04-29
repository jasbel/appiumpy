from behave import given, when, then
from pages.tab_bottom_page import TabBottomComponent
from pages.home_page import HomePage
from pages.options_page import OptionsPage
from pages.tab_top_page import TabTopComponent

import time

@given('el usuario abre la aplicación')
def step_impl_init_aplication(context):
    screen = context.feature.name

    if '[Options]' in screen:
        context.options = OptionsPage(context.driver)
    elif '[Home]' in screen:
        context.home = HomePage(context.driver)
    else:
        raise Exception("No se puede determinar el PageObject para esta feature")


@given('el usuario navega a cada tab y valida el titulo')
def step_navega_tabs(context):
    bottom = TabBottomComponent(context.driver)
    top = TabTopComponent(context.driver)

    bottom.go_to_options()
    assert top.get_title_text("Options") == "Options"

    bottom.go_to_home()
    assert top.get_title_text("Barik NFC") == "Barik NFC"

    bottom.go_to_temporary()
    assert top.get_title_text("Barik NFC") == "Barik NFC"

    bottom.go_to_transactions()
    assert top.get_title_text("Transactions") == "Transactions"

@given('el usuario abre la aplicacion')
def step_open_aplication(context):
    context.home = HomePage(context.driver)
    time.sleep(2)

@when('el navega por las pestanias')
def step_navigate_pestanias(context):
    context.home.navigate_pestanias()

@then('confirma el correcto funcionamiento')
def step_confirm(context):
    time.sleep(2)

    
