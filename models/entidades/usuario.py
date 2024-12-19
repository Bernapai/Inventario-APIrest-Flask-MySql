
from datetime import datetime
from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(100), nullable=False)
    contrasena = db.Column(db.String (255), nullable=False)
    rol=db.Column(db.String(255), nullable=False)
    fecha_creacion= db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, nombre_usuario, contrasena, rol):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol

    
    def serialize(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre_usuario': self.nombre_usuario,
            'contrasena': self.contrasena,
            'rol': self.rol,
            'fecha_creacion': self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')
        }

   