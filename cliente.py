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

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    caminho_arquivo = filedialog.askopenfilename()
    root.destroy()  # Fecha a janela depois de selecionar o arquivo
    return caminho_arquivo

def enviar_arquivo():
    global socket_instance
    caminho_arquivo = selecionar_arquivo()

    if caminho_arquivo:
        with open(caminho_arquivo, "rb") as file:
            arquivo_bytes = file.read()
            payload = {
                "comando": "/arquivo",
                "nome_arquivo": os.path.basename(caminho_arquivo),
                "conteudo_arquivo": arquivo_bytes
            }
            socket_instance.send(json.dumps(payload).encode())
    else:
        print("Nenhum arquivo selecionado.")

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

def criar_interface_grafica():
    global caixa_chat, entrada_mensagem
    root = tk.Tk()
    root.title("Chat")

    # Caixa de chat
    caixa_chat = tk.Text(root, height=20, width=50)
    caixa_chat.config(state=tk.DISABLED)
    caixa_chat.pack(padx=10, pady=10)

    # Entrada de mensagem
    entrada_mensagem = tk.Entry(root, width=50)
    entrada_mensagem.pack(padx=10, pady=(0, 10))

    # Botão de enviar
    botao_enviar = tk.Button(root, text="Enviar", command=enviar_mensagem)
    botao_enviar.pack(padx=10, pady=(0, 10))

    root.mainloop()

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

    criar_interface_grafica()

elif op == 0:
    print("Fechando...")
    exit()
