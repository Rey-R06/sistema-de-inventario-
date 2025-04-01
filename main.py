from models.productos import create_table
from views.menu import mostrar_menu

def main():
    """
    Punto de entrada principal del programa.
    Llama a la función que muestra el menú y gestiona la interacción con el usuario.
    """
    print("Bienvenido al Gestor de Inventario")
    
    # Crear la base de datos y la tabla si no existen
    create_table()
    # Mostrar el menú principal
    mostrar_menu()

if __name__ == "__main__":
    main()