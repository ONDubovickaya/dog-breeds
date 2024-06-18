import tkinter as tk
from tkinter import ttk
import subprocess

def show_withFilter_window():
    subprocess.Popen(['python', 'withFilter.py'])

def show_noFilter_window():
    subprocess.Popen(['python', 'noFilter.py'])

root = tk.Tk()
root.title("Породы собак")
root.geometry('270x50') 
button = tk.Button(root, text="С фильтрами", command=show_withFilter_window)
button.pack()

button2 = tk.Button(root, text="БЕЗ фильтров", command=show_noFilter_window)
button2.pack()

root.mainloop()
