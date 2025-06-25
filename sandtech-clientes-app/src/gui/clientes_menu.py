from tkinter import Tk, Menu, messagebox, Toplevel, Label, Entry, Button, Listbox, END
from controllers.cliente_controller import ClienteController

class ClientesMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Clientes")
        self.cliente_controller = ClienteController()

        # Create the menu
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        # Add menu items
        self.client_menu = Menu(self.menu)
        self.menu.add_cascade(label="Clientes", menu=self.client_menu)
        self.client_menu.add_command(label="Dar de alta", command=self.dar_alta)
        self.client_menu.add_command(label="Dar de baja", command=self.dar_baja)
        self.client_menu.add_command(label="Modificar", command=self.modificar)
        self.client_menu.add_command(label="Listar", command=self.listar)
        self.client_menu.add_command(label="Buscar", command=self.buscar)
        self.client_menu.add_separator()
        self.client_menu.add_command(label="Salir", command=self.master.quit)

    def dar_alta(self):
        alta_win = Toplevel(self.master)
        alta_win.title("Alta de Cliente")

        Label(alta_win, text="Nombre:").grid(row=0, column=0)
        nombre_entry = Entry(alta_win)
        nombre_entry.grid(row=0, column=1)

        Label(alta_win, text="Apellido:").grid(row=1, column=0)
        apellido_entry = Entry(alta_win)
        apellido_entry.grid(row=1, column=1)

        Label(alta_win, text="Email:").grid(row=2, column=0)
        email_entry = Entry(alta_win)
        email_entry.grid(row=2, column=1)

        def guardar_cliente():
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            email = email_entry.get()
            if nombre and apellido and email:
                try:
                    self.cliente_controller.alta_cliente(nombre, apellido, email)
                    messagebox.showinfo("Éxito", "Cliente dado de alta correctamente.")
                    alta_win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo dar de alta: {e}")
            else:
                messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")

        Button(alta_win, text="Guardar", command=guardar_cliente).grid(row=3, column=0, columnspan=2)

    def dar_baja(self):
        baja_win = Toplevel(self.master)
        baja_win.title("Baja de Cliente")

        Label(baja_win, text="Código de Cliente:").grid(row=0, column=0)
        codigo_entry = Entry(baja_win)
        codigo_entry.grid(row=0, column=1)

        def eliminar_cliente():
            codigo = codigo_entry.get()
            if codigo:
                if self.cliente_controller.baja_cliente(codigo):
                    messagebox.showinfo("Éxito", "Cliente dado de baja correctamente.")
                    baja_win.destroy()
                else:
                    messagebox.showwarning("No encontrado", "No se encontró el cliente.")
            else:
                messagebox.showwarning("Campo vacío", "Ingrese el código de cliente.")

        Button(baja_win, text="Eliminar", command=eliminar_cliente).grid(row=1, column=0, columnspan=2)

    def modificar(self):
        mod_win = Toplevel(self.master)
        mod_win.title("Modificar Cliente")

        Label(mod_win, text="Código de Cliente:").grid(row=0, column=0)
        codigo_entry = Entry(mod_win)
        codigo_entry.grid(row=0, column=1)

        Label(mod_win, text="Nuevo Nombre:").grid(row=1, column=0)
        nombre_entry = Entry(mod_win)
        nombre_entry.grid(row=1, column=1)

        Label(mod_win, text="Nuevo Apellido:").grid(row=2, column=0)
        apellido_entry = Entry(mod_win)
        apellido_entry.grid(row=2, column=1)

        Label(mod_win, text="Nuevo Email:").grid(row=3, column=0)
        email_entry = Entry(mod_win)
        email_entry.grid(row=3, column=1)

        def modificar_cliente():
            codigo = codigo_entry.get()
            nombre = nombre_entry.get()
            apellido = apellido_entry.get()
            email = email_entry.get()
            if codigo and nombre and apellido and email:
                if self.cliente_controller.modificar_cliente(codigo, nombre, apellido, email):
                    messagebox.showinfo("Éxito", "Cliente modificado correctamente.")
                    mod_win.destroy()
                else:
                    messagebox.showwarning("No encontrado", "No se encontró el cliente.")
            else:
                messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")

        Button(mod_win, text="Modificar", command=modificar_cliente).grid(row=4, column=0, columnspan=2)

    def listar(self):
        listar_win = Toplevel(self.master)
        listar_win.title("Lista de Clientes")

        clientes = self.cliente_controller.listar_clientes()
        listbox = Listbox(listar_win, width=60)
        listbox.pack()

        if clientes:
            for c in clientes:
                listbox.insert(END, f"Código: {c[0]} | Nombre: {c[1]} | Apellido: {c[2]} | Email: {c[3]}")
        else:
            listbox.insert(END, "No hay clientes registrados.")

    def buscar(self):
        buscar_win = Toplevel(self.master)
        buscar_win.title("Buscar Cliente")

        Label(buscar_win, text="Código de Cliente:").grid(row=0, column=0)
        codigo_entry = Entry(buscar_win)
        codigo_entry.grid(row=0, column=1)

        def buscar_cliente():
            codigo = codigo_entry.get()
            if codigo:
                cliente = self.cliente_controller.buscar_cliente(codigo)
                if cliente:
                    messagebox.showinfo("Cliente encontrado",
                        f"Código: {cliente[0]}\nNombre: {cliente[1]}\nApellido: {cliente[2]}\nEmail: {cliente[3]}")
                    buscar_win.destroy()
                else:
                    messagebox.showwarning("No encontrado", "No se encontró el cliente.")
            else:
                messagebox.showwarning("Campo vacío", "Ingrese el código de cliente.")

        Button(buscar_win, text="Buscar", command=buscar_cliente).grid(row=1, column=0, columnspan=2)

if __name__ == "__main__":
    root = Tk()
    app = ClientesMenu(root)
    root.mainloop()