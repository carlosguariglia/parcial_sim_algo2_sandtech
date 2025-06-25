class Cliente:
    def __init__(self, id_cliente, nombre, contacto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.contacto = contacto

    def __str__(self):
        return f"Cliente(ID: {self.id_cliente}, Nombre: {self.nombre}, Contacto: {self.contacto})"

    def to_dict(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "contacto": self.contacto
        }