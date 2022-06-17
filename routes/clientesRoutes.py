from flask import request, render_template
from server import app

@app.route('/clientes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def clientes():
    if request.method == 'GET':
        return render_template('clientes.html')