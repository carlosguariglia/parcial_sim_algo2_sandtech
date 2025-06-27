class Cliente:
    def __init__(self, codigo, nombre, apellido, email):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return f"Cliente(codigo={self.codigo}, nombre={self.nombre}, apellido={self.apellido}, email={self.email})"
