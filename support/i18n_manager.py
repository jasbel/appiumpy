import os
import json

class I18nManager:
    def __init__(self, base_path="i18n", default_lang="en"):
        self.translations = {}
        self.active_lang = default_lang
        self.base_path = base_path
        self.set_language(default_lang)

    def __getitem__(self, key):
        return self.t(key)

    def t(self, key: str) -> str:
        parts = key.split(".")
        current = self.translations.get(self.active_lang, {})
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return f"[falta la traducción para: '{key}']"
        if isinstance(current, str):
            return current
        return f"[traducción inválida para: '{key}']"

    def load_language(self, lang_code: str) -> None:
        path = os.path.join(self.base_path, f"{lang_code}.json")
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Idioma '{lang_code}' no encontrado en: {path}")
        with open(path, encoding="utf-8") as f:
            self.translations[lang_code] = json.load(f)

    def set_language(self, lang_code: str) -> None:
        if lang_code not in self.translations:
            self.load_language(lang_code)
        self.active_lang = lang_code
        print(f"[INFO] Idioma establecido a: {lang_code}")

    def get_active_language(self) -> str:
        return self.active_lang

def validate_keys(base_path="i18n"):
    import os
    import json

    all_keys = {}
    all_langs = []

    # Cargar todas las traducciones
    for filename in os.listdir(base_path):
        if filename.endswith(".json"):
            lang = filename[:-5]  # "es.json" → "es"
            all_langs.append(lang)
            path = os.path.join(base_path, filename)
            with open(path, encoding="utf-8") as f:
                all_keys[lang] = set(json.load(f).keys())

    reference_lang = all_langs[0]
    ref_keys = all_keys[reference_lang]

    has_error = False
    for lang in all_langs:
        missing = ref_keys - all_keys[lang]
        extra = all_keys[lang] - ref_keys

        if missing:
            has_error = True
            print(f"[❌] '{lang}' is missing keys: {sorted(missing)}")
        if extra:
            print(f"[⚠️] '{lang}' has extra keys not in '{reference_lang}': {sorted(extra)}")

    if not has_error:
        print("[✅] All language files are consistent!")

    return not has_error  # True si todo OK, False si hay errores

