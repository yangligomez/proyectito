import tkinter as tk
from Tooltip import Tooltip
from utils import centrar_ventana

class VentanaInicioSesion:
    def __init__(self, ventana, ventana_principal):
        self.ventana = ventana
        self.ventana_principal = ventana_principal

        self.ventana.title("Iniciar Sesión")
        self.ventana.geometry("900x600")
        centrar_ventana(self.ventana, 900, 600)
        self.ventana.config(bg="#f0f2f5")
        self.ventana.resizable(0, 0)
        self.ventana.lift()
        self.ventana.focus_force()
        self.ventana.grab_set()

        # Título principal
        self.label = tk.Label(
            self.ventana,
            text="Iniciar Sesión",
            bg="#f0f2f5",
            fg="#1877f2",
            font=("Segoe UI", 28, "bold")
        )
        self.label.place(relx=0.5, y=100, anchor=tk.CENTER)

        # Subtítulo
        self.label2 = tk.Label(
            self.ventana,
            text="Ingresa tus credenciales para continuar",
            bg="#f0f2f5",
            fg="#050505",
            font=("Segoe UI", 16)
        )
        self.label2.place(relx=0.5, y=160, anchor=tk.CENTER)

        entry_font = ("Segoe UI", 14)
        label_font = ("Segoe UI", 14)

        # Usuario
        self.lbl_usuario = tk.Label(self.ventana, text="Usuario:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_usuario.place(relx=0.3, y=250, anchor=tk.W)
        self.entry_usuario = tk.Entry(self.ventana, font=entry_font, width=30, bd=2, relief="groove")
        self.entry_usuario.place(relx=0.5, y=250, anchor=tk.W)
        Tooltip(self.entry_usuario, "Ingresa tu nombre de usuario o correo registrado")

        # Contraseña
        self.lbl_password = tk.Label(self.ventana, text="Contraseña:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_password.place(relx=0.3, y=320, anchor=tk.W)
        self.entry_password = tk.Entry(self.ventana, font=entry_font, width=30, bd=2, relief="groove", show="*")
        self.entry_password.place(relx=0.5, y=320, anchor=tk.W)
        Tooltip(self.entry_password, "Ingresa tu contraseña")

        # Botón Iniciar Sesión
        self.btn_iniciar = tk.Button(
            self.ventana,
            text="Iniciar Sesión",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 16, "bold"),
            bd=0,
            activebackground="#166fe5",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.verificar_credenciales,
        )
        self.btn_iniciar.place(relx=0.5, y=400, anchor=tk.CENTER, width=220, height=45)
        Tooltip(self.btn_iniciar, "Haz clic para iniciar sesión")

        # Botón Volver
        self.btn_volver = tk.Button(
            self.ventana,
            text="Regresar",
            bg="#1877f2",
            fg="#f8f9fa",
            font=("Segoe UI", 14),
            bd=0,
            activebackground="#d8dadf",
            activeforeground="#1877f2",
            cursor="hand2",
            relief="flat",
            command=self.regresar_a_principal
        )
        self.btn_volver.place(x=20, y=30, anchor=tk.W, width=100, height=30)
        Tooltip(self.btn_volver, "Volver a la ventana principal")

        # Botón Ayuda
        self.btn_ayuda = tk.Button(
            self.ventana,
            text="Ayuda",
            bg="#f22618",
            fg="white",
            font=("Segoe UI", 14),
            bd=0,
            activebackground="#166fe5",
            activeforeground="white",
            cursor="hand2",
            relief="flat"
        )
        self.btn_ayuda.place(x=880, y=30, anchor=tk.E, width=100, height=30)
        Tooltip(self.btn_ayuda, "Abrir ventana de ayuda")

    def regresar_a_principal(self):
        self.ventana_principal.deiconify()
        self.ventana.destroy()

    def verificar_credenciales(self):
        from conexion import obtener_conexion
        from tkinter import messagebox
        from view.ventanaRecepcionista import VentanaRecepcionista
        from view.ventanaVerificacionAdmin import VentanaVerificacionAdmin
        from view.ventanaVerificacionEstud import VentanaVerificacionEstud

        usuario = self.entry_usuario.get()
        clave = self.entry_password.get()

        conn = obtener_conexion()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT rol FROM usuario WHERE username=%s AND password=%s", (usuario, clave))
            resultado = cursor.fetchone()

            if resultado:
                rol = resultado[0]
                messagebox.showinfo("Éxito", f"Sesión iniciada como {rol}")
                self.ventana.destroy()  # Cierra solo la ventana de inicio de sesión

                # Abre la ventana correspondiente al rol
                if rol == "estudiante":
                    VentanaVerificacionEstud(self.ventana_principal, lambda: None)
                elif rol == "recepcionista":
                    VentanaRecepcionista(self.ventana_principal, usuario)
                elif rol == "administrador":
                    VentanaVerificacionAdmin(self.ventana_principal, lambda: None)
                else:
                    messagebox.showerror("Error", "Rol no reconocido.")
            else:
                messagebox.showerror("Error", "Credenciales inválidas.")
        except Exception as e:
            print("Error al verificar credenciales:", e)