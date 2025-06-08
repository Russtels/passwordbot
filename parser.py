import pytesseract
import json
from PIL import Image
import os

# Definir constantes globales para las rutas
RUTA_IMAGEN = './captura_periodica.png'
RUTA_JSON = os.path.join(os.path.dirname(__file__), 'content.json')

def leer_contenido_imagen(ruta_imagen):
    try:
        # Usar 'with' para manejo seguro del archivo
        with Image.open(ruta_imagen) as imagen:
            # Reducir la resolución un 10% para acelerar el procesamiento
            nueva_ancho = int(imagen.width * 0.6)
            nueva_alto = int(imagen.height * 0.6)
            imagen = imagen.resize((nueva_ancho, nueva_alto))

            # Ejecutar OCR en la imagen redimensionada
            texto = pytesseract.image_to_string(imagen, lang='spa')

        return texto.strip()
    except Exception as e:
        print(f"Error al leer la imagen: {e}")
        return None

def guardar_en_json(contenido, ruta_json):
    try:
        with open(ruta_json, 'w', encoding='utf-8') as archivo_json:
            json.dump({"contenido": contenido}, archivo_json, ensure_ascii=False, indent=4)
        print(f"Contenido guardado en {ruta_json}")
    except Exception as e:
        print(f"Error al guardar el JSON: {e}")

def main():
    contenido = leer_contenido_imagen(RUTA_IMAGEN)
    if contenido:
        guardar_en_json(contenido, RUTA_JSON)
    else:
        print("No se pudo extraer contenido de la imagen.")

if __name__ == "__main__":
    main()
