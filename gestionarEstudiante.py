import tkinter as tk
from tkinter import ttk
from Tooltip import Tooltip
from utils import centrar_ventana

class VentanaGestionarEstudiante:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Gestión de Estudiantes")
        self.ventana.geometry("900x600")
        centrar_ventana(self.ventana, 900, 600)
        self.ventana.config(bg="#f0f2f5")
        self.ventana.resizable(0, 0)
        self.ventana.lift()
        self.ventana.focus_force()
        self.ventana.grab_set()

        color_fondo = "#f0f2f5"
        color_boton = "#1877f2"
        color_texto = "white"
        fuente_titulo = ("Segoe UI", 22, "bold")
        fuente_boton = ("Segoe UI", 11, "bold")

        # Estilo para ttk.Button
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Rounded.TButton",
                        font=fuente_boton,
                        background=color_boton,
                        foreground=color_texto,
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor='none',
                        padding=10)
        style.map("Rounded.TButton",
                  background=[("active", "#166fe5")])

        # Botón Regresar (esquina superior izquierda)
        self.boton_volver = tk.Button(
            self.ventana,
            text="Regresar",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            bd=0,
            cursor="hand2",
            relief="flat",
            command=self.volver
        )
        self.boton_volver.place(x=20, y=20, width=90, height=30)
        Tooltip(self.boton_volver, "Regresar al panel anterior")

        # Botón Ayuda (debajo de Regresar)
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
        self.boton_ayuda.place(x=20, y=60, width=90, height=30)
        Tooltip(self.boton_ayuda, "¿Necesitas ayuda? Haz clic aquí.")

        # Botón Cerrar (esquina superior derecha)
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
        self.boton_cerrar.place(x=790, y=20, width=90, height=30)
        Tooltip(self.boton_cerrar, "Cerrar esta ventana")

        # Título principal
        self.label = tk.Label(
            self.ventana,
            text="Gestión de Estudiantes",
            bg=color_fondo,
            fg="#222",
            font=fuente_titulo
        )
        self.label.place(relx=0.5, y=40, anchor="center")

        # Botones de gestión (más pequeños y con márgenes)
        botones = [
            ("Actulizar\nEstudiante", self.cambiar_contrasena, "Restablece la contraseña de un estudiante"),
            ("Eliminar\nEstudiante", self.eliminar_estudiante, "Elimina un estudiante del sistema"),
            ("Registrar\nEstudiante", self.inscribir_estudiante, "Inscribe un estudiante al sistema"),
            ("Ver Inscritos\nBuscar", self.ver_inscritos, "Ver estudiantes inscritos en cursos"),
            ("Ver Perfil", self.ver_perfil, "Ver el perfil completo del estudiante"),
        ]

        total_botones = len(botones)
        margen_lateral = 40
        espacio_total = 900 - 2 * margen_lateral
        ancho = 130
        alto = 55
        separacion = (espacio_total - (ancho * total_botones)) // (total_botones - 1)
        y_botones = 180  # Antes estaba en 120, ahora más abajo

        self.boton_widgets = []
        for i, (texto, comando, tooltip) in enumerate(botones):
            x = margen_lateral + i * (ancho + separacion)
            btn = ttk.Button(
                self.ventana,
                text=texto,
                style="Rounded.TButton",
                command=comando
            )
            btn.place(x=x, y=y_botones, width=ancho, height=alto)
            Tooltip(btn, tooltip)
            self.boton_widgets.append(btn)

        # Botón Guardar Cambios (parte de abajo, centrado)
        self.boton_guardar = tk.Button(
            self.ventana,
            text="Guardar Cambios",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 13, "bold"),
            bd=0,
            cursor="hand2",
            relief="flat",
            #command=self.guardar_cambios
        )
        self.boton_guardar.place(relx=0.5, y=520, anchor="center", width=200, height=45)
        Tooltip(self.boton_guardar, "Haz clic para guardar los cambios realizados")

    # Métodos de los botones (vacíos para implementar después)
    def cambiar_contrasena(self):
        pass

    def eliminar_estudiante(self):
        pass

    def inscribir_estudiante(self):
        pass

    def ver_inscritos(self):
        pass

    def ver_perfil(self):
        pass

    def volver(self):
        self.ventana.destroy()
        self.ventana_principal.deiconify()

    def mostrar_ayuda(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tk
    VentanaGestionarEstudiante(root)
    root.mainloop()