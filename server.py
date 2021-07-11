import socket

HEADER_LENGTH = 8

HOST = "127.0.0.1"
PORT = 8888
listening = True


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    
    server_socket.bind((socket.gethostname(), PORT))
    #print(socket.getaddrinfo())
    server_socket.listen(5)
    client_socket, client_addr = server_socket.accept()

    while listening:
        print(f"{client_addr} connected")
        message_length = int(client_socket.recv(HEADER_LENGTH).decode("utf-8"))
        message = client_socket.recv(message_length).decode("utf-8")
        print(f"{client_addr}: {message}")

        sending_message = "hello client"
        server_message = f"{len(sending_message):<{HEADER_LENGTH}}{sending_message}"
        #print(server_message)

        client_socket.send(bytes(server_message, "utf-8"))
        #listening = False
