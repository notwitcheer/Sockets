# Network Sockets - Server

import socket

HOST_IP = '127.0.0.1'
HOST_PORT = 13000


s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f'Waiting for connexion on {HOST_IP}, port: {HOST_PORT}...' )
socket_connexion, client_adress = s.accept()
print('Etabslished connection with', client_adress)

while True:
    sent_text = input('You: ')
    socket_connexion.sendall(sent_text.encode())
    received_datas =  socket_connexion.recv(1024)
    if not received_datas:
        break
    print('Server: ', received_datas.decode())


s.close()
socket_connexion.close()