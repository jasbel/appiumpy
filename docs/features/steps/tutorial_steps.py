# archivo: features/steps/tutorial_steps.py
from behave import given, when, then

@given('tenemos behave instalado')
def step_impl(context):
    pass

@when('ejecutamos un paso simple')
def step_impl(context):
    assert True is not False

@when('ejecutamos un paso con "{texto}"')
def step_impl(context, texto):
    assert texto, "El texto está vacío"

@then('behave ejecutará el paso')
def step_impl(context):
    assert context.failed is False

@then('behave ejecutará el paso con "{texto}"')
def step_impl(context, texto):
    assert context.failed is False
    assert texto, "El texto está vacío"