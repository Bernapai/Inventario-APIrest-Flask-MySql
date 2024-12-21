from flask import jsonify
from models.services.categoriaServices import CategoriaServices


class CategoriaController:


    @staticmethod
    def agregar_categoria(data):
       try :
        # Validación de los campos obligatorios
            if not data or 'nombre' not in data or 'descripcion' not in data:
                return jsonify({'error': 'Nombre de categoría es obligatorio'}), 400
            else:
                # Llamamos al servicio para agregar la categoría
                categoria = CategoriaServices.agregar_categoria(data['nombre'], data['descripcion'])
                return jsonify(categoria.serialize()), 201
       except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def actualizar_categoria(id_categoria, data):
        # Recibimos los datos de la solicitud y pasamos a los servicios para actualizar la categoría
        nombre = data.get('nombre')
        descripcion = data.get('descripcion')

        # Llamamos al servicio para actualizar la categoría
        categoria = CategoriaServices.actualizar_categoria(id_categoria, nombre=nombre, descripcion = descripcion)
        
        if categoria is None:
            return jsonify({'mensaje': 'Categoría no encontrada'}), 404
        
        # Retornamos la respuesta serializada
        return jsonify(categoria.serialize()), 200

    @staticmethod
    def eliminar_categoria(id_categoria):
        # Llamamos al servicio para eliminar la categoría
        try:
            CategoriaServices.eliminar_categoria(id_categoria)
            return jsonify({'mensaje': 'Categoría eliminada exitosamente'}), 200
        except ValueError:
            return jsonify({'mensaje': 'Categoría no encontrada'}), 404

    @staticmethod
    def obtener_todas_categorias():
        # Llamamos al servicio para obtener todas las categorías
        categorias = CategoriaServices.obtener_todas_categorias()
        return jsonify([categoria.serialize() for categoria in categorias]), 200

    @staticmethod
    def obtener_categoria_por_id(id_categoria):
        # Llamamos al servicio para obtener una categoría por ID
        categoria = CategoriaServices.obtener_categoria_por_id(id_categoria)
        if categoria is None:
            return jsonify({'mensaje': 'Categoría no encontrada'}), 404
        return jsonify(categoria.serialize()), 200

    @staticmethod
    def obtener_categoria_por_nombre(nombre):
        # Llamamos al servicio para obtener una categoría por nombre
        categoria = CategoriaServices.obtener_categoria_por_nombre(nombre)
        if categoria is None:
            return jsonify({'mensaje': 'Categoría no encontrada'}), 404
        return jsonify(categoria.serialize()), 200
