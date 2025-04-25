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
