import subprocess
import time
import json
import os
import logging

logging.basicConfig(level=logging.INFO)

# Rutas de archivos
RUTA_JSON = os.path.join(os.path.dirname(__file__), 'content.json')

def ejecutar_script(script_name):
    try:
        logging.info(f"Ejecutando {script_name}...")
        inicio = time.time()

        # Ejecutar el script
        subprocess.run(["python", script_name], check=True)

        fin = time.time()
        tiempo_total = fin - inicio
        logging.info(f"{script_name} ejecutado exitosamente en {tiempo_total:.2f} segundos.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error al ejecutar {script_name}: {e}")

def leer_contenido_json(ruta_json):
    try:
        with open(ruta_json, 'r', encoding='utf-8') as archivo_json:
            data = json.load(archivo_json)
            return data.get("contenido", "")
    except Exception as e:
        logging.error(f"Error al leer el JSON: {e}")
        return ""

def main():
    while True:
        # Paso 1: Ejecutar squareDrawer.py para capturar la pantalla
        ejecutar_script("squareDrawer.py")
        
        # Paso 2: Ejecutar parser.py para extraer el contenido de la imagen
        ejecutar_script("parser.py")
        
        # Paso 3: Verificar el contenido extraído
        contenido = leer_contenido_json(RUTA_JSON)

        if "CONTRASEÑA DE LA RAFFLE:" in contenido:
            logging.info("Contenido válido encontrado. Ejecutando sender.py...")
            ejecutar_script("sender.py")
        else:
            logging.info("Contenido no válido. Volviendo a capturar...")

        # Esperar 1 segundo antes de repetir el proceso
        time.sleep(1)

if __name__ == "__main__":
    main()
