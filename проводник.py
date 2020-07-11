#Подключаем модуль
import pyautogui
import os
from tkinter.simpledialog import *
from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
root = Tk()
def update(pute):
    txt.delete(1.0,END)
    files = os.listdir(pute)
    for i in range(len(files)):
        txt.insert(INSERT, files[i] + "\n")
def kak_file():
    try:
        a = askstring("Путь", "Путь к файлу")
        os.startfile(b + a)
    except:
        messagebox.showerror("Ошибка", "Файл не найден!")
def kak_papku_out():
    try:
        a = askstring("Путь", "Полный путь к папке")
        txt.delete(1.0,END)
        files = os.listdir(a)
        for i in range(len(files)):
            txt.insert(INSERT, files[i] + "\n")
    except:
        messagebox.showerror("Ошибка", "Файл не найден!")
def kak_papku():
    try:
        global a
        b = a
        a = askstring("Путь", "Полный путь к папке")
        files = os.listdir(b + a)
        txt.delete(1.0,END)
        l.config(text=str(b+a))
        for i in range(len(files)):
            txt.insert(INSERT, files[i] + "\n")
    except:
        messagebox.showerror("Ошибка", "Файл не найден!")
#Каталог из которого будем брать файлы
a = r"c:\\"

#Получаем список файлов в переменную files
files = os.listdir(a)
##for i in files:
##    l = Label(text=i)
##    l.pack()
l = Label(text=str(a))
l.pack()
txt = scrolledtext.ScrolledText(root, width=80, height=30, font="Helvetica, 18")
root.config(background="white")
root.title("Проводник")
txt.pack(side="right")
for i in range(len(files)):
    txt.insert(INSERT, files[i] + "\n")
b = Button(text="Открыть из этой директории папку", command=kak_papku, font="Helvetica, 16")
b1 = Button(text="Открыть файл из этой директории", command=kak_file, font="Helvetica, 16")
b2 = Button(text="Открыть папку не из этой директории", command=kak_papku_out, font="Helvetica, 16")
b3 = Button(text="Питон", command=lambda: update(r"C:\Игорь\питон\\"), font="Helvetica, 16")
b4 = Button(text="Python 37", command=lambda: update(r"C:\Users\Игорь\AppData\Local\Programs\Python\Python37\\"), font="Helvetica, 16")
b.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
root.mainloop()
