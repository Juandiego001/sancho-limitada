from server import db

class Clientes(db.Model):
    cedula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(60), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    foto =  db.Column(db.Integer, nullable=False)

    def __init__(self, cedula, nombre, direccion, telefono, foto = None):
        self.cedula = cedula
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.foto = foto