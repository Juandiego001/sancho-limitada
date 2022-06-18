from flask import render_template, redirect, Blueprint
from models.clientesModel import Clientes
from server import db

def clientesGet():
    clientes = Clientes.query.all()
    return render_template('clientes.html', clientes=clientes)

def clientesPost(form, files):
    # Datos del cliente
    cedula = form['cedula']
    nombre = form['nombre']
    direccion = form['direccion']
    telefono = form['telefono']

    # Foto del cliente
    foto = files['foto']
    if foto.filename != '':
        extension = foto.filename.split('.')[1]
        foto.save('./static/' + str(cedula) +  '.'  + extension)
        foto = 1
    else:
        foto = 0

    cliente = Clientes(cedula, nombre, direccion, telefono, foto)
    db.session.add(cliente)
    db.session.commit()

    return redirect('/clientes')

def clientesPut(cedula, nuevoCliente):

    return redirect('/clientes')

def clientesDelete(cedula):
    cliente = Clientes.query.get(cedula)
    db.session.delete(cliente)
    db.session.commit()
    return redirect('/clientes')
    