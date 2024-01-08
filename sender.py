import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("localhost", 8080))
    filename = "image.jpg"

    client.sendall("file.jpg".encode())

    with open(filename, "rb") as file:
        data = file.read()
        client.sendall(data)
        client.send(b"<END>")
