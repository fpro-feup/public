from sympy import *

x = Symbol('x')

diff(x**2, x)
diff(log(x**2), x)


import tkinter as tk

window = tk.Tk()

def compute():
    res = diff(eval(entry.get()))
    label['text'] = res

entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text='Run', command=compute)
button.pack()
label = tk.Label(window)
label.pack()

window.mainloop()
