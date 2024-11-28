print("Nguyen Van Tam","\nMSSV: 235752021610054")
import turtle,random
colors=["red","blue","yellow"]
from tkinter import *
window = Tk()
window.title("Giao dien")
window.geometry('500x500')
lbl= Label(window, text='Hello')
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text=" nhan !!")
btn=Button(window,text="Nhan", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
