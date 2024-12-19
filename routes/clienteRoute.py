from flask import Blueprint,  request
from controllers.clienteController import ClienteController


cliente_bp = Blueprint('cliente_bp',__name__ )

# Ruta para obtener todos los clientes
@cliente_bp.route('/clientes', methods=['GET'])
def obtener_clientes():
    return ClienteController.obtener_todos_clientes()

# Ruta para obtener un cliente por id
@cliente_bp.route('/cliente/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    return ClienteController.obtener_cliente_por_id(id_cliente)

# Ruta para agregar un nuevo cliente
@cliente_bp.route('/cliente', methods=['POST'])
def agregar_cliente():
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return ClienteController.agregar_cliente(data)

# Ruta para actualizar un cliente
@cliente_bp.route('/cliente/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return ClienteController.actualizar_cliente(id_cliente, data)

# Ruta para eliminar un cliente
@cliente_bp.route('/cliente/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    return ClienteController.eliminar_cliente(id_cliente)