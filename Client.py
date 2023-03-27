# Name: Allison Butler
# Class: CS 372
# Project: Client/Server Chat
# Description:
# 1. The client creates a socket and connects to ‘localhost’ and port xxxx
# 2. When connected, the client prompts for a message to send
# 3. If the message is /q, the client quits
# 4. Otherwise, the client sends the message
# 5. The client calls recv to receive data
# 6. The client prints the data
# 7. Back to step 2
# 8. Sockets are closed (can use with in python3)
# Sources: https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client,
# https://www.biob.in/2018/04/simple-server-and-client-chat-using.html,
# https://pythontic.com/modules/socket/send,
# Computer Networking, A Top-Down Approach, James F. Kurose, Keith W. Ross,
# CS 372 modules

import socket

clientHost = 'localhost'
clientPort = 3000

# creating the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    # socket connects via host and port established above
    clientSocket.connect((clientHost, clientPort))
    while True:
        # client side can now respond with input
        message = input("Client: ")
        if message == "/q":
            break
        clientSocket.sendall(message.encode('utf-8'))
        # using fixed length for messages :(
        messageToDecode = clientSocket.recv(1024)
        print(f"Server: {messageToDecode.decode()}")
# indicates the connection is closed
print("Client has left the chat... \n")

