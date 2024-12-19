
from config import db



class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.String(20),nullable=True, unique=True)
    email=db.Column(db.String(100), nullable=True, unique=True)
    direccion=db.Column(db.Text, nullable=True, unique=True)


    def __init__(self,nombre,telefono,email,direccion):
      self.nombre = nombre
      self.telefono = telefono
      self.email = email
      self.direccion = direccion


    def serialize (self):
      return {
         'id_cliente': self.id_cliente,
         'nombre': self.nombre,
         'telefono': self.telefono,
         'email': self.email,
         'direccion': self.direccion
      }

  