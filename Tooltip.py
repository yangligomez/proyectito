import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
        self.widget.bind("<ButtonPress>", self.hide_tooltip)  # Oculta el tooltip antes del click

    def show_tooltip(self, event=None):
        self.hide_tooltip()
        try:
            x, y, _, _ = self.widget.bbox("insert")
        except Exception:
            x, y = 0, 0
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        # Hace la ventana tooltip "passthrough" para eventos del mouse (solo en Windows 8+)
        if hasattr(self.tooltip, 'attributes'):
            try:
                self.tooltip.attributes('white', '#ffffe0')
            except Exception:
                pass
        label = tk.Label(
            self.tooltip,
            text=self.text,
            background="#ffffe0",
            foreground="black",
            relief=tk.SOLID,
            borderwidth=1,
            font=("tahoma", "10", "normal")
        )
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None