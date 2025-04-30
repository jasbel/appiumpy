import sys
import subprocess

key_value = {
  "home": "home_screen",
  "options": "options_screen",
  "common": "common",
}

feature_name = sys.argv[1] if len(sys.argv) > 1 else "home"
app = sys.argv[2] if len(sys.argv) > 2 else "barik"

if feature_name not in key_value:
    raise ValueError(f"Nombre de feature inválido: '{feature_name}'")


feature = f"features/{key_value[feature_name]}.feature"

subprocess.run([
    "python", "-m", "behave", feature,
    "-D", f"app={app}"
])

# python run_behave.py features/options_screen.feature barik
