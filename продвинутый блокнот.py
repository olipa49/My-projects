from tkinter import *
from tkinter import ttk
def save():
    global f
    f.close()
    root.destroy()
def a():
    global e1
    f = open("index.html", "a")
    f.write("<a href="+e1.get()+">\n")
    f.close()
def a_():
    f = open("index.html", "a")
    f.write("<a/>\n")
    f.close()
def p():
    f = open("index.html", "a")
    f.write("<p>\n")
    f.close()
def p_():
    f = open("index.html", "a")
    f.write("<p/>\n")
    f.close()
def div():
    f = open("index.html", "a")
    f.write("<div>\n")
    f.close()
def div_():
    f = open("index.html", "a")
    f.write("<div/>\n")
    f.close()
def text():
    global e1
    f = open("index.html", "a")
    f.write(e1.get()+"\n")
    f.close()
root = Tk()
b1 = ttk.Button(text="<a>(href из поля)", command=a)
b2 = ttk.Button(text="<a/>", command=a_)
b3 = ttk.Button(text="<p>", command=p)
b4 = ttk.Button(text="<p/>", command=p_)
b5 = ttk.Button(text="<div>", command=div)
b6 = ttk.Button(text="<div/>", command=div_)
b7 = ttk.Button(text="Текст из поля", command=text)
e1 = Entry()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
e1.pack()
root.mainloop()
