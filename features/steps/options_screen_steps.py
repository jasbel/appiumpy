from behave import given, then, when
from pages.options_page import OptionsPage
import time

@given('el usuario se posiciona en el tab Options')
def step_go_to_options_tab(context):
    context.options.go_to_options_tab()

@when('el usuario explora los items disponibles')
def step_explore_options_items(context):
    context.options.explore_options_items()

@then('deberían mostrarse los contenidos correspondientes')
def step_verify_options_content(context):
    context.options.verify_options_content()

@when('el usuario selecciona la opción Language')
def step_select_language_option(context):
    context.options.select_language_option()

@then('deberían existir los radio buttons para Spanish, Basque e English')
def step_verify_languages_exist(context):
    context.options.verify_languages_exist()

@then('debería estar seleccionado por defecto English')
def step_verify_default_language(context):
    context.options.verify_default_language()

@when('el usuario selecciona la opción Proofs')
def step_select_proofs_option(context):
    context.options.select_proofs_option()

@then('deberían visualizarse los toggles disponibles')
def step_verify_proofs_toggles(context):
    context.options.verify_proofs_toggles()

@when('el usuario explora la sección inferior')
def step_explore_bottom_section(context):
    context.options.explore_bottom_section()

@then('debería estar visible el botón "Privacy Policy"')
def step_verify_privacy_policy_button(context):
    context.options.verify_privacy_policy_button()
