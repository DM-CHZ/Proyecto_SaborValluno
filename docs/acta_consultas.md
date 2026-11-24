# Acta de Consultas al Cliente (Docente)

**Proyecto:** Sistema de Pedidos Sabor Valluno  
**Variante:** A

| N.º | Fecha | Pregunta realizada al docente | Respuesta del docente | Cómo se aplicó en el código |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 10/11/2026 | En la regla de retraso en delivery, ¿a partir de cuántos minutos se considera retraso y cuál es la compensación? | Se considera retraso si pasa de 45 minutos desde que se registra el pedido, y la compensación es devolver el costo de envío. | Se crearon los métodos `tiene_retraso()` y `calcular_compensacion()` en `PedidoDelivery` (`modelo/pedidos.py`). |
| 2 | 12/11/2026 | Si un pedido para llevar incluye un combo con 2 platos y 1 bebida, ¿se cobra envase por el combo o por cada plato? | Se cobra Bs 2 por cada plato que esté dentro del combo; las bebidas no pagan envase. | Se creó el método `contar_platos()` en `Producto` y `Combo` suma los platos internos (`modelo/productos.py`). |
| 3 | 17/11/2026 | ¿Un pedido por delivery se puede pagar con tarjeta sumando el 3 % de comisión? | No, para delivery solo se acepta efectivo o QR. | Se creó `permite_delivery()` en `MetodoPago` (`Tarjeta` devuelve `False`) y se valida en `PedidoDelivery` (`modelo/pagos.py`). |