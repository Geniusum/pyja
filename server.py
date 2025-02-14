import socket
import threading

HOST, PORT = "0.0.0.0", 12345
buffer_bytes = 8

def handle_client(conn, addr):
    print(f"Connexion from {addr}")
    with conn:
        while True:
            buffer_size:bytes = conn.recv(buffer_bytes)
            if not buffer_size: break
            buffer_size = int.from_bytes(buffer_size)
            print("Buffer size :", buffer_size)
            buffer = conn.recv(buffer_size)
            response = bytes(f"OK ({buffer_size}) : {buffer}", "utf-8")
            conn.sendall(response)
    print(f"Client {addr} disconnected")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Serveur listening on {PORT}...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        thread.start()
