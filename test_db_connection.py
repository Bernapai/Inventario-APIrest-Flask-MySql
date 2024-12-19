import mysql.connector

# Establecer la conexión a la base de datos MySQL
try:
    conn = mysql.connector.connect(
        host='localhost',          # Dirección del servidor (puede ser 'localhost' o la IP de tu servidor)
        user='root',               # Tu nombre de usuario en MySQL (en este caso 'root')
        password='Juanber123()',   # La contraseña de tu usuario de MySQL
        database='inventario'      # El nombre de tu base de datos
    )

    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Verificar que la conexión es exitosa
    cursor.execute('SELECT DATABASE();')
    result = cursor.fetchone()

    print(f'Conectado correctamente a la base de datos: {result[0]}')

    # Cerrar cursor y conexión
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
