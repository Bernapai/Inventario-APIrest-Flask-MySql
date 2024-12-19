from flask import Blueprint,  request
from controllers.movimientosController import MovimientosController

movimientos_bp = Blueprint('movimientos_bp', __name__)

# Ruta para obtener todos los movimientos
@movimientos_bp.route('/movimientos', methods=['GET'])
def obtener_movimientos():
    return MovimientosController.obtener_todos_movimientos()

# Ruta para obtener un movimiento por id
@movimientos_bp.route('/movimiento/<int:id_movimiento>', methods=['GET'])
def obtener_movimiento(id_movimiento):
    return MovimientosController.obtener_movimiento_por_id(id_movimiento)

# Ruta para agregar un nuevo movimiento
@movimientos_bp.route('/movimiento', methods=['POST'])
def agregar_movimiento():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return MovimientosController.agregar_movimiento(data)

# Ruta para actualizar un movimiento
@movimientos_bp.route('/movimiento/<int:id_movimiento>', methods=['PUT'])
def actualizar_movimiento(id_movimiento):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return MovimientosController.actualizar_movimiento(id_movimiento, data)

# Ruta para eliminar un movimiento
@movimientos_bp.route('/movimiento/<int:id_movimiento>', methods=['DELETE'])
def eliminar_movimiento(id_movimiento):
    return MovimientosController.eliminar_movimiento(id_movimiento)