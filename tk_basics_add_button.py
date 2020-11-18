from tkinter import *
from tkinter import ttk
root = Tk()
button = ttk.Button(root, text = "Get Info")
button.pack()
button['text'] = "Show Info"
button.config(text = "ok")
print(button.config())
print(str(button))
label = ttk.Label(root, text = "The name is: nnn").pack()
root.mainloop()