import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    """
    Crea y devuelve una conexión a la base de datos MySQL.
    """
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="security_toolkit"
    )
    return conexion


def guardar_escaneo(ip, puerto_inicio, puerto_fin, puertos_abiertos):
    """
    Guarda el resultado de un escaneo de puertos en la base de datos.
    """
    conexion = conectar()
    cursor = conexion.cursor()

    puertos_texto = ", ".join(str(p) for p in puertos_abiertos) if puertos_abiertos else "Ninguno"

    query = """
        INSERT INTO escaneos (ip, puerto_inicio, puerto_fin, puertos_abiertos)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (ip, puerto_inicio, puerto_fin, puertos_texto))

    conexion.commit()
    cursor.close()
    conexion.close()
    print("\n✅ Resultado guardado en la base de datos.")