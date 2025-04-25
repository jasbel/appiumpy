# archivo: features/environment.py
def before_all(context):
    # Configuración global antes de todas las pruebas
    context.config.setup_logging()

def before_feature(context, feature):
    # Antes de cada feature
    context.database = conectar_base_datos()

def after_scenario(context, scenario):
    # Después de cada escenario
    context.database.rollback()

def after_all(context):
    # Limpieza final
    context.database.close()