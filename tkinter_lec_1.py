from tkinter import *

def handler1(event):
    print('Hello World!')

def handler2(event):
    exit()


# инициализация

root = Tk()
hello_label = Label(root, text="Hello, World!", font='Times 16')
hello_label.pack()


# Главный цикл (проект)
root.mainloop()

