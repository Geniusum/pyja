import socket
import threading

HOST, PORT = "0.0.0.0", 12345

def handle_client(conn, addr):
    print(f"Connexion from {addr}")
    with conn:
        data = b""
        end_byte = 0
        end_byte = end_byte.to_bytes()
        while True:
            byte = conn.recv(1)
            if byte == end_byte: break
            data += byte
        response = b"OK: " + data
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
