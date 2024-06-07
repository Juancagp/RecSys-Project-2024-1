import os
from codecarbon import EmissionsTracker
from datetime import datetime
import json
import subprocess

# Función para entrenar un modelo, rastrear las emisiones de CO2 y guardar la información de entrenamiento
def track_training_C02_emissions(command, model_name, data_name):

    logs_file_path = os.path.join("..", "trained_models", model_name, data_name)
    json_file_path = os.path.join(logs_file_path, "trainingData.json")
    
    codecarbon_tracker = EmissionsTracker()

    try:
        start_time = datetime.now()

        codecarbon_tracker.start()

        training_process = subprocess.run(command, shell=True, capture_output=True, text=True)

        emissions = codecarbon_tracker.stop()

        end_time = datetime.now()
        print(f"Salida de STDOUT: {training_process.stdout}")
        print(f"CO2_emissions_kg: {emissions}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    existing_data = []
    if os.path.exists(json_file_path):
        try:
            with open(json_file_path, 'r') as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            print(f"El archivo {json_file_path} está vacío o contiene datos inválidos, se inicializará como una lista vacía.")
            existing_data = []

    training_info = {
        "training_iteration": len(existing_data) + 1,  # Número de iteración basado en el tamaño del dataset existente
        "date": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "execution_time_seconds": (end_time - start_time).total_seconds(),
        "CO2_emissions_kg": emissions
    }

    existing_data.append(training_info)

    with open(json_file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)

    return emissions