import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Packing Widgets example")
# this makes your window a fixed size; it cannot be resize in the (x,y) directions
window.resizable(False,False)

label1 = tk.Label(window,text="Text that does\nnothing is a label", bg="#ee0000")

dogphoto = PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto, borderwidth=3, relief=SUNKEN)

lable3 = tk.Label(window, text="Note that an image can be in a label or a button!", borderwidth=4, relief=SUNKEN)

entry1 = tk.Entry(window,text="Entry widgets can be typed in", borderwidth=3, relief=SUNKEN)

combo = ttk.Combobox(window,values=["1","2","3"])

# Using .grid() instead of .pack()

label1.grid(row = 1, column = 1)
label2.grid(row = 1, column = 2, rowspan = 2)
lable3.grid(row = 2, column = 1)

# entry1 is centered on the 2 columns that have been created
entry1.grid(row=3, column = 1, columnspan=2)

window.mainloop()