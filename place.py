from tkinter import *

root = Tk()
root.geometry('800x800+1000+300')

label = Label(root, bg="black")
label.place(relheight=.8, relwidth=.8, relx=.5, rely=.5, anchor="c")

root.mainloop()
