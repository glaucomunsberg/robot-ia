
import socket

from communication.network import Wifi
from brain.neocortex.parietal.cognition.command_decoder import CommandDecoder


class Reader:

    _instance = None
    wifi = None
    server = None
    conn = None
    command_decoder = CommandDecoder()

    is_running = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.wifi = Wifi()

        return cls._instance

    def __init__(self):
        if self.server is None:
            try:
                self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # check if bind is necessary
                self.server.bind(('', 80))  # Porta 80 para HTTP
                self.server.settimeout(5)
                self.server.listen(5)
                print("Servidor inicializado")
            except OSError as e:
                print(f' >> INIT ERROR: {e}')
                self.close_socket()

    def set_running(self, is_running: bool):
        """Set the running status of the server"""
        print(f"Setting running status to {is_running}")
        self.is_running = is_running
        if self.is_running is False and self.conn is not None:
            self.conn.close()

    def read(self):
        """Read the data from the client"""

        # create a while loop to keep the server running with 1 second of sleep
        if self.server is None:
            print("Servidor não inicializado!")
            return

        time = 0
        self.conn = None
        while self.is_running:
            time += 1
            print(f"Listening... ")

            try:
                self.conn, addr = self.server.accept()
                print("Cliente conectado:", addr)
                request = self.conn.recv(1024)
                print("Request:", request)
                # print request body
                print(f"Request body: {request.decode('utf-8')}")
                # split in first { and join all the rest
                self.command_decoder.decode_from_text(
                    "{".join(request.decode('utf-8').split("{")[1:]))
                # Envia resposta HTTP
                self.conn.send(
                    "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nIt's work!")
            except OSError as e:
                print(f' >> ERROR: {e}')
                self.is_running = False
            finally:
                # appearantly, context managers are currently not supported in MicroPython, therefore the connection is closed manually
                if self.conn is not None:
                    self.conn.close()
                print('Listening closed.')

    def close_socket(self):
        self.is_running = False
        self.server.close()
        print(' >> Socket closed.')

    def reset_socket(self):
        self.close_socket()
        self.server = None
        self.conn = None
        self.is_running = False
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # check if bind is necessary
        self.server.bind(('', 80))  # Porta 80 para HTTP
        self.server.settimeout(5)
        self.server.listen(5)
        print("Servidor reset_socket")
