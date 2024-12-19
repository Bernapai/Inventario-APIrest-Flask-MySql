
from models.entidades.cliente import Cliente
from datetime import datetime
from config import db



class Ventas (db.Model):
    __tablename__ = 'ventas'
    id_venta = db.Column(db.Integer, primary_key=True)
    id_cliente= db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'))
    fecha= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    total= db.Column(db.Float, nullable=False)
    usuario= db.Column(db.String(100), nullable=False)

    def __init__(self, id_cliente, fecha, total, usuario):
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.total = total
        self.usuario = usuario

    def serialize(self):
        return {
            'id_venta': self.id_venta,
            'id_cliente': self.id_cliente,
            'fecha': self.fecha.isoformat(),
            'total': self.total,
            'usuario': self.usuario
        }
