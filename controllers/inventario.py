from db_connection import create_connection

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
    with create_connection() as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (?, ?, ?, ?)",#Codigo que inserta los datos
                (nombre, precio, stock, categoria)
                )
            print("-----------Producto agregado-----------")
            conexion.commit()#Guarda los cambios

def agregar_producto():
    """
    Pregunta al usuario si desea agregar un producto.
    Si ingresa un valor inválido, muestra un mensaje de error y vuelve a preguntar.
    no retorna nada
    """
    #Cuando el usuario ya inserto el primer producto le sale la siguiente pregunta"Agregar otro producto?\n1-Si\n2-No"
    #si se equivoca e ingresa un valor no valido cambiara ban a true por ende el primer mensaje cambiara de 
    #"Agregar producto?\n1-Si\n2-No\n-" a "Agregar otro producto ?\n1-Si\n2-No\n-"
    ban = False  
    ciclo = True
    while ciclo:
        try:
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
                            ciclo = False
                except ValueError:
                        print("⚠️ Ingrese un número válido (1 o 2).")
                        ban = True    
            elif i == 2:
                ciclo = False
        except ValueError:
            print("⚠️ Ingrese un número válido (1 o 2).")

