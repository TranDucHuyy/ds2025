from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import requests

class ProxyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Construct the backend server URL
        try:
            backend_url = f"http://{backend_ip}:{backend_port}{self.path}"  # Dynamic backend IP and port

            # Read the POST data from the client
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            # Forward the request to the backend server
            headers = {key: self.headers[key] for key in self.headers.keys()}
            response = requests.post(backend_url, data=post_data, headers=headers)

            # Send the response back to the client
            self.send_response(response.status_code)
            for key, value in response.headers.items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(response.content)
        except Exception as e:
            # Handle errors gracefully
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Proxy error: {e}".encode())

def get_local_ip():
    """
    Gets the machine's actual IP address on the local network (e.g., 192.168.x.x).
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Connect to an arbitrary public IP (Google DNS) to determine the local interface IP
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return "127.0.0.1"

def run_proxy(proxy_port):
    proxy_ip = get_local_ip()
    print(f"Proxy is running on {proxy_ip}:{proxy_port}")
    print("Clients should connect to this address.")

    server_address = (proxy_ip, proxy_port)
    httpd = HTTPServer(server_address, ProxyHandler)
    print(f"Proxy is forwarding requests to {backend_ip}:{backend_port}")
    httpd.serve_forever()

if __name__ == "__main__":
    proxy_port = int(input("Enter the proxy port (e.g., 8080): "))
    backend_ip = input("Enter the backend server IP address (e.g., 192.168.1.100): ")
    backend_port = int(input("Enter the backend server port (e.g., 5000): "))
    run_proxy(proxy_port)

