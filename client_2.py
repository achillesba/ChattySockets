import socket
import threading


def send_messages():
    while True:
        str_message = input("Enter a message to send to server: ")

        if str_message.lower() == "exit":
            print("Exiting the message sender.")
            s.shutdown(socket.SHUT_WR)
            break
        try:
            byte_message = str_message.encode("utf-8")
            s.sendall(byte_message + b"\n")
            print("\n")
        except ConnectionResetError:
            print("Server has disconnected. Type 'exit' to close the server.")
            break


def receive_messages():
    while True:
        try:
            byte_message = s.recv(1024)

            if byte_message == b"":
                print("Server has disconnected. Type 'exit' to close the client.")
                s.close()
                break

            str_message = byte_message.decode("utf-8")
            print(f"Received message from server: {str_message}")
        except ConnectionResetError:
            print("Server has disconnected. Type 'exit' to close the client.")
            s.close()
            break



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 22357))

thread1 = threading.Thread(target=receive_messages, daemon=True)
thread1.start()
send_messages()