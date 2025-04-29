Feature: Validar elementos de Home Screen [Home]
  Como usuario
  Quiero asegurarme que los botones principales y la tarjeta existen
  Para comprobar la carga correcta del Home

  Scenario: Validar botones y tarjeta en Home
    Given el usuario abre la aplicación
    And el usuario se posiciona en el tab Home
    Then deberían estar visibles los botones Barik NFC y Barik Mobile
    And debería visualizarse la tarjeta con texto "Card and trips view"
