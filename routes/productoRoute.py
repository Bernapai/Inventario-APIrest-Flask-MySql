from flask import Blueprint,request
from controllers.productoController import ProductoController
from routes.authJwtRoute import token_required
# Creamos un Blueprint para las rutas de productos

producto_bp = Blueprint('producto_bp', __name__)

# Ruta para obtener todos los productos
@producto_bp.route('/productos', methods=['GET'])
def obtener_productos():
    return ProductoController.obtener_todos_productos()

# Ruta para obtener un producto por id
@producto_bp.route('/producto/<int:id_producto>', methods=['GET'])
def obtener_producto(id_producto):
    return ProductoController.obtener_producto(id_producto)

# Ruta para buscar un producto por nombre
@producto_bp.route('/productos/<string:nombre>', methods=['GET'])
def buscar_producto(nombre):
    return ProductoController.buscar_producto(nombre)
    
# Ruta para agregar un nuevo producto
@producto_bp.route('/producto', methods=['POST'])
@token_required
def agregar_producto():
    data = request.get_json() 
    return ProductoController.agregar_producto(data)

# Ruta para actualizar un producto
@producto_bp.route('/producto/<int:id_producto>', methods=['PUT'])
@token_required
def actualizar_producto(id_producto):
    data = request.get_json()  # Obtenemos los datos del cuerpo de la solicitud
    return ProductoController.actualizar_producto(id_producto, data)

# Ruta para eliminar un producto
@producto_bp.route('/producto/<int:id_producto>', methods=['DELETE'])
@token_required
def eliminar_producto(id_producto):
    return ProductoController.eliminar_producto(id_producto)