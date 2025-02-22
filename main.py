import views.TiendaVirtual as tienda

if __name__ == "__main__":
    app = tienda.TiendaVirtual(["Laptop", "Smartphone", "Tablet", "Smartwatch"])
    app.mainloop()