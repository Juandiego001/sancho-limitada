from flask import render_template, redirect, Blueprint, make_response, request
from models.facturasModel import Facturas
from models.clientesModel import Clientes
from models.productosModel import Productos
from models.detallesModel import Detalles
from server import db
import json
from datetime import datetime

def facturasGet():
    # Obtenemos los productos agregados que se han almacenado en las cookies
    productosAgregados = request.cookies.get('productosAgregados')

    auxProductosAgregados = []
    if productosAgregados != None:
        productosAgregados = json.loads(productosAgregados)
        print("preba")
        # Obtener los nombres de los productos con el código registrado en las cookies
        for producto in productosAgregados:
            print(producto)
            codigo = producto['codigoProducto'] 
            cantidad = producto['cantidadProducto']
            nombre = Productos.query.get(codigo).nombre
            auxProductosAgregados.append({'codigoProducto': codigo, 'nombreProducto': nombre, 'cantidadProducto': cantidad})    

    facturas = Facturas.query.all()
    productos = Productos.query.all()

    return render_template('facturas.html', facturas=facturas, productos=productos, productosAgregados=auxProductosAgregados)


# Método para crear facturas
def facturasPost(form):
    cedula_cliente = form['cedula_cliente']
    cliente = Clientes.query.get(cedula_cliente)

    resp = make_response(redirect('/facturas'))

    productosAgregados = request.cookies.get('productosAgregados')
    productosAgregados = json.loads(productosAgregados)
    # El cliente existirá cuando sea diferente de None
    if cliente != None:
        fecha = datetime.date(datetime.now())
        metodo = form['metodo']

        # Se debe calcular el valorTotal
        valorTotal = 0
        
        for productoAgregado in productosAgregados:
            codigo = int(productoAgregado['codigoProducto'])
            cantidad = int(productoAgregado['cantidadProducto'])
        
            producto = Productos.query.get(codigo)
            precio = producto.precio
            valorTotal += precio * cantidad

        factura = Facturas(cedula_cliente, fecha, metodo, valorTotal)
        db.session.add(factura)
        db.session.flush()

        # Se debe crear el detalle con la factura recién creada y los productos creados
        codigo_factura = factura.codigo

        for productoAgregado in productosAgregados:
            codigo = int(productoAgregado['codigoProducto'])
            cantidad = int(productoAgregado['cantidadProducto'])
            detalle = Detalles(codigo_factura, codigo, cantidad)
            db.session.add(detalle)
            db.session.commit()

        db.session.commit()

        # Se limpian las cookies
        resp.set_cookie('productosAgregados', '', expires=0)
    return resp

# Método para editar/actualizar las facturas
def facturasPut(codigo, form):
    factura = Facturas.query.get(codigo)

    nuevaCedula = form['cedula_cliente']

    # Se valida que la nueva cédula exista en la base de datos
    cliente = Clientes.query.get(nuevaCedula)
    if cliente != None:
        nuevoMetodo = form['metodo']

        factura.cedula_cliente = nuevaCedula
        factura.metodo = nuevoMetodo

        db.session.commit()

    return redirect('/facturas')

def facturasDelete(codigo):
    factura = Facturas.query.get(codigo)

    db.session.delete(factura)
    db.session.commit()
    return redirect('/facturas')

# Método para agregar productos a una factura
def facturasProducto(form):

    producto = {}
    producto['codigoProducto'] = form['codigoProducto']
    producto['cantidadProducto'] = form['cantidadProducto']

    facturas = Facturas.query.all()
    productos = Productos.query.all()

    resp = make_response(redirect('/facturas'))
    productosAgregados = request.cookies.get('productosAgregados')

    if productosAgregados != None:
        productosAgregados = json.loads(productosAgregados)
        productosAgregados.append(producto)
        resp.set_cookie('productosAgregados', json.dumps(productosAgregados))
    else:
        resp.set_cookie('productosAgregados', json.dumps([producto]))

    return resp

# Método para editar productos agregados a una factura
def facturasProductoPut(index, form):
    productosAgregados = request.cookies.get('productosAgregados')
    productosAgregados = json.loads(productosAgregados)

    # Nuevos datos para el producto
    nuevoCodigo = form['codigoProducto']
    nuevaCantidad = form['cantidadProducto']
    
    producto = productosAgregados[index]
    producto['codigoProducto'] = nuevoCodigo
    producto['cantidadProducto'] = nuevaCantidad

    productosAgregados[index] = producto

    resp = make_response(redirect('/facturas'))
    resp.set_cookie('productosAgregados', json.dumps(productosAgregados))
    return resp

# Método para eliminar productos agregados a una factura
def facturasProductoDelete(index):
    productosAgregados = request.cookies.get('productosAgregados')
    productosAgregados = json.loads(productosAgregados)
    del productosAgregados[index]

    resp = make_response(redirect('/facturas'))
    resp.set_cookie('productosAgregados', json.dumps(productosAgregados))
    return resp

# Método para ver los detalles de una factura
def facturasDetalles(codigo):
    detalles = Detalles.query.filter_by(codigo_factura=codigo)
    detallesResults = db.session.execute(detalles)

    # Se debe enviar el valor por cada producto
    detallesProducto = []
    for detalle in detallesResults.scalars():
        # Obtenemos código del producto y la cantidad para después 
        # determinar el precio y hallar el costo por cada producto
        codigo_producto = detalle.codigo_producto
        cantidad = detalle.cantidad

        producto = Productos.query.get(codigo_producto)
        precio = producto.precio
        nombre = producto.nombre

        cantidadPrecio = cantidad * precio

        detallesProducto.append({'codigo_producto': codigo_producto, 'nombre': nombre, 'cantidad': cantidad, 'precio': precio, 'cantidadPrecio': cantidadPrecio})

    # Debemos obtener el valorTotal de la factura
    valorTotal = Facturas.query.get(codigo).valorTotal

    return render_template('detalles.html', codigo_factura=codigo, detallesProducto=detallesProducto, valorTotal=valorTotal)
    factura.codigo = nuevoCodigo
    factura.fecha = fecha
    factura.metodo = metodo
    factura.valorTotal = valorTotal

    db.session.commit()
    return redirect('/facturas')











# Método que retorna el valor total de una factura brindando el código
def facturasCodigo(codigo):
    factura = Facturas.query.get(codigo)
    valorTotal = factura.valorTotal
    return {'valorTotal': valorTotal}