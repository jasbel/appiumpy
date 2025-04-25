# @slow
Feature: Configuración de una alarma en la app de Reloj

  Scenario: Crear una alarma para las 10:20
    Given que abro la aplicación de reloj
    When navego a la pestaña de alarmas
    And presiono el botón para agregar una nueva alarma
    And selecciono la hora "10"
    And selecciono los minutos "20"
    Then confirmo la alarma de la "10" horas con "20" minutos
