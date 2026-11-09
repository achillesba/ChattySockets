import socket
import threading


def send_messages():
    while True:
        str_message = input("Enter a message to send to client: ")

        if str_message.lower() == "exit":
            print("Exiting the message sender.")
            clientSocket.shutdown(socket.SHUT_WR)
            break
        try:
            byte_message = str_message.encode("utf-8")
            clientSocket.sendall(byte_message + b"\n")
            print("\n")
        except ConnectionResetError:
            print("Client has disconnected. Type 'exit' to close the server.")
            break


def receive_messages():
    while True:
        try:
            byte_message = clientSocket.recv(1024)

            if byte_message == b"":
                print("Client has disconnected. Type 'exit' to close the server.")
                clientSocket.close()
                break

            str_message = byte_message.decode("utf-8")
            print(f"Received message from client: {str_message}")
        except ConnectionResetError:
            print("Client has disconnected. Type 'exit' to close the server.")
            clientSocket.close()
            break



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 22357))
s.listen(5)
clientSocket, address = s.accept()
print(f"Connection established to address {address}")

thread1 = threading.Thread(target=receive_messages, daemon=True)
thread1.start()
send_messages()
clientSocket.close()
s.close()