from flask import Blueprint, request
from controllers.detalleController import DetalleController

detalle_bp = Blueprint('detalle_bp', __name__)

# Ruta para obtener todos los detalles de venta
@detalle_bp.route('/detalles', methods=['GET'])
def obtener_detalles():
    return DetalleController.obtener_todos_detalles()

# Ruta para obtener un detalle por id
@detalle_bp.route('/detalle/<int:id_detalle>', methods=['GET'])
def obtener_detalle(id_detalle):
    return DetalleController.obtener_detalle_por_id(id_detalle)

# Ruta para agregar un nuevo detalle
@detalle_bp.route('/detalle', methods=['POST'])
def agregar_detalle():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return DetalleController.agregar_detalle(data)

# Ruta para actualizar un detalle
@detalle_bp.route('/detalle/<int:id_detalle>', methods=['PUT'])
def actualizar_detalle(id_detalle):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return DetalleController.actualizar_detalle(id_detalle, data)

# Ruta para eliminar un detalle
@detalle_bp.route('/detalle/<int:id_detalle>', methods=['DELETE'])
def eliminar_detalle(id_detalle):
    return DetalleController.eliminar_detalle(id_detalle)