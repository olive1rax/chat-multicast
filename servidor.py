import socket
import threading
import json
import time
from datetime import date


connections = [] # Variável para salvar as conexões dos clientes.


def lidar_usuario(connection: socket.socket, address: str) -> None:
    while True:
        try:
            msg = connection.recv(1024)
            msg_dumped = json.load(msg)

            if msg:
                print(f'\n{msg_dumped["mensagem"]}')
                
                msg_a_enviar = f'\n{msg_dumped ["mensagem"]}'
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


op = int(input("Ação desejada:\n"
               "1 - Criar servidor\n"
               "0 - Fechar\n"))

if op == 1:
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

