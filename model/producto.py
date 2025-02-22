class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio
    
    def get_stock(self):
        return self.__stock
    
    def set_stock(self, stock):
        self.__stock = stock
        
    def set_precio(self, precio):
        self.__precio = precio  
        
    def set_nombre(self, nombre):
        self.__nombre = nombre

    