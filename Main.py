from ventanaPrincipal import VentanaPrincipal
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root, usar_root=True)  # Nuevo argumento
    root.mainloop()