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
            print(f'Ocorreu um erro: {e}') 
            connection.close()
            break

connections = [] # Variável para salvar as conexões dos clientes.


def lidar_usuario(connection: socket.socket, address: str) -> None:
    while True:
        try:
            msg = connection.recv(1024)
            msg_dumped = json.loads(msg)

            if msg:
                print(f'\n{msg_dumped["mensagem"]}')
                
                msg_a_enviar = f'\n{msg_dumped["mensagem"]}'
                transmitir(msg_a_enviar, connection)
            else:
                remover_conexao(connection)
                break

        except Exception as e:
            print(f'Ocorreu um erro: {e}')
            remover_conexao(connection)
            break


def transmitir(mensagem: str, connection: socket.socket) -> None:
    for conexao_cliente in connections:
        if conexao_cliente != connection:
            try:
                conexao_cliente.send(mensagem.encode())
                
            except Exception as e:
                print(f'Ocorreu um erro: {e}')
                remover_conexao(conexao_cliente)


def remover_conexao(conn: socket.socket) -> None:
    if conn in connections:
        conn.close()
        connections.remove(conn)


op = int(input("Digite a opção desejada:\n"
               "1 - Usuario\n"
               "2 - Servidor\n"
               "0 - Fechar\n"))


if op == 1:
    IP_SERVIDOR = str(input("Digite o ip do servidor: "))
    PORTA_SERVIDOR = int(input("Digite a porta do servidor: "))
    usuario = str(input("Digite seu nome de usuário: "))

    try:
        socket_instance = socket.socket()
        socket_instance.connect((IP_SERVIDOR, PORTA_SERVIDOR))
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

            if msg == 'fechar':
                print("Saindo da sessão...")
                break

            payload = json.dumps(payload)

            socket_instance.send(bytes(payload, 'utf-8'))

        socket_instance.close()

    except Exception as e:
        print(f'Ocorreu um erro\n {e}')
        socket_instance.close()

if op == 2:
    LISTENING_PORT = int(input("Digite a porta do servidor: "))

    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen((4))

        print('Servidor online!')

        while True:
            socket_connection, address = socket_instance.accept()
            connections.append(socket_connection)
            threading.Thread(target=lidar_usuario, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'Ocorreu um erro\n {e}')
    finally:
        if len(connections) > 0:
            for conn in connections:
                remover_conexao(conn)

        socket_instance.close()

if op == 0:
    print("Fechando...")
    exit
