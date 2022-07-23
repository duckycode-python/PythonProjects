import socket as s
import subprocess
import os
HOST = "192.168.43.113"
PORT = 33000
BUFFER = 1024

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(2)
print(server_socket)

while True:
    client_socket, adress = server_socket.accept()
    print(f"Connected with {adress}")
    command = client_socket.recv(BUFFER).decode("utf8")
    