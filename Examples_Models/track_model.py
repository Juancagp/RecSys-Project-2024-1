import os
import subprocess
import json
from datetime import datetime
from codecarbon import EmissionsTracker

# Función para entrenar un modelo, rastrear las emisiones de CO2 y guardar la información de entrenamiento
def track_training_C02_emissions(command, trained_model_folder):

    # Inicializamos el tracker
    tracker = EmissionsTracker()

    #iniciamos el tracker
    tracker.start()
    
    try:
        # Obtenemos la fecha y hora de inicio
        start_time = datetime.now()

        # Ejecutamos el comando de entrenamiento
        training_process = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Obtenemos la fecha y hora de finalización
        end_time = datetime.now()

        # Imprimimos la salida de la ejecución
        print(f"Salida de STDOUT: {training_process.stdout}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")
    
    # Detenemos el tracker y obtenemos las emisiones finales
    emissions = tracker.stop()

    # Ruta del archivo JSON
    json_file_path = os.path.join("..", "trained_models", trained_model_folder ,"trainingData.json")
    
    # Leer el archivo JSON existente
    existing_data = []
    if os.path.exists(json_file_path):
        try:
            with open(json_file_path, 'r') as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            print(f"El archivo {json_file_path} está vacío o contiene datos inválidos, se inicializará como una lista vacía.")
            existing_data = []

    # Preparar la información del entrenamiento
    training_info = {
        "training_iteration": len(existing_data) + 1,  # Número de iteración basado en el tamaño del dataset existente
        "date": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "execution_time_seconds": (end_time - start_time).total_seconds(),
        "CO2_emissions_kg": emissions
    }

    # Agregar la nueva información del entrenamiento
    existing_data.append(training_info)

    # Escribir los datos actualizados al archivo JSON
    with open(json_file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)

    # Finalmente, retornamos las emisiones de CO2
    return emissions