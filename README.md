# 📦 Gestor de Inventarios API

Este proyecto es una **API RESTful** para un sistema de **gestión de inventarios**, desarrollado con **Python** 🐍 y **Flask** ⚡, y con una base de datos **MySQL** 🗄️. La API permite realizar operaciones de gestión de productos, categorías, proveedores, clientes, ventas y más, ofreciendo una manera eficiente de gestionar el inventario de un negocio.

## 🗂️ Tablas del Sistema

El sistema está basado en una base de datos relacional con las siguientes tablas:

- **Productos**: Registra los productos que están disponibles en el inventario, incluyendo detalles como nombre, precio, cantidad disponible, etc. 📦
- **Categorías**: Organiza los productos en categorías para una gestión más eficiente (por ejemplo: tecnología, ropa, alimentos). 🏷️
- **Proveedores**: Contiene información sobre los proveedores de los productos, como nombre, contacto, dirección y teléfono. 🤝
- **Movimientos**: Registra las entradas y salidas de productos en el inventario, como compras, devoluciones, ajustes, entre otros. ↔️
- **Ventas**: Registra las ventas realizadas, incluyendo detalles sobre el cliente, productos vendidos y fecha de la transacción. 💸
- **Clientes**: Almacena la información de los clientes que han realizado compras en el sistema, como nombre, dirección, teléfono y correo electrónico. 🧑‍🤝‍🧑
- **Usuarios**: Permite la gestión de usuarios que tienen acceso al sistema, mediante autenticacion por token para administrar el inventario y las ventas. 👤
- **Detalle de Venta**: Relaciona los productos vendidos en cada venta, permitiendo un desglose detallado de las transacciones. 🧾

## ⚙️ Funcionalidades

### Gestión de Productos
- **Agregar**, **editar**, **eliminar** productos. ➕✏️❌
- **Consultar** productos por nombre o categoría. 🔍

### Gestión de Categorías
- **Agregar**, **editar**, **eliminar** categorías de productos. 🏷️

### Gestión de Proveedores
- **Agregar**, **editar**, **eliminar** proveedores. 🏢

### Gestión de Ventas
- **Registrar ventas** de productos. 🛒
- **Ver detalles** de cada venta (productos vendidos, cantidad, precio, etc.). 📊

### Gestión de Clientes
- **Agregar**, **editar**, **eliminar** clientes. 🧑‍🤝‍🧑

### Movimiento de Inventarios
- **Registrar movimientos** de inventarios (entradas y salidas de productos). 📦🔄

### Gestión de Usuarios
- **Crear** y **gestionar usuarios** del sistema mediante un Login. 👥🔧

## 🛠️ Tecnologías Usadas

- **Python** 🐍: Lenguaje de programación principal para desarrollar la API.
- **Flask** ⚡: Framework de desarrollo web ligero para crear la API.
- **MySQL** 🗄️: Base de datos relacional para almacenar los datos del sistema.
- **SQLAlchemy** 🔗: ORM para facilitar la interacción con la base de datos.

---

## 🔧 Requisitos

- **Python** 3.x
- **MySQL** 8.x
- **Flask** 2.x
- **SQLAlchemy** 1.x

---

