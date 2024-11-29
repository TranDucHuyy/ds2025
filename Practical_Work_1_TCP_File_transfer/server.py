import socket

def receive_file():
    server_ip = '127.0.0.1'
    server_port = 21003

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, server_port))
        server_socket.listen(1)

        print(f"Server is waiting for connection at {server_ip}:{server_port}...")

        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        file_info = client_socket.recv(1024).decode()
        filename, file_size = file_info.split(',')
        file_size = int(file_size)

        print(f"Receiving file: {filename} (Size: {file_size} bytes)")

        client_socket.send("Ready to receive file".encode())

        with open(f'received_{filename}', 'wb') as file:
            bytes_received = 0
            while bytes_received < file_size:
                data = client_socket.recv(1024)
                file.write(data)
                bytes_received += len(data)

                client_socket.send("ACK".encode())

        print(f"File '{filename}' received successfully and saved.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    receive_file()
