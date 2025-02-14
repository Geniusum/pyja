import socket

HOST, PORT = "127.0.0.1", 12345
buffer_bytes = 8

text_to_send = "Hello, World!"
buffer_size = len(text_to_send)

def send_buffer_size(client, buffer_size:int, bytes:int):
    client.sendall(buffer_size.to_bytes(bytes))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    send_buffer_size(client, buffer_size, buffer_bytes)
    client.sendall(bytes(text_to_send, "utf-8"))
    response = client.recv(1024)
    print("Server response:", response.decode())