-- Versión de MySQL 8.0
CREATE DATABASE sancho_limitada;

use sancho_limitada;

-- Creación de tablas
CREATE TABLE CLIENTES(
    cedula INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(60) NOT NULL,
    telefono BIGINT NOT NULL,
    foto VARCHAR(50) NULL
);

CREATE TABLE FACTURAS(
    codigo INTEGER AUTO_INCREMENT NOT NULL,
    cedula_cliente INTEGER NOT NULL,
    fecha DATE NOT NULL,
    metodo VARCHAR(30) NOT NULL,
    valorTotal FLOAT NULL,

    PRIMARY KEY(codigo),
    INDEX (cedula_cliente),

    CONSTRAINT fk_cliente_1 FOREIGN KEY (cedula_cliente) REFERENCES CLIENTES(cedula) 
    ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE PRODUCTOS(
    codigo INTEGER PRIMARY KEY,
    categoria VARCHAR(30) NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    precio FLOAT NOT NULL,
    cantidadBodega INTEGER NOT NULL,
    estado VARCHAR(1),
    CONSTRAINT chk_estado_1 CHECK (estado = 'A' OR estado = 'I')
);

CREATE TABLE DETALLES(
    id INTEGER NOT NULL AUTO_INCREMENT,
    codigo_factura INTEGER NOT NULL,
    codigo_producto INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,

    PRIMARY KEY(id),
    INDEX (codigo_factura),
    INDEX (codigo_producto),

    CONSTRAINT fk_factura_1 FOREIGN KEY(codigo_factura) REFERENCES FACTURAS(codigo) 
    ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_producto_1 FOREIGN KEY(codigo_producto) REFERENCES PRODUCTOS(codigo)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- Inserción de elementos de prueba
-- Inserción de clientes
INSERT INTO CLIENTES(cedula, nombre, direccion, telefono) 
VALUES(123, 'Juan', 'Calle 92 #08-23', 3155910666);

INSERT INTO CLIENTES(cedula, nombre, direccion, telefono) 
VALUES(321, 'Fulano', 'Calle 29 #23-08', 666591315);

-- Inserción de facturas, productos y detalles
-- Factura que registra la compra de 1 producto 10 veces
-- al cliente de cédula 123
INSERT INTO PRODUCTOS VALUES(1, 'Talla XXL', 'Camisa', 50000, 100, 'A');
INSERT INTO FACTURAS(cedula_cliente, fecha, metodo) VALUES(123, '2022-06-17', 'Credit card', 500000);
INSERT INTO DETALLES(codigo_factura, codigo_producto, cantidad)
VALUES(1, 1, 10);

-- Obtener todas las facturas de un cliente con el valor total a pagar
SELECT C.cedula, F.valorTotal FROM CLIENTES C JOIN FACTURAS F ON C.cedula = F.cedula_cliente WHERE C.cedula = 123;