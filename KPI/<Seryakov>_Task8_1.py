#'Introduction to programming':Task 8.1
#Seryakov Vlad, FB-21

import tkinter as tk

class Program():
    def __init__(self, master):
        self.master = master
        master.title("tk")
        master.geometry("400x200")
        self.number = 0
        self.number_label = tk.Label(master,text = self.number)
        self.inc_button = tk.Button(master, text = "Inc",width=40, height=2, command=self.increment)
        self.dec_button = tk.Button(master, text = "Dec",width=40, height=2, command=self.decrement)
        self.clear_button = tk.Button(master, text = "Clear",width=40, height=2, command=self.clear)
        self.goodbye_button = tk.Button(master, text = "Goodbye",width=40,height=2, command=self.master.quit)
        self.number_label.pack()
        self.inc_button.pack()
        self.dec_button.pack()
        self.clear_button.pack()
        self.goodbye_button.pack()

    def increment(self):
        if self.number < 100:
            self.number += 1
        self.update_label()

    def decrement(self):
        if self.number > -100:
            self.number -= 1
        self.update_label()

    def clear(self):
        self.number = 0
        self.update_label()

    def update_label(self):
        self.number_label.config(text=self.number)

root = tk.Tk()
root.resizable(width=False, height=False)
inc_dec_gui = Program(root)
root.mainloop()