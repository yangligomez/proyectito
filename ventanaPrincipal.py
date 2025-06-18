import tkinter as tk 
from Tooltip import Tooltip
from PIL import Image, ImageTk
from ventanaRegistro import VentanaRegistro
from ventanaInicioSesion import VentanaInicioSesion
from utils import centrar_ventana
from tkinter import messagebox

class VentanaPrincipal:
    def __init__(self, ventana_principal, usar_root=False):
        self.ventana_principal = ventana_principal
        if usar_root:
            self.ventana = ventana_principal  # root será la ventana principal
        else:
            self.ventana = tk.Toplevel()
        self.ventana.title("Inicio de Sesión")
        self.ventana.geometry("900x600")  # Tamaño anterior conservado
        centrar_ventana(self.ventana, 900, 600)  # Centrar la ventana
        self.ventana.config(bg="#f0f2f5")
        self.ventana.resizable(0, 0)
        self.ventana.lift()           # Pone la ventana al frente
        self.ventana.focus_force()    # Da el foco a la ventana
   

        # Título principal
        self.label = tk.Label(
            self.ventana,
            text="¡Bienvenido!\n Programa de Cursos",
            bg="#f0f2f5",
            fg="#1877f2",
            font=("Segoe UI", 28, "bold")
        )
        self.label.place(relx=0.5, y=100, anchor=tk.CENTER)

        # Subtítulo
        self.label2 = tk.Label(
            self.ventana,
            text="Inicia sesión o regístrate para continuar",
            bg="#f0f2f5",
            fg="#050505",
            font=("Segoe UI", 16)
        )
        self.label2.place(relx=0.5, y=210, anchor=tk.CENTER)

        # Botón Registrarse
        self.boton1 = tk.Button(
            self.ventana,
            text="Registrarse",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 18, "bold"),
            bd=0,
            activebackground="#166fe5",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.abrir_registro
        )
        self.boton1.place(relx=0.5, y=300, anchor=tk.CENTER, width=320, height=50)
        Tooltip(
    self.boton1,
    "Solo estudiantes pueden registrarse aquí.\n"
    "Si eres administrador o recepcionista, inicia sesión y solicita tu inscripción."
)

        icono1 = tk.PhotoImage(file="icons/user_add.png")
        self.boton1.config(image=icono1, compound=tk.LEFT, padx=10)
        self.boton1.image = icono1  # Mantener una referencia al icono

        # Botón Iniciar Sesión
        self.boton2 = tk.Button(
            self.ventana,
            text="Iniciar Sesión",
            bg="white",
            fg="#1877f2",
            font=("Segoe UI", 18, "bold"),
            bd=1,
            highlightbackground="#1877f2",
            highlightcolor="#1877f2",
            activebackground="#e7f3ff",
            activeforeground="#1877f2",
            cursor="hand2",
            relief="solid",
            command=self.abrir_inicio_sesion
        )
        self.boton2.place(relx=0.5, y=380, anchor=tk.CENTER, width=320, height=50)
        Tooltip(self.boton2, "Si ya tienes una cuenta, inicia sesión aquí")
        
        icono2 = tk.PhotoImage(file="icons/user_go.png")
        self.boton2.config(image=icono2, compound=tk.LEFT, padx=10)
        self.boton2.image = icono2  # Mantener una referencia al icono

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
        command=self.mostrar_ayuda)
        
        self.boton_ayuda.place(x=20, y=20, width=80, height=30)
        Tooltip(self.boton_ayuda, "help\nAbrir ventana de ayuda")

        
    def abrir_registro(self):
        self.ventana.withdraw()
        VentanaRegistro(self.ventana)
        
    def volver_a_principal(self):
        self.ventana.deiconify()
        
    def abrir_inicio_sesion(self):
        self.ventana.withdraw()
        VentanaInicioSesion(self.ventana)

    def mostrar_ayuda(self):
        messagebox.showinfo(
        "Ayuda",
        "Solo estudiantes pueden registrarse desde este botón (Registrarse).\n"
        "Si eres administrador o recepcionista, debes iniciar sesión y solicitar tu inscripción al administrador."
    )



