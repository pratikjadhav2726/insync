import socket

HEADER_LENGTH = 8
HOST = socket.gethostbyname("wss://localhost:5001/ws")
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    print(HOST)
    client_socket.connect((HOST, PORT))

    sending_message = "Hey server!"

    #client_message = f"{len(sending_message):<{HEADER_LENGTH}}{sending_message}"
    #print(client_message)
    #client_socket.send("hello")


    client_socket.send(bytes(sending_message, "utf-8"))

    message_length = 1024
    message = client_socket.recv(message_length).decode("utf-8")
    #message = client_socket.recv(1024)
    print("Hi")
    print(message)