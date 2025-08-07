# Network Sockets - Client

import socket
import time


HOST_IP = '127.0.0.1'
HOST_PORT = 13000


print(f'Waiting for connexion on {HOST_IP}, port: {HOST_PORT}...' )
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except:
        print('Connection failed. Trying again...')
        time.sleep(4)
    else:
        print('Etabslished connection with', (HOST_IP, HOST_PORT))
        break


while True:
    received_datas = s.recv(1024)
    if not received_datas:
        break
    print('Server: ', received_datas.decode())
    sent_text = input('You: ')
    s.sendall(sent_text.encode())
    

s.close()