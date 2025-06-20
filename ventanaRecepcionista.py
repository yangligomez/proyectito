import tkinter as tk
from Tooltip import Tooltip
from utils import centrar_ventana

class VentanaRecepcionista:
    def __init__(self, ventana_principal, usuario="Recepcionista"):
        self.ventana_principal = ventana_principal
        self.usuario = usuario
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Panel de Recepcionista")
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
            bd=0, cursor="hand2", relief="flat", command=self.cerrar_recepcionista
        )
        self.btn_cerrar.place(x=800, y=20, width=80, height=30)
        Tooltip(self.btn_cerrar, "Cerrar sesión y regresar al login")

        # Título
        self.label = tk.Label(
            self.ventana,
            text="Panel de Recepcionista",
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

        # Gestión de estudiantes (Interfaz sin funcionalidad)
        x_izq = 80
        y_inicio = 180
        sep = 100

        self.lbl_gestion_estudiantes = tk.Label(
            self.ventana,
            text="GESTIÓN DE ESTUDIANTES",
            bg=color_fondo,
            fg=color_principal,
            font=fuente_seccion
        )
        self.lbl_gestion_estudiantes.place(x=x_izq, y=y_inicio)

        self.btn_gestionar_estudiantes = tk.Button(
            self.ventana, text="Gestionar Estudiantes", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18
        )
        self.btn_gestionar_estudiantes.place(x=x_izq, y=y_inicio + sep, width=200, height=40)
        Tooltip(self.btn_gestionar_estudiantes, "Ver, buscar, agregar, editar o eliminar estudiantes")

        # Gestión de inscripciones (Interfaz sin funcionalidad)
        x_der = 540

        self.lbl_gestion_inscripciones = tk.Label(
            self.ventana,
            text="GESTIÓN DE INSCRIPCIONES",
            bg=color_fondo,
            fg=color_principal,
            font=fuente_seccion
        )
        self.lbl_gestion_inscripciones.place(x=x_der, y=y_inicio)

        self.btn_inscribir = tk.Button(
            self.ventana, text="Inscribir Estudiante", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18
        )
        self.btn_inscribir.place(x=x_der, y=y_inicio + sep, width=200, height=40)
        Tooltip(self.btn_inscribir, "Inscribir un estudiante en un curso disponible")

        self.btn_cancelar = tk.Button(
            self.ventana, text="Cancelar Inscripción", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18
        )
        self.btn_cancelar.place(x=x_der, y=y_inicio + 2*sep, width=200, height=40)
        Tooltip(self.btn_cancelar, "Cancelar inscripción antes del inicio del curso")

        self.btn_ver_inscripciones = tk.Button(
            self.ventana, text="Ver Inscripciones", font=fuente_boton, bg="white", fg=color_principal,
            bd=1, relief="solid", cursor="hand2", width=18
        )
        self.btn_ver_inscripciones.place(x=x_der, y=y_inicio + 3*sep, width=200, height=40)
        Tooltip(self.btn_ver_inscripciones, "Ver todas las inscripciones registradas")

    def cerrar_recepcionista(self):
        self.ventana.destroy()

    def mostrar_ayuda(self):
        tk.messagebox.showinfo(
            "Ayuda - Panel de Recepcionista",
            "Este es un panel para la interfaz de Recepcionista.\n\n" +
            "Las funcionalidades aún no están implementadas."
        )

    def volver(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = VentanaRecepcionista(root, "Recepcionista de Prueba")
    root.mainloop()
