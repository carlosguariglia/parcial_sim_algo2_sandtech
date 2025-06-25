import unittest
from src.controllers.cliente_controller import ClienteController
from src.models.cliente import Cliente

class TestClienteController(unittest.TestCase):

    def setUp(self):
        self.controller = ClienteController()
        self.test_cliente = Cliente(id=100, name="Test Client", contact_info="test@example.com")
        self.controller.add_cliente(self.test_cliente)

    def tearDown(self):
        self.controller.delete_cliente(self.test_cliente.id)

    def test_add_cliente(self):
        cliente = Cliente(id=101, name="New Client", contact_info="new@example.com")
        self.controller.add_cliente(cliente)
        self.assertIn(cliente, self.controller.get_all_clientes())
        self.controller.delete_cliente(cliente.id)

    def test_delete_cliente(self):
        self.controller.delete_cliente(self.test_cliente.id)
        self.assertNotIn(self.test_cliente, self.controller.get_all_clientes())

    def test_modify_cliente(self):
        updated_info = "updated@example.com"
        self.controller.modify_cliente(self.test_cliente.id, name="Updated Client", contact_info=updated_info)
        modified_cliente = self.controller.get_cliente_by_id(self.test_cliente.id)
        self.assertEqual(modified_cliente.contact_info, updated_info)

    def test_get_cliente_by_id(self):
        cliente = self.controller.get_cliente_by_id(self.test_cliente.id)
        self.assertEqual(cliente.id, self.test_cliente.id)

    def test_get_cliente_not_found(self):
        cliente = self.controller.get_cliente_by_id(999)  # Assuming 999 does not exist
        self.assertIsNone(cliente)

if __name__ == '__main__':
    unittest.main()