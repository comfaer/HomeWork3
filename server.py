import random
import socket

HOST = "127.0.0.1"
PORT = 65432

correct_answer = random.randint(0, 10)


def process_command(command: str) -> str:
    splitted_command = command.split(" ")
    if splitted_command[0] == "exit":
        exit("Server stopped.")
    if splitted_command[0] != "guess" or len(splitted_command) < 2:
        return "Wrong command"
    number = int(splitted_command[1])
    if number < correct_answer:
        return "Less"
    elif number > correct_answer:
        return "More"
    elif number == correct_answer:
        return "Correct"


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.bind((HOST, PORT))
        soc.listen()
        while True:
            (connection, address) = soc.accept()
            with connection:
                print(f"Connected: {address}.")
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    else:
                        answer = process_command(data.decode("UTF-8"))
                        connection.sendall(str.encode(answer))


if __name__ == "__main__":
    server()
