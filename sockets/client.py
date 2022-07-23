import socket as s

HOST = "192.168.43.113"
PORT = 33000
BUFFER = 1024

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

client_socket.connect((HOST, PORT))

name = input("Twoja nazwa:").encode("utf8")
client_socket.send(name)