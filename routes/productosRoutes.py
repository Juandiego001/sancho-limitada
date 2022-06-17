from flask import request, render_template
from server import app

@app.route('/productos', methods=['GET', 'POST', 'PUT', 'DELETE'])
def productos():
    if request.method == 'GET':
        return render_template('productos.html')