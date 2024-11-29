import socket

def send_file():

    server_ip = '127.0.0.1'
    server_port = 21003

    filename = 'send.txt'
    with open(filename, 'rb') as file:

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))


        file_data = file.read()
        client_socket.sendall(file_data)

        print(f"File '{filename}' has been sent")

        client_socket.close()

if __name__ == "__main__":
    send_file()
