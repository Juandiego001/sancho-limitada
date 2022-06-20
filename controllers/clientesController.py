from flask import render_template, redirect, Blueprint
from models.clientesModel import Clientes
from models.facturasModel import Facturas
from server import db
import os

def clientesGet():
    clientes = Clientes.query.all()

    # Clientes ordenados por compras
    clientesOrdenados = []
    queryClientes = db.session.query(Facturas.cedula_cliente, db.func.count(Facturas.cedula_cliente)).\
        group_by(Facturas.cedula_cliente).\
        order_by(db.desc(db.func.count(Facturas.cedula_cliente)))

    resultadosQuery = db.session.execute(queryClientes)

    for cedulaCliente in resultadosQuery.scalars():
        queryCantidad = db.session.query(db.func.count(Facturas.cedula_cliente))\
            .filter_by(cedula_cliente=cedulaCliente)

        cantidades = db.session.execute(queryCantidad)
        for cantidad in cantidades.scalars():
            clientesOrdenados.append({'cedula': cedulaCliente, 'cantidad': cantidad})
        

    return render_template('clientes.html', clientes=clientes, clientesOrdenados=clientesOrdenados)

def clientesPost(form, files):
    # Datos del cliente
    cedula = form['cedula']
    nombre = form['nombre']
    direccion = form['direccion']
    telefono = form['telefono']

    # Foto del cliente
    foto = files['foto']
    if foto.filename != '':
        foto.save('./static/' + str(cedula) +  '.jpg')
        foto = 1
    else:
        foto = 0

    cliente = Clientes(cedula, nombre, direccion, telefono, foto)
    db.session.add(cliente)
    db.session.commit()

    return redirect('/clientes')

def clientesPut(cedula, form, files):
    cliente = Clientes.query.get(cedula)

    nuevaCedula = form['cedula']
    nombre = form['nombre']
    direccion = form['direccion']
    telefono = form['telefono']

    cliente.cedula = nuevaCedula
    cliente.nombre = nombre
    cliente.direccion = direccion
    cliente.telefono = telefono 

    # Verificar si existe la foto y no será cambiada
    foto = files['foto']
    if cliente.foto == 1 and foto.filename == '':
        old = './static/' + str(cedula) + '.jpg'
        new = './static/' + str(nuevaCedula) + '.jpg'
        os.rename(old, new)

    # Verificar si no existe foto y se agregará una nueva
    if cliente.foto == 0 and foto.filename != '':
        cliente.foto = 1
        foto.save('./static/' + str(nuevaCedula) +  '.jpg')

    # Verificar si existe la foto, desea ser eliminada y no se ha agregado una nueva foto
    if cliente.foto == 1 and 'eliminarFoto' in form and foto.filename == '':
        cliente.foto = 0
        os.remove('./static/' + str(cedula) +  '.jpg')

    # Verificar si existe la foto, desea ser eliminada y se desea agregar una nueva foto
    if cliente.foto == 1 and 'eliminarFoto' in form and foto.filename != '':
        os.remove('./static/' + str(cedula) +  '.jpg')
        foto.save('./static/' + str(nuevaCedula) +  '.jpg')

    # Verificar si existe la foto, no desea ser eliminada y se desea agregar una nueva foto
    if cliente.foto == 1 and not('eliminarFoto' in form) and foto.filename != '':
        os.remove('./static/' + str(cedula) +  '.jpg')
        foto.save('./static/' + str(nuevaCedula) +  '.jpg')

    db.session.commit()

    return redirect('/clientes')

def clientesDelete(cedula):
    cliente = Clientes.query.get(cedula)

    # Si el cliente existe se debe borrar la foto
    if cliente.foto == 1:
        os.remove('./static/' + str(cedula) + '.jpg')

    db.session.delete(cliente)
    db.session.commit()
    return redirect('/clientes')