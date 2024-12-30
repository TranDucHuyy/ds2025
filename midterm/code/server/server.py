from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the RPC methods
def upload_file(file_name, file_data):
    try:
        print(f"Receiving file: {file_name}")
        with open(file_name, 'wb') as file:
            file.write(file_data.encode('latin1'))  # Convert data back to bytes
        print(f"File {file_name} received successfully.")
        return {"status": "success", "message": f"File {file_name} uploaded successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Map method names to functions
methods = {
    "upload_file": upload_file,
}

@app.route("/rpc", methods=["POST"])
def rpc():
    try:
        # Parse JSON request
        rpc_request = request.get_json()

        # Extract method and arguments
        method_name = rpc_request.get("method")
        args = rpc_request.get("args", {})

        # Invoke the requested method
        if method_name in methods:
            result = methods[method_name](**args)
        else:
            result = {"status": "error", "message": "Unknown method."}

        return jsonify(result)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # Get user input for port
    try:
        port = int(input("Enter the port to start the server on (e.g., 5000): "))
        app.run(host="0.0.0.0", port=port)
    except ValueError:
        print("Invalid port. Please enter a valid number.")
