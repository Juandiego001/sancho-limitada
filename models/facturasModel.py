from server import db

class Facturas(db.Model):
    cedula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(60), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    foto =  db.Column(db.String(400), nullable=True)

    def __repr__(self):
        return 'Cliente: %r' % self