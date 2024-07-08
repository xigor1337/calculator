import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

WINDOWS_SIZE = "800x800"
MAIN_COLOR = "#525252"
TEXT_COLOR = "#d9d9d9"

class Template():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(WINDOWS_SIZE)
        self.root.title("Calculator")
        self.root.configure(bg=MAIN_COLOR)

        # top bar functions
        self.menubar = tk.Menu(self.root, bg=MAIN_COLOR)

        self.filemenu = tk.Menu(self.menubar, tearoff=0, bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.filemenu.add_command(label="Export history", command=exit)
        self.filemenu.add_command(label="Force Close", command=exit)

        self.menusmenu = tk.Menu(self.menubar, tearoff=0, bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.menusmenu.add_command(label="Calculator", command=self.calculator_option)
        self.menusmenu.add_command(label="Functions", command=self.functions_option)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.menusmenu, label="Menus")

        self.root.config(menu=self.menubar)

    def calculator_option(self):
        if self.root.state() == 'normal':
            Main()
        else:
            messagebox.showinfo(title="Error", message="You can`t open the same windows twice")

    def functions_option(self):
        if self.root.state() == 'normal':
            Functions()
            print(self.root)
        else:
            messagebox.showinfo(title="Error", message="You can`t open the same windows twice")

class Main(Template):
    def __init__(self):
        super().__init__()

        # calculator
        # display
        self.view = ""
        self.display = tk.Label(text="", height=5, font=("Arial", 16), bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.display.pack(pady=10)

        # buttons
        self.calc = tk.Frame(self.root, bg=MAIN_COLOR)
        self.calc.columnconfigure(0, weight=1)
        self.calc.columnconfigure(1, weight=1)
        self.calc.columnconfigure(2, weight=1)
        self.calc.columnconfigure(3, weight=1)

        self.button_create("1", 1, 0, self.send_1)
        self.button_create("2", 1, 1, self.send_2)
        self.button_create("3", 1, 2, self.send_3)
        self.button_create("4", 2, 0, self.send_4)
        self.button_create("5", 2, 1, self.send_5)
        self.button_create("6", 2, 2, self.send_6)
        self.button_create("7", 3, 0, self.send_7)
        self.button_create("8", 3, 1, self.send_8)
        self.button_create("9", 3, 2, self.send_9)

        self.button_create("+", 0, 0, self.send_sum)
        self.button_create("-", 0, 1, self.send_subtraction)
        self.button_create("*", 0, 2, self.send_multiplication)
        self.button_create("/", 0, 3, self.send_division)
        self.button_create("0", 1, 3, self.send_0)
        self.button_create("clear", 2, 3, self.clear)
        self.button_create("=", 3, 3, self.solution)

        self.calc.pack(fill="x")

        self.root.mainloop()

    def button_create(self, text, row, col, command):
        self.btn = tk.Button(self.calc, text=text, command=command, height=2, bg="#d6e2ff", bd=1, relief="solid", font=("Arial", 16))
        self.btn.grid(row=row, column=col, sticky=tk.W + tk.E, padx=2, pady=2)

    def send(self, value):
        self.view += value
        self.display.config(text=self.view)

    def send_1(self):
        self.send("1")

    def send_2(self):
        self.send("2")

    def send_3(self):
        self.send("3")

    def send_4(self):
        self.send("4")

    def send_5(self):
        self.send("5")

    def send_6(self):
        self.send("6")

    def send_7(self):
        self.send("7")

    def send_8(self):
        self.send("8")

    def send_9(self):
        self.send("9")

    def send_0(self):
        self.send("0")

    def send_sum(self):
        if self.view[-1].isdecimal() == False:
            pass
        else:
            self.send("+")

    def send_subtraction(self):
        if self.view[-1].isdecimal() == False:
            pass
        else:
            self.send("-")

    def send_multiplication(self):
        if self.view[-1].isdecimal() == False:
            pass
        else:
            self.send("*")

    def send_division(self):
        if self.view[-1].isdecimal() == False:
            pass
        else:
            self.send("/")

    def solution(self):
        #check for errors
        if (self.view[0].isdecimal() == False and self.view[0] != "-") or self.view[-1].isdecimal() == False:
            messagebox.showinfo(title="Error", message="Calculation must start and end with a number")
        else:
            # change to list
            current_numer = ""
            list = []
            for object in self.view.strip():
                if object.isdecimal() or object == "*" or object == "/":
                    current_numer += object
                else:
                    list.append(current_numer)
                    list.append(object)
                    current_numer = ""
            else:
                list.append(current_numer)
            print(list)

            # calculate multiplication and division
            if list[0] == '':
                list[0] = "0"
            list2 = []
            for object in list:
                if object.isdecimal() or object == "+" or object == "-":
                    list2.append(object)
                else:
                    temp_list = []
                    current = ""
                    for i in object:
                        if i == "*" or i == "/":
                            temp_list.append(current)
                            current = ""
                            temp_list.append(i)
                        else:
                            current = current + i
                    else:
                        temp_list.append(current)
                    print(temp_list)

                    first = int(temp_list[0])
                    for index, object in enumerate(temp_list[1:]):
                        if object == "*":
                            first *= int(temp_list[index + 2])
                        elif object == "/":
                            first //= int(temp_list[index + 2])
                        else:
                            pass
                    list2.append(str(first))
            print(list2)

            # calculate sum and subtraction
            solution = int(list2[0])
            for index, object in enumerate(list2[1:]):
                if object == "+":
                    solution += int(list2[index + 2])
                elif object == "-":
                    solution -= int(list2[index + 2])
                else:
                    pass
            print(solution)
            self.display.config(text=str(solution))
            self.view = str(solution)

    def clear(self):
        self.view = ""
        self.display.config(text=self.view)

class Functions(Template):
    def __init__(self):
        super().__init__()

        self.inputframe = tk.Frame(self.root)
        self.inputframe.columnconfigure(0, weight=1)

        self.title = tk.Label(self.root, text="Input function formula here:", font=("Arial", 16), bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.title.pack()

        # formula inputs
        self.input_formula = tk.Entry(self.root, font=("Arial", 16), bg=MAIN_COLOR, relief="solid", justify='center')
        self.input_formula.pack(fill="x")


        # range inputs
        self.range_frame = tk.Frame(self.root)
        self.range_frame.columnconfigure(0, weight=1)
        self.range_frame.columnconfigure(1, weight=1)

        self.range_left_label = tk.Label(self.range_frame, text="Left part of input range", font=("Arial", 16), bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.range_left_label.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.range_left = tk.Entry(self.range_frame, font=("Arial", 16), bg=MAIN_COLOR, relief="solid", justify='center')
        self.range_left.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.range_right_label = tk.Label(self.range_frame, text="Right part of input range", font=("Arial", 16), bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.range_right_label.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.range_right = tk.Entry(self.range_frame, font=("Arial", 16), bg=MAIN_COLOR, relief="solid", justify='center')
        self.range_right.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.range_frame.pack(fill="x")

        self.btn = tk.Button(self.root, text="plot", command=self.make_function, width=20, height=2, bg="#fec3c3", relief="flat")
        self.btn.pack(pady=5)

        self.root.mainloop()

    def make_function(self):
        formula = self.input_formula.get()
        range_left = self.range_left.get()
        range_right = self.range_right.get()

        # range error check
        correct = True
        if range_left[0].isdecimal() == False and range_left[0] != "-":
            messagebox.showinfo(title="Error", message="There is invalid symbol in the left range")
            correct = False
        for i in range_left[1:].strip():
            if i.isdecimal() == False:
                messagebox.showinfo(title="Error", message="There is invalid symbol in the left range")
                correct = False
                break
        for i in range_right.strip():
            if i.isdecimal() == False:
                messagebox.showinfo(title="Error", message="There is invalid symbol in the right range")
                correct = False
                break

        # formula error check
        allow = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", "x"]
        for i in formula.strip():
            if i not in allow:
                messagebox.showinfo(title="Error", message="There is invalid symbol in the formula")
                correct = False
                break

        # plot calculation
        if correct == True:
            # plot calculation
            x_axis = []
            y_axis = []
            for x in range(int(range_left.strip()), int(range_right.strip()) + 1):
                y = eval(formula.strip())
                # print("x =", x, "y =", y)
                x_axis.append(x)
                y_axis.append(y)
            plt.plot(x_axis, y_axis, "ro")
            plt.show()

Main()