from email.mime import image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class Estudiante:
    def __init__(self, cedula, nombre, apellido, telefono, email):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

        self.imagenes = {}
        self.cursos_registrados = []  # Lista para almacenar los cursos registrados

        # Definir cursos disponibles ANTES de crear la ventana
        self.cursos_disponibles = [
            "Curso de Barismo",
            "Curso de Técnico en Celulares", 
            "Curso de Atletismo"
        ]

        # Ventana principal
        self.ventana = tk.Tk()
        self.ventana.title(f"Bienvenido {self.nombre}")
        self.ventana.geometry("900x600")
        self.ventana.configure(bg="#f0f2f5")  # Color de fondo

        self.construir_interfaz()
        self.ventana.mainloop()

    def construir_interfaz(self):
        # Estilos para ttk
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton",
                        font=("Segoe UI", 12, "bold"),
                        background="#1877f2",
                        foreground="white")
        style.map("TButton",
                  background=[("active", "#166fe5")])
        style.configure("Active.TButton",
                        font=("Segoe UI", 12, "bold"),
                        background="#166fe5",
                        foreground="white")

        # Boton CURSOS
        self.btn_cursos = ttk.Button(self.ventana, text="CURSOS", style="TButton",
                                     command=self.abrir_cursos)
        self.btn_cursos.place(x=240, y=100, width=120, height=40)

        # Boton MIS CURSOS
        self.btn_mis_cursos = ttk.Button(self.ventana, text="MIS CURSOS", style="TButton",
                                         command=self.abrir_mis_cursos)
        self.btn_mis_cursos.place(x=380, y=100, width=120, height=40)

        # Boton PERFIL
        self.btn_perfil = ttk.Button(self.ventana, text="PERFIL", style="TButton",
                                     command=self.abrir_perfil)
        self.btn_perfil.place(x=520, y=100, width=120, height=40)

        self.activar_boton(self.btn_cursos)

        # Botón VOLVER (azul)
        self.btn_volver = tk.Button(self.ventana, text="VOLVER",
                                   bg="#1877f2", fg="white",
                                   font=("Segoe UI", 12, "bold"),
                                   bd=0, cursor="hand2", relief="flat",
                                   activebackground="#166fe5",
                                   activeforeground="white",
                                   command=self.ventana.destroy)
        self.btn_volver.place(x=20, y=30, width=100, height=30)

        # Botón AYUDA 
        self.btn_ayuda = tk.Button(self.ventana, text="AYUDA",
                                  bg="#f22618", fg="white",
                                  font=("Segoe UI", 12, "bold"),
                                  bd=0, cursor="hand2", relief="flat",
                                  activebackground="#d11a0f",
                                  activeforeground="white")
        self.btn_ayuda.place(x=780, y=30, width=100, height=30)

        # Título principal (más arriba)
        tk.Label(self.ventana,
                 text=f"Bienvenido, {self.nombre}",
                 bg="#f0f2f5",
                 fg="#1877f2",
                 font=("Segoe UI", 28, "bold")
        ).place(relx=0.5, y=60, anchor="center")

        # Crear contenedor inicial
        self.crear_contenedor()
        self.mostrar_cursos_disponibles()

    def crear_contenedor(self):
        if hasattr(self, 'contenedor'):
            self.contenedor.destroy()
        self.contenedor = tk.Frame(self.ventana, bg="white")
        self.contenedor.place(x=0, y=150, width=900, height=500)

    def activar_boton(self, boton_activo):
        for b in [self.btn_cursos, self.btn_mis_cursos, self.btn_perfil]:
            b.configure(style="TButton")
        boton_activo.configure(style="Active.TButton")

    def crear_tarjeta_curso(self, nombre, x, y, ruta_imagen, descripcion, es_mis_cursos=False):
        tarjeta = tk.Frame(self.contenedor, bg="white", highlightbackground="#1877f2", highlightthickness=2)
        tarjeta.place(x=x, y=y, width=230, height=300)

        # Cargar imagen
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((230, 300))
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.imagenes[nombre] = imagen_tk

            fondo = tk.Label(tarjeta, image=self.imagenes[nombre], bg="white")
            fondo.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            # Si no se puede cargar la imagen, usar un fondo de color
            fondo = tk.Label(tarjeta, text="Imagen no disponible", bg="#f0f2f5", fg="gray")
            fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Texto del curso
        tk.Label(tarjeta, text=nombre, font=("Segoe UI", 10, "bold"),
                 bg="#f0f2f5", fg="#1877f2", wraplength=180, justify="center"
        ).place(relx=0.5, rely=0.75, anchor="center")

        # Botón según el contexto
        if es_mis_cursos:
            # Botón para cancelar curso
            btn_cancelar = tk.Button(tarjeta, text="Cancelar curso", bg="#f22618", fg="white",
                                   font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2",
                                   command=lambda: self.cancelar_curso(nombre))
            btn_cancelar.place(relx=0.5, rely=0.9, anchor="center")
        else:
            # Botón para inscribirse
            tk.Button(tarjeta, text="Ver curso", bg="#1877f2", fg="white",
                      font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2",
                      command=lambda: self.inscribirse_curso(nombre)
            ).place(relx=0.5, rely=0.9, anchor="center")

        # Descripción del curso
        lbl_descripcion = tk.Label(self.contenedor, text=descripcion,
                                   font=("Segoe UI", 12),
                                   bg="white", fg="#050505",
                                   wraplength=180, justify="center")
        lbl_descripcion.place(x=x, y=y+310, width=230)

        return tarjeta

    def mostrar_cursos_disponibles(self):
        self.crear_contenedor()

        self.crear_tarjeta_curso("Curso de Barismo", 50, 50, "imagenes\\barista.png",
                                "Aprende a preparar café de calidad y técnicas de barismo.")
        self.crear_tarjeta_curso("Curso de Técnico en Celulares", 300, 50, "imagenes\\reparacion.png",
                                "Aprende a reparar dispositivos móviles y técnicas de diagnóstico.")
        self.crear_tarjeta_curso("Curso de Atletismo", 550, 50, "imagenes\\Sin título (2).png",
                                "Mejora tu rendimiento deportivo con este curso de atletismo.")

    def mostrar_mis_cursos(self):
        self.crear_contenedor()

        if not self.cursos_registrados:
            mensaje = tk.Label(self.contenedor, text="No estás inscrito en ningún curso.",
                              font=("Segoe UI", 16), bg="white", fg="gray")
            mensaje.place(relx=0.5, rely=0.5, anchor="center")
            return

        # Información de los cursos
        info_cursos = {
            "Curso de Barismo": {
                "imagen": "imagenes\\barista.png",
                "descripcion": "Aprende a preparar café de calidad y técnicas de barismo."
            },
            "Curso de Técnico en Celulares": {
                "imagen": "imagenes\\reparacion.png",
                "descripcion": "Aprende a reparar dispositivos móviles y técnicas de diagnóstico."
            },
            "Curso de Atletismo": {
                "imagen": "imagenes\\Sin título (2).png",
                "descripcion": "Mejora tu rendimiento deportivo con este curso de atletismo."
            }
        }

        x_pos = 50
        for curso in self.cursos_registrados:
            if curso in info_cursos:
                data = info_cursos[curso]
                self.crear_tarjeta_curso(curso, x_pos, 50, data["imagen"], 
                                       data["descripcion"], es_mis_cursos=True)
                x_pos += 250  # Espacio entre tarjetas

    def mostrar_perfil(self):
        self.crear_contenedor()

        tk.Label(self.contenedor, text="Perfil del Estudiante", font=("Segoe UI", 18, "bold"),
                bg="white", fg="#1877f2").place(x=280, y=20)

        campos = ["Nombre", "Apellido", "Cédula", "Teléfono", "Correo"]
        valores = [self.nombre, self.apellido, self.cedula, self.telefono, self.email]

        y = 80
        for campo, valor in zip(campos, valores):
            tk.Label(self.contenedor, text=f"{campo}:", font=("Segoe UI", 12),
                    bg="white", fg="black").place(x=180, y=y)

            entry = tk.Entry(self.contenedor, font=("Segoe UI", 12), width=30)
            entry.insert(0, valor)
            entry.config(state="readonly")
            entry.place(x=300, y=y)
            y += 40

    def abrir_mis_cursos(self):
        self.activar_boton(self.btn_mis_cursos)
        self.mostrar_mis_cursos()

    def abrir_cursos(self):
        self.activar_boton(self.btn_cursos)
        self.mostrar_cursos_disponibles()

    def abrir_perfil(self):
        self.activar_boton(self.btn_perfil)
        self.mostrar_perfil()

    def cancelar_curso(self, nombre):
        if nombre in self.cursos_registrados:
            self.cursos_registrados.remove(nombre)
            messagebox.showinfo("Curso cancelado", f"Has cancelado tu inscripción a {nombre}")
            self.mostrar_mis_cursos()  # Actualizar la vista
        else:
            messagebox.showwarning("Error", f"No estás inscrito en {nombre}")

    def inscribirse_curso(self, nombre_curso):
        if nombre_curso not in self.cursos_registrados:
            self.cursos_registrados.append(nombre_curso)
            messagebox.showinfo("¡Inscripción exitosa!", f"Te has inscrito a {nombre_curso}")
            # Opcional: cambiar automáticamente a la pestaña de mis cursos
            self.abrir_mis_cursos()
        else:
            messagebox.showwarning("Ya inscrito", f"Ya estás inscrito en {nombre_curso}")


if __name__ == "__main__":
    estudiante1 = Estudiante("12345678", "Juan", "Pérez", "321654987", "juanp@gmail.com")