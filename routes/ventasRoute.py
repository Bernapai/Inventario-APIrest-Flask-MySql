from flask import Blueprint, request
from controllers.ventasController import VentasController

# Creamos un Blueprint para las rutas de ventas
ventas_bp = Blueprint('ventas_bp', __name__)

# Ruta para obtener todas las ventas
@ventas_bp.route('/ventas', methods=['GET'])
def obtener_ventas():
    return VentasController.obtener_ventas()

# Ruta para obtener una venta por id
@ventas_bp.route('/ventas/<int:id_venta>', methods=['GET'])
def obtener_venta(id_venta):
    return VentasController.obtener_venta(id_venta)

# Ruta para agregar una nueva venta
@ventas_bp.route('/ventas', methods=['POST'])
def agregar_venta():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return VentasController.agregar_venta(data)

# Ruta para actualizar una venta existente
@ventas_bp.route('/ventas/<int:id_venta>', methods=['PUT'])
def actualizar_venta(id_venta):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return VentasController.actualizar_venta(id_venta, data)

# Ruta para eliminar una venta
@ventas_bp.route('/ventas/<int:id_venta>', methods=['DELETE'])
def eliminar_venta(id_venta):
    return VentasController.eliminar_venta(id_venta)