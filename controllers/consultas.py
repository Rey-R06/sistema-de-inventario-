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
            return "📭 No hay productos registrados."

def solicitar_datos_producto():
    datos = traer_datos("SELECT * FROM productos")
    if datos:
        headers = ["Id", "Nombre", "Precio", "Cantidad", "Categoria"]
        print(tabulate(datos, headers=headers, tablefmt="grid"))  # Formato bonito
    else:
        print("📭 No hay productos registrados.")
    while True:
        try:
            eleccion = int(input(("Buscar por: \n1.Nombre \n2-Precio \n3-Cantidad \n4-Categoria \n-0-Salir\n-")))

            if eleccion == 0:
                break

            if eleccion == 1:
                buscar_por_nombre()
        
    
            
        except ValueError:
            print("Ingrese un valor valido")

def buscar_por_nombre():
    nombre = input("Ingrese el nombre: ")
    datos = traer_datos("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    if datos:
        headers = ["Id", "Nombre", "Precio", "Cantidad", "Categoria"]
        print(tabulate(datos, headers=headers, tablefmt="grid"))  # Formato bonito



#nombre  
#precio  
#stock  
#categoria  
    
