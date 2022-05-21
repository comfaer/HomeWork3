import socket

HOST = "127.0.0.1"
PORT = 65432


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT))
        while True:
            command = input("Enter command:")
            if not len(command):
                print("Exit client.")
                break
            soc.sendall(str.encode(command))
            response = soc.recv(1024).decode("UTF-8")
            print(f"Answer: {response}.")


if __name__ == '__main__':
    client()
