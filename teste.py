import socket
import threading
import json
import time
from datetime import date


def receber_mensagem(connection: socket.socket): # Função para receber e tratar as mensagens.
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Ocorreu um erro: msg{e}') 
            connection.close()
            break

def conectar(porta):

    try:
        socket_instance = socket.socket()
        socket_instance.connect(('127.0.0.1', porta))
        threading.Thread(target=receber_mensagem, args=[socket_instance]).start()

        print('Entrou no chat!')

        while True:
            msg = str(input("Digite a mensagem: "))
            time_raw = time.localtime()
            time_value = time.strftime("%H:%M:%S", time_raw)
            today = date.today()
            date_value = today.strftime("%d/%m/%y")
            payload = {
                "usuario": usuario,
                "mensagem": msg,
                "hora": time_value,
                "data": date_value,
            }

            if msg == 'altos':
                porta = input("Digite a porta: ")
                socket_instance.close()
                conectar(porta)
                break

            if msg == 'fechar':
                print("Saindo da sessão...")
                break

            payload = json.dumps(payload)

            socket_instance.send(bytes(payload, 'utf-8'))

        socket_instance.close()

    except Exception as e:
        print(f'Ocorreu um erro conect\n {e}')
        socket_instance.close()

op = int(input("Ação desejada:\n"
               "1 - Entrar em um servidor\n"
               "0 - Fechar\n"))


if op == 1:
    porta = input("Digite a porta: ")
    usuario = str(input("Digite o usuário: "))
    conectar(porta)

if op == 0:
    print("Fechando...")
    exit
