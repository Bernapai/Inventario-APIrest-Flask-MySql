from flask import jsonify
from  models.services.ventasServices import VentasServices

class VentasController:
    @staticmethod
    def agregar_venta(data):
        try:
              # Obtener los datos del cuerpo de la solicitud
            # Validación de los campos obligatorios
            if not data or 'id_cliente' not in data or 'fecha' not in data or 'total' not in data or 'usuario' not in data:
                return jsonify({'error': 'Datos incompletos'}), 400
            # Llamar al servicio para agregar la nueva venta
            nueva_venta = VentasServices.agregar_venta(
                data['id_cliente'],
                data['fecha'],
                data['total'],
                data['usuario']
            )
            return jsonify(nueva_venta.serialize()), 201  # Retornar la venta agregada en formato JSON
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def actualizar_venta(id_venta):
        try:
            id_cliente = data.get('id_cliente')
            fecha = data.get('fecha')
            total = data.get('total')
            usuario = data.get('usuario')

            # Llamar al servicio para actualizar la venta
            venta_actualizada = VentasServices.actualizar_venta(  id_venta = id_venta, id_cliente = id_cliente, fecha = fecha, total = total, usuario = usuario)
            
            if not venta_actualizada:
                return jsonify({'error': 'Venta no encontrada'}), 404
            else :
                return jsonify(venta_actualizada), 200
            

    @staticmethod
    def eliminar_venta(id_venta):
        try:
            # Llamar al servicio para eliminar la venta
            venta_eliminada = VentasServices.eliminar_venta(id_venta)
            if not venta_eliminada:
                return jsonify({'error': 'Venta no encontrada'}), 404
            return jsonify({'message': 'Venta eliminada exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def obtener_ventas():
        try:
            # Llamar al servicio para obtener todas las ventas
            ventas = VentasServices.obtener_todas_ventas()
            return jsonify([venta.serialize() for venta in ventas]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    

    @staticmethod
    def obtener_venta(id_venta):
        try:
            # Llamar al servicio para obtener una venta por ID
            venta = VentasServices.obtener_venta_por_id(id_venta)
            if not venta:
                return jsonify({'error': 'Venta no encontrada'}), 404
            return jsonify(venta.serialize()), 200
        except Exception as e:
            return jsonify({'error': str(e)}),

    


