# sandtech-clientes-app/src/main.py

import tkinter as tk
from gui.clientes_menu import ClientesMenu

def main():
    root = tk.Tk()
    root.title("SandTech - Gestión de Clientes")
    root.geometry("500x350")
    root.configure(bg="#e3eaf2")
    root.eval('tk::PlaceWindow . center')

    app = ClientesMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()