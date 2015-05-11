#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A Tkinter-based GUI module for generating strong passwords.
Works both under Python 2 and 3.
"""

from sys import version
if version.split()[0][0] == '2':
    import Tkinter as tk
elif version.split()[0][0] == '3':
    import tkinter as tk
else:
    print ("Невозможно определить установленную версию интерпретатора Python")
    exit()

import string
import random


def genpswd(event):
    """ generate password """
    
    chars = ""
    if l.get():
        chars = chars + string.ascii_letters
    if d.get():
        chars = chars + string.digits
    if p.get():
        chars = chars + string.punctuation
    if not l.get() and not d.get() and not p.get():
        return
    
    pswd = ''
    for x in range(0,int(number.get())):
        pswd = pswd + random.choice(chars)
    
    psvar.set(pswd)

def copypswd(event):
    """ copy password to clipboard """
    root.clipboard_clear()
    root.clipboard_append(psvar.get())


root = tk.Tk()

fr1 = tk.Frame(root)

l = tk.IntVar()
L = tk.Checkbutton(fr1, text = "Буквы", variable = l)
L.select()

d = tk.IntVar()
D = tk.Checkbutton(fr1, text = "Цифры", variable = d)
D.select()

p = tk.IntVar()
P = tk.Checkbutton(fr1, text = "Символы", variable = p)
P.select()

psvar = tk.StringVar()
ps = tk.Label(root, textvariable=psvar, font=("Helvetica", 18))
psvar.set("   пароль   ")

cpBtn = tk.Button(root, text = "Копировать в буфер обмена")
genBtn = tk.Button(root, text = "Новый пароль")

fr2 = tk.Frame(root)

num = tk.StringVar()
num.set( "10" )
number = tk.Spinbox(fr2, from_ =0, to=50, width = 2, textvariable = num)
numLbl = tk.Label(fr2, text="символов")



fr1.pack(anchor="w")
L.pack(side = "left")
P.pack(side = "left")
D.pack(side = "left")
fr2.pack()
number.pack(side = "left")
numLbl.pack(side = "left")
ps.pack()
genBtn.pack()
cpBtn.pack()


genBtn.bind("<Button-1>", genpswd)
cpBtn.bind("<Button-1>", copypswd)

root.mainloop()
