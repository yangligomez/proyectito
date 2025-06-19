from email.mime import image
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Estudiante:
    def __init__(self, cedula, nombre, apellido, telefono, email):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

        self.imagenes = {}

        # Ventana principal
        self.ventana = tk.Toplevel()
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

        # Botón CURSOS
        self.btn_cursos = ttk.Button(self.ventana, text="CURSOS", style="TButton",
                                     command=lambda: self.activar_boton(self.btn_cursos))
        self.btn_cursos.place(x=240, y=120, width=120, height=40)

        # Botón MIS CURSOS
        self.btn_mis_cursos = ttk.Button(self.ventana, text="MIS CURSOS", style="TButton",
                                         command=lambda: self.activar_boton(self.btn_mis_cursos))
        self.btn_mis_cursos.place(x=380, y=120, width=120, height=40)

        # Botón PERFIL
        self.btn_perfil = ttk.Button(self.ventana, text="PERFIL", style="TButton",
                                     command=lambda: self.activar_boton(self.btn_perfil))
        self.btn_perfil.place(x=520, y=120, width=120, height=40)

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

        # Botón AYUDA (rojo)
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

        # Crear tarjetas de cursos (más abajo para que no se encimen)
        self.crear_tarjeta_curso("CURSO DE BARISMO", 100, 200, "imagenes\\barista.png",
                                 "Aprende a preparar café de calidad y técnicas de barismo.")
        self.crear_tarjeta_curso("CURSO DE TECNICO CELULARES", 350, 200, "imagenes\\reparacion.png",
                                 "Aprende a reparar dispositivos móviles y técnicas de diagnóstico.")
        self.crear_tarjeta_curso("CURSO DE ATLETISMO", 600, 200, "imagenes\\Sin título (2).png",
                                 "Mejora tu rendimiento deportivo con este curso de atletismo.")

    def activar_boton(self, boton_activo):
        for b in [self.btn_cursos, self.btn_mis_cursos, self.btn_perfil]:
            b.configure(style="TButton")
        boton_activo.configure(style="Active.TButton")

    def crear_tarjeta_curso(self, nombre, x, y, ruta_imagen, descripcion):
        tarjeta = tk.Frame(self.ventana, bg="white", highlightbackground="#1877f2", highlightthickness=2)
        tarjeta.place(x=x, y=y, width=230, height=300)

        # Cargar imagen
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((230, 300))
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.imagenes[nombre] = imagen_tk

        fondo = tk.Label(tarjeta, image=self.imagenes[nombre], bg="white")
        fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Texto y botón encima de la imagen
        tk.Label(tarjeta, text=nombre, font=("Segoe UI", 10, "bold"),
                 bg="#f0f2f5", fg="#1877f2", wraplength=180, justify="center"
        ).place(relx=0.5, rely=0.75, anchor="center")
        tk.Button(tarjeta, text="Ver curso", bg="#1877f2", fg="white",
                  font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2",
                  activebackground="#166fe5", activeforeground="white"
        ).place(relx=0.5, rely=0.9, anchor="center")

        # Descripción del curso
        lbl_descripcion = tk.Label(self.ventana, text=descripcion,
                                   font=("Segoe UI", 12),
                                   bg="#f0f2f5", fg="#050505",
                                   wraplength=180, justify="center")
        lbl_descripcion.place(x=x, y=y+310, width=230)


if __name__ == "__main__":
    estudiante1 = Estudiante("12345678", "Juan", "Pérez", "321654987", "juanp@gmail.com")
