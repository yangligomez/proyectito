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
        self.boton1.place(relx=0.5, y=300, anchor=tk.CENTER, width=360, height=50)
        Tooltip(
    self.boton1,
    "Solo Estudiantes pueden registrarse aquí.\n"
    "Si eres administrador o recepcionista da Click en Iniciar sesión."
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
        
        #Boton cerrar
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
        Tooltip(self.boton_cerrar, "Cerrar la aplicación")
        

        # --- Botón Menú para Iniciar Sesión ---
        self.rol_seleccionado = tk.StringVar(value="Iniciar Sesión")
        self.menu_button = tk.Menubutton(
            self.ventana,
            textvariable=self.rol_seleccionado,
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
            width=20
        )
        self.menu = tk.Menu(self.menu_button, tearoff=0)
        self.menu.add_command(label="Estudiante", command=lambda: self.seleccionar_rol("Estudiante"))
        self.menu.add_command(label="Recepcionista", command=lambda: self.seleccionar_rol("Recepcionista"))
        self.menu.add_command(label="Administrador", command=lambda: self.seleccionar_rol("Administrador"))
        self.menu_button.config(menu=self.menu)
        self.menu_button.place(relx=0.5, y=380, anchor=tk.CENTER, width=360, height=50)
        Tooltip(self.menu_button, "Selecciona el tipo de usuario para iniciar sesión")

        # Botón para confirmar inicio de sesión
        self.boton_confirmar = tk.Button(
            self.ventana,
            text="Confirmar",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 14, "bold"),
            bd=0,
            activebackground="#166fe5",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.abrir_inicio_sesion
        )
        self.boton_confirmar.place(relx=0.5, y=440, anchor=tk.CENTER, width=200, height=40)
        Tooltip(self.boton_confirmar, "Haz clic para iniciar sesión con el rol seleccionado")

    def abrir_registro(self):
        self.ventana.withdraw()
        VentanaRegistro(self.ventana)
        
    def volver_a_principal(self):
        self.ventana.deiconify()
        
    def seleccionar_rol(self, rol):
        self.rol_seleccionado.set(f"Iniciar Sesión {rol}")
        self.rol_actual = rol

    def abrir_inicio_sesion(self):
        rol = getattr(self, "rol_actual", None)
        if not rol:
            messagebox.showwarning("Selecciona un rol", "Por favor selecciona un rol para iniciar sesión.")
            return
        self.ventana.withdraw()
        # Aquí puedes abrir la ventana correspondiente según el rol
        if rol == "Estudiante":
            VentanaInicioSesion(self.ventana, rol="estudiante")
        elif rol == "Recepcionista":
            VentanaInicioSesion(self.ventana, rol="recepcionista")
        elif rol == "Administrador":
            VentanaInicioSesion(self.ventana, rol="admin")
        else:
            messagebox.showerror("Error", "Rol no reconocido.")

    def mostrar_ayuda(self):
        messagebox.showinfo(
        "Ayuda",
        "Solo Estudiantes pueden registrarse desde el botón (Registrarse).\n"
        "Si eres Estudiante registrado puedes iniciar sesión desde el botón (Iniciar Sesión).\n"
        "Si eres Administrador o Recepcionista, debes iniciar sesión para acceder a tu inscripción y/o consultas."
        "Para más información, contacta al servidor."
    )



