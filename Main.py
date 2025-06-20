import tkinter as tk
from ventanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root, usar_root=True)
    root.mainloop()
