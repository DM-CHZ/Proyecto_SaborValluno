from datetime import datetime, timedelta
from modelo.productos import Plato, Bebida, Combo
from modelo.clientes import Cliente
from modelo.pedidos import PedidoLocal, PedidoLlevar, PedidoDelivery, EstadoPedido
from modelo.pagos import Efectivo, QR, Tarjeta


# 1. Caso de referencia Variante A
silpancho = Plato("Silpancho", 35, "Segundo", ["domingo", "lunes"])
moco = Bebida("Mocochinchi", 6, "vaso")
combo1 = Combo("Combo 1", [silpancho, moco], 0.10)
assert combo1.calcular_precio() == 36.90

cli = Cliente(1, "Ana", "71234567", "Quillacollo")
ped1 = PedidoDelivery(1, cli, "Quillacollo")
ped1.agregar_producto(combo1, 2)
assert ped1.calcular_total() == 88.80

# 2. Combo dentro de otro combo
sopa = Plato("Sopa Mani", 15, "Sopa", ["domingo", "lunes"])
combo2 = Combo("Combo 2", [combo1, sopa], 0.10)
assert combo2.calcular_precio() == 46.71
assert combo2.contar_platos() == 2

# 3. Chicharron solo domingos
chicha = Plato("Chicharron", 50, "Segundo", ["domingo"])
assert chicha.esta_disponible("domingo") == True
assert chicha.esta_disponible("martes") == False

# 4. Jarra x3
jarra = Bebida("Chicha", 8, "jarra")
assert jarra.calcular_precio() == 24

# 5. Para llevar Bs 2 por plato
ped2 = PedidoLlevar(2, cli)
ped2.agregar_producto(combo2, 1)
assert ped2.calcular_cargos() == 4.0

# 6. Envio gratis desde 150 solo Cercado
ped3 = PedidoDelivery(3, cli, "Cercado")
ped3.agregar_producto(chicha, 3)
assert ped3.calcular_cargos() == 0.0

# 7. Estado invalido lanza error
ped4 = PedidoLocal(4, cli, 5)
ped4.agregar_producto(silpancho, 1)
ped4.cambiar_estado(EstadoPedido.EN_PREPARACION)
try:
    ped4.cambiar_estado(EstadoPedido.CANCELADO)
    assert False
except ValueError:
    pass

# 8. Tarjeta 3% y retraso delivery
tarjeta = Tarjeta(35)
assert tarjeta.procesar_pago(35) == 36.05
ped5 = PedidoDelivery(5, cli, "Sacaba", datetime.now() + timedelta(minutes=50))
assert ped5.tiene_retraso() == True
assert ped5.calcular_compensacion() == 15.0

print("Todas las pruebas pasaron bien.")