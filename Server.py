# Name: Allison Butler
# Class: CS 372
# Project: Client/Server Chat
# Description:
# 1. The server creates a socket and binds to ‘localhost’ and port xxxx
# 2. The server then listens for a connection
# 3. When connected, the server calls recv to receive data
# 4. The server prints the data, then prompts for a reply
# 5. If the reply is /q, the server quits
# 6. Otherwise, the server sends the reply
# 7. Back to step 3
# 8. Sockets are closed (can use with in python3)
# Sources: https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client,
# https://www.biob.in/2018/04/simple-server-and-client-chat-using.html,
# https://pythontic.com/modules/socket/send,
# Computer Networking, A Top-Down Approach, James F. Kurose, Keith W. Ross,
# CS 372 modules

import socket

serverHost = 'localhost'
serverPort = 3000

# creating the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    # connects via host and port established above
    serverSocket.bind((serverHost, serverPort))
    # server is ready to listen to client request
    serverSocket.listen()
    # connection conformation:
    print(f"Server listening on HOST: {serverHost} using PORT: {serverPort}")
    # .accept() blocks execution and waits for an incoming connection
    connected, address = serverSocket.accept()
    print(f"{str(address)} connection confirmed")
    print("Type '/q' to quit")
    with connected:
        while True:
            # using fixed length for messages :(
            messageToDecode = connected.recv(1024)
            if not messageToDecode:
                break
            print(f"Client: {messageToDecode.decode()}")
            # server can now reply to client:
            reply = input("Server: ")
            if reply == "/q":
                break
            connected.sendall(reply.encode('utf-8'))
        # indicates the connection is closed
        print("Server has left the chat... \n")


