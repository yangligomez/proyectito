import tkinter as tk
from Tooltip import Tooltip
from utils import centrar_ventana

class VentanaAdmin:
    def __init__(self, ventana_principal):
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

        # Título
        self.label = tk.Label(
            self.ventana,
            text="Panel de Administrador",
            bg=color_fondo,
            fg=color_principal,
            font=fuente_titulo
        )
        self.label.place(relx=0.5, y=60, anchor=tk.CENTER)

        # --- GESTIÓN DE USUARIOS (Izquierda) ---
        x_izq = 100
        y_inicio = 150
        sep = 50

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

        # Botón Cambiar Contraseña
        self.btn_cambiar_pass = tk.Button(
            self.ventana, text="Cambiar Contraseña", font=fuente_boton, bg="#e7f3ff", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18, command=self.cambiar_contrasena
        )
        self.btn_cambiar_pass.place(x=x_izq, y=y_inicio + 3*sep, width=200, height=40)
        Tooltip(self.btn_cambiar_pass, "Cambia tu contraseña de administrador")

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

        # Botón Cerrar sesión (abajo centrado)
        self.btn_cerrar = tk.Button(
            self.ventana, text="Cerrar sesión", font=fuente_boton, bg="#f22618", fg="white",
            bd=0, cursor="hand2", relief="flat", command=self.cerrar_admin
        )
        self.btn_cerrar.place(relx=0.5, y=520, anchor="center", width=220, height=40)
        Tooltip(self.btn_cerrar, "Cerrar sesión y regresar al login")

    # Métodos vacíos para implementar después
    def registrar_recepcionista(self):
        pass

    def gestionar_recepcionistas(self):
        pass

    def ver_lista_estudiantes(self):
        pass

    def buscar_estudiante(self):
        pass

    def gestionar_estudiantes(self):
        pass

    def crear_curso(self):
        pass

    def modificar_curso(self):
        pass

    def ver_cursos(self):
        pass

    def generar_informes(self):
        pass

    def ver_estadisticas(self):
        pass

    def cambiar_contrasena(self):
        pass

    def cerrar_admin(self):
        self.ventana.destroy()
        # Si quieres mostrar la ventana principal de nuevo, descomenta la siguiente línea:
        # self.ventana.master.deiconify()

# Para pruebas rápidas:
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    VentanaAdmin(root)
    root.mainloop()