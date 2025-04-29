from behave import given, then, when
from pages.home_page import HomePage


@given('el usuario se posiciona en el tab Home')
def go_to_home_tab(context):
    # context.home.go_to_home_tab()
    pass

@then('deberían estar visibles los botones Barik NFC y Barik Mobile')
def step_verify_home_buttons(context):
    context.home.verify_home_buttons()

@then('debería visualizarse la tarjeta con texto "Card and trips view"')
def step_verify_home_card(context):
    context.home.verify_home_card()
