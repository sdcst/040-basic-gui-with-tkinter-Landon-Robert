#!python3
import tkinter as tk
from tkinter import ttk
from tkinter import *
window = tk.Tk()
window.title("tk")
window.geometry("450x40")
entry1 = tk.Entry(window,text="Entry widgets can be typed in")
label1 = tk.Label(window,text=" X ",)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", relief=SUNKEN)
label2 = tk.Label(window,text=" = ",)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", relief=SUNKEN)

entry1.grid(row = 1, column = 1,)
label1.grid(row = 1, column = 2,)
entry2.grid(row = 1, column = 3,)
label2.grid(row = 1, column = 4,)
entry3.grid(row = 1, column = 5,)








window.mainloop()
