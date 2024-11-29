import socket

def receive_file():

    server_ip = '127.0.0.1'
    server_port = 21003

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Server is waiting for connection at {server_ip}:{server_port}...")

    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    with open('received.txt', 'wb') as file:
        print("Receiving file...")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print("File received and saved as'received.txt'.")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    receive_file()
