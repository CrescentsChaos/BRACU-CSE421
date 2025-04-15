import socket
import threading

port = 6565
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
format = 'utf-8'
buffer = 16
disconnect_message = "end"

server_socket_addr = (host_ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)
server.listen()

print(f"Server is listening on {host_ip}:{port}")

def handle_client(connection, address):
    print(f"Server is connected to {address}")

    connected = True
    while connected:
        message_length = connection.recv(buffer).decode(format)
        if not message_length:
            break

        message_length = int(message_length.strip())
        message = connection.recv(message_length).decode(format)

        print(f"Received from {address}: {message}")

        if message.lower() == disconnect_message:
            connection.send("Disconnected!".encode(format))
            print(f"Server is disconnected from {address}")
            connected = False
        else:
            count = 0
            for i in message:
                i = i.lower()
                if i =="a" or i =="e" or i =="i" or i =="o" or i =="u":
                    count += 1

            if count == 0:
                response = "Not enough vowels"
            elif count <= 2:
                response = "Enough vowels I guess"
            else:
                response = "Too many vowels"

            connection.send(response.encode(format))

    connection.close()

while True:
    connection, address = server.accept()
    thread = threading.Thread(target=handle_client, args=(connection, address))
    thread.start()
