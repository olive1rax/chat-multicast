import socket
import threading
import json
import os

# Variáveis globais para manter a conexão com o servidor e a caixa de chat
socket_instance = None
caixa_chat = None
entrada_mensagem = None
usuario = None

SERVIDORES = [
    {"nome": "Alto Tietê", "ip": "127.0.0.1", "porta": 8001},
    {"nome": "Médio Tietê", "ip": "127.0.0.1", "porta": 8002},
    {"nome": "Tietê Interiorano", "ip": "127.0.0.1", "porta": 8003},
    {"nome": "Baixo Tietê", "ip": "127.0.0.1", "porta": 8004}
]

def fechar_conexao():
    global socket_instance
    if socket_instance:
        try:
            socket_instance.close()
        except Exception as e:
            print(f'Erro ao fechar a conexão: {e}')

def receber_mensagem(connection: socket.socket):
    global caixa_chat
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                caixa_chat.config(state="normal")
                caixa_chat.insert(tk.END, msg.decode() + "\n")
                caixa_chat.config(state="disabled")
        except Exception as e:
            print(f'Ocorreu um erro: {e}') 
            fechar_conexao()
            break

socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conectar_servidor(op_servidor, usuario, txtChat):
    global socket_instance
    try:
        endereco = ('localhost', 8000 + op_servidor)  # Altere aqui se necessário
        socket_instance.connect(endereco)
        socket_instance.send(usuario.encode())
        # Iniciar thread para lidar com recebimento de mensagens
        receber_mensagens_thread = threading.Thread(target=lidar_mensagens, args=(socket_instance, txtChat))
        receber_mensagens_thread.start()
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")

def lidar_mensagens(connection, txtChat):
    while True:
        try:
            msg = connection.recv(1024).decode()
            if msg:
                txtChat.insert(tk.END, msg + "\n")  # Adiciona a mensagem ao txtChat
            else:
                break
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            break

def enviar_mensagem(mensagem):
    global socket_instance, usuario
    if mensagem:
        payload = {
            "usuario": usuario,
            "mensagem": mensagem,
            "hora": "",
            "data": ""
        }
        socket_instance.send(json.dumps(payload).encode())