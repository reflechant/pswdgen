#!/usr/bin/env python
"""
A Tkinter-based GUI module for generating strong passwords.
Works both under Python 2 and 3.
"""

from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
import string
import random

pswd = ''

def genpswd(event):
    """ generate password """
    global pswd
    global psvar
    global l
    global d
    global p
    #global number
    chars = ""
    if l.get():
        chars = chars + string.ascii_letters
    if d.get():
        chars = chars + string.digits
    if p.get():
        chars = chars + string.punctuation
    
    pswd = ''
    for x in range(0,int(number.get())):
        pswd = pswd + random.choice(chars)
    
    psvar.set(pswd)

def copypswd(event):
    """ copy password to clipboard """
    global pswd
    root.clipboard_clear()
    root.clipboard_append(pswd)


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
ps = tk.Label(root, textvariable=psvar, width = 15, font=("Helvetica", 18))
psvar.set("   пароль   ")

cpBtn = tk.Button(root, text = "Копировать в буфер обмена")
genBtn = tk.Button(root, text = "Новый пароль")

fr2 = tk.Frame(root)

num = tk.StringVar()
num.set( "10" )
number = tk.Spinbox(fr2, from_ =0, to=50, width = 2, textvariable = num)
numLbl = tk.Label(fr2, text="символов")



# L.grid(row = 1, sticky = "W")
# P.grid(row = 2, sticky = "W")
# D.grid(row = 3, sticky = "W")
# number.grid(row = 4, sticky = "W")
# numLbl.grid(row = 4, sticky = "E")
# ps.grid(row = 5, sticky = "W")
# genBtn.grid(row = 6, sticky = "WE")
# cpBtn.grid(row = 7, sticky = "WE")
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