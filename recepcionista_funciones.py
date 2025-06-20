class Recepcionista:
    def __init__(self, cedula, nombre, apellido, telefono, email):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def inscribir_estudiante(self, cedula_est, id_curso, conexion):
        cursor = conexion.cursor()
        try:
            query = """
                INSERT INTO inscripcion (cedula_estudiante, id_curso)
                VALUES (%s, %s)
            """
            cursor.execute(query, (cedula_est, id_curso))
            conexion.commit()
            print("Estudiante inscrito exitosamente.")
        except Exception as e:
            print("Error al inscribir:", e)

    def cancelar_inscripcion(self, cedula_est, id_curso, conexion):
        cursor = conexion.cursor()
        try:
            query = """
                DELETE FROM inscripcion 
                WHERE cedula_estudiante = %s AND id_curso = %s
                AND fecha_inscripcion > CURDATE() - INTERVAL 1 DAY
            """
            cursor.execute(query, (cedula_est, id_curso))
            conexion.commit()
            print("Inscripción cancelada.")
        except Exception as e:
            print("Error al cancelar:", e)

    def gestionar_estudiante(self, accion, datos, conexion):
        cursor = conexion.cursor()
        try:
            if accion == 'agregar':
                query = """
                    INSERT INTO estudiante (cedula, nombre, apellido, telefono, email)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, datos)
            elif accion == 'editar':
                query = """
                    UPDATE estudiante SET nombre=%s, apellido=%s,
                    telefono=%s, email=%s WHERE cedula=%s
                """
                cursor.execute(query, datos)
            elif accion == 'eliminar':
                query = "DELETE FROM estudiante WHERE cedula = %s"
                cursor.execute(query, (datos,))
            conexion.commit()
            print(f"Estudiante {accion} correctamente.")
        except Exception as e:
            print("Error en gestión:", e)