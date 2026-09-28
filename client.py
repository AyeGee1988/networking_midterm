import socket

# Client settings - must match the server
HOST = '127.0.0.1'  # Server's IP address (localhost)
PORT = 65432        # Server's port number

def start_client():
    try:
        # Create a TCP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            
            # Connect to the server
            client_socket.connect((HOST, PORT))
            print(f"[CLIENT] Successfully connected to {HOST}:{PORT}")

            # List of test messages to send
            messages = [
                "Hello, server!",
                "How are you?",
                "This is a test message.",
                "Goodbye!"
            ]

            # Send each message and wait for a response
            for msg in messages:
                # Encode string to bytes and send
                client_socket.sendall(msg.encode('utf-8'))
                print(f"[CLIENT] Sent: {msg}")

                # Wait for server's response
                response = client_socket.recv(1024).decode('utf-8')
                print(f"[CLIENT] Received: {response}")

        # Connection closed cleanly when 'with' block exits
        print("\n[CLIENT] Connection closed.")

    except ConnectionRefusedError:
        # This runs if the server is not running
        print("[CLIENT] ERROR: Connection refused - is the server running?")

# Run the client
if __name__ == "__main__":
    start_client()
