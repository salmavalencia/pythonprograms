import socket


def send_text(sending_socket, text):
    text = text + "\n"
    data = text.encode()
    sending_socket.send(data)


def get_text(receiving_socket):
    buffer = ""

    socket_open = True
    while socket_open:

        data = receiving_socket.recv(1024)

        if not data:
            socket_open = False

        buffer = buffer + data.decode()

        terminator_pos = buffer.find("\n")

        while terminator_pos > -1:
            message = buffer[:terminator_pos]

            buffer = buffer[terminator_pos + 1:]

            yield message
            terminator_pos = buffer.find("\n")


def display():
    print("SIMPLE CHAT APP\n\n")

    print("Select an option\n\n")

    print("\t1. Be a server.")
    print("\t2. Be a client.")
    print("\t3. Exit\n")

    print("Option: ")


def chat(op2):
    if op2 == 1:
        chosen_socket = server()

    if op2 == 2:
        chosen_socket = client()

    while True:
        print("\t1. Send message")
        print("\t2. Wait for message")
        print("\t3. Quit")

        print("Option: ")

        op1 = int(input())

        if op1 == 1:

            print("Message: ")
            text = input()
            send_text(chosen_socket, text)

        elif op1 == 2:
            print("Waiting for message...")
            message = next(get_text(chosen_socket))
            print(message)

            print("\nLeave reply?(yes or no)")
            b = input()

            if b == "yes":
                print("Message: ")
                text = input()
                send_text(chosen_socket, text)

            elif b == "no":
                print("")
            else:
                print("Invalid input")

        elif op1 == 3:

            break

        else:
            print("Invalid input")


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8082))
    server_socket.listen()
    print("Waiting for connection")
    connection_socket, address = server_socket.accept()
    print("Client connected")
    return connection_socket


def client():
    print("Type the address you wish to connect")
    ipserver = input()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ipserver, 8082))
    print("Connected")
    return client_socket


def option(a):
    if a == 1:
        chat(1)
    elif a == 2:
        chat(2)
    elif a == 3:
        exit(0)
    else:
        print("Invalid input")


display()
op = int(input())
option(op)
