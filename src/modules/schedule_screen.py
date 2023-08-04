import datetime
import os
from src.commons.formatter import get_input, show_print

from src.entities.scheduling import Scheduling
from src.modules.client_screen import client_list
from src.modules.service_screen import service_list

schedule_list: list[Scheduling] = []

def schedule_screen():
    os.system('clear')
    print('Tela de Agendamento')
    print('Selecione uma opção')
    option_str = get_input('[1] Agendar horário [2] Listagem Agendamentos [3] Remoção Agendamento: ')    

    try:
        option = int(option_str)
        if option == 1:
            schedule_registration()
        elif option == 2:
            schedule_listing()
        elif option == 3:
            schedule_removal()
        else:
            show_print('Digite uma das opções')
    except ValueError:
        show_print('Por favor, digite 1, 2 ou 3.')

def schedule_registration() -> list[Scheduling]:
    os.system('clear')
    print('Tela de Agendamento')

    client_name_input = get_input('Nome Cliente: ')
    client_name = _get_client_by_name(client_name_input)

    service_name_input = get_input('Nome do Serviço: ')
    service_name =_get_service_by_name(service_name_input)

    datetime_str = get_input('Marque um horário "Dia/Mês/Ano Hora:Minutos" : ')
    datetime_ = datetime.datetime.strptime(datetime_str, '%d/%m/%Y %H:%M')
    scheduling = Scheduling(datetime_, client_name, service_name)
    schedule_list.append(scheduling)

def schedule_listing() -> list[Scheduling]:
    os.system('clear')
    if len(schedule_list) == 0:
        show_print('Lista de agendamentos está vazia')

    print('Tela de Lista de Agendamentos')
    for index, schedule in enumerate(schedule_list):
        show_print(f'{index}. {schedule.person.name} ({schedule.person.nickname}), {schedule.person.telephone} - {schedule.service.name}, {schedule.datetime_}')

def schedule_removal() -> None:
    os.system('clear')
    delete_schedule = get_input('Digite o NOME do cliente para remover agendamento remover: ')

    for index, schedule in enumerate(schedule_list):
        if schedule.person.name == delete_schedule:
            del schedule_list[index]

def _get_client_by_name(client_name_input: str):
    for person in client_list:
        if person.name == client_name_input:
            return person

def _get_service_by_name(service_name_input: str):
    for service in service_list:
        if service.name == service_name_input:
            return service
