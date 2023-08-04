import os
from src.commons.formatter import get_input, show_print
from src.entities.service import Service

service_list: list[Service] = []

def service_screen():
    os.system('clear')
    print('Tela de Serviço')
    print('Selecione uma opção')
    option_str = get_input('[1] Cadastro de Serviço [2] Listagem de Serviços [3] Remoção de Serviço: ')

    try:
        option = int(option_str)
        if option == 1:
            service_registration()
        elif option == 2:
            service_listing()
        elif option == 3:
            service_removal()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2 ou 3.')

def service_registration() -> list[Service]:
    os.system('clear')
    print('Tela de Cadastro de Serviço')
    name = get_input('Nome do Serviço: ')
    value_str = get_input('Valor: ')
    value = float(value_str)
    service = Service(name, value)
    service_list.append(service)

def service_listing() -> list[Service]:
    os.system('clear')
    if len(service_list) == 0:
        show_print('Lista de serviços está vazia')

    print('Tela de Lista de Clientes')
    for index, service in enumerate(service_list):
        show_print(f'{index}. {service.name}, {service.value}')

def service_removal() -> None:
    os.system('clear')
    delete_service = get_input('Digite o NOME do serviço que deseja remover: ')

    for index, service in enumerate(service_list):
        if service.name == delete_service:
            del service_list[index]
