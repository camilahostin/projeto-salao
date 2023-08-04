from entities.service import Service


service_list: list[Service] = []

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
