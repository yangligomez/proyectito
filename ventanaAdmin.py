import tkinter as tk
from Tooltip import Tooltip
from utils import centrar_ventana
from conexion import obtener_conexion

class VentanaAdmin:
    def __init__(self, ventana_principal, usuario="Administrador"):
        self.ventana_principal = ventana_principal
        self.usuario = usuario
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Panel de Administrador")
        self.ventana.geometry("900x600")
        centrar_ventana(self.ventana, 900, 600)
        self.ventana.config(bg="#f0f2f5")
        self.ventana.resizable(0, 0)
        self.ventana.lift()
        self.ventana.focus_force()
        self.ventana.grab_set()

        color_fondo = "#f0f2f5"
        color_principal = "#1877f2"
        fuente_titulo = ("Segoe UI", 28, "bold")
        fuente_boton = ("Segoe UI", 14, "bold")
        fuente_seccion = ("Segoe UI", 16, "bold")

        # Botón Volver (esquina superior izquierda)
        self.boton_volver = tk.Button(
            self.ventana,
            text="Volver",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            bd=0,
            cursor="hand2",
            relief="flat",
            command=self.volver
        )
        self.boton_volver.place(x=20, y=20, width=80, height=30)
        Tooltip(self.boton_volver, "Regresar a la ventana anterior")

        # Botón Ayuda (debajo de Volver)
        self.boton_ayuda = tk.Button(
            self.ventana,
            text="Ayuda",
            bg="#f22618",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            bd=0,
            cursor="hand2",
            relief="flat",
            command=self.mostrar_ayuda
        )
        self.boton_ayuda.place(x=20, y=60, width=80, height=30)
        Tooltip(self.boton_ayuda, "¿Necesitas ayuda? Haz clic aquí.")

        # Botón Cerrar sesión (esquina superior derecha)
        self.btn_cerrar = tk.Button(
            self.ventana, text="Cerrar sesión", font=("Segoe UI", 12, "bold"), bg="#f22618", fg="white",
            bd=0, cursor="hand2", relief="flat", command=self.cerrar_admin
        )
        self.btn_cerrar.place(x=800, y=20, width=80, height=30)
        Tooltip(self.btn_cerrar, "Cerrar sesión y regresar al login")

        # Título
        self.label = tk.Label(
            self.ventana,
            text="Panel de Administrador",
            bg=color_fondo,
            fg=color_principal,
            font=fuente_titulo
        )
        self.label.place(relx=0.5, y=60, anchor=tk.CENTER)

        # Saludo debajo del título
        self.label_saludo = tk.Label(
            self.ventana,
            text=f"¡Hola, {self.usuario}!",
            bg=color_fondo,
            fg=color_principal,
            font=("Segoe UI", 18, "bold")
        )
        self.label_saludo.place(relx=0.5, y=110, anchor=tk.CENTER)

        # --- GESTIÓN DE USUARIOS (Izquierda) ---
        x_izq = 100
        y_inicio = 150
        sep = 100

        self.lbl_gestion_usuarios = tk.Label(
            self.ventana,
            text="GESTIÓN DE USUARIOS",
            bg=color_fondo,
            fg=color_principal,
            font=fuente_seccion
        )
        self.lbl_gestion_usuarios.place(x=x_izq, y=y_inicio)

        # Botón Estudiantes
        self.btn_estudiantes = tk.Button(
            self.ventana, text="Estudiantes", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18, command=self.ver_lista_estudiantes
        )
        self.btn_estudiantes.place(x=x_izq, y=y_inicio + sep, width=200, height=40)
        Tooltip(self.btn_estudiantes, "Gestiona los estudiantes registrados")

        # Botón Recepcionistas
        self.btn_recep = tk.Button(
            self.ventana, text="Recepcionistas", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18, command=self.gestionar_recepcionistas
        )
        self.btn_recep.place(x=x_izq, y=y_inicio + 2*sep, width=200, height=40)
        Tooltip(self.btn_recep, "Gestiona los recepcionistas del sistema")

        # Botón Administradores (antes: Cambiar Contraseña)
        self.btnAdmin = tk.Button(
            self.ventana, text="Administradores", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18, command=self.cambiar_contrasena
        )
        self.btnAdmin.place(x=x_izq, y=y_inicio + 3*sep, width=200, height=40)
        Tooltip(self.btnAdmin, "Gestiona los administradores del sistema")

        # --- GESTIÓN DE CURSOS (Derecha) ---
        x_der = 600

        self.lbl_gestion_cursos = tk.Label(
            self.ventana,
            text="GESTIÓN DE CURSOS",
            bg=color_fondo,
            fg=color_principal,
            font=fuente_seccion
        )
        self.lbl_gestion_cursos.place(x=x_der, y=y_inicio)

        # Botón Oferta de Cursos
        self.btn_cursos = tk.Button(
            self.ventana, text="Oferta de Cursos", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18, command=self.crear_curso
        )
        self.btn_cursos.place(x=x_der, y=y_inicio + sep, width=200, height=40)
        Tooltip(self.btn_cursos, "Gestiona la oferta de cursos")

        # Botón Informes de Inscripción
        self.btn_informes = tk.Button(
            self.ventana, text="Informes de Inscripción", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18, command=self.generar_informes
        )
        self.btn_informes.place(x=x_der, y=y_inicio + 2*sep, width=200, height=40)
        Tooltip(self.btn_informes, "Genera y exporta informes de inscripción")

        # Botón Estadísticas Generales
        self.btn_estadisticas = tk.Button(
            self.ventana, text="Estadísticas Generales", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18, command=self.ver_estadisticas
        )
        self.btn_estadisticas.place(x=x_der, y=y_inicio + 3*sep, width=200, height=40)
        Tooltip(self.btn_estadisticas, "Visualiza estadísticas del sistema")

            # Métodos vacíos para implementar después
    def gestionar_recepcionistas(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT cedula, nombre, apellido FROM recepcionista")
            recepcionistas = cursor.fetchall()
            if not recepcionistas:
                print("No hay recepcionistas registrados.")
            else:
                print("\n--- Lista de Recepcionistas ---")
                for rec in recepcionistas:
                    print(f"Cédula: {rec[0]} | Nombre: {rec[1]} {rec[2]}")
        except Exception as e:
            print("Error al consultar recepcionistas:", e)


    def ver_lista_estudiantes(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT cedula, nombre, apellido FROM estudiante")
            estudiantes = cursor.fetchall()
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                print("\n--- Lista de Estudiantes ---")
                for est in estudiantes:
                    print(f"Cédula: {est[0]} | Nombre: {est[1]} {est[2]}")
        except Exception as e:
            print("Error al consultar estudiantes:", e)
    def buscar_estudiante(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cedula = tk.simpledialog.askstring("Buscar Estudiante", "Ingrese la cédula del estudiante:")

        if not cedula:
            print("Búsqueda cancelada.")
            return

        try:
            cursor.execute("SELECT cedula, nombre, apellido, telefono, email FROM estudiante WHERE cedula = %s", (cedula,))
            estudiante = cursor.fetchone()
            if estudiante:
                print("\n--- Estudiante encontrado ---")
                print(f"Cédula: {estudiante[0]}")
                print(f"Nombre: {estudiante[1]} {estudiante[2]}")
                print(f"Teléfono: {estudiante[3]}")
                print(f"Email: {estudiante[4]}")
            else:
                print("Estudiante no encontrado.")
        except Exception as e:
            print("Error en la búsqueda:", e)


    def gestionar_estudiantes(self):
        conn = obtener_conexion()
        cursor = conn.cursor()

        opcion = tk.simpledialog.askstring(
            "Gestión de Estudiantes",
            "¿Qué acción deseas realizar? (agregar / editar / eliminar)"
        )

        if opcion == "agregar":
            datos = []
            campos = ["Cédula", "Nombre", "Apellido", "Teléfono", "Email"]
            for campo in campos:
                valor = tk.simpledialog.askstring("Agregar Estudiante", f"Ingrese {campo}:")
                datos.append(valor)
            try:
                query = """
                    INSERT INTO estudiante (cedula, nombre, apellido, telefono, email)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, tuple(datos))
                conn.commit()
                print("Estudiante agregado exitosamente.")
            except Exception as e:
                print("Error al agregar estudiante:", e)

        elif opcion == "editar":
            cedula = tk.simpledialog.askstring("Editar Estudiante", "Ingrese la cédula del estudiante:")
            campos = ["Nombre", "Apellido", "Teléfono", "Email"]
            nuevos = []
            for campo in campos:
                valor = tk.simpledialog.askstring("Editar Estudiante", f"Nuevo {campo}:")
                nuevos.append(valor)
            nuevos.append(cedula)
            try:
                query = """
                    UPDATE estudiante SET nombre=%s, apellido=%s,
                    telefono=%s, email=%s WHERE cedula=%s
                """
                cursor.execute(query, tuple(nuevos))
                conn.commit()
                print("Estudiante actualizado.")
            except Exception as e:
                print("Error al editar estudiante:", e)

        elif opcion == "eliminar":
            cedula = tk.simpledialog.askstring("Eliminar Estudiante", "Ingrese la cédula del estudiante:")
            try:
                query = "DELETE FROM estudiante WHERE cedula = %s"
                cursor.execute(query, (cedula,))
                conn.commit()
                print("Estudiante eliminado.")
            except Exception as e:
                print("Error al eliminar estudiante:", e)
        else:
            print("Opción inválida o cancelada.")

    def crear_curso(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, nombre, estado, cupos_disponibles FROM curso")
            cursos = cursor.fetchall()
            if not cursos:
                print("No hay cursos registrados.")
            else:
                print("\n--- Oferta de Cursos ---")
                for curso in cursos:
                    print(f"ID: {curso[0]} | Nombre: {curso[1]} | Estado: {curso[2]} | Cupos: {curso[3]}")
        except Exception as e:
            print("Error al consultar cursos:", e)

    def modificar_curso(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        try:
            curso_id = tk.simpledialog.askinteger("Modificar Curso", "Ingrese el ID del curso a modificar:")
            if curso_id is None:
                return

            # Obtener curso actual
            cursor.execute("SELECT nombre, descripcion, duracion, cupos_disponibles FROM curso WHERE id = %s", (curso_id,))
            curso = cursor.fetchone()
            if not curso:
                print("Curso no encontrado.")
                return

            # Pedir nuevos valores
            nuevo_nombre = tk.simpledialog.askstring("Modificar Curso", f"Nuevo nombre (actual: {curso[0]}):") or curso[0]
            nueva_descripcion = tk.simpledialog.askstring("Modificar Curso", f"Descripción (actual: {curso[1]}):") or curso[1]
            nueva_duracion = tk.simpledialog.askstring("Modificar Curso", f"Duración (actual: {curso[2]}):") or curso[2]
            nuevos_cupos = tk.simpledialog.askinteger("Modificar Curso", f"Cupos disponibles (actual: {curso[3]}):") or curso[3]

            # Actualizar
            cursor.execute("""
                UPDATE curso SET nombre=%s, descripcion=%s, duracion=%s, cupos_disponibles=%s
                WHERE id = %s
            """, (nuevo_nombre, nueva_descripcion, nueva_duracion, nuevos_cupos, curso_id))
            conn.commit()
            print("Curso modificado exitosamente.")
        except Exception as e:
            print("Error al modificar curso:", e)

    def ver_cursos(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id, nombre, estado, cupos_disponibles FROM curso")
            cursos = cursor.fetchall()
            if not cursos:
                print("No hay cursos registrados.")
            else:
                print("\n--- Lista de Cursos ---")
                for curso in cursos:
                    print(f"ID: {curso[0]} | Nombre: {curso[1]} | Estado: {curso[2]} | Cupos: {curso[3]}")
        except Exception as e:
            print("Error al consultar cursos:", e)

    def generar_informes(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT id_curso, nombre_curso, total_inscritos FROM vista_inscripciones_por_curso")
            informes = cursor.fetchall()
            if not informes:
                print("No hay inscripciones registradas.")
            else:
                print("\n--- Informe de Inscripciones por Curso ---")
                for inf in informes:
                    print(f"Curso ID: {inf[0]} | Nombre: {inf[1]} | Inscritos: {inf[2]}")
        except Exception as e:
            print("Error al generar informe:", e)


    def ver_estadisticas(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        try:
            # Total estudiantes
            cursor.execute("SELECT COUNT(*) FROM estudiante")
            total_estudiantes = cursor.fetchone()[0]

            # Cursos activos y cerrados
            cursor.execute("SELECT estado, COUNT(*) FROM curso GROUP BY estado")
            cursos_estado = cursor.fetchall()
            activos = cerrados = 0
            for estado, total in cursos_estado:
                if estado == "activo":
                    activos = total
                elif estado == "cerrado":
                    cerrados = total

            # Inscripciones confirmadas
            cursor.execute("SELECT COUNT(*) FROM inscripcion WHERE estado = 'confirmada'")
            inscripciones = cursor.fetchone()[0]

            print("\n--- Estadísticas Generales ---")
            print(f"Estudiantes registrados: {total_estudiantes}")
            print(f"Cursos activos: {activos}")
            print(f"Cursos cerrados: {cerrados}")
            print(f"Inscripciones confirmadas: {inscripciones}")
        except Exception as e:
            print("Error al obtener estadísticas:", e)
            
    def cambiar_contrasena(self):
        from tkinter import simpledialog, messagebox
        conn = obtener_conexion()
        cursor = conn.cursor()

        username = tk.simpledialog.askstring("Cambio de Contraseña", "Ingrese su usuario:")
        cedula = tk.simpledialog.askstring("Cambio de Contraseña", "Ingrese su cédula:")
        nueva_clave = tk.simpledialog.askstring("Cambio de Contraseña", "Ingrese la nueva contraseña:", show="*")

        if not username or not cedula or not nueva_clave:
            print("Operación cancelada.")
            return

        try:
            cursor.execute(
                "UPDATE usuario SET password=%s WHERE username=%s AND cedula=%s AND rol='administrador'",
                (nueva_clave, username, cedula)
            )
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
            else:
                messagebox.showwarning("Error", "Datos no coinciden o usuario no es administrador.")
        except Exception as e:
            print("Error al cambiar contraseña:", e)

    def cerrar_admin(self):
        self.ventana.destroy()
        # Si quieres mostrar la ventana principal de nuevo, descomenta la siguiente línea:
        # self.ventana_principal.deiconify()

    def mostrar_ayuda(self):
        tk.messagebox.showinfo(
            "Ayuda",
            "Desde aquí puedes gestionar usuarios, cursos, informes y estadísticas.\n"
            "Usa los botones de la izquierda para usuarios y los de la derecha para cursos.\n"
            "Para más ayuda, contacta al soporte técnico."
        )

    def volver(self):
        respuesta = tk.messagebox.askquestion(
            "Volver",
            "¿Estás seguro de que quieres regresar? Se perderán los cambios no guardados.",
            icon="warning"
        )
        if respuesta == "yes":
            self.ventana.destroy()
            self.ventana_principal.deiconify()  # Mostrar la ventana principal de nuevo