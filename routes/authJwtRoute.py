from flask import Blueprint, request, jsonify
import jwt
import datetime
from config import db
from functools import wraps
from models.entidades.usuario import Usuario
 

SECRET_KEY = 'jm68()'

auth_bp = Blueprint('auth_bp', __name__)

# Crear token de acceso
def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token es requerido'}), 401
        try:
            token = token.split()[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'El token ha expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token inválido'}), 401
        return f(*args, **kwargs, user_id=data['user_id'])
    return decorated

# Ruta de login
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nombre_usuario = data.get('nombre_usuario')
    contrasena = data.get('contrasena')

    user =  Usuario.query.filter_by(nombre_usuario=nombre_usuario, contrasena=contrasena).first()
    if not user:
        return jsonify({'message': 'Credenciales incorrectas'}), 401

    token = create_token(user.id)
    return jsonify({'token': token})


