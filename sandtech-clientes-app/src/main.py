# sandtech-clientes-app/src/main.py

import tkinter as tk
from gui.clientes_menu import ClientesMenu
import sqlite3

def main():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # Create the clientes table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL
        )
    ''')

    # Forzar que el AUTOINCREMENT empiece en 100
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='clientes'")
    cursor.execute("INSERT INTO sqlite_sequence (name, seq) VALUES ('clientes', 99)")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    root = tk.Tk()
    root.title("SandTech - Gestión de Clientes")
    root.geometry("400x300")
    
    app = ClientesMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()