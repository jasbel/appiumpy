import os
import shutil
from behave.model_core import Status
from drivers.driver_factory import create_driver
from time import sleep
from support.i18n_manager import I18nManager


def before_all(context):

    context.i18n = I18nManager(base_path="i18n", default_lang="en")

    """Create the allure results folder before all tests run."""
    allure_results_dir = "reports/allure-results"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir)


def before_scenario(context, scenario):
    context.driver = create_driver(context)
    context.driver.implicitly_wait(5)

def before_step(context, step):
    delay = 1
    if 'slow' in context.tags:
        delay = 3
    sleep(delay)

def after_scenario(context, scenario):
    sleep(1)

    if hasattr(context, "driver"):
        context.driver.quit()
