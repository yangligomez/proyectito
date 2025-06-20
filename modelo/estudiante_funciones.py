from conexion import obtener_conexion

def obtener_estudiante_por_usuario(usuario):
    """
    Busca y retorna información del estudiante según el usuario desde la base de datos MySQL.
    Retorna un diccionario con los datos si existe, o None si no se encuentra.
    """
    try:
        conexion = obtener_conexion()
        if conexion is None:
            return None
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, edad FROM estudiantes WHERE usuario = %s", (usuario,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        if resultado:
            return {"nombre": resultado[0], "edad": resultado[1]}
        return None
    except Exception as e:
        print(f"Error al obtener estudiante: {e}")
        return None