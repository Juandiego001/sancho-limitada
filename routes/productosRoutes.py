from flask import request, render_template
from server import app
from controllers.productosController import productosGet, productosPost, productosPut, productosDelete


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
