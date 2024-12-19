
from datetime import datetime
from models.entidades.producto import Producto  # Importa Producto
from config import db


class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    id_movimiento = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey ('productos.id_producto'))
    cantidad=db.Column(db.Integer, nullable=False)
    tipo_movimiento = db.Column(db.String(50), nullable=True)
    fecha = db.Column(db.Date, nullable=False, default=datetime.utcnow) 
    usuario = db.Column(db.String(100), nullable=False)



    def __init__(self, id_producto, cantidad, tipo_movimiento,fecha, usuario):
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.tipo_movimiento = tipo_movimiento
        self.fecha = fecha
        self.usuario = usuario

    def serialize(self):
        return {
            'id_movimiento': self.id_movimiento,
            'id_producto': self.id_producto,
            'cantidad': self.cantidad,
            'tipo_movimiento': self.tipo_movimiento,
            'fecha': self.fecha.strftime('%Y-%m-%d'),
            'usuario': self.usuario
        }


   