from controllers.inventario import agregar_producto
from controllers.consultas import solicitar_datos_producto

def mostrar_menu():
    """
    Funcion para mostrar el menu
    :param parametros: no ultiliza.
    :return: no returna nada solo muestra el menu
    """
    while True:
        try:
            eleccion = int(input("1-Insertar nuevos productos\n2-Consultar producto\n0-Salir\n-"))
            if eleccion == 0:
                break
            if eleccion == 1:
                 agregar_producto()
            elif eleccion == 2:
                 solicitar_datos_producto()
        except ValueError:
                print("⚠️ Ingrese un número válido.")   
                