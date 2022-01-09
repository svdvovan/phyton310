from tkinter import *

window = Tk()
window.geometry('600x800+1000+300')
window.title("RainBow")

l = Label(window)
e = Entry(window)
l.pack(fill=X)
e.pack(fill=X)


class ButtonRainBow:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.printButton()

    def printButton(self):
        Btn = Button(window, bg=self.color, command=self.changeLabel, width=20, height=1,
                     font=("Comic Sans MS", 20, "italic"))
        Btn.pack(fill=X)

    def changeLabel(self):
        e.delete(0, END)
        l['text'] = self.name
        e.insert(0, string=self.color)


but2 = ButtonRainBow("red", "Красный")
but2 = ButtonRainBow("orange", "Оранжевый")
but2 = ButtonRainBow("yellow", "Желтый")
but2 = ButtonRainBow("green", "Зеленый")
but2 = ButtonRainBow("light blue", "Голубой")
but2 = ButtonRainBow("blue", "Синий")
but2 = ButtonRainBow("purple", "Фиолетовый")

window.mainloop()
