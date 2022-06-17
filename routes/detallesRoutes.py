from flask import request, render_template
from server import app

@app.route('/detalles', methods=['GET', 'POST', 'PUT', 'DELETE'])
def detalles():
    if request.method == 'GET':
        return render_template('detalles.html')