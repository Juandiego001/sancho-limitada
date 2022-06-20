from flask import render_template, redirect, Blueprint
from models.productosModel import Productos
from server import db

def productosGet():
    productos = Productos.query.all()

    print('Prueba')
    print(productos)

    # Debemos obtener los productos que están activos
    productosActivos = []
    for producto in productos:
        if producto.estado == 'A':
            productosActivos.append(producto)

    return render_template('productos.html', productos=productos, productosActivos=productosActivos)

def productosPost(form):
    codigo = form['codigo']

    # Verificamos si el código ya existe o no
    existe = Productos.query.get(codigo)

    if not(existe):
        categoria = form['categoria']
        nombre = form['nombre']
        precio = form['precio']
        cantidadBodega = form['cantidadBodega']
        estado = form['estado']

        producto = Productos(codigo, categoria, nombre, precio, cantidadBodega, estado)
        db.session.add(producto)
        db.session.commit()

    return redirect('/productos')

def productosPut(codigo, form):
    producto = Productos.query.get(codigo)

    nuevoCodigo = form['codigo']
    categoria = form['categoria']
    nombre = form['nombre']
    precio = form['precio']
    cantidadBodega = form['cantidadBodega']
    estado = form['estado']

    producto.codigo = nuevoCodigo
    producto.categoria = categoria
    producto.nombre = nombre
    producto.precio = precio
    producto.cantidadBodega = cantidadBodega
    producto.estado = estado

    db.session.commit()
    return redirect('/productos')

def productosDelete(codigo):
    producto = Productos.query.get(codigo)

    db.session.delete(producto)
    db.session.commit()
    return redirect('/productos')

# Método para activar un producto
def productosActivar(codigo):
    producto = Productos.query.get(codigo)
    producto.estado = 'A'
    db.session.commit()
    return redirect('/productos')

# Métodos para desactivar un producto
def productosDesactivar(codigo):
    producto = Productos.query.get(codigo)
    producto.estado = 'I'
    db.session.commit()
    return redirect('/productos')
