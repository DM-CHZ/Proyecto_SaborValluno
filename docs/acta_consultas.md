# Acta de Consultas y Supuestos de Diseño

**Proyecto:** Sistema de Pedidos Sabor Valluno  
**Variante:** A  
**Fecha de definición:** 23/11/2026

> **Nota:** No se realizaron consultas directas al docente sobre ambigüedades del enunciado. Los siguientes criterios se definieron como supuestos de diseño del equipo (con apoyo de IA) para asegurar la consistencia entre el diagrama UML v2 y la implementación.

| N.º | Ambigüedad identificada | Criterio / Supuesto asumido | Justificación | Cómo se aplicó en el código |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Tiempo límite y compensación por retraso en delivery. | Se considera retraso cuando la entrega supera los **45 minutos** desde el registro, y la compensación es el **reembolso del costo de envío** (Bs 0 si fue gratis). | Es un estándar razonable para entregas locales y evita descontar sobre el costo de la comida. | Se implementaron `tiene_retraso()` y `calcular_compensacion()` en `PedidoDelivery` (`modelo/pedidos.py`). |
| 2 | Cobro de envase en pedidos para llevar que incluyen combos. | Se cobra **Bs 2,00 por cada plato** contenido dentro del combo; las bebidas no generan cargo de envase. | Mantiene la regla de la Variante A ("Bs 2 por cada plato") sin penalizar las bebidas incluidas en promociones. | Se creó el método polimórfico `contar_platos()` en `Producto` y `Combo` suma sus platos internos (`modelo/productos.py`). |
| 3 | Uso de tarjeta en pedidos por delivery (comisión del 3 %). | Los pedidos por delivery solo aceptan **Efectivo o QR**; el pago con tarjeta queda restringido a pedidos en local o para llevar. | Evita problemas de cobro físico con POS móvil en entregas a domicilio. | Se creó `permite_delivery()` en `MetodoPago` (`Tarjeta` retorna `False`) y se valida en `PedidoDelivery` (`modelo/pagos.py`). |
