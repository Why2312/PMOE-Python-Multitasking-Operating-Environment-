import socket
import threading
import sys
import time

# Define server settings
HOST = '5.12.112.50'
PORT = 2000
BUFFER_SIZE = 4096
print("VERSION 1.0.0")

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Define a function to handle incoming messages from the server
def receive_messages():
    while True:
        try:
            # Receive incoming data from the server
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break

            # Print the incoming message
            message = data.decode()
            sys.stdout.write(message + "\n")
            sys.stdout.flush()
            client_socket.close()
        except:
            break


# Start a new thread to receive incoming messages from the server
threading.Thread(target=receive_messages).start()

# Send the client's username and the name of the chat room they want to join to the server
time.sleep(1)
username = input('Please enter your username: ')
chat_room_name = input('Please enter the name of the chat room you want to join: ')
client_socket.sendall(chat_room_name.encode())

# Start a loop to send messages to the server
while True:
    try:
        # Read the user's input from the command line
        message = input(f'{username}> ')
        

        # Send the message to the server
        client_socket.sendall(f'{username}>{message}\n'.encode())
    except:
        break

client_socket.close()
