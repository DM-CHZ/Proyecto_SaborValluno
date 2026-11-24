from datetime import date, datetime
from modelo.productos import Plato, Bebida
from modelo.clientes import Cliente
from modelo.pedidos import PedidoLocal, PedidoLlevar, PedidoDelivery, EstadoPedido
from modelo.pagos import Efectivo, QR, Tarjeta
from restaurante import Restaurante


rest = Restaurante()
p1 = Plato("Silpancho", 35, "Segundo", ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"])
p2 = Plato("Chicharron", 50, "Segundo", ["domingo"])
b1 = Bebida("Mocochinchi", 6, "vaso")
rest.registrar_producto(p1)
rest.registrar_producto(p2)
rest.registrar_producto(b1)
rest.armar_combo([p1, b1])
rest.registrar_cliente(Cliente(1, "Carlos Mamani", "71234567", "Av. Blanco Galindo"))

num_pedido = 1

while True:
    print("\n=== SABOR VALLUNO ===")
    print("1. Registrar producto")
    print("2. Armar combo")
    print("3. Ver menu por dia")
    print("4. Registrar cliente")
    print("5. Crear pedido")
    print("6. Agregar o quitar producto a pedido")
    print("7. Ver detalle del pedido")
    print("8. Cambiar estado del pedido")
    print("9. Cobrar pedido")
    print("10. Reporte de ventas y top 3")
    print("0. Salir")

    opcion = input("\nElige una opcion: ")
    print()

    try:
        if opcion == "1":
            print("1. Plato")
            print("2. Bebida")
            tipo = input("Elige tipo: ")
            nom = input("Nombre: ")
            precio = float(input("Precio base: "))
            if tipo == "1":
                tc = input("Tipo comida: ")
                dias = input("Dias (separados por coma): ").split(",")
                rest.registrar_producto(Plato(nom, precio, tc, dias))
            else:
                print("1. Vaso")
                print("2. Jarra")
                t = input("Elige tamano: ")
                if t == "1":
                    tam = "vaso"
                else:
                    tam = "jarra"
                rest.registrar_producto(Bebida(nom, precio, tam))
            print("Producto guardado.")

        elif opcion == "2":
            for i in range(len(rest.productos)):
                print(i + 1, rest.productos[i].nombre)
            nums = input("Numeros separados por coma: ").split(",")
            elegidos = []
            for n in nums:
                elegidos.append(rest.productos[int(n) - 1])
            combo = rest.armar_combo(elegidos)
            print("Combo creado:", combo.nombre)

        elif opcion == "3":
            dia = input("Dia de la semana: ")
            for p in rest.listar_menu(dia):
                print("-", p.nombre, "Bs", p.calcular_precio())

        elif opcion == "4":
            idc = int(input("ID cliente: "))
            nom = input("Nombre: ")
            tel = input("Telefono: ")
            dir_c = input("Direccion: ")
            rest.registrar_cliente(Cliente(idc, nom, tel, dir_c))
            print("Cliente guardado.")

        elif opcion == "5":
            for c in rest.clientes:
                print(c.id_cliente, "-", c.nombre)
            idc = int(input("ID cliente: "))
            cli = None
            for c in rest.clientes:
                if c.id_cliente == idc:
                    cli = c
            print("1. Local")
            print("2. Para llevar")
            print("3. Delivery")
            tipo = input("Elige tipo de pedido: ")
            if tipo == "1":
                mesa = int(input("Mesa (1-15): "))
                ped = PedidoLocal(num_pedido, cli, mesa)
            elif tipo == "2":
                ped = PedidoLlevar(num_pedido, cli)
            else:
                print("1. Cercado")
                print("2. Quillacollo")
                print("3. Sacaba")
                print("4. Vinto")
                z = input("Elige zona: ")
                zonas = {"1": "Cercado", "2": "Quillacollo", "3": "Sacaba", "4": "Vinto"}
                ped = PedidoDelivery(num_pedido, cli, zonas[z])
            rest.registrar_pedido(ped)
            print("Pedido creado con ID:", num_pedido)
            num_pedido += 1

        elif opcion == "6":
            idp = int(input("ID pedido: "))
            ped = None
            for p in rest.pedidos:
                if p.id_pedido == idp:
                    ped = p
            print("1. Agregar producto")
            print("2. Quitar producto")
            acc = input("Elige accion: ")
            for i in range(len(rest.productos)):
                print(i + 1, rest.productos[i].nombre)
            idx = int(input("Numero producto: ")) - 1
            if acc == "1":
                cant = int(input("Cantidad: "))
                ped.agregar_producto(rest.productos[idx], cant)
            else:
                ped.eliminar_producto(rest.productos[idx])
            print("Pedido actualizado.")

        elif opcion == "7":
            idp = int(input("ID pedido: "))
            for p in rest.pedidos:
                if p.id_pedido == idp:
                    print(p.mostrar_detalle())

        elif opcion == "8":
            idp = int(input("ID pedido: "))
            print("1. EN_PREPARACION")
            print("2. LISTO")
            print("3. ENTREGADO")
            print("4. CANCELADO")
            op_est = input("Elige nuevo estado: ")
            estados = {
                "1": EstadoPedido.EN_PREPARACION,
                "2": EstadoPedido.LISTO,
                "3": EstadoPedido.ENTREGADO,
                "4": EstadoPedido.CANCELADO
            }
            for p in rest.pedidos:
                if p.id_pedido == idp:
                    p.cambiar_estado(estados[op_est])
                    if isinstance(p, PedidoDelivery) and p.estado == EstadoPedido.ENTREGADO:
                        p.hora_entrega = datetime.now()
            print("Estado cambiado.")

        elif opcion == "9":
            idp = int(input("ID pedido: "))
            ped = None
            for p in rest.pedidos:
                if p.id_pedido == idp:
                    ped = p
            total = ped.calcular_total()
            print("Total a pagar: Bs", total)
            print("1. Efectivo")
            print("2. QR")
            print("3. Tarjeta")
            mp = input("Elige metodo de pago: ")
            if mp == "1":
                rec = float(input("Monto recibido: "))
                pago = Efectivo(total, rec)
            elif mp == "2":
                cod = input("Codigo 10 digitos: ")
                pago = QR(total, cod)
            else:
                pago = Tarjeta(total)
            print(rest.cobrar_pedido(idp, pago))

        elif opcion == "10":
            print("Ventas hoy:", rest.reporte_ventas(date.today()))
            print("Top 3 vendidos:", rest.productos_mas_vendidos())

        elif opcion == "0":
            break

    except Exception as e:
        print("Error:", e)