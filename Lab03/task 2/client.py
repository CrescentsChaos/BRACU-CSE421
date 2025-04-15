import socket

port = 6565
host_ip = socket.gethostbyname(socket.gethostname())
format = 'utf-8'
buffer = 16
disconnect_message = "end"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host_ip, port))

def send_message(msg):
    message = msg.encode(format)
    message_length = str(len(message)).encode(format)
    message_length += b' ' * (buffer - len(message_length))

    client.send(message_length)  
    client.send(message)        

    response = client.recv(1024).decode(format)
    print(f"Response: {response}")

while True:
    msg = input("Enter message: ")
    send_message(msg)
    if msg.lower() == disconnect_message:
        break

client.close()
