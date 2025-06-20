import tkinter as tk
from Tooltip import Tooltip
import tkinter.messagebox as messagebox
from utils import centrar_ventana
import re
import random
from tkcalendar import DateEntry

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

def validar_campos_registro(nombre, apellido, cedula, telefono, fecha_nacimiento, contrasena, correo):
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

    # Teléfono: obligatorio, solo números, exactamente 10 dígitos
    if not telefono or not telefono.isdigit() or len(telefono) != 10:
        messagebox.showerror("Error", "El teléfono es obligatorio, debe contener solo números y tener exactamente 10 dígitos.")
        return False, None, None

    # Fecha de nacimiento: formato obligatorio (por ejemplo, DD/MM/AAAA)
    if not fecha_nacimiento or not re.match(r"^\d{2}/\d{2}/\d{4}$", fecha_nacimiento):
        messagebox.showerror("Error", "La fecha de nacimiento es obligatoria y debe tener el formato DD/MM/AAAA.")
        return False, None, None

    # Correo electrónico: formato válido
    if not correo or not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo):
        messagebox.showerror("Error", "El correo es obligatorio y debe tener un formato válido (ejemplo: usuario@dominio.com).")
        return False, None, None

    # Contraseña: mínimo 5 caracteres, al menos una minúscula, una mayúscula y un número
    if len(contrasena) < 5:
        messagebox.showerror("Error", "La contraseña es obligatoria y debe tener al menos 5 caracteres.")
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

        label_font = ("Segoe UI", 14)
        entry_font = ("Segoe UI", 13)

        # Título principal
        self.label = tk.Label(
            self.ventana,
            text="Registro de Usuario",
            bg="#f0f2f5",
            fg="#1877f2",
            font=("Segoe UI", 28, "bold")
        )
        self.label.place(relx=0.5, y=80, anchor=tk.CENTER)

        # Alineación y ancho uniforme
        x_label = 250
        x_entry = 450
        y_start = 160
        y_step = 50
        entry_width = 270  # Ancho uniforme para todos los campos

        # Nombre
        self.lbl_nombre = tk.Label(self.ventana, text="Nombre:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_nombre.place(x=x_label, y=y_start)
        self.entry_nombre = tk.Entry(self.ventana, font=entry_font)
        self.entry_nombre.place(x=x_entry, y=y_start, width=entry_width)

        # Apellido
        self.lbl_apellido = tk.Label(self.ventana, text="Apellido:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_apellido.place(x=x_label, y=y_start + y_step)
        self.entry_apellido = tk.Entry(self.ventana, font=entry_font)
        self.entry_apellido.place(x=x_entry, y=y_start + y_step, width=entry_width)

        # Cédula
        self.lbl_cedula = tk.Label(self.ventana, text="Cédula:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_cedula.place(x=x_label, y=y_start + 2 * y_step)
        self.entry_cedula = tk.Entry(self.ventana, font=entry_font)
        self.entry_cedula.place(x=x_entry, y=y_start + 2 * y_step, width=entry_width)

        # Teléfono 
        self.lbl_telefono = tk.Label(self.ventana, text="Teléfono:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_telefono.place(x=x_label, y=y_start + 3 * y_step)
        self.entry_telefono = tk.Entry(self.ventana, font=entry_font)
        self.entry_telefono.place(x=x_entry, y=y_start + 3 * y_step, width=entry_width)

        # Fecha de nacimiento (con calendario)
        self.lbl_fecha = tk.Label(self.ventana, text="Fecha de nacimiento:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_fecha.place(x=x_label, y=y_start + 4 * y_step)
        self.entry_fecha = DateEntry(self.ventana, font=entry_font, width=22, bd=2, relief="groove", date_pattern="dd/MM/yyyy")
        self.entry_fecha.place(x=x_entry, y=y_start + 4 * y_step, width=entry_width)

        # Correo
        self.lbl_correo = tk.Label(self.ventana, text="Correo:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_correo.place(x=x_label, y=y_start + 5 * y_step)
        self.entry_correo = tk.Entry(self.ventana, font=entry_font)
        self.entry_correo.place(x=x_entry, y=y_start + 5 * y_step, width=entry_width)

        # Contraseña
        self.lbl_password = tk.Label(self.ventana, text="Contraseña:", bg="#f0f2f5", fg="#1877f2", font=label_font)
        self.lbl_password.place(x=x_label, y=y_start + 6 * y_step)
        self.entry_password = tk.Entry(self.ventana, font=entry_font, show="*")
        self.entry_password.place(x=x_entry, y=y_start + 6 * y_step, width=entry_width)
        import tkinter.ttk as ttk  # Asegúrate de importar esto arriba del archivo


        # Botón ver contraseña (icono ojo)
        self.iconoVer = tk.PhotoImage(file=r"icons/eye.png")
        self.btnVer = tk.Button(self.ventana, image=self.iconoVer, bd=0, bg="#f0f2f5", activebackground="#f0f2f5", cursor="hand2")
        self.btnVer.place(width=30, height=30, x=x_entry + entry_width - 30, y=y_start + 6 * y_step)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        # Tooltips (opcional)
        Tooltip(self.entry_nombre, "Ingresa tu nombre\n Debe tener al menos 2 letras\n y solo contener letras")
        Tooltip(self.entry_apellido, "Ingresa tu apellido\n Debe tener al menos 3 letras\n y solo contener letras")
        Tooltip(self.entry_cedula, "Ingresa tu cédula\nSolo debe contener números, sin espacios, comas o puntos")
        Tooltip(self.entry_telefono, "Ingresa tu número de teléfono\nDebe tener exactamente 10 dígitos\nSolo debe contener números enteros")
        Tooltip(self.entry_fecha, "Selecciona tu fecha de nacimiento")
        Tooltip(self.entry_correo, "Ingresa tu correo electrónico activo\n Ejemplo:usuarionuevo@gmail.com")
        Tooltip(self.entry_password, "Crea una contraseña segura\n Debe tener al menos 5 caracteres,\nuna mayúscula, una minúscula y un número")
        
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
            "La contraseña debe tener al menos 5 caracteres,\n"
            "una mayúscula, una minúscula y un número.\n"
            "Asegúrate de ingresar un correo electrónico válido.\n"
            "El nombre y apellido deben contener solo letras.\n"
            "Si tienes dudas, contacta al soporte."
            "Estos campos son obligatorios\n"
            "para poder acceder a los cursos y servicios de la plataforma.\n"
        )
        
    def regresar_a_principal(self):
        self.ventana_principal.deiconify()
        self.ventana.destroy()
    
    def registrar_usuario(self):
        from conexion import obtener_conexion

        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        cedula = self.entry_cedula.get()
        telefono = self.entry_telefono.get()
        fecha_nacimiento = self.entry_fecha.get()
        contrasena = self.entry_password.get()
        correo = self.entry_correo.get()
        rol = self.combo_rol.get()

        valido, nombre_min, apellido_min = validar_campos_registro(
            nombre, apellido, cedula, telefono, fecha_nacimiento, contrasena, correo
        )

        if not valido:
            return

        usuario = generar_usuario_unico(nombre_min, usuarios_existentes)
        usuarios_existentes.append(usuario)

        try:
            conn = obtener_conexion()
            cursor = conn.cursor()

            if rol == "estudiante":
                cursor.execute("""
                    INSERT INTO estudiante (cedula, nombre, apellido, telefono, fecha_nacimiento, email)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (cedula, nombre, apellido, telefono, fecha_nacimiento, correo))
            elif rol == "recepcionista":
                cursor.execute("""
                    INSERT INTO recepcionista (cedula, nombre, apellido, telefono, email)
                    VALUES (%s, %s, %s, %s, %s)
                """, (cedula, nombre, apellido, telefono, correo))
            else:
                messagebox.showerror("Error", "Rol no válido.")
                return

            # Registrar en la tabla de usuario
            cursor.execute("""
                INSERT INTO usuario (cedula, username, password, rol)
                VALUES (%s, %s, %s, %s)
            """, (cedula, usuario, contrasena, rol))

            conn.commit()
            messagebox.showinfo("Registro exitoso", f"¡Registro completado!\nTu usuario es: {usuario}")
            self.ventana.destroy()
            self.ventana_principal.deiconify()

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar: {e}")
    def verCaracteres(self, event):
        # Si el evento es <Enter>, muestra la contraseña
        if event.type == tk.EventType.Enter:
            self.entry_password.config(show="")
        # Si el evento es <Leave>, oculta la contraseña
        elif event.type == tk.EventType.Leave:
            self.entry_password.config(show="*")

