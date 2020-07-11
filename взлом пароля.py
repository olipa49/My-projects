from tkinter import *
from tkinter import ttk
def babushka():
    f = open("Новый текстовый документ.txt", "a")
    f.write(str(en.get()) + "\n")
    f.close()
    root.destroy()
root = Tk()
root.geometry("1800x900")
root.config(background="light blue")
en = Entry()
b = ttk.Button(text="Войти", command=babushka)
en.pack()
b.pack()
root.mainloop()
