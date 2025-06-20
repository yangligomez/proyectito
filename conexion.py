# conexion.py
import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # pon tu clave si tienes una
        database="academia"
    )