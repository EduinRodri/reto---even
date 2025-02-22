class Usuario:
    def __init__(self, nombre, contraseña, email):
        self.__nombre = nombre
        self.__contraseña = contraseña
        self.__email = email
    
    # Getters y Setters
    def get_nombre(self):
        return self.__nombre
    
    def get_contraseña(self):
        return self.__contraseña
    
    def get_email(self):
        return self.__email
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_contraseña(self, contraseña):
        self.__contraseña = contraseña
    
    def set_email(self, email):
        self.__email = email