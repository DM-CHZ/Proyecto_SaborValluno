from modelo.productos import Combo
from modelo.pedidos import PedidoLocal, EstadoPedido
from modelo.pagos import Efectivo


class Restaurante:
    def __init__(self):
        self.__productos = []
        self.__clientes = []
        self.__pedidos = []

    @property
    def productos(self):
        return self.__productos

    @property
    def clientes(self):
        return self.__clientes

    @property
    def pedidos(self):
        return self.__pedidos

    def registrar_producto(self, producto):
        self.__productos.append(producto)

    def armar_combo(self, productos):
        nombre = f"Combo {len(self.__productos) + 1}"
        combo = Combo(nombre, productos, 0.10)
        self.__productos.append(combo)
        return combo

    def listar_menu(self, dia):
        lista = []
        for p in self.__productos:
            if p.esta_disponible(dia):
                lista.append(p)
        return lista

    def registrar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def registrar_pedido(self, pedido):
        if isinstance(pedido, PedidoLocal):
            for p in self.__pedidos:
                if isinstance(p, PedidoLocal) and p.mesa == pedido.mesa:
                    if p.estado != EstadoPedido.ENTREGADO and p.estado != EstadoPedido.CANCELADO:
                        raise ValueError("Mesa ocupada")
        self.__pedidos.append(pedido)

    def cobrar_pedido(self, id_pedido, metodo):
        pedido = None
        for p in self.__pedidos:
            if p.id_pedido == id_pedido:
                pedido = p
        if pedido is None:
            raise ValueError("Pedido no encontrado")
        total = pedido.calcular_total()
        pedido.asignar_pago(metodo)
        pagado = metodo.procesar_pago(total)
        comp = f"COMPROBANTE\n{pedido.mostrar_detalle()}\nPagado: Bs {pagado}"
        if isinstance(metodo, Efectivo):
            comp += f"\nCambio: Bs {metodo.calcular_cambio(total)}"
        return comp

    def reporte_ventas(self, fecha):
        ventas = {"Local": 0, "Llevar": 0, "Delivery": 0}
        for p in self.__pedidos:
            if p.fecha_hora.date() == fecha and p.estado != EstadoPedido.CANCELADO and p.pago is not None:
                monto = p.pago.procesar_pago(p.calcular_total())
                if isinstance(p, PedidoLocal):
                    ventas["Local"] += monto
                elif p.__class__.__name__ == "PedidoLlevar":
                    ventas["Llevar"] += monto
                else:
                    ventas["Delivery"] += monto
        return ventas

    def productos_mas_vendidos(self):
        conteo = {}
        for p in self.__pedidos:
            if p.estado != EstadoPedido.CANCELADO:
                for d in p.detalles:
                    nom = d.producto.nombre
                    if nom in conteo:
                        conteo[nom] += d.cantidad
                    else:
                        conteo[nom] = d.cantidad
        lista = list(conteo.items())
        lista.sort(key=lambda x: x[1], reverse=True)
        return lista[:3]