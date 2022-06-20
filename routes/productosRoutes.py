from flask import request, render_template
from server import app
from controllers.productosController import *


@app.route('/productos')
def productosRouteGet():
    return productosGet()

@app.route('/productos-post', methods=['GET', 'POST'])
def productosRoutePost():
    return productosPost(request.form)

@app.route('/productos-put/<codigo>', methods=['GET', 'POST'])
def productosRoutePut(codigo):
    return productosPut(codigo, request.form)

@app.route('/productos-delete/<codigo>')
def productosRouteDelete(codigo):
    return productosDelete(codigo)

# Método para activar un producto
@app.route('/productos-activar/<codigo>', methods=['GET', 'POST'])
def productosRouteActivar(codigo):
    return productosActivar(codigo)

# Método para desactivar un producto
@app.route('/productos-desactivar/<codigo>', methods=['GET', 'POST'])
def productosRouteDesactivar(codigo):
    return productosDesactivar(codigo)