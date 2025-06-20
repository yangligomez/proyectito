from conexion import obtener_conexion

class Administrador:
    def __init__(self, cedula, nombre, apellido, telefono, email):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    # Gestionar recepcionistas
    @staticmethod
    def agregar_recepcionista(datos):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO recepcionista (cedula, nombre, apellido, telefono, email, usuario, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def editar_recepcionista(cedula, nuevos_datos):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "UPDATE recepcionista SET nombre=%s, apellido=%s, telefono=%s, email=%s, usuario=%s, password=%s WHERE cedula=%s"
        cursor.execute(query, (*nuevos_datos, cedula))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_recepcionista(cedula):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM recepcionista WHERE cedula=%s"
        cursor.execute(query, (cedula,))
        conexion.commit()
        cursor.close()
        conexion.close()

    # Gestionar estudiantes
    @staticmethod
    def agregar_estudiante(datos):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO estudiante (cedula, nombre, apellido, telefono, correo, usuario, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def editar_estudiante(cedula, nuevos_datos):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "UPDATE estudiante SET nombre=%s, apellido=%s, telefono=%s, correo=%s, usuario=%s, password=%s WHERE cedula=%s"
        cursor.execute(query, (*nuevos_datos, cedula))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_estudiante(cedula):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM estudiante WHERE cedula=%s"
        cursor.execute(query, (cedula,))
        conexion.commit()
        cursor.close()
        conexion.close()

    # Gestionar cursos
    @staticmethod
    def agregar_curso(datos):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "INSERT INTO curso (nombre, descripcion, cupo) VALUES (%s, %s, %s)"
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def editar_curso(id_curso, nuevos_datos):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "UPDATE curso SET nombre=%s, descripcion=%s, cupo=%s WHERE id_curso=%s"
        cursor.execute(query, (*nuevos_datos, id_curso))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def eliminar_curso(id_curso):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "DELETE FROM curso WHERE id_curso=%s"
        cursor.execute(query, (id_curso,))
        conexion.commit()
        cursor.close()
        conexion.close()

    # Generar informes de inscripción
    @staticmethod
    def generar_informe_inscripciones():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        query = """
            SELECT e.cedula, e.nombre, e.apellido, c.nombre AS curso, i.fecha_inscripcion
            FROM inscripcion i
            JOIN estudiante e ON i.cedula_estudiante = e.cedula
            JOIN curso c ON i.id_curso = c.id_curso
        """
        cursor.execute(query)
        informe = cursor.fetchall()
        cursor.close()
        conexion.close()
        return informe