SETUP INSTRUCTIONS FOR HTTP OVER RPC PROJECT
============================================

This document provides the steps and script to set up the HTTP over RPC project on another machine.

1. PREREQUISITES
----------------
Ensure the following are installed on the target machine:
- Python 3.x
- pip (Python package manager)
- git (for cloning the repository)

2. INSTALLATION STEPS
----------------------
Follow these steps to set up and run the project:

A. Clone the project repository: git clone <https://github.com/TranDucHuyy/ds2025.git> cd <PROJECT_FOLDER>
B. Install required Python dependencies: pip install -r setup/requirements.txt


3. CONFIGURE AND START SERVERS
------------------------------
A. Start the Flask Backend Server:
- Navigate to the `server/` folder.
= Run the following command:
   ```
   python3 server.py
   ```

B. Start the Proxy Server:
- Navigate to the `proxy/` folder.
- Run the following command:
   ```
   python3 proxy.py
   ```

4. TESTING THE SYSTEM
---------------------
A. Client:
- Navigate to the `client/` folder.
- Run the following command to start the client:
  ```
  python3 client.py
  ```
- Follow the on-screen prompts to send requests.

B. Independent Testing (Optional):
- Use Postman or other HTTP tools to send POST requests to:
  - Proxy: `http://<PROXY_IP>:<PROXY_PORT>/rpc`
  - Server: `http://<SERVER_IP>:<SERVER_PORT>/rpc`

5. TROUBLESHOOTING
------------------
- **Missing Dependencies:** Ensure `requirements.txt` is installed correctly.
- **Port Conflicts:** Verify that the specified ports are not in use by other applications.
- **Network Issues:** Ensure the target machine can communicate with the specified IP addresses and ports.

6. NOTES
--------
- Ensure all configuration files (if any) are updated with the correct IP addresses and ports before starting the servers.
- Logs are generated for each component to monitor the request flow.


