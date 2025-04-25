# Ejecutar un archivo específico
behave features/tutorial.feature

# Ejecutar un escenario específico
behave features/tutorial.feature:10

# Filtrar por etiquetas
behave --tags=@important

# Excluir etiquetas
behave --tags=~@skip

# Especificar formato de salida
behave --format=json --outfile=resultado.json