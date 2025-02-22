import tkinter as tk
from tkinter import messagebox

class TiendaVirtual(tk.Tk):
    def __init__(self, productos: list[str]):
        super().__init__()

        self.title("Tienda Virtual de Electrónicos")
        self.geometry("600x400")

        self.productos_frame = tk.Frame(self)
        self.productos_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.producto_var = tk.StringVar()

        for producto in productos:
            producto_button = tk.Button(self.productos_frame, text=producto, command=lambda p=producto: self.agregar_producto(p))
            producto_button.pack(pady=5)

        self.carrito_text = tk.Text(self, height=10, width=30)
        self.carrito_text.insert(tk.END, "Carrito de compras:\n")
        self.carrito_text.config(state=tk.DISABLED)
        self.carrito_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.botones_frame = tk.Frame(self)
        self.botones_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.ver_button = tk.Button(self.botones_frame, text="Ver Carrito", command=self.ver_carrito)
        self.ver_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def agregar_producto(self, producto):
        self.carrito_text.config(state=tk.NORMAL)
        self.carrito_text.insert(tk.END, "- " + producto + "\n")
        self.carrito_text.config(state=tk.DISABLED)

    def ver_carrito(self):
        messagebox.showinfo("Carrito de Compras", "Productos en el carrito:\n" + self.carrito_text.get("1.0", tk.END))


