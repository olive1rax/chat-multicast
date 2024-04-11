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


def usuario(connection: socket.socket):
    while True:
        try:
            msg = connection.recv(1024)
            msg_dumped = json.loads(msg)
            


