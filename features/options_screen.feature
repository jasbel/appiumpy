Feature: Validar elementos de Options Screen [Options]
  Como usuario
  Quiero validar las acciones y configuraciones dentro de Options
  Para comprobar su correcto funcionamiento

  Scenario: Validar navegación y elementos en Options
    Given el usuario abre la aplicación
    And el usuario se posiciona en el tab Options
    When el usuario explora los items disponibles
    Then deberían mostrarse los contenidos correspondientes

  Scenario: Validar cambio de lenguaje
    Given el usuario abre la aplicación
    And el usuario se posiciona en el tab Options
    When el usuario selecciona la opción Language
    Then deberían existir los radio buttons para Spanish, Basque e English
    And debería estar seleccionado por defecto English

  Scenario: Validar toggles en Proofs
    Given el usuario abre la aplicación
    And el usuario se posiciona en el tab Options
    When el usuario selecciona la opción Proofs
    Then deberían visualizarse los toggles disponibles

  Scenario: Validar botón Privacy Policy
    Given el usuario abre la aplicación
    And el usuario se posiciona en el tab Options
    When el usuario explora la sección inferior
    Then debería estar visible el botón "Privacy Policy"
