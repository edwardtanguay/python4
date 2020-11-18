from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "English: house")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        ttk.Button(master, text = "German",
                   command = self.german_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "French",
                   command = self.french_hello).grid(row = 1, column = 1)

    def german_hello(self):
        self.label.config(text = 'das Haus')

    def french_hello(self):
        self.label.config(text = 'la maison')
            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()
