import unittest
from unittest.mock import Mock, patch

from src.modules.client_screen import (client_list, customer_listing,
                                       customer_registration, customer_removal)


class TestClientScreen(unittest.TestCase):

    @patch('src.modules.client_screen.get_input', side_effect = ['Claudia', '(47) 99123-4567', 'clau', '123.456.789-00'])
    def test_should_register_client_in_client_list(self, mock_get_input: Mock):
        # Arrange
        # Action
        customer_registration()
        # Assert
        self.assertEqual(client_list[0].name, 'Claudia')
        self.assertEqual(client_list[0].telephone, '(47) 99123-4567')
        self.assertEqual(client_list[0].nickname, 'clau')
        self.assertEqual(client_list[0].cpf, '123.456.789-00')

    @patch('src.modules.client_screen.show_print')
    @patch('src.modules.client_screen.get_input')
    def test_should_return_message_empty_list(self, mock_get_input: Mock, mock_print: Mock):
        # Arrange
        # Action
        expected_msn = 'Lista de clientes está vazia'
        customer_listing()
        # Assert
        self.assertTrue(len(client_list) == 0)
        self.assertEqual(expected_msn, mock_print.call_args[0][0])

    @patch('src.modules.client_screen.show_print')
    @patch('src.modules.client_screen.get_input', side_effect=['Claudia', '(47) 99123-4567', 'clau', '123.456.789-00'])
    def test_should_return_list_of_clients(self, mock_get_input: Mock, mock_print: Mock):
        # Arrange
        customer_registration()
        # Action
        customer_listing()
        expected_msn = '0. Claudia, (47) 99123-4567 - 123.456.789-00'
        # Assert
        self.assertEqual(expected_msn, mock_print.call_args[0][0])
        self.assertFalse(len(client_list) == 0)

    @patch('src.modules.client_screen.get_input', side_effect=['Claudia', '(47) 99123-4567', 'clau', '123.456.789-00', '123.456.789-00'])
    def test_should_erase_client_from_client_list(self, mock_get_input: Mock):
        # Arrange
        customer_registration()
        # Action
        customer_removal()
        # Assert
        self.assertTrue(len(client_list) == 0)
