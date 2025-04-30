# python scripts/i18n_test.py

""" Este es un script para comprobar el funcionamiento de traducciones
* correr python scripts/i18n_test
* ejecucion
Comando (lang [code] | get [key] | exit): get greeting
Hello

Comando (lang [code] | get [key] | exit): lang es
[INFO] Language set to: es
"""
from bootstrap import init_setup; init_setup()
from support.i18n_manager import I18nManager

def main():
    i18n = I18nManager()
    i18n.set_language("en")

    while True:
        command = input("\nComando (lang [code] | get [key] | exit): ").strip().split()

        if not command:
            continue

        if command[0] == "exit":
            break
        elif command[0] == "lang" and len(command) == 2:
            try:
                i18n.set_language(command[1])
            except Exception as e:
                print(f"[ERROR] {e}")
        elif command[0] == "get" and len(command) == 2:
            print(i18n.t(command[1]))
        else:
            print("Comando no reconocido.")

if __name__ == "__main__":
    main()
