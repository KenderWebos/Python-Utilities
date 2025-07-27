import json
import os

def load_config(path="automation\key_sound_project\key_sound_1.3\config.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Archivo {path} no encontrado en {os.getcwd()}")
        raise
    except json.JSONDecodeError:
        print(f"Error: {path} no es un JSON válido")
        raise