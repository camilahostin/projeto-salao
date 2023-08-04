import unittest
from unittest.mock import Mock, patch

from src.modules.service_screen import (service_list, service_listing,
                                        service_registration, service_removal)


class TestServiceScreen(unittest.TestCase):

    @patch('src.modules.service_screen.get_input', side_effect = ['Corte de Cabelo', '110.00'])
    def test_should_register_service_in_service_list(self, mock_get_input: Mock):
        # Arrange
        # Action
        service_registration()
        # Assert
        self.assertEqual(service_list[0].name, 'Corte de Cabelo')
        self.assertEqual(service_list[0].value, 110.00)

    @patch('src.modules.service_screen.show_print')
    @patch('src.modules.service_screen.get_input')
    def test_should_return_message_empty_list(self, mock_get_input: Mock, mock_print: Mock):
        # Arrange
        # Action
        expected_msn = 'Lista de serviços está vazia'
        service_listing()
        # Assert
        self.assertTrue(len(service_list) == 0)
        self.assertEqual(expected_msn, mock_print.call_args[0][0])

    @patch('src.modules.service_screen.show_print')
    @patch('src.modules.service_screen.get_input', side_effect=['Corte de Cabelo', '110.0'])
    def test_should_return_list_of_services(self, mock_get_input: Mock, mock_print: Mock):
        # Arrange
        service_registration()
        # Action
        service_listing()
        expected_msn = '0. Corte de Cabelo, 110.0'
        # Assert
        self.assertEqual(expected_msn, mock_print.call_args[0][0])
        self.assertFalse(len(service_list) == 0)

    @patch('src.modules.service_screen.get_input', side_effect=['Corte de Cabelo', '110.0', 'Corte de Cabelo'])
    def test_should_erase_service_from_service_list(self, mock_get_input: Mock):
        # Arrange
        service_registration()
        # Action
        service_removal()
        # Assert
        self.assertTrue(len(service_list) == 0)
