import tkinter as tk
from Tooltip import Tooltip
import tkinter.messagebox as messagebox
from utils import centrar_ventana
import re
import random

# Base simulada de usuarios existentes
usuarios_existentes = ["Ejuan123", "Eana456", "Epedro789"]

def generar_usuario_unico(nombre, usuarios_existentes):
    inicial = 'E'
    nombre_simple = nombre.strip().split()[0].lower()
    while True:
        numero = random.randint(100, 999)
        usuario = f"{inicial}{nombre_simple}{numero}"
        if usuario not in usuarios_existentes:
            return usuario

def validar_campos_registro(nombre, apellido, cedula, fecha_nacimiento, contrasena, correo):
    # Verifica si todos los campos están vacíos
    if not nombre and not apellido and not cedula and not fecha_nacimiento and not contrasena and not correo:
        messagebox.showerror("Error", "Por favor, completa todos los campos antes de registrarte.")
        return False, None, None

    nombre = nombre.strip().lower()
    apellido = apellido.strip().lower()

    # Nombre: mínimo 2 letras, solo letras
    if not nombre or len(nombre) < 2 or not nombre.isalpha():
        messagebox.showerror("Error", "El campo nombre es obligatorio y debe tener al menos 2 letras (solo letras).")
        return False, None, None

    # Apellido: mínimo 3 letras, solo letras
    if not apellido or len(apellido) < 3 or not apellido.isalpha():
        messagebox.showerror("Error", "El campo apellido es obligatorio y debe tener al menos 3 letras (solo letras).")
        return False, None, None

    # Cédula: mínimo 6 caracteres, solo números
    if not cedula or len(cedula) < 6 or not cedula.isdigit():
        messagebox.showerror("Error", "La cédula es obligatoria, debe tener al menos 6 dígitos y solo contener números.")
        return False, None, None

    # Fecha de nacimiento: formato obligatorio (por ejemplo, DD/MM/AAAA)
    if not fecha_nacimiento or not re.match(r"^\d{2}/\d{2}/\d{4}$", fecha_nacimiento):
        messagebox.showerror("Error", "La fecha de nacimiento es obligatoria y debe tener el formato DD/MM/AAAA.")
        return False, None, None

    # Correo electrónico: formato válido
    if not correo or not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
        messagebox.showerror("Error", "El correo es obligatorio y debe tener un formato válido (ejemplo: usuario@dominio.com).")
        return False, None, None

    # Contraseña: mínimo 8 caracteres, al menos una minúscula, una mayúscula, un número y un caracter especial
    if len(contrasena) < 8:
        messagebox.showerror("Error", "La contraseña es obligatoria y debe tener al menos 8 caracteres.")
        return False, None, None
    if not re.search(r"[a-z]", contrasena):
        messagebox.showerror("Error", "La contraseña debe contener al menos una letra minúscula.")
        return False, None, None
    if not re.search(r"[A-Z]", contrasena):
        messagebox.showerror("Error", "La contraseña debe contener al menos una letra mayúscula.")
        return False, None, None
    if not re.search(r"\d", contrasena):
        messagebox.showerror("Error", "La contraseña debe contener al menos un número.")
        return False, None, None
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena):
        messagebox.showerror("Error", "La contraseña debe contener al menos un caracter especial.")
        return False, None, None

    return True, nombre, apellido

