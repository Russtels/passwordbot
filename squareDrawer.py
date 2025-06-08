import cv2
import numpy as np
import pyautogui
import os

# Definir constantes globales para evitar cálculos repetitivos
ANCHO_RECTANGULO = 400
ALTO_RECTANGULO = 70
PUNTO_INICIAL = (620, 230)  # Posición inicial del rectángulo
RUTA_CAPTURA = os.path.join(os.path.dirname(__file__), 'captura_periodica.png')

def capturar_area():
    # Captura la porción de la pantalla dentro del rectángulo definido
    captura = pyautogui.screenshot(region=(PUNTO_INICIAL[0], PUNTO_INICIAL[1], ANCHO_RECTANGULO, ALTO_RECTANGULO))
    return np.array(captura)

def capturar_periodicamente():
    # Capturar y guardar la región
    captura = capturar_area()
    imagen = cv2.cvtColor(captura, cv2.COLOR_BGR2RGB)
    cv2.imwrite(RUTA_CAPTURA, cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR))
    print(f"Imagen guardada como {RUTA_CAPTURA}")

if __name__ == "__main__":
    capturar_periodicamente()
