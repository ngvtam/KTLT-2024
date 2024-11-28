print("Nguyen Van Tam","\nMSSV: 235752021610054")
from tkinter import *
window=Tk()
window.title("giao dien")
window.geometry('300x300')
a=Label(window,text=" rang")
a.place(x=120,y=100)
def ShowChoice():
    a.configure(text="Ve thoi")
def clicked():
    a.configure(text="thi")
def chot():
    a.configure(text="dốt")
b=Button(window,text="ve",command=ShowChoice)
b.place(x=125,y=130)
c=Button(window,text=" lai",command=clicked)
c.place(x=120,y=160)
d=Button(window,text="chiu",command=chot)
d.place(x=123,y=190)
