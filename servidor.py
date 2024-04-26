import socket
import threading
import json
import time
from datetime import date

connections = []  # Variável para salvar as conexões dos clientes.
servidor_ativo = True  # Variável para controlar o estado do servidor.

def lidar_usuario(connection: socket.socket, address: str) -> None:
    global servidor_ativo
    while servidor_ativo:
        try:
            msg = connection.recv(1024)
            if msg:
                msg_dumped = json.loads(msg)
                print(f'\n{msg_dumped["mensagem"]}')

                if msg_dumped["mensagem"] == "fechar servidor":
                    print("Fechando servidor...")
                    fechar_servidor()
                    break

                transmitir(msg.decode(), connection)
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

def fechar_servidor():
    global servidor_ativo
    servidor_ativo = False
    for conn in connections:
        conn.close()
    connections.remove(conn)
    exit

op = int(input("Ação desejada:\n"
               "1 - Criar servidor\n"
               "0 - Fechar\n"))

if op == 1:
    LISTENING_PORT = int(input("Digite a porta do servidor: "))

    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(4)

        print('Servidor online!')

        while servidor_ativo:
            socket_connection, address = socket_instance.accept()
            connections.append(socket_connection)
            threading.Thread(target=lidar_usuario, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'Ocorreu um erro\n {e}')
    finally:
        socket_instance.close()

elif op == 0:
    print("Fechando...")
    exit()