import os
from src.commons.formatter import get_input, show_print
from src.entities.person import Person


client_list: list[Person] = []

def client_screen():
    os.system('clear')
    print('Tela de Cliente')
    print('Selecione uma opção')
    option_str = get_input('[1] Cadastro [2] Listagem Clientes [3] Remoção Cliente: ')

    try:
        option = int(option_str)

        if option == 1:
            customer_registration()
        elif option == 2:
            customer_listing()
        elif option == 3:
            customer_removal()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2 ou 3.')

def customer_registration() -> list[Person]:
    os.system('clear')
    print('Tela de Cadastro de Cliente')
    name = get_input('Nome: ')
    telephone = get_input('Telefone: ')
    nickname = get_input('Apelido: ')
    cpf = get_input('CPF: ')
    person = Person(name, telephone, nickname, cpf)
    client_list.append(person)

def customer_listing() -> list[Person]:
    os.system('clear')
    if len(client_list) == 0:
        show_print('Lista de clientes está vazia')

    print('Tela de Lista de Clientes')
    for index, person in enumerate(client_list):
        show_print(f'{index}. {person.name}, {person.telephone} - {person.cpf}')

def customer_removal() -> None:
    os.system('clear')
    delete_client = get_input('Digite o CPF do cliente que deseja remover: ')

    for index, person in enumerate(client_list):
        if person.cpf == delete_client:
            del client_list[index]
