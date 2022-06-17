from flask import request, render_template
from server import app

@app.route('/facturas', methods=['GET', 'POST', 'PUT', 'DELETE'])
def facturas():
    if request.method == 'GET':
        return render_template('facturas.html')