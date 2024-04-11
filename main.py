import socket
import threading
import json
import time
from datetime import date


def receber_mensagem(connection: socket.socket):
    while True:
        try:
            msg = connection.recv(1024)
            if msg:
                print(msg.decode())
            else:
                connection.closes
