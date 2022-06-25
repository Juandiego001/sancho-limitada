# sancho-limitada
Resolución de la primera parte de la prueba técnica desarrollando un aplicativo web de una empresa con características de e-commerce.

# Para correr el proyecto
Todo el proyecto ha sido trabajado con Python, el micro framework Flask, la librería SQLAlchemy y MySQL como motor de bases de datos.

Para instalar estos módulos se debe ejecutar:
• pip install Flask
• pip install SQLAlchemy
• pip install mysqlclient

Posteriormente, se debe crear la base de datos con el script proporcionado en la carpeta database, donde se encontrará el script de creación de la base de datos.
Luego de ello, se debe cambiar la contraseña y el usuario en el servidor de la base de datos (actualmente ambos están como 'root').
Finalmente se ejecuta: python server.py y ya estará todo listo.

# Contexto de la prueba
El contexto de la prueba se puede encontrar en el PDF de la carpeta de documentación. No obstante, se agregará aquí:

La distribuidora Sancho Limitada, se especializa en la venta de ropa (retail) para
caballero. Lo ha contratado como desarrollador para realizar un aplicativo web
responsive, el cual permitirá registrar clientes (cédula, nombre, dirección, teléfono
y foto), productos (código del producto, categoría, nombre, precio, cantidad en
bodega, estado -activo, inactivo-) y facturas (código de la factura, cliente que
realiza la compra, productos, cantidad de productos, fecha de compra, valor total
y método de pago). Se debe poder:

• Registrar y Editar Productos.
• Registrar y Editar Clientes.
• Registrar y Editar Facturas.
• Listar Productos.
• Listar Clientes.
• Listar Facturas.
• Desactivar productos (dejando de aparecer en el listado).
• Eliminar Clientes.
• Listar clientes ordenados por cantidad de compras realizadas (factura =
compra).

Se le solicita que junto a este desarrollo facilite un servicio API para consultar
facturas por código, el cuál recibe un código de factura y retorna el valor total, ya
que los clientes de la empresa deben conectar su sistema contable a este servicio.
