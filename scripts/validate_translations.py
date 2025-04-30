# python scripts/validate_translations.py
from bootstrap import init_setup; init_setup()
from support.i18n_manager import validate_keys

if __name__ == "__main__":
    validate_keys("i18n")