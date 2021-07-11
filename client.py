import socket

HEADER_LENGTH = 8
HOST = "https://insyncpy.herokuapp.com" #"127.0.0.1" "wss://echo.websocket.org" 
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    sending_message = "Hey server!"

    #client_message = f"{len(sending_message):<{HEADER_LENGTH}}{sending_message}"
    #print(client_message)
    #client_socket.send("hello")


    client_socket.send(bytes(sending_message, "utf-8"))

    message_length = 1024
    message = client_socket.recv(message_length).decode("utf-8")
    #message = client_socket.recv(1024)

    print(f"{message}")