from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
def postroyt_setku():
	if combo.get() not in ["put","get","post", "delete"]:
		messagebox.showerror("Так нельзя!", "Такого вида в списке нет!")
	elif entry0.get() == '':
		messagebox.showerror("Так нельзя!", "И какой метод быдем использовать?")
	else:
		c = combo.get()
		e = entry0.get()
		label1.destroy()
		label2.destroy()
		combo.destroy()
		entry0.destroy()
		b.destroy()
def zapros():
	pass
def sozdanie_zaprosa():
	pass
root = Tk()
root.title("Программа для отправки API-запросов")
#первая страница
label0 = Label(root, text="Программа для отправки API-запросов", font="Helvetica, 20")
label1 = Label(root, text="Вид(Просьба не дописывать варианты):", font="Helvetica, 14")
combo = Combobox(root, state="readonly")  
combo['values'] = ("get", "post", "put", "delete")  
combo.current(1)  # установите вариант по умолчанию  
entry0 = Entry(root, width=30)
label2 = Label(root, text="Метод(Адрес сайта):", font="Helvetica, 14")
b = Button(text="Далее", command=postroyt_setku)
label0.grid(row=0, column=0, pady=5, padx=5)
label1.grid(row=1, column=0, sticky=W, pady=5, padx=5)
combo.grid(row=2, column=0, sticky=W, pady=5, padx=5) 
label2.grid(row=3, column=0, sticky=W, pady=5, padx=5)
entry0.grid(row=4, column=0, sticky=W, pady=5, padx=5)
b.grid(row=5, column=0, sticky=W, pady=5, padx=5)
root.mainloop()
