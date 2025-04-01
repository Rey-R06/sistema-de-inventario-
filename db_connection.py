import sqlite3

def create_connection():
    """Crea una conexión a la base de datos SQLite"""
    return sqlite3.connect('mi_tienda.db')