from flask import Flask, render_template
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



# Incializando servidor
if __name__ == '__main__':
    app.run(port = 3001)


