import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 22357))

message = s.recv(2048) #2048 bytes

print(f"Message recieved: {message.decode()}")