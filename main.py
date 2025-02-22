from images import images
from model.producto import Producto, producto
import views.TiendaVirtual as tienda


product_list = [Producto("Laptop", 14000000, "images/laptop.jpg"), Producto("Mouse", 100000, "images/mouse.jpg"), Producto("Teclado", 840000, "images/teclado.jpg")]

if __name__ == "__main__":
    app = tienda.TiendaVirtual(product_list)
    app.mainloop()