from flask import jsonify
from models.services.clienteServices import ClienteServices


class ClienteController:
    
    @staticmethod
    def agregar_cliente(data):
       try :
        # Validación de los campos obligatorios
            if not data or 'nombre' not in data or 'telefono' not in data or 'email' not in data or 'direccion' not in data:
                return jsonify({'error': 'Datos incompletos'}), 400
            else:
                # Llamamos al servicio para agregar el cliente
                cliente = ClienteServices.agregar_cliente(data['nombre'], data['telefono'], data['email'], data.get('direccion'))
                # Retornamos la respuesta serializada
                return jsonify(cliente.serialize()), 201
       except Exception as e:
            return jsonify({'error': str(e)}), 500
            
    @staticmethod
    def actualizar_cliente(id_cliente, data):
        # Recibimos los datos de la solicitud y pasamos a los servicios para actualizar el cliente
        nombre = data.get('nombre')
        telefono = data.get('telefono')
        email = data.get('email')
        direccion = data.get('direccion')

        # Llamamos al servicio para actualizar el cliente
        cliente = ClienteServices.actualizar_cliente(id_cliente,  telefono=telefono, direccion=direccion, email=email)
        
        if cliente is None:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
        
        # Retornamos la respuesta serializada
        return jsonify(cliente.serialize()), 200

    @staticmethod
    def eliminar_cliente(id_cliente):
        # Llamamos al servicio para eliminar el cliente
        try:
            ClienteServices.eliminar_cliente(id_cliente)
            return jsonify({'mensaje': 'Cliente eliminado exitosamente'}), 200
        except ValueError:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404

    @staticmethod
    def obtener_todos_clientes():
        # Llamamos al servicio para obtener todos los clientes
        clientes = ClienteServices.obtener_todos_clientes()
        return jsonify([cliente.serialize() for cliente in clientes]), 200

    @staticmethod
    def obtener_cliente_por_id(id_cliente):
        # Llamamos al servicio para obtener un cliente por ID
        cliente = ClienteServices.obtener_cliente_por_id(id_cliente)
        if cliente is None:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
        return jsonify(cliente.serialize()), 200

    @staticmethod
    def obtener_cliente_por_telefono(telefono):
        # Llamamos al servicio para obtener un cliente por teléfono
        cliente = ClienteServices.obtener_cliente_por_telefono(telefono)
        if cliente is None:
            return jsonify({'mensaje': 'Cliente no encontrado'}), 404
        return jsonify(cliente.serialize()), 200
    
 
    @staticmethod
    def buscar_cliente_por_nombre(nombre):
        # Llamamos al servicio para obtener los clientes que coinciden con el nombre
        clientes = ClienteServices.buscar_cliente_por_nombre(nombre)
        if not clientes:
            return jsonify({'mensaje': 'No se encontraron clientes con ese nombre'}), 404
        return jsonify([cliente.serialize() for cliente in clientes]), 200