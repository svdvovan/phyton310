from tkinter import *

root = Tk()
root.geometry('800x100+1000+300')
# f = Frame(root)
# f.pack(pady=50)

# btn7 = Button(f, text='7', padx=10, pady=5).grid(row=0, column=0)
# btn8 = Button(f, text='8', padx=10, pady=5).grid(row=0, column=1)
# btn9 = Button(f, text='9', padx=10, pady=5).grid(row=0, column=2)
# btn4 = Button(f, text='4', padx=10, pady=5).grid(row=1, column=0)
# btn5 = Button(f, text='5', padx=10, pady=5).grid(row=1, column=1)
# btn6 = Button(f, text='6', padx=10, pady=5).grid(row=1, column=2)
# btn1 = Button(f, text='1', padx=10, pady=5).grid(row=2, column=0)
# btn2 = Button(f, text='2', padx=10, pady=5).grid(row=2, column=1)
# btn3 = Button(f, text='3', padx=10, pady=5).grid(row=2, column=2)
# btn0 = Button(f, text='0', padx=10, pady=5).grid(row=3, column=3, columnspan=3)

# btn_list = [
#     '7', '8', '9',
#     '4', '5', '6',
#     '1', '2', '3',
#     '0'
# ]
#
# row = 0
# column = 0
# for i in btn_list:
#     if i == 0:
#         Button(f, text=i, padx=10, pady=5).grid(row=row, columnspan=3)
#     Button(f, text=i, padx=10, pady=5).grid(row=row, column=column)
#     column += 1
#     if column == 3:
#         column = 0
#         row += 1
#
mainMenu = Menu(root)
root.config(menu=mainMenu)
# mainMenu.add_command(label="file")
# mainMenu.add_command(label="exit")

fileMenu = Menu(mainMenu, tearoff=0)
fileMenu.add_command(label="открыть")
fileMenu.add_command(label="сохранить")
fileMenu.add_separator()
fileMenu.add_command(label="выход")
mainMenu.add_cascade(label="file", menu=fileMenu)

helpMenu = Menu(mainMenu, tearoff=0)
helpMenuSub = Menu(helpMenu, tearoff=0)
helpMenuSub.add_command(label="перейти на сайт")
helpMenuSub.add_command(label="Помогите")
helpMenu.add_cascade(label="Помощь", menu=helpMenuSub)
helpMenu.add_command(label="О программе")
mainMenu.add_cascade(label="Справка", menu=helpMenu)

l_url = Label(root, text="Введите url страницы:").grid(row=0, column=0, pady=10)
e_url = Entry(root, width=100).grid(row=0, column=1, padx=15, sticky=E)

l_start = Button(root, text="Парсить").grid(row=1, column=0, padx=10, pady=10, sticky=W)

root.mainloop()
