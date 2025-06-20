from ventanaPrincipal import VentanaPrincipal
import tkinter as tk
from recepcionista_funciones import Recepcionista
from conexion import obtener_conexion  # si ya tienes un archivo para conectar a la BD

conn = obtener_conexion()

recep = Recepcionista("111", "Laura", "Suárez", "3001234567", "laura@correo.com")
recep.inscribir_estudiante("123456789", 1, conn)  # Usa un curso real de tu BD
# Crear una instancia del recepcionista (puede ser temporal para pruebas)
recep = Recepcionista("111", "Laura", "Suárez", "3001234567", "laura@correo.com")

# Probar inscripción
conn = obtener_conexion()
recep.inscribir_estudiante("123456789", 1, conn)

# Probar cancelación
recep.cancelar_inscripcion("123456789", 1, conn)

from recepcionista_funciones import Recepcionista
from conexion import obtener_conexion

conn = obtener_conexion()
recep = Recepcionista("111", "Laura", "Suárez", "3001234567", "laura@correo.com")
recep.inscribir_estudiante("123456789", 1, conn)  # Usa cédula e ID de curso reales

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root, usar_root=True)  # Nuevo argumento
    root.mainloop()