# config.py
from flask_sqlalchemy import SQLAlchemy

# Crear una instancia global de SQLAlchemy
db = SQLAlchemy()


class Config:
    # Configuración de la base de datos, usando mysqlconnector como dialecto
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Juanber123()@localhost:3306/inventario'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilitar el seguimiento de modificaciones
    SECRET_KEY = 'Juanber123()'  # Mejor guardar este valor en una variable de entorno en un entorno de producción
