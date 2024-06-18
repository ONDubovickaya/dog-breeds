import tkinter as tk
from tkinter import ttk
import subprocess

def show_beforeFilter11():
    subprocess.Popen(['python', 'filterBefore1.py'])

def show_afterFilter12():
    subprocess.Popen(['python', 'filterAfter1.py'])

def show_beforeFilter21():
    subprocess.Popen(['python', 'filterBefore2.py'])

def show_afterFilter22():
    subprocess.Popen(['python', 'filterAfter2.py'])

def show_beforeFilter31():
    subprocess.Popen(['python', 'filterBefore3.py'])

def show_afterFilter32():
    subprocess.Popen(['python', 'filterAfter3.py'])

root = tk.Tk()
root.title("Породы собак")
root.geometry('270x350') 

label1 = ttk.Label(root, text = "На входе 1 лайк")
label1.pack()

button11 = tk.Button(root, text="Сначала фильтровать", command=show_beforeFilter11)
button11.pack()

button12 = tk.Button(root, text="Фильтровать после", command=show_afterFilter12)
button12.pack()

lbl = ttk.Label(root, text = " ")
lbl.pack()

label2 = ttk.Label(root, text = "На входе n штук лайков")
label2.pack()

button21 = tk.Button(root, text="Сначала фильтровать", command=show_beforeFilter21)
button21.pack()

button22 = tk.Button(root, text="Фильтровать после", command=show_afterFilter22)
button22.pack()

lbl1 = ttk.Label(root, text = " ")
lbl1.pack()

label2 = ttk.Label(root, text = "На входе n штук лайков и w штук дизлайков")
label2.pack()

button31 = tk.Button(root, text="Сначала фильтровать", command=show_beforeFilter31)
button31.pack()

button32 = tk.Button(root, text="Фильтровать после", command=show_afterFilter32)
button32.pack()

root.mainloop()
