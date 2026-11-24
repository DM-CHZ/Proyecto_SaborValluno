# Registro Personal de Uso de IA

* **Estudiante:** Deymar Abram Mamani Chavez
* **Variante:** A
* **Fecha de elaboración:** 23/11/2026

## Detalle de consultas realizadas

### 1. Estructura base y modelo de dominio
* **Fecha:** 23/11/2026
* **Herramienta:** Gemini
* **Tipo de uso:** Concepto / Generación de código
* **Consulta textual:** *"Construye el codigo segun el diagrama UML con la variante A"*
* **Qué acepté:** La estructura de las clases abstractas (`Producto`, `Pedido`, `MetodoPago`) con `@abstractmethod` y el encapsulamiento mediante propiedades `@property`.
* **Qué modifiqué y por qué:** Simplifiqué la sintaxis quitando anotaciones de tipos avanzadas y funciones complejas para mantener un código claro, directo y fácil de defender.
* **Archivos o clases:** `modelo/productos.py`, `modelo/clientes.py`
* **¿Lo explico sin ayuda?:** Sí

### 2. Alineación estricta con UML v2 y reglas de negocio
* **Fecha:** 23/11/2026
* **Herramienta:** Gemini
* **Tipo de uso:** Generación de código
* **Consulta textual:** *"Haz que el codigo sea directo relacionado con el diagrama UML v2"*
* **Qué acepté:** La implementación de polimorfismo en `calcular_precio()`, `contar_platos()` y `calcular_cargos()` evitando el uso de `isinstance` para tipos de producto.
* **Qué modifiqué y por qué:** Ajusté los parámetros de `armar_combo()` para que coincidan exactamente con la firma del diagrama UML v2, ordené los días de la semana iniciando en `"domingo"` y verifiqué los montos de la Variante A.
* **Archivos o clases:** `modelo/pedidos.py`, `modelo/pagos.py`, `restaurante.py`
* **¿Lo explico sin ayuda?:** Sí

### 3. Interfaz de consola y pruebas unitarias
* **Fecha:** 23/11/2026
* **Herramienta:** Gemini
* **Tipo de uso:** Revisión / Interfaz
* **Consulta textual:** *"Que todas las opciones en el menu de consola se muestren en lista vertical"*
* **Qué acepté:** La estructura del bucle `while True`, el manejo de excepciones `try/except` y los casos de prueba automatizados con `assert`.
* **Qué modifiqué y por qué:** Organicé todas las subopciones en listas verticales numeradas con un espacio en blanco al seleccionar cada opción para mejorar la legibilidad en consola.
* **Archivos o clases:** `main.py`, `pruebas.py`
* **¿Lo explico sin ayuda?:** Sí

---

**Declaración:** Declaro que este registro incluye todos mis usos de IA realizados el día 23/11/2026 para el desarrollo de este proyecto y que comprendo y puedo explicar sin ayuda todo el código que entrego.
