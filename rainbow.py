from tkinter import *

window = Tk()
window.geometry('600x800+1000+300')
window.title("RainBow")

l = Label(window)
e = Entry(window, justify='center')
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


color = {
    'red': 'Красный',
    'orange': 'Оранжевый',
    'yellow': 'Желтый',
    'green': 'Зеленый',
    'light blue': 'Голубой',
    'blue': 'Синий',
    'purple': 'Фиолетовый',
}


def makeButton():
    for but in color.items():
        but2 = ButtonRainBow(but[0], but[1])


makeButton()
window.mainloop()
