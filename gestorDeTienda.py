import sqlite3

# Conexión (si no existe, se crea)
conexion = sqlite3.connect("mi_tienda.db")
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

def create_table():# Conexión (si no existe, se crea)
    
    with sqlite3.connect("mi_tienda.db") as conexion:
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
        conexion.commit()
        print("\n✅se creo la tabla productos correctamente")
      


def insert_data():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    stock = int(input("Cantidad: "))
    categoria = input("categoria del producto: ")

    # Insertar en la base de datos
    with sqlite3.connect("mi_tienda.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (?, ?, ?, ?)",
                (nombre, precio, stock, categoria)
            )
            conexion.commit()
            print("\n✅ Producto añadido correctamente")

def traer_datos():
      # nombre = input("Nombre del producto: ")
       #categoria = input("categoria del producto: ")

    # Insertar en la base de datos
       with sqlite3.connect("mi_tienda.db") as conexion:
             cursor = conexion.cursor()
             intruccion = f"select * from productos"
             cursor.execute(intruccion)
             datos = cursor.fetchall()
             conexion.commit()
             print(datos)

traer_datos()