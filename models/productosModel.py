from server import db

class Productos(db.Model):
    __tablename__ = 'productos'
    codigo = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(30), nullable=False)
    nombre = db.Column(db.String(60), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    cantidadBodega =  db.Column(db.String(400), nullable=False)
    estado = db.Column(db.String(1), nullable=False, default='A')

    def __init__(self, codigo, categoria, nombre, precio, cantidadBodega, estado):
        self.codigo = codigo
        self.categoria = categoria
        self.nombre = nombre
        self.precio = precio
        self.cantidadBodega = cantidadBodega
        self.estado = estado