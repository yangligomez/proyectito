import tkinter as tk
from tkinter import messagebox
from utils import centrar_ventana
from Tooltip import Tooltip
from view.ventanaEstudiante import Estudiante

class VentanaVerificacionEstud:
    def __init__(self, ventana_principal, usuario):
        self.ventana_principal = ventana_principal
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Panel Estudiante")
        self.ventana.geometry("900x600")
        centrar_ventana(self.ventana, 900, 600)
        self.ventana.config(bg="#f0f2f5")
        self.ventana.resizable(0, 0)
        self.ventana.lift()
        self.ventana.focus_force()
        self.ventana.grab_set()

        # Botón Regresar
        self.boton_regresar = tk.Button(
            self.ventana,
            text="Regresar",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            bd=0,
            cursor="hand2",
            relief="flat",
            command=self.regresar
        )
        self.boton_regresar.place(x=20, y=20, width=80, height=30)
        Tooltip(self.boton_regresar, "Regresar a la ventana anterior")

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

        # Botón Cerrar
        self.boton_cerrar = tk.Button(
            self.ventana,
            text="Cerrar",
            bg="#f22618",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            bd=0,
            cursor="hand2",
            relief="flat",
            command=self.ventana.destroy
        )
        self.boton_cerrar.place(x=800, y=20, width=80, height=30)
        Tooltip(self.boton_cerrar, "Cerrar esta ventana")

        # Título principal
        tk.Label(
            self.ventana,
            text="Panel Estudiante",
            bg="#f0f2f5",
            fg="#1877f2",
            font=("Segoe UI", 28, "bold")
        ).place(relx=0.5, y=100, anchor="center")

        # Aquí abres directamente el panel del estudiante
        Estudiante(self.ventana, usuario)

    def mostrar_ayuda(self):
        messagebox.showinfo(
            "Ayuda",
            "Bienvenido al panel de estudiante.\n"
            "Si tienes problemas para acceder, contacta al soporte técnico."
        )

    def regresar(self):
        respuesta = messagebox.askquestion(
            "Regresar",
            "¿Estás seguro de que quieres regresar? Se perderán los cambios no guardados.",
            icon="warning"
        )
        if respuesta == "yes":
            self.ventana_principal.deiconify()
            self.ventana.destroy()