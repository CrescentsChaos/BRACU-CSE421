import socket

port = 6565
host_ip = socket.gethostbyname(socket.gethostname())
format = 'utf-8'
buffer = 16
disconnect_message = "end"

server_socket_addr = (host_ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)
server.listen()

print(f"Server is listening on {host_ip}:{port}")

while True:
    connection, address = server.accept()
    print(f"Server is connected to {address}")

    message_length = connection.recv(buffer).decode(format)
    if not message_length:
        connection.close()
        continue

    message_length = int(message_length.strip())
    message = connection.recv(message_length).decode(format)

    print(f"Received hours: {message}")

    hours = int(message)
    if hours <= 40:
        salary = hours * 200
    else:
        salary = 8000 + (hours - 40) * 300
    response = f"Calculated Salary: Tk {salary}"

    connection.send(response.encode(format))
    connection.close()
