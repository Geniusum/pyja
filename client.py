import socket

HOST, PORT = "10.1.10.63", 12345
end_byte = 0
end_byte = end_byte.to_bytes()

text_to_send = b"Hello, World!" + end_byte

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(text_to_send)
    response = client.recv(1024)
    print("Server response:", response.decode())