from http import server
import socket as s

HOST = "192.168.43.113"
PORT = 33000
BUFFER = 1024

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen(2)

while True:
    client_socket, adress = server_socket.accept()
    print(f"Uzyskano połączenie od {adress[0]}")
    
    name = client_socket.recv(BUFFER).decode("utf8")
    numer = client_socket.recv(BUFFER).decode("utf8")
    print(f"{adress[0]}>{name}{numer}")