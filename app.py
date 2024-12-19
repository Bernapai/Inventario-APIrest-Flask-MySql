from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config, db
from routes.categoriaRoute import categoria_bp
from routes.clienteRoute import cliente_bp
from routes.detalleRoute import detalle_bp
from routes.movimientosRoute import movimientos_bp
from routes.productoRoute import producto_bp
from routes.proveedorRoute import proveedor_bp
from routes.usuarioRoute import usuario_bp
from routes.ventasRoute import ventas_bp

# Crear la aplicación de Flask
app = Flask(__name__)

# Cargar la configuración desde config.py
app.config.from_object(Config)


# Asociar la aplicación con la instancia de db
db.init_app(app)

# Registro de Blueprints
app.register_blueprint(categoria_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(detalle_bp)
app.register_blueprint(movimientos_bp)
app.register_blueprint(producto_bp)
app.register_blueprint(proveedor_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(ventas_bp)

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
