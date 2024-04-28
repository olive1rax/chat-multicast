import socket
import threading
import json
import time
import os
from datetime import date

# Variável global para manter a conexão com o servidor
socket_instance = None

def fechar_conexao():
    global socket_instance
    if socket_instance:
        try:
            socket_instance.close()
        except Exception as e:
            print(f'Erro ao fechar a conexão: {e}')

def receber_mensagem(connection: socket.socket):
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

SERVIDORES = [
    {"nome": "Alto Tietê", "ip": "127.0.0.1", "porta": 8001},
    {"nome": "Médio Tietê", "ip": "127.0.0.1", "porta": 8002},
    {"nome": "Tietê Interiorano", "ip": "127.0.0.1", "porta": 8003},
    {"nome": "Baixo Tietê", "ip": "127.0.0.1", "porta": 8004}
    ]

def conectar_servidor(op_servidor, usuario):
    global socket_instance
    try:
        fechar_conexao()

        servidor_escolhido = SERVIDORES[op_servidor - 1]
        socket_instance = socket.socket()
        socket_instance.connect((servidor_escolhido['ip'], servidor_escolhido['porta']))
        threading.Thread(target=receber_mensagem, args=[socket_instance]).start()

        print('Você entrou no chat!')

        payload = {"log": "join", "usuario": usuario, "mensagem": "entrou no servidor"}
        socket_instance.send(json.dumps(payload).encode())

    except Exception as e:
        print(f'Ocorreu um erro\n {e}')
        socket_instance.close()

op = int(input("Ação desejada:\n"
               "1 - Entrar em um servidor\n"
               "0 - Fechar\n"))

if op == 1:
    usuario = str(input("Digite seu nome de usuário: "))

    print("Servidores disponíveis:")
    for i, servidor in enumerate(SERVIDORES):
        print(f"{i+1} - {servidor['nome']}")

    op_servidor = int(input("Escolha o servidor desejado: "))

    if socket_instance and SERVIDORES[op_servidor - 1]['ip'] == socket_instance.getpeername()[0]:
        print("Você já está conectado a este servidor!")
    else:
        conectar_servidor(op_servidor, usuario)

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
            fechar_conexao()
            break
        
        elif msg == '/trocar servidor':
            print("Trocando de servidor...")
            op_servidor = int(input("Escolha o novo servidor desejado: "))
            conectar_servidor(op_servidor, usuario)
            continue

        payload = json.dumps(payload)
        # print("Mensagem enviada:", payload) # Ver STRING enviada
        socket_instance.send(bytes(payload, 'utf-8'))

    socket_instance.close()

elif op == 0:
    print("Fechando...")
    exit()
