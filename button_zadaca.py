from tkinter import *

window = Tk()
window.geometry('600x800+1000+300')
window.title("Калькулятор")
FIRST = 5
SECOND =10
l = Label(window, text=f"Операции над числами {FIRST} и {SECOND}")
l.pack()

def umn():
    print(FIRST*SECOND)

def delen():
    print(FIRST/SECOND)

def vich():
    print(FIRST-SECOND)

def sum():
    print(FIRST+SECOND)

btn = Button(window, text="сложение", command=sum, width=20, height=5, font=("Comic Sans MS", 20, "italic"))
btn2 = Button(window, text="деление", command=delen, width=20, height=2, font=("Comic Sans MS", 20, "italic"))
btn3 = Button(window, text="умножение", command=umn, width=20, height=2, font=("Comic Sans MS", 20, "italic"))
btn4 = Button(window, text="вычитание", command=vich, width=20, height=2, font=("Comic Sans MS", 20, "italic"))



#
btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()

window.mainloop()