import views.TiendaVirtual as tienda


product_list = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "TV"]

if __name__ == "__main__":
    app = tienda.TiendaVirtual(product_list)
    app.mainloop()