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


dog.place(x=64, y=0)
label1.place(x=130, y=40)
label2.place(x=0, y=100)


window.mainloop()