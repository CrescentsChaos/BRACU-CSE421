import socket

port = 6565
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
format = 'utf-8'

server_socket_addr = (host_ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)
server.listen()

print(f"Server is ready and listening on {host_ip}:{port}")

while True:
    connection, address = server.accept()
    print(f"Server is connected to {address} established.")

    data = connection.recv(1024).decode(format)
    if data:
        print(f"Received: {data}")

    connection.close()
