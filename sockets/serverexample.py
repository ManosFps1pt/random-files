import socket
import threading

# Connection Data
host = "192.168.1.100"
port = 55_555


# special messages
disc_message = "$DISCONNECT$"
nick_message = "$NICK$"

# Starting Server
print("Starting server")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Handling Messages From Clients
def handle(client, addr):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            if message == disc_message:
                client.close()
            print(f"msg from {addr}")
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode())
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        print("waiting for (other) connections")
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode())
        client.send('Connected to server!'.encode())

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client, address))
        thread.start()


if __name__ == '__main__':
    receive()
