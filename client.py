import socket

server_ip = "127.0.0.1"
port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

client.send("get_metrics".encode("utf-8"))
response = client.recv(1024).decode("utf-8")
print(f"Metrics: {response}")

client.send("close".encode("utf-8"))
client.close()
