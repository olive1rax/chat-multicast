import socket
import threading
import json
import os
import tkinter as tk
from tkinter import filedialog
from datetime import date

# Variáveis globais para manter a conexão com o servidor e a caixa de chat
socket_instance = None
caixa_chat = None
entrada_mensagem = None

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
                caixa_chat.config(state=tk.NORMAL)
                caixa_chat.insert(tk.END, msg.decode() + "\n")
                caixa_chat.config(state=tk.DISABLED)
        except Exception as e:
            print(f'Ocorreu um erro: {e}') 
            fechar_conexao()
            break

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

def enviar_mensagem():
    global socket_instance
    mensagem = entrada_mensagem.get()
    if mensagem:
        if mensagem == 'arquivo':
            enviar_arquivo()
        elif mensagem == '/trocar servidor':
            op_servidor = int(input("Escolha o novo servidor desejado: "))
            conectar_servidor(op_servidor, "Eu")
        elif mensagem == 'fechar conexao':
            fechar_conexao()
        else:
            payload = {
                "usuario": "Eu",
                "mensagem": mensagem,
                "hora": "",
                "data": ""
            }
            socket_instance.send(json.dumps(payload).encode())
            entrada_mensagem.delete(0, tk.END)
