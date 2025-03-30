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

def create_table():
    """
    Funcion que crea una tabla en la base de datos si no existe la tabla,
    si no existe la base de datos se crea con el scrips.
    :param parametros: no ultiliza.
    :return: No returna ningun valor
    """
    with sqlite3.connect("mi_tienda.db") as conexion:# Conexión (si no existe, se crea)
        cursor = conexion.cursor()#Este código crea un cursor, que es un objeto utilizado para ejecutar consultas SQL en la base de datos SQLite.

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL CHECK(precio > 0),
                stock INTEGER DEFAULT 0,
                categoria TEXT
            )
        ''')
        conexion.commit()#Guarda los cambios
        print("\n✅se creo la tabla productos correctamente")
      


def insert_data():
    """
    Funcion que inserta datos a la base de datos mas especifico a la unica tabla que es productos
    :param parametros: no ultiliza.
    :return: No returna ningun valor solo muestra un mensaje si se agrego el producto o no
    """
    nombre = input("Nombre: ")
    while True:
        try:#Captura si el cliente ingresa un valor no valido
            precio = float(input("Precio: "))
            stock = int(input("cantidad: "))
            break                
        except ValueError:
              print("Debe ingresar un valor numérico.")
    categoria = input("Categoria: ")
    # Insertar en la base de datos
    with sqlite3.connect("mi_tienda.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (?, ?, ?, ?)",#Codigo que inserta los datos
                (nombre, precio, stock, categoria)
                )
            print("-----------Producto agregado-----------")
            conexion.commit()#Guarda los cambios

def traer_datos():
    """
    Funcion que trae todos los datos de la tabla productos
    :param parametros: no ultiliza.
    :return: no returna nada solo imprime los datos
    """
      # nombre = input("Nombre del producto: ") 
       #categoria = input("categoria del producto: ")

    with sqlite3.connect("mi_tienda.db") as conexion: # Conectar a la base de datos (se crea si no existe)
        cursor = conexion.cursor() # Crear un cursor para ejecutar consultas
        intruccion = f"select * from productos" # Consulta SQL para obtener todos los registros
        cursor.execute(intruccion)# Ejecutar la consulta
        datos = cursor.fetchall()# Obtener todos los resultados
        # Mostrar los datos    
        if datos:
            for fila in datos:
                print(fila)  
        else:
            print("📭 No hay productos registrados.")

def menu():
    """
    Funcion para mostrar el menu
    :param parametros: no ultiliza.
    :return: no returna nada solo muestra el menu
    """
    while True:
        try:
            eleccion = int(input("1-Insertar nuevos productos\n0-Salir\n-"))
            if eleccion == 0:
                break
            if eleccion == 1:
                #Cuando el usuario ya inserto el primer producto le sale la siguiente pregunta"Agregar otro producto?\n1-Si\n2-No"
                #si se equivoca e ingresa un valor no valido cambiara ban a true por ende el primer mensaje cambiara de 
                #"Agregar producto?\n1-Si\n2-No\n-" a "Agregar otro producto ?\n1-Si\n2-No\n-"
                ban = False  
                while True:
                    if ban:
                        i = int(input("Agregar otro producto ?\n1-Si\n2-No\n-"))
                    else:
                        i = int(input("Agregar producto?\n1-Si\n2-No\n-"))
                    if i == 1:
                        try: 
                            i = 1
                            while i != 2:#siempre que la respuesta sea diferente a 2 al menos que sea un valor invalido seguira en este bucle
                                insert_data()
                                i = int(input("Agregar otro producto?\n1-Si\n2-No\n-"))
                            if i == 2:
                                break
                        except ValueError:
                                print("⚠️ Ingrese un número válido (1 o 2).")
                                ban = True
                    else: 
                        break
        except ValueError:
                print("⚠️ Ingrese un número válido.")   
                
#Agregar limpiador de consola
menu()