import sqlite3
from db_connection import create_connection

def create_table():
    """
    Función que crea la tabla 'productos' en la base de datos si no existe.
    Si la base de datos no existe, se crea automáticamente.

    :return: No retorna ningún valor.
    """
    try:
          with create_connection() as conexion:  # Usamos la función create_connection() para la conexión
            cursor = conexion.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL CHECK(precio > 0),
                    stock INTEGER DEFAULT 0,
                    categoria TEXT
                )
            ''')
            
            print("✅ Se verificó/creó la tabla 'productos' correctamente.")

    except sqlite3.Error as e:
        print(f"⚠️ Error al crear la tabla: {e}")
