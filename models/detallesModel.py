from server import db

class Detalles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_factura = db.Column(db.Integer, nullable=False)
    codigo_producto = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)