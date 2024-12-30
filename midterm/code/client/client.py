import requests
import os

def send_request(server_url, method_name, args):
    try:
        # Prepare the RPC request
        rpc_request = {
            "method": method_name,
            "args": args
        }

        # Send the HTTP POST request
        response = requests.post(server_url, json=rpc_request)

        # Process the server's response
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Error: Server returned status code {response.status_code}")
            print(response.json())
    except Exception as e:
        print(f"Client error: {e}")

if __name__ == "__main__":
    # Simplified input for the server address and port
    server_address = input("Enter the server address (e.g., localhost): ")
    server_port = input("Enter the server port (e.g., 5000): ")

    # Automatically construct the server URL
    server_url = f"http://{server_address}:{server_port}/rpc"

    while True:
        file_name = input("Enter the name of the file to send (or type 'exit' to quit): ")
        if file_name.lower() == 'exit':
            print("Exiting the program.")
            break
        try:
            # Read file data
            file_path = os.path.join(os.getcwd(), file_name)
            with open(file_path, 'rb') as file:
                file_data = file.read().decode('latin1')  # Encode to a safe string format

            # Send RPC request
            send_request(server_url, "upload_file", {"file_name": file_name, "file_data": file_data})
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found. Please try again.")
