#'Introduction to programming':Task 8.2
#Seryakov Vlad, FB-21

import tkinter as tk

class Program:
    def __init__(self, master):
        self.master = master
        master.title("tk")
        master.geometry("400x250")
        self.label = tk.Label(master, text="Введіть A, T, C, G:", width= 40, height=2)
        self.label.pack()

        self.text = tk.Text(master, width=55, height=3)
        self.text.pack()

        self.count_button = tk.Button(master, text="Count", command=self.count, width=40, height=2)
        self.count_button.pack()

        self.clear_button = tk.Button(master, text="Clear", command=self.clear, width=40, height=2)
        self.clear_button.pack()

        self.goodbye_button = tk.Button(master, text="Goodbye", command=master.quit, width=40, height=2)
        self.goodbye_button.pack()

        self.result_label = tk.Label(master, text="Num As: 0,Num Ts: 0,Num Cs: 0,Num Gs: 0", width=40, height=2)
        self.result_label.pack()

    def count(self):
        sequence = self.text.get("1.0", tk.END)
        a_count = sequence.count("A")
        t_count = sequence.count("T")
        c_count = sequence.count("C")
        g_count = sequence.count("G")
        result = f"Num As: {a_count},Num Ts: {t_count},Num Cs: {c_count},Num Gs: {g_count}"
        self.result_label.config(text=result)

    def clear(self):
        self.text.delete("1.0", tk.END)
        self.result_label.config(text="Num As: 0,Num Ts: 0,Num Cs: 0,Num Gs: 0")

root = tk.Tk()
root.geometry("400x250")
root.resizable(width=False, height=False)
dna_counter = Program(root)
root.mainloop()