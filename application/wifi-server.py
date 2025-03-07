import time
import socket
import network
SSID = ""  # Substitua pelo nome da sua rede Wi-Fi
PASSWORD = ""  # Substitua pela senha do Wi-Fi


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

# Aguarda a conexão
while not wifi.isconnected():
    print("Conectando ao Wi-Fi...")
    time.sleep(1)

print("Conectado! IP:", wifi.ifconfig()[0])

# Cria o socket do servidor web
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))  # Porta 80 para HTTP
server.listen(5)

print("Servidor rodando...")

while True:
    conn, addr = server.accept()  # Aguarda conexão
    print("Cliente conectado:", addr)

    request = conn.recv(1024)  # Recebe requisição HTTP
    print("Requisição recebida:", request)

    response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nIt's work!"
    conn.send(response)  # Envia resposta
    conn.close()  # Fecha conexão
