from db.database import Database

class ClienteController:
    """
    Controlador para gestionar operaciones CRUD de clientes en la base de datos SQLite.
    """
    def __init__(self):
        self.db = Database("clientes.db")
        self._crear_tabla()

    def _crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS clientes (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
        self.db.execute(query)

    def alta_cliente(self, nombre, apellido, email):
        query = "INSERT INTO clientes (nombre, apellido, email) VALUES (?, ?, ?)"
        self.db.execute(query, (nombre, apellido, email))

    def baja_cliente(self, codigo):
        query = "DELETE FROM clientes WHERE codigo = ?"
        result = self.db.execute(query, (codigo,))
        return result.rowcount > 0 if result else False

    def modificar_cliente(self, codigo, nombre, apellido, email):
        query = "UPDATE clientes SET nombre=?, apellido=?, email=? WHERE codigo=?"
        result = self.db.execute(query, (nombre, apellido, email, codigo))
        return result.rowcount > 0 if result else False

    def listar_clientes(self):
        query = "SELECT codigo, nombre, apellido, email FROM clientes"
        return self.db.fetchall(query)

    def buscar_cliente(self, codigo):
        query = "SELECT codigo, nombre, apellido, email FROM clientes WHERE codigo=?"
        return self.db.fetchone(query, (codigo,))