from db.database import Database
from utils.logger import log_info, log_warning, log_error

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
        log_info("Tabla 'clientes' verificada o creada.")

    def alta_cliente(self, nombre, apellido, email):
        query = "INSERT INTO clientes (nombre, apellido, email) VALUES (?, ?, ?)"
        self.db.execute(query, (nombre, apellido, email))
        log_info(f"Alta de cliente: {nombre} {apellido} ({email})")

    def baja_cliente(self, codigo):
        query = "DELETE FROM clientes WHERE codigo = ?"
        result = self.db.execute(query, (codigo,))
        if result and result.rowcount > 0:
            log_info(f"Baja de cliente código: {codigo}")
            return True
        else:
            log_warning(f"Intento de baja fallido para código: {codigo}")
            return False

    def modificar_cliente(self, codigo, nombre, apellido, email):
        query = "UPDATE clientes SET nombre=?, apellido=?, email=? WHERE codigo=?"
        result = self.db.execute(query, (nombre, apellido, email, codigo))
        if result and result.rowcount > 0:
            log_info(f"Modificación de cliente código: {codigo}")
            return True
        else:
            log_warning(f"Intento de modificación fallido para código: {codigo}")
            return False

    def listar_clientes(self):
        query = "SELECT codigo, nombre, apellido, email FROM clientes"
        clientes = self.db.fetchall(query)
        log_info(f"Listado de clientes: {len(clientes)} encontrados.")
        return clientes

    def buscar_cliente(self, codigo):
        query = "SELECT codigo, nombre, apellido, email FROM clientes WHERE codigo=?"
        cliente = self.db.fetchone(query, (codigo,))
        if cliente:
            log_info(f"Búsqueda exitosa de cliente código: {codigo}")
        else:
            log_warning(f"Búsqueda fallida de cliente código: {codigo}")
        return cliente