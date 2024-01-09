import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("localhost", 8080))
    server.listen()

    client, addr = server.accept()
    filename = client.recv(1024).decode()

    with open(filename, "wb") as file:
        file_bytes = b""
        done = False

        while not done:
            data = client.recv(1024)
            file_bytes += data
            print(data)

            if data[-5:] == b"<END>":
                done = True

        file.write(file_bytes[:-5])  # Exclude the "<END>" marker