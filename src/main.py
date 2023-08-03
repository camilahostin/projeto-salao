import datetime
from entities.person import Person
from entities.scheduling import Scheduling
from entities.service import Service

client_list: list[Person] = []
service_list: list[Service] = []
schedule_list: list[Scheduling] = []

def run():
    print('Selecione uma opção')
    option_str = input('[1] Cliente [2] Serviços [3] Agendamento: ')

    try:
        option = int(option_str)

        if option == 1:
            client_screen()
        elif option == 2:
            service_screen()
        elif option == 3:
            schedule_screen()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2 ou 3.')

def client_screen():
    print('Tela de Cliente')
    print('Selecione uma opção')
    option_str = input('[1] Cadastro [2] Listagem Clientes [3] Remoção Cliente: ')

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

def customer_registration():
    print('Tela de Cadastro de Cliente')
    name = input('Nome: ')
    telephone = input('Telefone: ')
    nickname = input('Apelido: ')
    cpf = input('CPF: ')
    person = Person(name, telephone, nickname, cpf)
    client_list.append(person)

def customer_listing():
    if len(client_list) == 0:
        print('Lista de clientes está vazia')

    print('Tela de Lista de Clientes')
    for index, person in enumerate(client_list):
        print(f'{index}. {person.name}, {person.telephone} - {person.cpf}')

def customer_removal():
    delete_client = input('Digite o CPF do cliente que deseja remover: ')

    for index, person in enumerate(client_list):
        if person.cpf == delete_client:
            print('oi')
            del client_list[index]

def service_screen():
    print('Tela de Serviço')
    print('Selecione uma opção')
    option_str = input('[1] Cadastro de Serviço [2] Listagem de Serviços [3] Remoção de Serviço: ')

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

def service_registration():
    print('Tela de Cadastro de Serviço')
    name = input('Nome do Serviço: ')
    value = input('Valor: ')
    service = Service(name, value)
    service_list.append(service)

def service_listing():
    if len(service_list) == 0:
        print('Lista de serviços está vazia')

    print('Tela de Lista de Clientes')
    for index, service in enumerate(service_list):
        print(f'{index}. {service.name}, {service.value}')

def service_removal():
    delete_service = input('Digite o NOME que deseja remover: ')

    for index, service in enumerate(service_list):
        if service.name == delete_service:
            del service_list[index]

def schedule_screen():
    print('Tela de Agendamento')
    print('Selecione uma opção')
    option_str = input('[1] Agendar horário [2] Listagem Agendamentos [3] Remoção Agendamento: ')    

    try:
        option = int(option_str)
        if option == 1:
            schedule_registration()
        elif option == 2:
            schedule_listing()
        elif option == 3:
            schedule_removal()
        else:
            print('Digite uma das opções')
    except ValueError:
        print('Por favor, digite 1, 2 ou 3.')

def schedule_registration():
    print('Tela de Agendamento')
    client_name = input('Nome Cliente: ')
    service_name = input('Nome do Serviço: ')
    datetime_str = input('Marque um horário "Dia/Mês/Ano Hora:Minutos" : ')
    datetime_ = datetime.datetime.strptime(datetime_str, '%d/%m/%Y %H:%M')
    scheduling = Scheduling(client_name, service_name, datetime_)
    schedule_list.append(scheduling)

def schedule_listing():
    if len(schedule_list) == 0:
        print('Lista de agendamentos está vazia')

    print('Tela de Lista de Agendamentos')
    for index, schedule in enumerate(schedule_list):
        for index, person in enumerate(client_list):
            for index, service in enumerate(service_list):
                print(f'{index}. {person.name} ({person.nickname}), {person.telephone} - {service.name}, {schedule.datetime_}')

def schedule_removal():
    delete_schedule = input('Digite o NOME do cliente para remover agendamento remover: ')

    for index, schedule in enumerate(schedule_list):
        for index, service in enumerate(service_list):
            for index, person in enumerate(client_list):
                if person.name == delete_schedule:
                    del schedule_list[index]

if __name__ == '__main__':
    while True:
        run()
