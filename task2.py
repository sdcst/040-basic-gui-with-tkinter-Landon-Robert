#!python3
import tkinter as tk
from tkinter import ttk
from tkinter import *
window = tk.Tk()
window.title("T-town Veterinary Clinic Database")
window.geometry("620x200")

photo = PhotoImage(file="dog.png")
dog = tk.Label(window, image=photo)
label1 = tk.Label(window,text="Client Database",borderwidth=1)
label2 = tk.Label(window,text="Name")
label3 = tk.Label(window,text="Type")
label4 = tk.Label(window,text="Breed")
label5 = tk.Label(window,text="Owner")
label6 = tk.Label(window,text="Birth Date")
button1 = tk.Button(window,text="< Previous",borderwidth=1)
button2 = tk.Button(window,text="Next >",borderwidth=1)
button3 = tk.Button(window,text="Search by Name")
button4 = tk.Button(window,text="Save Entry",borderwidth=1)
box = tk.Entry(window,text="Entry widgets can be typed in", relief=SUNKEN)
box1 = tk.Entry(window,text="Entry widgets can be typed in", relief=SUNKEN)
box2 = tk.Entry(window,text="Entry widgets can be typed in", relief=SUNKEN)
box3 = tk.Entry(window,text="Entry widgets can be typed in", relief=SUNKEN)
box4 = tk.Entry(window,text="Entry widgets can be typed in", relief=SUNKEN)
box5 = tk.Entry(window,text="Entry widgets can be typed in", relief=SUNKEN)

dog.grid(row = 2, column = 1)
button3.grid(row = 1, column = 4)
box.grid(row = 1, column = 5)
label1.grid(row = 2, column = 3)
label2.grid(row = 3, column = 1)
label3.grid(row = 3, column = 2)
label4.grid(row = 3, column = 3)
label5.grid(row = 3, column = 4)
label6.grid(row = 3, column = 5)
box1.grid(row = 4, column = 1)
box2.grid(row = 4, column = 2)
box3.grid(row = 4, column = 3)
box4.grid(row = 4, column = 4)
box5.grid(row = 4, column = 5)
button1.grid(row = 5, column = 1)
button4.grid(row = 5, column = 3)
button2.grid(row = 5, column = 5)




window.mainloop()