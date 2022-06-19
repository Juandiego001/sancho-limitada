from server import db
from sqlalchemy.orm import declarative_base
from models.clientesModel import *

Base = declarative_base()

class Facturas(db.Model):
    __tablename__ = 'facturas'
    codigo = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    cedula_cliente = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    metodo = db.Column(db.String(30), nullable=False)
    valorTotal =  db.Column(db.Float, nullable=False, default=0.0)

    def __init__(self, codigo, cedula_cliente, fecha, metodo, valorTotal):
        self.codigo = codigo
        self.cedula_cliente = cedula_cliente
        self.fecha = fecha
        self.metodo = metodo
        self.valorTotal = valorTotal