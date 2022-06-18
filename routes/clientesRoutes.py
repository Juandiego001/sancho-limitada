from flask import request, render_template
from server import app
from controllers.clientesController import clientesGet, clientesPost, clientesPut, clientesDelete

@app.route('/clientes')
def clientesRouteGet():
    return clientesGet()

@app.route('/clientes-post', methods=['POST'])
def clientesRoutePost():
    return clientesPost(request.form, request.files)

@app.route('/clientes-put/<cedula>', methods=['POST', 'GET'])
def clientesRoutePut(cedula):
    return clientesPut(cedula, request.form, request.files)

@app.route('/clientes-delete/<cedula>')
def clientesRouteDelete(cedula):
    return clientesDelete(cedula)


