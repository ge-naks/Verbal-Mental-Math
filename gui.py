import tkinter as tk
from tkinter import ttk
from vmm import start

window = tk.Tk()

window.title('AudioMac')
window.geometry('1000x800')


label = ttk.Label(master = window, text = "Start")

label.pack()

entry = ttk.Entry(master = window)

entry.pack()

button = ttk.Button(master = window, text = " button", command= start )

button.pack()

window.mainloop()

