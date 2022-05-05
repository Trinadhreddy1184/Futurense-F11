from flask import *
from tkinter import *
import tkinter as tk
app=Flask(__name__,template_folder='template')
def fun():
    root=Tk()
    root.title("Flask integration")
    root.geometry('400x200')
    toplabel = Label(root, text="Hi this is a test")
    toplabel.place(x = 120, y = 80)
    root.mainloop()

@app.route('/')
def func():
    return fun()

if __name__ == '__main__':
    app.run(host='192.168.4.161',port='1234',debug=True)
