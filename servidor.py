import socket
import threading
import json

connections = []  # Variável para salvar as conexões dos clientes.
servidor_ativo = True  # Variável para controlar o estado do servidor.

def lidar_usuario(connection: socket.socket, address: str) -> None:
    global servidor_ativo
    while servidor_ativo:
        try:
            msg = connection.recv(1024)
            if msg:
                msg_dumped = json.loads(msg)
                usuario = msg_dumped.get("usuario", "Usuário Desconhecido")
                mensagem = msg_dumped.get("mensagem", "Mensagem Não Encontrada")
                if msg_dumped.get("log") == "join":
                    print(f'{usuario} {mensagem}')
                else:
                    print(f'{usuario}: {mensagem}')
                if mensagem == "fechar servidor":
                    print("Fechando servidor...")
                    fechar_servidor()
                    break

                transmitir(f'{usuario}: {mensagem}', connection)
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
    connections.clear()

SERVIDORES = [
    {"nome": "Alto Tietê",  "porta": 8001},
    {"nome": "Médio Tietê",  "porta": 8002},
    {"nome": "Tietê Interiorano",  "porta": 8003},
    {"nome": "Baixo Tietê",  "porta": 8004}
]

print("Servidores disponíveis:")
for i, servidor in enumerate(SERVIDORES):
    print(f"{i+1} - {servidor['nome']}")

op_servidor = int(input("Escolha o servidor desejado: "))
if 1 <= op_servidor <= len(SERVIDORES):
    servidor_escolhido = SERVIDORES[op_servidor - 1]
    LISTENING_PORT = servidor_escolhido["porta"]

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
else:
    print("Escolha inválida. Saindo...")
1