## Arranco servidor de pruebas
* En otra terminal
`appium`

* En el proyecto
`source venv/Scripts/activate`
`behave`


## Allure Report

descargar allure y copiar en C:\tools\allure\bin

`allure --version`

abrir el servidor
`allure serve reports/allure-results`

generar el archivo
`allure generate reports/allure-results -o reports/allure-report --clean`

abrir el archivo
`allure open reports/allure-report`


## Comandos de ejecucoin simple
behave features/reloj.feature -D app=clock
behave features/barik.feature -D app=barik
behave features/common.feature -D app=barik


# Android Studio
## modo inspeccion
ir  a `menu/tools/layout inspector`
al ejecutar y correr el mobile.
aparecera el icono con lupita en la derecha

