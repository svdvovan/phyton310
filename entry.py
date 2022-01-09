from tkinter import *

window = Tk()
window.geometry('600x400+1000+300')
window.title("entry")

def add_str():
    e.insert(END, "Привед")

def del_str():
    e.delete(0, END)

def get_str():
    l['text'] = e.get()

l = Label(window)
l = Label(window, text="Поле ввода")
l.pack()
e = Entry(window, show='*')
# e.insert(0, "привет ")
# e.insert(END, "привет")

btn1 = Button(window, text="Добавить", command=add_str, width=20, height=1, font=("Comic Sans MS", 20, "italic"))
btn2 = Button(window, text="Получить", command=get_str, width=20, height=1, font=("Comic Sans MS", 20, "italic"))
btn3 = Button(window, text="Удалить", command=del_str, width=20, height=1, font=("Comic Sans MS", 20, "italic"))


btn1.pack()
btn2.pack()
btn3.pack()


e.pack()

window.mainloop()