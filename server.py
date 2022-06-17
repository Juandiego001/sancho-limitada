from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


# Configuración de la db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sancho_limitada'

mysql = MySQL()

@app.route('/')
def index():
    return render_template('index.html')

# Rutas
from routes.clientesRoutes import *
from routes.productosRoutes import *
from routes.facturasRoutes import *
from routes.detallesRoutes import *

# Incializando servidor
if __name__ == '__main__':
    app.run(port = 3001, debug = True)


