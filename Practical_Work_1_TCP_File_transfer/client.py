import socket
import os

def send_file():
    server_ip = '127.0.0.1'
    server_port = 21003
    filename = 'send.txt'

    try:
        with open(filename, 'rb') as file:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, server_port))
            
            file_name = os.path.basename(filename)
            file_size = os.path.getsize(filename)
            client_socket.send(f"{file_name},{file_size}".encode())

            ack = client_socket.recv(1024)
            print(f"Server acknowledgment: {ack.decode()}")

            while chunk := file.read(1024):
                client_socket.send(chunk)
                ack = client_socket.recv(1024)  
                print(f"Acknowledgment received: {ack.decode()}")

            print(f"File '{filename}' has been sent successfully")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    send_file()
