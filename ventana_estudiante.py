from email.mime import image
import tkinter as tk
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk 


class Estudiante:
    def __init__(self, cedula, nombre, apellido, telefono, email):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

        self.imagenes = {}

        # Llama a la función que construye la interfaz
        self.ventana = tk.Tk()
        self.ventana.title(f"Bienvenido {self.nombre}")
        self.ventana.geometry("900x600")
        self.ventana.configure(bg="white")

        self.construir_interfaz()
        self.ventana.mainloop()

    def construir_interfaz(self):

        self.btn_cursos = ttk.Button(self.ventana, text="CURSOS", command=lambda: self.activar_boton(self.btn_cursos))
        self.btn_cursos.place(x=240, y=30, width=120, height=40)

        self.btn_mis_cursos = ttk.Button(self.ventana, text="MIS CURSOS", command=lambda: self.activar_boton(self.btn_mis_cursos))
        self.btn_mis_cursos.place(x=380, y=30, width=120, height=40)

        self.btn_perfil = ttk.Button(self.ventana, text="PERFIL", command=lambda: self.activar_boton(self.btn_perfil))
        self.btn_perfil.place(x=520, y=30, width=120, height=40)

        self.activar_boton(self.btn_cursos)

        self.btn_volver = ttk.Button(self.ventana, text="VOLVER", command=self.ventana.destroy)
        self.btn_volver.place(x=20, y=30, width=100, height=30)

        self.btn_ayuda = ttk.Button(self.ventana, text="AYUDA")
        self.btn_ayuda.place(x=780, y=30, width=100, height=30)

        # Crear tarjetas de cursos
        self.crear_tarjeta_curso("CURSO DE BARISMO", 100, 150, "imagenes\\barista.png",
                                 "Aprende a preparar café de calidad y técnicas de barismo.")
        
        self.crear_tarjeta_curso("CURSO DE TECNICO CELULARES", 350, 150, "imagenes\\reparacion.png",
                                 "Aprende a reparar dispositivos móviles y técnicas de diagnóstico.")
        
        self.crear_tarjeta_curso("CURSO DE ATLETISMO", 600, 150, "imagenes\\Sin título (2).png",
                                 "Mejora tu rendimiento deportivo con este curso de atletismo.")

    def activar_boton(self, boton_activo):
        for b in [self.btn_cursos, self.btn_mis_cursos, self.btn_perfil]:
            b.configure(style="TButton")
        boton_activo.configure(style="Active.TButton")

    def crear_tarjeta_curso(self, nombre, x, y, ruta_imagen,descripcion):
        tarjeta = tk.Frame(self.ventana, bg="white", highlightbackground="black", highlightthickness=2)
        tarjeta.place(x=x, y=y, width=230, height=300)

        # Cargar imagen
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((230,300))
        imagen_tk = ImageTk.PhotoImage(imagen)
        self.imagenes[nombre] = imagen_tk

        fondo = tk.Label(tarjeta, image=self.imagenes[nombre], bg="white")
        fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # texto y boton encima de la imagen
        tk.Label(tarjeta, text=nombre, font=("Arial", 10, "bold"), bg="white", wraplength=180, justify="center").place(relx=0.5, rely=0.75, anchor="center")
        tk.Button(tarjeta, text="Ver curso", bg="#c82333", fg="white").place(relx=0.5, rely=0.9, anchor="center")

        # Descripción del curso
        lbl_descripcion = tk.Label(self.ventana, text=descripcion, font=("Arial", 12), bg="white", wraplength=180, justify="center")
        lbl_descripcion.place(x=x, y=y+310, width=230)


if __name__ == "__main__":
    estudiante1 = Estudiante("12345678", "Juan", "Pérez", "321654987", "juanp@gmail.com")
