import discord
import os
import json
from dotenv import load_dotenv

# Cargar las credenciales del archivo .env
load_dotenv("credentials.env")
TOKEN = os.getenv("TOKEN").strip() if os.getenv("TOKEN") else None
CHANNEL_IDS = [channel_id.strip() for channel_id in os.getenv("CHANNELID", "").split(",") if channel_id.strip().isdigit()]

# Ruta del archivo JSON con el contenido
RUTA_JSON = os.path.join(os.path.dirname(__file__), 'content.json')
RUTA_ULTIMA_CONTRASENA = os.path.join(os.path.dirname(__file__), 'lastPass.json')

# Funciones para leer y guardar datos
def leer_contenido_json(ruta_json):
    try:
        with open(ruta_json, 'r', encoding='utf-8') as archivo_json:
            data = json.load(archivo_json)
            return data.get("contenido", "")
    except Exception as e:
        print(f"Error al leer el JSON: {e}")
        return ""

def leer_ultima_contrasena(ruta_archivo):
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)
                return data.get("last_password", "")
        return ""
    except Exception as e:
        print(f"Error al leer la última contraseña: {e}")
        return ""

def guardar_ultima_contrasena(ruta_archivo, contrasena):
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump({"last_password": contrasena}, archivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al guardar la última contraseña: {e}")

# Inicializar el cliente de Discord para selfbot
client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print(f"Selfbot listo. Conectado como {client.user}")

    contenido = leer_contenido_json(RUTA_JSON)
    ultima_contrasena = leer_ultima_contrasena(RUTA_ULTIMA_CONTRASENA)

    if "CONTRASEÑA DE LA RAFFLE:" in contenido:
        try:
            partes = contenido.split("CONTRASEÑA DE LA RAFFLE:")
            if len(partes) > 1:
                palabra_clave = partes[1].strip().split()[0]

                if palabra_clave != ultima_contrasena:
                    mensaje = f"La contraseña de la raffle es: {palabra_clave}"

                    # Enviar mensaje a todos los canales especificados
                    for channel_id in CHANNEL_IDS:
                        canal = client.get_channel(int(channel_id))
                        if canal:
                            await canal.send(mensaje)
                            print(f"Mensaje enviado al canal {channel_id}: {mensaje}")
                        else:
                            print(f"No se pudo encontrar el canal con ID {channel_id}")

                    guardar_ultima_contrasena(RUTA_ULTIMA_CONTRASENA, palabra_clave)
                else:
                    print("La contraseña es la misma que la última enviada. No se enviará de nuevo.")
            else:
                print("No se encontró la palabra clave después de la frase requerida.")
        except Exception as e:
            print(f"Error al procesar el contenido: {e}")
    else:
        print("El contenido no contiene la frase requerida.")

    await client.close()

if TOKEN:
    try:
        client.run(TOKEN)
    except discord.errors.LoginFailure as e:
        print("Error de autenticación: el token proporcionado no es válido. Verifica el valor de TOKEN en credentials.env.")
    except Exception as e:
        print(f"Error inesperado al intentar iniciar sesión: {e}")
else:
    print("Token no encontrado. Asegúrate de que credentials.env contiene el TOKEN correctamente.")
