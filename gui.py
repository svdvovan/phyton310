from tkinter import *
from tkinter import ttk
import time

root = Tk()

root.title("my first GUI")

# root.iconbitmap("D:/Global_foto/logo_parser.png")
root.geometry("400x300+450+250")


def cliced():
    print("Ты нажал!")
    root.destroy()
    window = Tk()
    window.title("second windows")
    window.geometry("400x300+450+250")
    def getTime():
        btnTimme['Text'] = time.strftime("%H:%M:%S")
    btnTimme= Button(window, text="Узнать время", command=getTime)


    btnTimme.pack()

# def getTime():
#     btnTimme['Text']= time.strftime("%H:%M:%S")

# root.resizable(0, 1)
# root.config(bg="green")
# root['bg'] = 'blue'
# x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
# y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
# root.wm_geometry("+%d+%d" % (x, y))
btn = Button(root, text="Кнопка", command=cliced, width=20, height=5, font=("Comic Sans MS", 20, "italic"))
btn.pack()

root.mainloop()
