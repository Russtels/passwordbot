# 🕷️ Screen Scraper & Discord Notifier

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![OCR](https://img.shields.io/badge/OCR-Tesseract-5F4992?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)

Una herramienta de automatización en Python que captura periódicamente una región específica de la pantalla, extrae cualquier texto visible mediante Reconocimiento Óptico de Caracteres (OCR), y envía la información extraída a uno o más canales de Discord a través de webhooks.

---

## 📝 Descripción del Proyecto

Este script lo hice con el fin de parsear en contenido de video/streams/sorteos (como podrían ser contraseñas, códigos, logs, o cualquier otra información) y transmitirlo discretamente a Discord.

Fue creado como un ejercicio avanzado para explorar la automatización de tareas, el OCR y la integración con APIs externas.

### Casos de Uso (Educativos)
* **Monitorear logs** o consolas de aplicaciones que no tienen una API de notificaciones.
* **Capturar alertas** o notificaciones del sistema operativo que aparecen en un lugar fijo.
* **Extraer datos** de forma automatizada de aplicaciones heredadas (legacy) que no permiten copiar texto.


## 📋 Requisitos Indispensables

Este proyecto tiene dependencias tanto de software como de librerías de Python.

### 1. Google Tesseract OCR Engine
Esta es la dependencia más importante y **no es una librería de Python**. Debes instalar el motor Tesseract en tu sistema operativo.
* **[Instrucciones de Instalación de Tesseract](https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md)**
* Durante la instalación en Windows, **asegúrate de que Tesseract se añada al PATH de tu sistema** para que Python pueda encontrarlo.

### 2. Librerías de Python
El archivo `requirements.txt` contiene las librerías necesarias.
* `Pillow`: Para tomar las capturas de pantalla.
* `pytesseract`: El conector de Python para el motor Tesseract.
* `discord-py`: Para realizar las peticiones a la API de Discord.

## 🚀 Instalación y Configuración

1.  **Instala Tesseract OCR**: Sigue las instrucciones del enlace de arriba y verifica que esté correctamente instalado en tu sistema.
2.  **Clona el Repositorio**:
    ```bash
    git clone [https://github.com/Russtels/passwordbot.git](https://github.com/Russtels/passwordbot.git)
    cd passwordbot
    ```
3.  **Instala las Dependencias de Python**:
    *(Se recomienda usar un entorno virtual)*
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configura el Script**:
    * **Abre el archivo `.py` principal** en un editor de texto.
    * **Modifica la lista `channel_ids` (o similar)**: Reemplaza los valores de ejemplo con tus propias URLs de webhooks de Discord.
    * **Ajusta las coordenadas**: Cambia los valores de las variables que definen el área de la pantalla a capturar (`x`, `y`, `width`, `height`).
5.  **Ejecuta el Script**:
    ```bash
    python main.py
    ```
    El script comenzará a ejecutarse en segundo plano, monitoreando y enviando la información según la configuración.

---
