### duda de funcionamiento

necesito entender el docstring
Text DocString


necsitos saber como funciona row[...]
crear_usuario(row['nombre'], row['email'], row['rol'])

necesito saber el manejo de pass
pass

necesito saber el manejo de assert 
assert texto, "El texto está vacío": quiero todas las casuisticas de asserts

necesito saber el manejo de with
def before_scenario(context, scenario):
    with context.app.app_context():
        context.db.create_all()




### resoluciones
context => util que se ejecuta en cada caso


# instalacion
`pip install behave`
# Tutorial

``` sh .feature
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
```

`“features/steps”`
``` py
from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
```

`behave`

## feature
``` sh
Feature: Fight or flight
  In order to increase the ninja survival rate,
  As a ninja commander
  I want my ninjas to decide whether to take on an
  opponent based on their skill levels

  Scenario: Weaker opponent
    Given the ninja has a third level black-belt
     When attacked by a samurai
     Then the ninja should engage the opponent

  Scenario: Stronger opponent
    Given the ninja has a third level black-belt
     When attacked by Chuck Norris
     Then the ninja should run for his life
```
# BDD
desarrollo guiado por comportamiento
# Feature Testing Setup : Funciones
`Given, When, Then (And, But)`

`Step Data, Text, Table`
"<name>"

"""
  Lorem ..
"""

Given a set of specific users
    | name      | department  |
    | Barry     | Beer Cans   |
    | Pudey     | Silly Walks |
    | Two-Lumps | Silly Walks |

## tag
@slow
@wip
@needs_database @slow

### Languages Other Than English
`behave --lang-list`
`behave --lang=fr`

# Using behave
https://behave.readthedocs.io/en/stable/behave.html 
manejo de tags

# API behance reference
# Fixtures



# Características avanzadas
### Uso de tablas
``` sh gherkin
Scenario: Comprobar múltiples usuarios
  Given que tengo los siguientes usuarios:
    | nombre  | email               | rol     |
    | Alice   | alice@example.com   | admin   |
    | Bob     | bob@example.com     | usuario |
  When compruebo los permisos
  Then "Alice" debería tener acceso de administrador
```

``` py !context.table
@given('que tengo los siguientes usuarios')
def step_impl(context):
    for row in context.table:
        # row.cells contiene: ["Alice", "alice@example.com", "admin"]
        crear_usuario(row['nombre'], row['email'], row['rol'])
```

### Text DocString
``` sh
Scenario: Email de verificación
  When envío un email de verificación
  Then el mensaje debería contener:
    """
    Gracias por registrarte.
    Por favor confirma tu email haciendo clic en el enlace:
    http://ejemplo.com/confirmar
    """
``` 

``` py //! context.text
@then('el mensaje debería contener')
def step_impl(context):
    # context.text contiene el texto entre comillas triples
    assert context.text in context.mensaje_enviado
```

## Ejecución paralela y optimización
# Usando pytest-parallel
`python -m pytest features/ --behave --workers 4`
