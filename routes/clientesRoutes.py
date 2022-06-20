from flask import request, render_template, redirect
from server import app
from controllers.clientesController import *

@app.route('/clientes')
def clientesRouteGet():
    return clientesGet()

@app.route('/clientes-post', methods=['GET', 'POST'])
def clientesRoutePost():
    return clientesPost(request.form, request.files)

@app.route('/clientes-put/<cedula>', methods=['GET', 'POST'])
def clientesRoutePut(cedula):
    return clientesPut(cedula, request.form, request.files)

@app.route('/clientes-delete/<cedula>')
def clientesRouteDelete(cedula):
    return clientesDelete(cedula)


