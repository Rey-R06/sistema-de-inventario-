from db_connection import create_connection
from tabulate import tabulate

def traer_datos(consulta, params=()):
    """
    Funcion que trae todos los datos de la tabla productos
    :param parametros: no ultiliza.
    :return: no returna nada solo imprime los datos
    """
      # nombre = input("Nombre del producto: ") 
       #categoria = input("categoria del producto: ")

    with create_connection() as conexion: # Conectar a la base de datos (se crea si no existe)
        cursor = conexion.cursor() # Crear un cursor para ejecutar consultas
         # Consulta SQL para obtener todos los registros
        cursor.execute(consulta, params)# Ejecutar la consulta
        datos = cursor.fetchall()# Obtener todos los resultados
        # Mostrar los datos    
        if datos:
            return datos
        else:
            return ""

def solicitar_datos_producto():
    datos = traer_datos("SELECT * FROM productos")
    if datos:
        headers = ["Id", "Nombre", "Precio", "Cantidad", "Categoria"]
        print(tabulate(datos, headers=headers, tablefmt="grid"))  # Formato bonito
    else:
        print("📭 No hay productos registrados.")
    while True:
        try:
            eleccion = int(input(("Buscar por: \n1.Nombre \n2-Categoria \n3-Precio \n4-Cantidad \n-0-Salir\n-")))

            if eleccion == 0:
                break

            if eleccion == 1:
                buscar_por_nombre_o_categoria("nombre")
            elif eleccion == 2:
                buscar_por_nombre_o_categoria("categoria")
            elif eleccion == 3:
                buscar_por_precio_o_cantidad("precio")
            elif eleccion == 4:
                buscar_por_precio_o_cantidad("stock")
            elif eleccion == 0:
                break
        except ValueError:
            print("Ingrese un valor valido")

def buscar_por_nombre_o_categoria(columna):
    """
    Busca productos en el inventario por nombre o categoría exacta.
    
    Realiza una búsqueda exacta en la base de datos de productos según
    la columna especificada ('nombre' o 'categoria') y muestra los resultados
    en formato de tabla.

    Parámetros:
        columna (str): Nombre de la columna por la que se filtrará
                      ('nombre' o 'categoria')

    Comportamiento:
        1. Solicita al usuario el término de búsqueda
        2. Ejecuta consulta SQL con filtro exacto (WHERE = ?)
        3. Muestra resultados en formato de tabla o mensaje si no hay coincidencias

    Características:
        - Usa parámetros SQL para prevenir inyecciones
        - Muestra resultados formateados con tabulate
        - Maneja casos sin resultados encontrados

    Dependencias:
        - tabulate (para mostrar resultados en formato de tabla)
        - traer_datos() (función que ejecuta consultas SQL)
    """
    nombre_o_categoria = input(f"Ingrese el {columna}: ")
    datos = traer_datos(f"SELECT * FROM productos WHERE {columna} = ?", (nombre_o_categoria,))
    
    if datos:
        headers = ["Id", "Nombre", "Precio", "Cantidad", "Categoria"]
        print(tabulate(datos, headers=headers, tablefmt="grid"))  # Formato bonito
    else:
        print("📭 No hay productos registrados.")



def buscar_por_precio_o_cantidad(columna):
    """
    Busca productos en el inventario según criterios de precio o cantidad.
    
    Permite realizar búsquedas específicas u ordenamientos de los productos
    según la columna especificada ('precio' o 'cantidad').

    Parámetros:
        columna (str): Nombre de la columna por la que se filtrará/ordenará
                       ('precio' o 'cantidad')

    Comportamiento:
        1. Muestra un menú interactivo con opciones de búsqueda
        2. Ejecuta la consulta SQL correspondiente a la opción seleccionada
        3. Muestra los resultados en formato de tabla ordenada
        4. Gestiona casos cuando no hay resultados

    Opciones del menú:
        1 - Búsqueda por valor exacto
        2 - Orden descendente (mayor a menor)
        3 - Orden ascendente (menor a mayor)
        0 - Salir del menú

    Dependencias:
        - tabulate (para mostrar resultados en formato de tabla)
        - traer_datos() (función que ejecuta consultas SQL)

    Manejo de errores:
        - Valida que existan datos antes de mostrar resultados
        - Detecta entradas numéricas inválidas
    """
    while eleccion != 0:
        eleccion = int(input(f"Buscar por:\n1-{columna.capitalize()} especifico\n2-Mayor a menor \n3-Menor a mayor\n0-Salir\n-"))
        
        datos = []  # Inicializamos datos como lista vacía

        while eleccion != 0:
            if eleccion == 1:
                precio_o_cantidad = float(input(f"{columna.capitalize()}: "))
                datos = traer_datos(f"SELECT * FROM productos WHERE {columna} = ?", (precio_o_cantidad,))
            elif eleccion == 2:
                datos = traer_datos(f"SELECT * FROM productos ORDER BY {columna} desc")
            elif eleccion == 3:
                datos = traer_datos(f"SELECT * FROM productos ORDER BY {columna} asc")
            elif eleccion == 0:
                break
            
            if datos:
                headers = ["Id", "Nombre", "Precio", "Cantidad", "Categoria"]
                print(tabulate(datos, headers=headers, tablefmt="grid"))  # Formato bonito
                break
            else:
                print("📭 No hay productos registrados.")
                break

