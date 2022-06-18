from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/sancho_limitada'
app.config[' SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Index
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


