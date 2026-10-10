import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 22357))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Connection established from address {address}")
    clientSocket.send(bytes("Welcome to the server!!!", "utf-8"))
    clientSocket.close()