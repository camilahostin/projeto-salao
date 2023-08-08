import datetime
import unittest
from unittest.mock import Mock, patch
from src.modules.client_screen import customer_registration

from src.modules.schedule_screen import schedule_list, schedule_listing, schedule_registration, schedule_removal
from src.modules.service_screen import service_registration


class TestScheduleScreen(unittest.TestCase):

    @patch('src.modules.schedule_screen.get_input', side_effect = ['Claudia', 'Corte de Cabelo', '14/08/2023 15:30'])
    @patch('src.modules.service_screen.get_input', side_effect = ['Corte de Cabelo', '110.00'])
    @patch('src.modules.client_screen.get_input', side_effect = ['Claudia', '(47) 99123-4567', 'clau', '123.456.789-00'])
    def test_should_register_schedule_in_schedule_list(self, mock_get_input: Mock,
                                                       mock__client: Mock, mock__service: Mock):
        # Arrange
        datetime_ = datetime.datetime(2023, 8, 14, 15, 30)
        # Action
        customer_registration()
        service_registration()
        schedule_registration()
        # Assert
        self.assertEqual(schedule_list[0].person.name, 'Claudia')
        self.assertEqual(schedule_list[0].service.name, 'Corte de Cabelo')
        self.assertEqual(schedule_list[0].datetime_, datetime_)

    @patch('src.modules.schedule_screen.show_print')
    @patch('src.modules.schedule_screen.get_input')
    def test_should_return_message_empty_list(self, mock_get_input: Mock, mock_print: Mock):
        # Arrange
        # Action
        expected_msn = 'Lista de agendamentos está vazia'
        schedule_listing()
        # Assert
        self.assertTrue(len(schedule_list) == 0)
        self.assertEqual(expected_msn, mock_print.call_args[0][0])

    @patch('src.modules.schedule_screen.get_input', side_effect = ['Claudia', 'Corte de Cabelo', '14/08/2023 15:30', 'Claudia'])
    @patch('src.modules.service_screen.get_input', side_effect = ['Corte de Cabelo', '110.00'])
    @patch('src.modules.client_screen.get_input', side_effect = ['Claudia', '(47) 99123-4567', 'clau', '123.456.789-00'])
    def test_should_erase_schedule_from_schedule_list(self, mock_get_input: Mock,
                                                       mock__client: Mock, mock__service: Mock):
        # Arrange
        customer_registration()
        service_registration()
        schedule_registration()
        # Action
        schedule_removal()
        # Assert
        self.assertTrue(len(schedule_list) == 0)

    @patch('src.modules.schedule_screen.show_print')
    @patch('src.modules.schedule_screen.get_input', side_effect = ['Claudia', 'Corte de Cabelo', '14/08/2023 15:30', 'Claudia'])
    @patch('src.modules.service_screen.get_input', side_effect = ['Corte de Cabelo', '110.00'])
    @patch('src.modules.client_screen.get_input', side_effect = ['Claudia', '(47) 99123-4567', 'clau', '123.456.789-00'])
    def test_should_return_list_of_clients(self, mock_get_input: Mock, mock__client: Mock,
                                           mock__service: Mock, mock_print: Mock):
        # Arrange
        customer_registration()
        service_registration()
        schedule_registration()
        # Action
        schedule_listing()
        expected_msn = '0. Claudia (clau), (47) 99123-4567 - Corte de Cabelo, 2023-08-14 15:30:00'
        # Assert
        self.assertFalse(len(schedule_list) == 0)
        self.assertEqual(expected_msn, mock_print.call_args[0][0])
