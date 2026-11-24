from abc import ABC, abstractmethod


class MetodoPago(ABC):
    def __init__(self, monto):
        self.monto = monto

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, valor):
        if valor <= 0:
            raise ValueError("Monto invalido")
        self.__monto = round(valor, 2)

    @abstractmethod
    def procesar_pago(self, total):
        pass

    @abstractmethod
    def permite_delivery(self):
        pass


class Efectivo(MetodoPago):
    def __init__(self, monto, monto_recibido):
        super().__init__(monto)
        self.monto_recibido = monto_recibido

    @property
    def monto_recibido(self):
        return self.__monto_recibido

    @monto_recibido.setter
    def monto_recibido(self, valor):
        if valor <= 0:
            raise ValueError("Monto recibido invalido")
        self.__monto_recibido = round(valor, 2)

    def calcular_cambio(self, total):
        if self.__monto_recibido < total:
            raise ValueError("No alcanza el dinero recibido")
        return round(self.__monto_recibido - total, 2)

    def procesar_pago(self, total):
        self.calcular_cambio(total)
        return round(total, 2)

    def permite_delivery(self):
        return True


class QR(MetodoPago):
    def __init__(self, monto, codigo):
        super().__init__(monto)
        self.codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if len(valor) != 10 or not valor.isdigit():
            raise ValueError("El codigo QR debe tener 10 digitos")
        self.__codigo = valor

    def procesar_pago(self, total):
        return round(total, 2)

    def permite_delivery(self):
        return True


class Tarjeta(MetodoPago):
    def __init__(self, monto, comision=0.03):
        super().__init__(monto)
        self.comision = comision

    @property
    def comision(self):
        return self.__comision

    @comision.setter
    def comision(self, valor):
        self.__comision = valor

    def procesar_pago(self, total):
        return round(total * (1 + self.__comision), 2)

    def permite_delivery(self):
        return False