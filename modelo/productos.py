from abc import ABC, abstractmethod


class Producto(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if valor == "":
            raise ValueError("Nombre vacio")
        self.__nombre = valor

    @property
    def precio_base(self):
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self.__precio_base = round(valor, 2)

    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def esta_disponible(self, dia):
        pass

    def contar_platos(self):
        return 0


class Plato(Producto):
    def __init__(self, nombre, precio_base, tipo_comida, dias_venta):
        super().__init__(nombre, precio_base)
        self.tipo_comida = tipo_comida
        self.dias_venta = dias_venta

    @property
    def tipo_comida(self):
        return self.__tipo_comida

    @tipo_comida.setter
    def tipo_comida(self, valor):
        self.__tipo_comida = valor

    @property
    def dias_venta(self):
        return self.__dias_venta

    @dias_venta.setter
    def dias_venta(self, valor):
        self.__dias_venta = valor

    def calcular_precio(self):
        return self.precio_base

    def esta_disponible(self, dia):
        for d in self.__dias_venta:
            if d.lower() == dia.lower():
                return True
        return False

    def contar_platos(self):
        return 1


class Bebida(Producto):
    def __init__(self, nombre, precio_base, tamano):
        super().__init__(nombre, precio_base)
        self.tamano = tamano

    @property
    def tamano(self):
        return self.__tamano

    @tamano.setter
    def tamano(self, valor):
        if valor.lower() != "vaso" and valor.lower() != "jarra":
            raise ValueError("Tamano debe ser vaso o jarra")
        self.__tamano = valor.lower()

    def calcular_precio(self):
        if self.__tamano == "jarra":
            return round(self.precio_base * 3, 2)
        return self.precio_base

    def esta_disponible(self, dia):
        return True

    def contar_platos(self):
        return 0


class Combo(Producto):
    def __init__(self, nombre, productos, descuento=0.10):
        super().__init__(nombre, 1)
        self.descuento = descuento
        self.__productos = []
        self.productos = productos

    @property
    def descuento(self):
        return self.__descuento

    @descuento.setter
    def descuento(self, valor):
        self.__descuento = valor

    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self, lista):
        if len(lista) < 2:
            raise ValueError("Un combo necesita 2 o mas productos")
        for p in lista:
            if p == self:
                raise ValueError("Un combo no puede contenerse a si mismo")
        self.__productos = lista

    def calcular_precio(self):
        suma = 0
        for p in self.__productos:
            suma = suma + p.calcular_precio()
        return round(suma * (1 - self.__descuento), 2)

    def esta_disponible(self, dia):
        for p in self.__productos:
            if not p.esta_disponible(dia):
                return False
        return True

    def contar_platos(self):
        total = 0
        for p in self.__productos:
            total = total + p.contar_platos()
        return total