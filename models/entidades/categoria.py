
from config import db

class Categoria(db.Model):
    __tablename__ = 'categorias'
   # Definimos los atributos de la clase (columnas de la tabla)
    id_categoria = db.Column(db.Integer, primary_key=True)  # ID de la categoría (clave primaria)
    nombre = db.Column(db.String(100), nullable=False, unique=True)  # Nombre de la categoría
    descripcion = db.Column(db.String(255))  # Descripción de la categoría (opcional)
    


      # Constructor para inicializar la categoría
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


     # Método para representar la categoría como un diccionario (útil para las respuestas JSON)
    def serialize(self):
        return {
            'id_categoria': self.id_categoria,
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }
