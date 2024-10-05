import socket
import threading

# Connection Data
host = "127.0.0.1"
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []

client, addr = server.accept()

print(f"Connected with {str(addr)}")

client.send("hi".encode())

