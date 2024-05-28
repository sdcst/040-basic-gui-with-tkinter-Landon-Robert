#!python3
import tkinter as tk
from tkinter import ttk
from tkinter import *
window = tk.Tk()
window.title("T-town Veterinary Clinic Database")
window.geometry("256x135")

photo = PhotoImage(file="dog.png")
dog = tk.Label(window, image = photo)
label1 = tk.Label(window, text = "Pochacco!")
label2 = tk.Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#99FFFF")
label3 = tk.Label(window, text = "  ")
label4 = tk.Label(window, text = "  ")
label5 = tk.Label(window, text = "  ")
label6 = tk.Label(window, text = "  ")

label3.grid(row = 0, column = 0)
label5.grid(row = 0, column = 1)
dog.grid(row = 0, column = 2)
label1.grid(row = 0, column = 3)
label4.grid(row = 0, column = 4)
label6.grid(row = 0, column = 5)
label2.grid(columnspan = 6)


window.mainloop()