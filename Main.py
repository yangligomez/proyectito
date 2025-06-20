import tkinter as tk
from view.ventanaPrincipal import VentanaPrincipal
class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.app = VentanaPrincipal(self.root, usar_root=True)
        self.root.mainloop()

Main()
