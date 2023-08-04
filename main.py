from src.modules.client_screen import client_screen
from src.modules.schedule_screen import schedule_screen
from src.modules.service_screen import service_screen


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

if __name__ == '__main__':
    while True:
        run()
