# Sistema de Pedidos - Sabor Valluno

Proyecto Integrador de Programación Orientada a Objetos (POO) desarrollado en Python 3 utilizando únicamente la biblioteca estándar.

## Variante asignada: Variante A
* **Descuento del combo:** 10 % sobre la suma de sus productos.
* **Envase para llevar:** Bs 2,00 por cada plato (incluidos platos dentro de combos).
* **Envío gratis en delivery:** Desde Bs 150,00 de subtotal, únicamente en la zona Cercado.
* **Pedido mínimo en delivery:** Bs 40,00.
* **Regla adicional:** El chicharrón se vende únicamente los días domingo.

## Estructura del proyecto
* `modelo/`: Contiene las clases base y subclases (`productos.py`, `pedidos.py`, `pagos.py`, `clientes.py`).
* `restaurante.py`: Clase gestora principal (`Restaurante`).
* `main.py`: Aplicación de consola con menú interactivo.
* `pruebas.py`: Casos de prueba automatizados con `assert`.
* `docs/`: Diagramas UML v1 y v2, acta de consultas y registro de uso de IA.

## Cómo ejecutar
1. Abrir una terminal en la carpeta raíz del proyecto.
2. Para iniciar el sistema de consola:
   ```bash
   python main.py