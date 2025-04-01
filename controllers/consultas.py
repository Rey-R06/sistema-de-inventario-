from db_connection import create_connection

def traer_datos(intruccion):
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
        cursor.execute(intruccion)# Ejecutar la consulta
        datos = cursor.fetchall()# Obtener todos los resultados
        # Mostrar los datos    
        if datos:
            for fila in datos:
                print(fila)  
        else:
            print("📭 No hay productos registrados.")

def solicitar_datos_producto():
    print(traer_datos("SELECT * FROM productos"))
    while True:
        try:
            eleccion = int(input(("Buscar por: \n1.Nombre \n2-Precio \n3-Cantidad \n4-Categoria \-0-Salir")))

            if eleccion == 0:
                break
            
        except ValueError:
            print("Ingrese un valor valido")

def filtrar_por_nombre():
    print


#nombre  
#precio  
#stock  
#categoria  
    
