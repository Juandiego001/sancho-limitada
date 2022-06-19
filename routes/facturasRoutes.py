from flask import request, render_template
from server import app
from controllers.facturasController import facturasGet, facturasPost, facturasPut, facturasDelete, facturasCodigo, facturasProducto

@app.route('/facturas')
def facturasRouteGet():
    return facturasGet()

@app.route('/facturas-post', methods=['GET', 'POST'])
def facturasRoutePost():
    return facturasPost(request.form)

@app.route('/facturas-put/<codigo>', methods=['GET', 'POST'])
def facturasRoutePut(codigo):
    return facturasPut(codigo, request.form)

@app.route('/facturas-delete/<codigo>')
def facturasRouteDelete(codigo):
    return facturasDelete(codigo)

# Obtener facturas por codigo
@app.route('/facturas/<codigo>')
def facturasRouteCodigo(codigo):
    return facturasCodigo(codigo)

# Agregar productos a una factura
@app.route('/facturas-productos', methods=['GET', 'POST'])
def facturasRouteProducto():
    return facturasProducto(request.form)