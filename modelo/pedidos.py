from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum


class EstadoPedido(Enum):
    REGISTRADO = "REGISTRADO"
    EN_PREPARACION = "EN_PREPARACION"
    LISTO = "LISTO"
    ENTREGADO = "ENTREGADO"
    CANCELADO = "CANCELADO"


class DetallePedido:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    @property
    def producto(self):
        return self.__producto

    @producto.setter
    def producto(self, valor):
        self.__producto = valor

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor < 1 or valor > 20:
            raise ValueError("La cantidad debe ser entre 1 y 20")
        self.__cantidad = valor

    def calcular_subtotal(self):
        return round(self.__producto.calcular_precio() * self.__cantidad, 2)


class Pedido(ABC):
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.__fecha_hora = datetime.now()
        self.__estado = EstadoPedido.REGISTRADO
        self.cliente = cliente
        self.__detalles = []
        self.__pago = None

    @property
    def id_pedido(self):
        return self.__id_pedido

    @id_pedido.setter
    def id_pedido(self, valor):
        self.__id_pedido = valor

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    @property
    def estado(self):
        return self.__estado

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):
        self.__cliente = valor

    @property
    def detalles(self):
        return list(self.__detalles)

    @property
    def pago(self):
        return self.__pago

    def agregar_producto(self, producto, cantidad):
        if self.__estado != EstadoPedido.REGISTRADO:
            raise ValueError("Solo se modifica en estado REGISTRADO")
        for d in self.__detalles:
            if d.producto.nombre == producto.nombre:
                d.cantidad = d.cantidad + cantidad
                return
        self.__detalles.append(DetallePedido(producto, cantidad))

    def eliminar_producto(self, producto):
        if self.__estado != EstadoPedido.REGISTRADO:
            raise ValueError("Solo se modifica en estado REGISTRADO")
        for d in self.__detalles:
            if d.producto.nombre == producto.nombre:
                self.__detalles.remove(d)
                return
        raise ValueError("Producto no encontrado en el pedido")

    def _acepta_pago(self, pago):
        return True

    def asignar_pago(self, pago):
        if not self._acepta_pago(pago):
            raise ValueError("Este pedido no acepta ese metodo de pago")
        pago.procesar_pago(self.calcular_total())
        self.__pago = pago

    def cambiar_estado(self, nuevo):
        if self.__estado == EstadoPedido.REGISTRADO and (nuevo == EstadoPedido.EN_PREPARACION or nuevo == EstadoPedido.CANCELADO):
            self.__estado = nuevo
        elif self.__estado == EstadoPedido.EN_PREPARACION and nuevo == EstadoPedido.LISTO:
            self.__estado = nuevo
        elif self.__estado == EstadoPedido.LISTO and nuevo == EstadoPedido.ENTREGADO:
            self.__estado = nuevo
        else:
            raise ValueError("Cambio de estado no valido")

    def contar_platos(self):
        total = 0
        for d in self.__detalles:
            total = total + (d.producto.contar_platos() * d.cantidad)
        return total

    def calcular_subtotal(self):
        suma = 0
        for d in self.__detalles:
            suma = suma + d.calcular_subtotal()
        return round(suma, 2)

    @abstractmethod
    def calcular_cargos(self):
        pass

    def calcular_total(self):
        return round(self.calcular_subtotal() + self.calcular_cargos(), 2)

    def mostrar_detalle(self):
        texto = f"Pedido #{self.__id_pedido} - Cliente: {self.__cliente.nombre} - Estado: {self.__estado.value}\n"
        for d in self.__detalles:
            texto += f"  {d.producto.nombre} x{d.cantidad} = Bs {d.calcular_subtotal()}\n"
        texto += f"Subtotal: Bs {self.calcular_subtotal()}\n"
        texto += f"Cargos: Bs {self.calcular_cargos()}\n"
        texto += f"Total: Bs {self.calcular_total()}"
        return texto


class PedidoLocal(Pedido):
    def __init__(self, id_pedido, cliente, mesa):
        super().__init__(id_pedido, cliente)
        self.mesa = mesa

    @property
    def mesa(self):
        return self.__mesa

    @mesa.setter
    def mesa(self, valor):
        if valor < 1 or valor > 15:
            raise ValueError("Mesa debe ser del 1 al 15")
        self.__mesa = valor

    def calcular_cargos(self):
        return 0.0


class PedidoLlevar(Pedido):
    def __init__(self, id_pedido, cliente, costo_envase=2.0):
        super().__init__(id_pedido, cliente)
        self.costo_envase = costo_envase

    @property
    def costo_envase(self):
        return self.__costo_envase

    @costo_envase.setter
    def costo_envase(self, valor):
        self.__costo_envase = valor

    def calcular_cargos(self):
        return round(self.contar_platos() * self.__costo_envase, 2)


class PedidoDelivery(Pedido):
    ZONAS = {"cercado": 8.0, "quillacollo": 15.0, "sacaba": 15.0, "vinto": 20.0}

    def __init__(self, id_pedido, cliente, zona, hora_entrega=None):
        super().__init__(id_pedido, cliente)
        self.zona = zona
        self.__envio_gratis_desde = 150.0
        self.__pedido_minimo = 40.0
        self.hora_entrega = hora_entrega

    @property
    def zona(self):
        return self.__zona

    @zona.setter
    def zona(self, valor):
        if valor.lower() not in PedidoDelivery.ZONAS:
            raise ValueError("Zona no valida")
        self.__zona = valor.lower()

    @property
    def costo_envio(self):
        return PedidoDelivery.ZONAS[self.__zona]

    @property
    def hora_entrega(self):
        return self.__hora_entrega

    @hora_entrega.setter
    def hora_entrega(self, valor):
        self.__hora_entrega = valor

    def calcular_cargos(self):
        sub = self.calcular_subtotal()
        if sub < self.__pedido_minimo:
            raise ValueError("No llega al pedido minimo de Bs 40")
        if self.__zona == "cercado" and sub >= self.__envio_gratis_desde:
            return 0.0
        return self.costo_envio

    def _acepta_pago(self, pago):
        return pago.permite_delivery()

    def tiene_retraso(self):
        if self.__hora_entrega is None:
            return False
        minutos = (self.__hora_entrega - self.fecha_hora).total_seconds() / 60
        return minutos > 45

    def calcular_compensacion(self):
        if self.tiene_retraso():
            return self.costo_envio
        return 0.0