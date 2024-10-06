import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
server = "dra-server.mywire.org"
port = 55_555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("connecting")

client.connect((server, port))
print(f"connected successfully to {server}")


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1048).decode()
            if message == 'NICK':
                client.send(nickname.encode())
            else:
                print(message)
        except socket.error:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break


# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(" "))
        client.send(message.encode())


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

