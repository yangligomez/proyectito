import tkinter as tk
from tkinter import messagebox
from utils import centrar_ventana

class VentanaVerificacionAdmin:
    def __init__(self, ventana_principal, callback_exito):
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Iniciar sesión Administrador")
        self.ventana.geometry("900x600")
        centrar_ventana(self.ventana, 900, 600)
        self.ventana.config(bg="#f0f2f5")
        self.ventana.resizable(0, 0)
        self.ventana.lift()
        self.ventana.focus_force()
        self.ventana.grab_set()

        self.callback_exito = callback_exito

        # Título principal
        tk.Label(
            self.ventana,
            text="Iniciar sesión como Administrador",
            bg="#f0f2f5",
            fg="#1877f2",
            font=("Segoe UI", 28, "bold")
        ).place(relx=0.5, y=100, anchor="center")

        label_font = ("Segoe UI", 14)
        entry_font = ("Segoe UI", 13)
        x_label = 250
        x_entry = 450
        y_usuario = 220
        y_password = 290
        entry_width = 270

        # Usuario
        tk.Label(self.ventana, text="Usuario:", bg="#f0f2f5", fg="#1877f2", font=label_font).place(x=x_label, y=y_usuario)
        self.entry_usuario = tk.Entry(self.ventana, font=entry_font)
        self.entry_usuario.place(x=x_entry, y=y_usuario, width=entry_width)

        # Contraseña
        tk.Label(self.ventana, text="Contraseña:", bg="#f0f2f5", fg="#1877f2", font=label_font).place(x=x_label, y=y_password)
        self.entry_password = tk.Entry(self.ventana, font=entry_font, show="*")
        self.entry_password.place(x=x_entry, y=y_password, width=entry_width)

        # Botón ver contraseña (icono ojo)
        self.iconoVer = tk.PhotoImage(file=r"icons/eye.png")
        self.btnVer = tk.Button(self.ventana, image=self.iconoVer, bd=0, bg="#f0f2f5", activebackground="#f0f2f5", cursor="hand2")
        self.btnVer.place(width=30, height=30, x=x_entry + entry_width - 30, y=y_password)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        # Botón ingresar
        self.btn_ingresar = tk.Button(
            self.ventana,
            text="Ingresar",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 18, "bold"),
            bd=0,
            activebackground="#166fe5",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.verificar
        )
        self.btn_ingresar.place(relx=0.5, y=400, anchor="center", width=220, height=50)

    def verCaracteres(self, event):
        # Si el evento es <Enter>, muestra la contraseña
        if event.type == tk.EventType.Enter:
            self.entry_password.config(show="")
        # Si el evento es <Leave>, oculta la contraseña
        elif event.type == tk.EventType.Leave:
            self.entry_password.config(show="*")

    def verificar(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        # Aquí puedes poner la lógica real de verificación
        if usuario == "admin" and password == "admin123":
            self.ventana.destroy()
            self.callback_exito()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")