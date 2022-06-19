from flask import render_template, redirect, Blueprint
from models.facturasModel import Facturas
from models.clientesModel import Clientes
from models.productosModel import Productos
from models.detallesModel import Detalles
from server import db

def facturasGet():
    facturas = Facturas.query.all()
    productos = Productos.query.all()

    return render_template('facturas.html', facturas=facturas, productos=productos)

# Método que retorna el valor total de una factura brindando el código
def facturasCodigo(codigo):
    factura = Facturas.query.get(codigo)
    valorTotal = factura.valorTotal
    return {'valorTotal': valorTotal}

def facturasPost(form):
    codigo = form['codigo']

    # Verificamos si el código ya existe o no
    existe = Facturas.query.get(codigo)

    if not(existe):
        cedula_cliente = form['cedula_cliente']

        # Debemos verificar si efectivamente existe la cédula del cliente
        existe = Clientes.query.get(cedula_cliente)
        if existe:
            fecha = form['fecha']
            metodo = form['metodo']
            valorTotal = form['valorTotal']

            factura = Facturas(codigo, fecha, metodo, valorTotal)
            db.session.add(factura)
            db.session.commit()

    return redirect('/facturas')

# Método para agregar productos a una factura
def facturasProducto(productosAgregados):

    print(productosAgregados)

    facturas = Facturas.query.all()
    productos = Productos.query.all()
    return render_template('facturas.html', facturas=facturas, productos=productos, detalles=detalles, productosAgregados=productosAgregados)


def facturasPut(codigo, form):
    factura = Facturas.query.get(codigo)

    nuevoCodigo = form['codigo']
    fecha = form['fecha']
    metodo = form['metodo']
    valorTotal = form['valorTotal']

    factura.codigo = nuevoCodigo
    factura.fecha = fecha
    factura.metodo = metodo
    factura.valorTotal = valorTotal

    db.session.commit()
    return redirect('/facturas')

def facturasDelete(codigo):
    factura = Facturas.query.get(codigo)

    db.session.delete(factura)
    db.session.commit()
    return redirect('/facturas')
    