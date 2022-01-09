from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title(f"my first GUI ")

# root.iconbitmap("D:/Global_foto/logo_parser.png")
root.geometry("400x400+450+250")

clic = 0


def counter():
    global clic
    clic += 1
    root.title(f"my first GUI {clic}")


def kill():
    root.destroy()


btn = Button(root, text="Кнопка", command=counter, width=20, height=5, font=("Comic Sans MS", 20, "italic"))
btn2 = Button(root, text="Закрыть", command=kill, width=20, height=2, font=("Comic Sans MS", 20, "italic"))
l = Label(root, text="виджет")
l.pack()
btn.pack()
btn2.pack()

root.mainloop()
