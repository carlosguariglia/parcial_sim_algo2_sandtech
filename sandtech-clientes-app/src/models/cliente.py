class Cliente:
    def __init__(self, codigo, nombre, apellido, email):
        """
        Constructor de la clase Cliente.

        Parametros:
        codigo (int): numero de identificacion del cliente.
        nombre (str): nombre del cliente.
        apellido (str): apellido del cliente.
        email (str): direccion correo electronica del cliente.

        """
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        """
        Representacion de objeto como cadena.

        Retorna una cadena que describe al objeto en forma de "Cliente(codigo=XX, nombre=XXX, apellido=XXX, email=XXX@XXX.XXX)".
        
        Returns:
        str: representacion del objeto como cadena.
        """
        return f"Cliente(codigo={self.codigo}, nombre={self.nombre}, apellido={self.apellido}, email={self.email})"
