import socket

# Server settings
HOST = '127.0.0.1'  # Localhost - only accepts connections from this machine
PORT = 65432        # Port number to listen on (must match client)

def start_server():
    # Create a TCP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        
        # Allows reuse of the port immediately after server closes
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind socket to the host and port
        server_socket.bind((HOST, PORT))
        
        # Start listening for incoming connections
        server_socket.listen()
        print(f"[SERVER] Listening on {HOST}:{PORT}...")
        print("[SERVER] Waiting for a client to connect...")

        try:
            # Accept a connection (this pauses here until a client connects)
            conn, addr = server_socket.accept()
            with conn:
                print(f"[SERVER] Connected by {addr}")
                
                while True:
                    # Receive data from client (up to 1024 bytes)
                    data = conn.recv(1024)
                    
                    # If no data received, client disconnected
                    if not data:
                        print("[SERVER] Client disconnected.")
                        break
                    
                    # Decode bytes to string and display
                    message = data.decode('utf-8')
                    print(f"[SERVER] Received: {message}")
                    
                    # Send a response back to the client
                    response = f"Server received: {message}"
                    conn.sendall(response.encode('utf-8'))
                    
        except KeyboardInterrupt:
            print("\n[SERVER] Shutting down gracefully.")

# Run the server
if __name__ == "__main__":
    start_server()
