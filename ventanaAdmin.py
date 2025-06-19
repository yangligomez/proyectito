import tkinter as tk
from Tooltip import Tooltip
from utils import centrar_ventana

class VentanaAdmin:
    def __init__(self, ventana_principal):
        self.ventana = tk.Toplevel(ventana_principal)
        self.ventana.title("Panel de Administrador")
        self.ventana.geometry("900x600")
        centrar_ventana(self.ventana, 900, 600)
        self.ventana.config(bg="#f0f2f5")
        self.ventana.resizable(0, 0)
        self.ventana.lift()
        self.ventana.focus_force()
        self.ventana.grab_set()

        color_fondo = "#f0f2f5"
        color_principal = "#1877f2"
        fuente_titulo = ("Segoe UI", 28, "bold")
        fuente_boton = ("Segoe UI", 14, "bold")

        # Título
        self.label = tk.Label(
            self.ventana,
            text="Panel de Administrador",
            bg=color_fondo,
            fg=color_principal,
            font=fuente_titulo
        )
        self.label.place(relx=0.5, y=60, anchor=tk.CENTER)

        # Menú de funcionalidades principales
        y_menu = 140
        x_menu = 120
        sep_menu = 200

        # Gestión de Recepcionistas
        self.menu_recep = tk.Menubutton(self.ventana, text="Recepcionistas", font=fuente_boton, bg="white", fg=color_principal, bd=1, relief="solid", width=18, cursor="hand2")
        self.menu_recep.menu = tk.Menu(self.menu_recep, tearoff=0)
        self.menu_recep["menu"] = self.menu_recep.menu
        self.menu_recep.menu.add_command(label="Registrar nuevo", command=self.registrar_recepcionista)
        self.menu_recep.menu.add_command(label="Consultar/Editar/Eliminar", command=self.gestionar_recepcionistas)
        self.menu_recep.place(x=x_menu, y=y_menu, width=180, height=40)
        Tooltip(self.menu_recep, "Gestiona los recepcionistas del sistema")

        # Gestión de Estudiantes
        self.menu_estudiantes = tk.Menubutton(self.ventana, text="Estudiantes", font=fuente_boton, bg="white", fg=color_principal, bd=1, relief="solid", width=18, cursor="hand2")
        self.menu_estudiantes.menu = tk.Menu(self.menu_estudiantes, tearoff=0)
        self.menu_estudiantes["menu"] = self.menu_estudiantes.menu
        self.menu_estudiantes.menu.add_command(label="Ver lista", command=self.ver_lista_estudiantes)
        self.menu_estudiantes.menu.add_command(label="Buscar por cédula/nombre", command=self.buscar_estudiante)
        self.menu_estudiantes.menu.add_command(label="Editar/Eliminar", command=self.gestionar_estudiantes)
        self.menu_estudiantes.place(x=x_menu + sep_menu, y=y_menu, width=180, height=40)
        Tooltip(self.menu_estudiantes, "Gestiona los estudiantes registrados")

        # Gestión de Cursos
        self.menu_cursos = tk.Menubutton(self.ventana, text="Oferta de Cursos", font=fuente_boton, bg="white", fg=color_principal, bd=1, relief="solid", width=18, cursor="hand2")
        self.menu_cursos.menu = tk.Menu(self.menu_cursos, tearoff=0)
        self.menu_cursos["menu"] = self.menu_cursos.menu
        self.menu_cursos.menu.add_command(label="Crear nuevo curso", command=self.crear_curso)
        self.menu_cursos.menu.add_command(label="Modificar/Cerrar curso", command=self.modificar_curso)
        self.menu_cursos.menu.add_command(label="Ver cursos activos/cerrados", command=self.ver_cursos)
        self.menu_cursos.place(x=x_menu + 2*sep_menu, y=y_menu, width=180, height=40)
        Tooltip(self.menu_cursos, "Gestiona la oferta de cursos")

        # Informes e informes de inscripción
        self.btn_informes = tk.Button(self.ventana, text="Informes de Inscripción", font=fuente_boton, bg="white", fg=color_principal, bd=1, relief="solid", cursor="hand2", command=self.generar_informes)
        self.btn_informes.place(x=180, y=220, width=220, height=40)
        Tooltip(self.btn_informes, "Genera y exporta informes de inscripción")

        # Estadísticas generales
        self.btn_estadisticas = tk.Button(self.ventana, text="Estadísticas Generales", font=fuente_boton, bg="white", fg=color_principal, bd=1, relief="solid", cursor="hand2", command=self.ver_estadisticas)
        self.btn_estadisticas.place(x=500, y=220, width=220, height=40)
        Tooltip(self.btn_estadisticas, "Visualiza estadísticas del sistema")

        # Opciones comunes
        self.btn_cambiar_pass = tk.Button(self.ventana, text="Cambiar Contraseña", font=fuente_boton, bg="#e7f3ff", fg=color_principal, bd=1, relief="solid", cursor="hand2", command=self.cambiar_contrasena)
        self.btn_cambiar_pass.place(x=180, y=500, width=220, height=40)
        Tooltip(self.btn_cambiar_pass, "Cambia tu contraseña de administrador")

        self.btn_cerrar = tk.Button(self.ventana, text="Cerrar sesión", font=fuente_boton, bg="#f22618", fg="white", bd=0, cursor="hand2", relief="flat", command=self.cerrar_admin)
        self.btn_cerrar.place(x=500, y=500, width=220, height=40)
        Tooltip(self.btn_cerrar, "Cerrar sesión y regresar al login")

    # Métodos vacíos para implementar después
    def registrar_recepcionista(self):
        pass

    def gestionar_recepcionistas(self):
        pass

    def ver_lista_estudiantes(self):
        pass

    def buscar_estudiante(self):
        pass

    def gestionar_estudiantes(self):
        pass

    def crear_curso(self):
        pass

    def modificar_curso(self):
        pass

    def ver_cursos(self):
        pass

    def generar_informes(self):
        pass

    def ver_estadisticas(self):
        pass

    def cambiar_contrasena(self):
        pass

    def cerrar_admin(self):
        self.ventana.destroy()
        # Si quieres mostrar la ventana principal de nuevo, descomenta la siguiente línea:
        # self.ventana.master.deiconify()

# Para pruebas rápidas:
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    VentanaAdmin(root)
    root.mainloop()