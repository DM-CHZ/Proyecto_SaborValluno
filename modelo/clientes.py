class Cliente:
    def __init__(self, id_cliente, nombre, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        if valor <= 0:
            raise ValueError("ID invalido")
        self.__id_cliente = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if valor == "":
            raise ValueError("Nombre vacio")
        self.__nombre = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        if not self.validar_telefono(valor):
            raise ValueError("Telefono debe tener 8 digitos y empezar con 6 o 7")
        self.__telefono = valor

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, valor):
        if valor == "":
            raise ValueError("Direccion vacia")
        self.__direccion = valor

    def validar_telefono(self, telefono):
        if len(telefono) == 8 and telefono.isdigit() and (telefono[0] == "6" or telefono[0] == "7"):
            return True
        return False