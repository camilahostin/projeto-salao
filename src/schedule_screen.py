import datetime
from entities.scheduling import Scheduling
from entities.person import Person
from entities.service import Service

schedule_list: list[Scheduling] = []
client_list: list[Person] = []
service_list: list[Service] = []

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
