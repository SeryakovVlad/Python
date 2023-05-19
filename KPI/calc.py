import tkinter as tk

class Calculator:
    def __init__(self, master):
        
        self.master = master
        master.title("Calculator")
        master.geometry("400x310")

        def validate_input(event):
            char = event.char
            if char.isdigit() or char == "+" or char == "-" or char == "*" or char == "/" or char == "." or char == "%" or char in '\b\n':
                pass
            else:
                return 'break'

        self.text = tk.Text(master, width=55, height=1, font=("Arial",30))
        self.text.bind('<Key>', validate_input)
        self.text.pack()

        button_frame1 = tk.Frame(master)
        button_frame1.pack(side=tk.TOP)

        self.c_button = tk.Button(button_frame1, width = 6,height=2, text="C", command=self.c_button)
        self.c_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.ce_button = tk.Button(button_frame1,width = 6,height=2, text="CE", command=self.ce_button)
        self.ce_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.percent_button = tk.Button(button_frame1,width = 6,height=2, text="%", command=self.percent_button)
        self.percent_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.devide_button = tk.Button(button_frame1,width = 6,height=2, text="/", command=self.devide_button)
        self.devide_button.pack(side=tk.LEFT, padx=5, pady=5)

        button_frame2 = tk.Frame(master)
        button_frame2.pack(side=tk.TOP)

        self.one_button = tk.Button(button_frame2,width = 6,height=2, text="1", command=self.one_button)
        self.one_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.two_button = tk.Button(button_frame2,width = 6,height=2, text="2", command=self.two_button)
        self.two_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.three_button = tk.Button(button_frame2,width = 6,height=2, text="3", command=self.three_button)
        self.three_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.multiply_button = tk.Button(button_frame2,width = 6,height=2, text="*", command=self.multiply_button)
        self.multiply_button.pack(side=tk.LEFT, padx=5, pady=5)

        button_frame3 = tk.Frame(master)
        button_frame3.pack(side=tk.TOP)

        self.four_button = tk.Button(button_frame3,width = 6,height=2, text="4", command=self.four_button)
        self.four_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.five_button = tk.Button(button_frame3,width = 6,height=2, text="5", command=self.five_button)
        self.five_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.six_button = tk.Button(button_frame3,width = 6,height=2, text="6", command=self.six_button)
        self.six_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.minus_button = tk.Button(button_frame3,width = 6,height=2, text="-", command=self.minus_button)
        self.minus_button.pack(side=tk.LEFT, padx=5, pady=5)

        button_frame4 = tk.Frame(master)
        button_frame4.pack(side=tk.TOP)

        self.seven_button = tk.Button(button_frame4,width = 6,height=2, text="7", command=self.seven_button)
        self.seven_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.eight_button = tk.Button(button_frame4,width = 6,height=2, text="8", command=self.eight_button)
        self.eight_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.nine_button = tk.Button(button_frame4,width = 6,height=2, text="9", command=self.nine_button)
        self.nine_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.plus_button = tk.Button(button_frame4,width = 6,height=2, text="+", command=self.plus_button)
        self.plus_button.pack(side=tk.LEFT, padx=5, pady=5)

        button_frame5 = tk.Frame(master)
        button_frame5.pack(side=tk.TOP)

        self.zero_button = tk.Button(button_frame5,width = 17,height=2, text="0", command=self.zero_button)
        self.zero_button.pack(side=tk.LEFT, padx=5, pady=5,)

        self.coma_button = tk.Button(button_frame5,width = 6,height=2, text=".", command=self.coma_button)
        self.coma_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.equal_button = tk.Button(button_frame5,width = 6,height=2, text="=", command=self.equal_button)
        self.equal_button.pack(side=tk.LEFT, padx=5, pady=5)

        master.bind("<Return>", lambda event: self.equal_button.invoke())
        

    def one_button(self):
        self.text.insert(tk.END, "1")
    def two_button(self):
        self.text.insert(tk.END, "2")
    def three_button(self):
        self.text.insert(tk.END, "3")
    def four_button(self):
        self.text.insert(tk.END, "4")
    def five_button(self):
        self.text.insert(tk.END, "5")
    def six_button(self):
        self.text.insert(tk.END, "6")
    def seven_button(self):
        self.text.insert(tk.END, "7")
    def eight_button(self):
        self.text.insert(tk.END, "8")
    def nine_button(self):
        self.text.insert(tk.END, "9")
    def zero_button(self):
        self.text.insert(tk.END, "0")
    def plus_button(self):
        current_text = list(self.text.get("1.0", tk.END))
        if current_text[-2] == "-" or current_text[-2] == "*" or current_text[-2] == "/" or current_text[-2] == "+" or current_text[-2] == ".":
            current_text = self.text.get("1.0", tk.END)
            updated_text = current_text[:-2]
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, updated_text)
            self.text.insert(tk.END, "+")
        else:
            self.text.insert(tk.END, "+")
    def minus_button(self):
        current_text = list(self.text.get("1.0", tk.END))
        if len(current_text) == 1:
            self.text.insert(tk.END, "-")
        try:
            if current_text[-2] == "-" or current_text[-2] == "*" or current_text[-2] == "/" or current_text[-2] == "+" or current_text[-2] == ".":
                current_text = self.text.get("1.0", tk.END)
                updated_text = current_text[:-2]
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, updated_text)
                self.text.insert(tk.END, "-")
            else:
                self.text.insert(tk.END, "-")
        except:
            pass
    def devide_button(self):
        current_text = list(self.text.get("1.0", tk.END))
        try:
            if current_text[-2] == "-" or current_text[-2] == "*" or current_text[-2] == "/" or current_text[-2] == "+" or current_text[-2] == ".":
                current_text = self.text.get("1.0", tk.END)
                updated_text = current_text[:-2]
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, updated_text)
                self.text.insert(tk.END, "/")
            else:
                self.text.insert(tk.END, "/")
        except:
            pass
    def multiply_button(self):
        current_text = list(self.text.get("1.0", tk.END))
        try:
            if current_text[-2] == "-" or current_text[-2] == "*" or current_text[-2] == "/" or current_text[-2] == "+" or current_text[-2] == ".":
                current_text = self.text.get("1.0", tk.END)
                updated_text = current_text[:-2]
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, updated_text)
                self.text.insert(tk.END, "*")
            else:
                self.text.insert(tk.END, "*")
        except:
            pass
    def coma_button(self):
        current_text = list(self.text.get("1.0", tk.END))
        try:
            if current_text[-2] == "-" or current_text[-2] == "*" or current_text[-2] == "/" or current_text[-2] == "+" or current_text[-2] == "%" or current_text[-2] == ".":
                pass
            else:
                self.text.insert(tk.END, ".")
        except:
            pass
    def percent_button(self):
        current_text = list(self.text.get("1.0", tk.END))
        try:
            if current_text[-2] == "-" or current_text[-2] == "*" or current_text[-2] == "/" or current_text[-2] == "+"or current_text[-2] == "%" or current_text[-2] == ".":
                pass
            else:
                self.text.insert(tk.END, "%")
        except:
            pass
    def c_button(self):
        self.text.delete(1.0, tk.END)
    def ce_button(self):
        current_text = self.text.get("1.0", tk.END)
        updated_text = current_text[:-2]
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, updated_text)

    def equal_button(self):
        try:
            current_text = list(self.text.get("1.0", tk.END))
            count_arr = []
            temp = ''
            for i in range(0, len(current_text)):
                try:
                    count_arr.append(int(current_text[i]))
                except:
                    if current_text[i] == '\n':
                        pass
                    else:
                        count_arr.append(current_text[i])
            result_arr = []
            temp = ""
            for i in range(0, len(count_arr)):
                if type(count_arr[i]) == int or count_arr[i] == '.' or (count_arr[i] == '-' and i == 0):
                    temp += str(count_arr[i])
                else:
                    result_arr.append(float(temp))
                    result_arr.append(count_arr[i])
                    temp = ""
            try:
                result_arr.append(float(temp))
            except ValueError:
                pass
            
            i = 0
            while len(result_arr) > 1 and '%' in result_arr:
                if result_arr[i] == '%':
                    res = result_arr[i-1] / 100
                    result_arr.pop(i)
                    result_arr[i-1] = res
                else:
                    i += 1

            i = 0
            while len(result_arr) > 1 and ('*' in result_arr or '/' in result_arr):
                if result_arr[i] == '*':
                    res = result_arr[i-1] * result_arr[i+1]
                    result_arr.pop(i-1)
                    result_arr.pop(i)
                    result_arr[i-1] = res
                elif result_arr[i] == '/':
                    try:
                        res = result_arr[i-1] / result_arr[i+1]
                        result_arr.pop(i-1)
                        result_arr.pop(i)
                        result_arr[i-1] = res
                    except ZeroDivisionError:
                        self.text.delete("1.0", tk.END)
                        self.text.insert(tk.END, "Error: Division by zero")
                        return
                else:
                    i += 1

            i = 0
            while len(result_arr) > 1 and '+' in result_arr or '-' in result_arr:
                if result_arr[i] == '+':
                    res = result_arr[i-1] + result_arr[i+1]
                    result_arr.pop(i-1)
                    result_arr.pop(i)
                    result_arr[i-1] = res
                elif result_arr[i] == '-':
                    res = result_arr[i-1] - result_arr[i+1]
                    result_arr.pop(i-1)
                    result_arr.pop(i)
                    result_arr[i-1] = res
                else:
                    i += 1

            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, result_arr[0])
        except:
            self.text.delete("1.0", tk.END)

root = tk.Tk()
root.geometry("400x310")
root.resizable(width=False, height=False)
dna_counter = Calculator(root)
root.mainloop()