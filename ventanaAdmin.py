import tkinter as tk
from Tooltip import Tooltip
from utils import centrar_ventana

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

        # Botón Volver
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

        # Botón Ayuda
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

        # Botón Cerrar sesión
        self.btn_cerrar = tk.Button(
            self.ventana, text="Cerrar", font=("Segoe UI", 12, "bold"), bg="#f22618", fg="white",
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

        # Saludo
        self.label_saludo = tk.Label(
            self.ventana,
            text=f"¡Hola, {self.usuario}!",
            bg=color_fondo,
            fg=color_principal,
            font=("Segoe UI", 18, "bold")
        )
        self.label_saludo.place(relx=0.5, y=110, anchor=tk.CENTER)

        # --- GESTIÓN DE USUARIOS ---
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

        self.btn_estudiantes = tk.Button(
            self.ventana, text="Estudiantes", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=20, command=self.ver_lista_estudiantes
        )
        self.btn_estudiantes.place(x=x_izq, y=y_inicio + sep, width=200, height=50)
        Tooltip(self.btn_estudiantes, "Gestiona los estudiantes registrados")

        self.btn_recep = tk.Button(
            self.ventana, text="Recepcionistas", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=20, command=self.gestionar_recepcionistas
        )
        self.btn_recep.place(x=x_izq, y=y_inicio + 2*sep, width=200, height=50)
        Tooltip(self.btn_recep, "Gestiona los recepcionistas del sistema")

        self.btnAdmin = tk.Button(
            self.ventana, text="Administradores", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=20, command=self.cambiar_contrasena
        )
        self.btnAdmin.place(x=x_izq, y=y_inicio + 3*sep, width=200, height=50)
        Tooltip(self.btnAdmin, "Gestiona los administradores del sistema")

        # --- GESTIÓN DE CURSOS ---
        x_der = 600

        self.lbl_gestion_cursos = tk.Label(
            self.ventana,
            text="GESTIÓN DE CURSOS",
            bg=color_fondo,
            fg=color_principal,
            font=fuente_seccion
        )
        self.lbl_gestion_cursos.place(x=x_der, y=y_inicio)

        self.btn_cursos = tk.Button(
            self.ventana, text="Oferta de Cursos", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=20, command=self.crear_curso
        )
        self.btn_cursos.place(x=x_der, y=y_inicio + sep, width=200, height=50)
        Tooltip(self.btn_cursos, "Gestiona la oferta de cursos")

        self.btn_informes = tk.Button(
            self.ventana, text="Informes de\n Inscripción", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=20, command=self.generar_informes
        )
        self.btn_informes.place(x=x_der, y=y_inicio + 2*sep, width=200, height=50)
        Tooltip(self.btn_informes, "Genera y exporta informes de inscripción")

        self.btn_estadisticas = tk.Button(
            self.ventana, text="Estadísticas\nGenerales", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=20, command=self.ver_estadisticas
        )
        self.btn_estadisticas.place(x=x_der, y=y_inicio + 3*sep, width=200, height=50)
        Tooltip(self.btn_estadisticas, "Visualiza estadísticas del sistema")

    # Métodos vacíos (solo los botones de Volver y Ayuda funcionan)
    def ver_lista_estudiantes(self):
        pass

    def gestionar_recepcionistas(self):
        pass

    def cambiar_contrasena(self):
        pass

    def crear_curso(self):
        pass

    def generar_informes(self):
        pass

    def ver_estadisticas(self):
        pass

    def cerrar_admin(self):
        self.ventana.destroy()

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
            self.ventana_principal.deiconify()
