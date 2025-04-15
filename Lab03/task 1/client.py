import socket

port = 6565
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)
server_address = (host_ip, port)
format = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

info_message = f"IP of client: {host_ip}, Device Name: {hostname}"
client.send(info_message.encode(format))

client.close()