class VentanaRegistro:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana = tk.Toplevel()
        self.ventana.title("Crear cuenta")
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
            text="Registro de Usuario",
            bg="#f0f2f5",
            fg="#1877f2",
            font=("Segoe UI", 28, "bold")
        )
        self.label.place(relx=0.5, y=80, anchor=tk.CENTER)

        # Subtítulo
        self.label2 = tk.Label(
            self.ventana,
            text="Completa tus datos:",
            bg="#f0f2f5",
            fg="#050505",
            font=("Segoe UI", 16)
        )
        self.label2.place(relx=0.5, y=130, anchor=tk.CENTER)

        entry_font = ("Segoe UI", 14)
        label_font = ("Segoe UI", 14)

        # Nombre completo
        self.lbl_nombre = tk.Label(self.ventana, text="Nombre completo:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_nombre.place(relx=0.25, y=200, anchor=tk.W)
        self.entry_nombre = tk.Entry(self.ventana, font=entry_font, width=30, bd=2, relief="groove")
        self.entry_nombre.place(relx=0.45, y=200, anchor=tk.W)
        Tooltip(self.entry_nombre, "Ingresa tu nombre completo, si solo tienes un nombre, ingrésalo aquí")

        # Apellidos
        self.lbl_apellidos = tk.Label(self.ventana, text="Apellidos:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_apellidos.place(relx=0.25, y=250, anchor=tk.W)
        self.entry_apellidos = tk.Entry(self.ventana, font=entry_font, width=30, bd=2, relief="groove")
        self.entry_apellidos.place(relx=0.45, y=250, anchor=tk.W)
        Tooltip(self.entry_apellidos, "Ingresa tus apellidos, si solo tienes uno, ingrésalo aquí")

        # Cédula
        self.lbl_cedula = tk.Label(self.ventana, text="Cédula:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_cedula.place(relx=0.25, y=300, anchor=tk.W)
        self.entry_cedula = tk.Entry(self.ventana, font=entry_font, width=20, bd=2, relief="groove")
        self.entry_cedula.place(relx=0.45, y=300, anchor=tk.W)
        Tooltip(self.entry_cedula, "Ingresa tu número de cédula o documento de identidad, sin puntos, comas o espacios")  

        # Fecha de nacimiento
        self.lbl_fecha = tk.Label(self.ventana, text="Fecha de nacimiento (DD/MM/AAAA):", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_fecha.place(relx=0.25, y=350, anchor=tk.W)
        self.entry_fecha = tk.Entry(self.ventana, font=entry_font, width=15, bd=2, relief="groove")
        self.entry_fecha.place(relx=0.62, y=350, anchor=tk.W)
        Tooltip(self.entry_fecha, "Ingresa tu fecha de nacimiento en formato DD/MM/AAAA\n si es un solo dígito de mes o día, usa un 0 al inicio")

        # Correo electrónico (opcional)
        self.lbl_correo = tk.Label(self.ventana, text="Correo electrónico:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_correo.place(relx=0.25, y=400, anchor=tk.W)
        self.entry_correo = tk.Entry(self.ventana, font=entry_font, width=30, bd=2, relief="groove")
        self.entry_correo.place(relx=0.55, y=400, anchor=tk.W)
        Tooltip(self.entry_correo, "Ingresa tu correo electrónico activo, si no tienes uno, puedes dejarlo en blanco")

        # Crear contraseña
        self.lbl_password = tk.Label(self.ventana, text="Crear contraseña:", bg="#f0f2f5", fg="#1877f2", font=("Segoe UI", 14))
        self.lbl_password.place(relx=0.25, y=450, anchor=tk.W)
        self.entry_password = tk.Entry(self.ventana, font=("Segoe UI", 14), width=30, bd=2, relief="groove", show="*")
        self.entry_password.place(relx=0.55, y=450, anchor=tk.W)
        Tooltip(self.entry_password, "Crea una contraseña segura, debe tener al menos 8 caracteres\n debe tener al menos una letra mayúscula, una minúscula, un número y un carácter especial")
        
        #boton de volver 
        self.btnVolver = tk.Button(
            self.ventana,
            text="Regresar",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 14),
            bd=0,
            activebackground="#166fe5",
            activeforeground="white",
            cursor="hand2",
            relief="flat"
        )   
        self.btnVolver.place(x=20, y=30, anchor=tk.W, width=100, height=30)
        Tooltip(self.btnVolver, "Volver a la ventana principal")
        self.btnVolver.config(command=self.regresar_a_principal)
        Tooltip(self.btnVolver, "Volver a la ventana de inicio")
        
        #boton ayuda 
        self.btnAyuda = tk.Button(
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
        self.btnAyuda.place(x=880, y=30, anchor=tk.E, width=100, height=30)
        Tooltip(self.btnAyuda, "Abrir ventana de ayuda")
        self.btnAyuda.config(command=self.mostrar_ayuda)
        
        
        # Botón Registrar
        self.btn_registrar = tk.Button(
            self.ventana,
            text="Registrar",
            bg="#1877f2",
            fg="white",
            font=("Segoe UI", 18, "bold"),
            bd=0,
            activebackground="#166fe5",
            activeforeground="white",
            cursor="hand2",
            relief="flat",
            command=self.registrar_usuario  # <--- ESTA LÍNEA ES LA CLAVE
        )
        self.btn_registrar.place(relx=0.5, y=560, anchor=tk.CENTER, width=220, height=50)
        Tooltip(self.btn_registrar, "Registrar usuario con los datos ingresados")
        
    def mostrar_ayuda(self):
        messagebox.showinfo(
            "Ayuda",
            "Por favor, completa todos los campos requeridos para registrarte.\n"
            "La contraseña debe ser segura y fácil de recordar.\n"
            "Si tienes dudas, contacta al soporte."
        )
        
    def regresar_a_principal(self):
        self.ventana_principal.deiconify()
        self.ventana.destroy()
    
    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellidos.get()
        cedula = self.entry_cedula.get()
        fecha_nacimiento = self.entry_fecha.get()
        contrasena = self.entry_password.get()
        correo = self.entry_correo.get()

        valido, nombre_min, apellido_min = validar_campos_registro(
            nombre, apellido, cedula, fecha_nacimiento, contrasena, correo
        )
        if not nombre and not apellido and not cedula and not fecha_nacimiento and not contrasena and not correo:
            messagebox.showerror("Error", "Por favor, completa todos los campos antes de registrarte.")
            return False, None, None
        if valido:
            usuario = generar_usuario_unico(nombre_min, usuarios_existentes)
            usuarios_existentes.append(usuario)  # Simula guardar el usuario
            messagebox.showinfo(
                "Registro exitoso",
                f"¡Registro exitoso!\nTu usuario es: {usuario}"
            )
            # Aquí puedes limpiar los campos o cerrar la ventana si lo deseas

