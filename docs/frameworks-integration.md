# settings.py for django
INSTALLED_APPS = [
    # apps...
    'behave_django',
]


# features/environment.py for flask
def before_all(context):
    context.app = create_app('test_config.py')
    context.client = context.app.test_client()
    context.db = db

def before_scenario(context, scenario):
    with context.app.app_context():
        context.db.create_all()

def after_scenario(context, scenario):
    with context.app.app_context():
        context.db.drop_all()