import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

MAIN_COLOR = "#525252"
TEXT_COLOR = "#d9d9d9"
BUTTON_COLOR = "#d6e2ff"

class Template():
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg=MAIN_COLOR)

        # top bar functions
        self.menubar = tk.Menu(self.root, bg=MAIN_COLOR)

        self.filemenu = tk.Menu(self.menubar, tearoff=0, bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.filemenu.add_command(label="Export history", command=exit)
        self.filemenu.add_command(label="Force Close", command=exit)

        self.menusmenu = tk.Menu(self.menubar, tearoff=0, bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.menusmenu.add_command(label="Calculator", command=self.calculator_option)
        self.menusmenu.add_command(label="Graph visualizer", command=self.functions_option)
        self.menusmenu.add_command(label="Informatics values", command=self.informatics_option)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.menusmenu, label="Menus")

        self.root.config(menu=self.menubar)

    def patter_creator(self):
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

        self.button_create("1", 1, 0, lambda: self.send("1"))
        self.button_create("2", 1, 1, lambda: self.send("2"))
        self.button_create("3", 1, 2, lambda: self.send("3"))
        self.button_create("4", 2, 0, lambda: self.send("4"))
        self.button_create("5", 2, 1, lambda: self.send("5"))
        self.button_create("6", 2, 2, lambda: self.send("6"))
        self.button_create("7", 3, 0, lambda: self.send("7"))
        self.button_create("8", 3, 1, lambda: self.send("8"))
        self.button_create("9", 3, 2, lambda: self.send("9"))
        self.button_create("0", 4, 1, lambda: self.send("0"))
        self.button_create("C", 4, 0, self.clear)

    def send(self, value):
        self.view += value
        self.display.config(text=self.view)

    def button_create(self, text, row, col, command):
        self.btn = tk.Button(self.calc, text=text, command=command, height=3, bg=BUTTON_COLOR, bd=1, relief="solid", font=("Arial", 16))
        self.btn.grid(row=row, column=col, sticky=tk.W + tk.E, padx=2, pady=2)

    def clear(self):
        self.view = ""
        self.display.config(text=self.view)

    def calculator_option(self):
        self.root.destroy()
        Main()

    def functions_option(self):
        self.root.destroy()
        Functions()

    def informatics_option(self):
        self.root.destroy()
        Informatics()


class Main(Template):
    def __init__(self):
        # standard calculator
        super().__init__()
        self.root.geometry("430x606")
        self.root.title("Calculator")

        self.patter_creator()

        self.button_create("+", 0, 0, self.send_sum)
        self.button_create("-", 0, 1, self.send_subtraction)
        self.button_create("*", 0, 2, self.send_multiplication)
        self.button_create("/", 0, 3, self.send_division)
        self.button_create("=", 4, 2, self.solution)

        self.calc.pack(fill="x")

        self.root.mainloop()

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
        # check for errors
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


class Functions(Template):
    def __init__(self):
        # graph visializator
        super().__init__()
        self.root.geometry("600x600")
        self.root.title("Functions")

        # only separates part of the windows
        self.separator = tk.Label(self.root, text="", font=("Arial", 16), bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.separator.pack()

        self.inputframe = tk.Frame(self.root)
        self.inputframe.columnconfigure(0, weight=1)

        self.title = tk.Label(self.root, text="Input function formula here:", font=("Arial", 16), bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.title.pack()

        # formula inputs
        self.input_formula = tk.Entry(self.root, font=("Arial", 16), bg=MAIN_COLOR, relief="solid", justify='center')
        self.input_formula.pack(fill="x")

        # only separates part of the windows
        self.separator = tk.Label(self.root, text="", font=("Arial", 16), bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.separator.pack()

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

        # only separates part of the windows
        self.separator = tk.Label(self.root, text="", font=("Arial", 16), bg=MAIN_COLOR, fg=TEXT_COLOR)
        self.separator.pack()

        self.btn = tk.Button(self.root, text="plot", command=self.make_function, width=20, height=2, bg=BUTTON_COLOR, relief="flat")
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


class Informatics(Template):
    def __init__(self):
        # IT values calculator
        super().__init__()
        self.root.geometry("430x790")
        self.root.title("IT values calculator")
        self.datatype = "DEC"

        self.patter_creator()

        self.button_create("HEX", 0, 0, self.send_HEX)
        self.button_create("DEC", 0, 1, self.send_DEC)
        self.button_create("OCT", 0, 2, self.send_OCT)
        self.button_create("BIN", 0, 3, self.send_BIN)

        self.button_create("A", 1, 3, lambda: self.send("A"))
        self.button_create("B", 2, 3, lambda: self.send("B"))
        self.button_create("C", 3, 3, lambda: self.send("C"))
        self.button_create("D", 4, 3, lambda: self.send("D"))
        self.button_create("E", 5, 3, lambda: self.send("E"))
        self.button_create("F", 6, 3, lambda: self.send("F"))

        self.calc.pack(fill="x")
        self.root.mainloop()

    def check_datatype(self):
        # check_HEX = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        check_DEC = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        check_OCT = ["0", "1", "2", "3", "4", "5", "6", "7"]
        check_BIN = ["0", "1"]
        correct = True

        # HEX can`t be inputed wrong
        if self.datatype == "DEC":
            for i in str(self.view):
                if i not in check_DEC:
                    correct = False
                    break
        if self.datatype == "OCT":
            for i in str(self.view):
                if i not in check_OCT:
                    correct = False
                    break
        if self.datatype == "BIN":
            for i in str(self.view):
                if i not in check_BIN:
                    correct = False
                    break

        return correct

    def send_HEX(self):
        if self.check_datatype() == False:
            messagebox.showinfo(title="Error", message="There is invalid symbol in the value")
        else:
            if self.datatype == "DEC":
                self.view = hex(int(self.view))[2:].upper()
            elif self.datatype == "OCT":
                self.view = hex(int(self.view, 8))[2:].upper()
            elif self.datatype == "BIN":
                self.view = hex(int(self.view, 2))[2:].upper()

            self.datatype = "HEX"
            self.display.config(text=self.view)

    def send_DEC(self):
        if self.check_datatype() == False:
            messagebox.showinfo(title="Error", message="There is invalid symbol in the value")
        else:
            if self.datatype == "HEX":
                self.view = int(str(self.view), 16)
            elif self.datatype == "OCT":
                self.view = int(self.view, 8)
            elif self.datatype == "BIN":
                self.view = int(str(self.view), 2)

            self.datatype = "DEC"
            self.display.config(text=self.view)

    def send_OCT(self):
        if self.check_datatype() == False:
            messagebox.showinfo(title="Error", message="There is invalid symbol in the value")
        else:
            if self.datatype == "HEX":
                self.view = oct(int(self.view, 16))[2:]
            elif self.datatype == "DEC":
                self.view = oct(int(self.view))[2:]
            elif self.datatype == "BIN":
                self.view =oct(int(self.view, 2))[2:]

            self.datatype = "OCT"
            self.display.config(text=self.view)

    def send_BIN(self):
        if self.check_datatype() == False:
            messagebox.showinfo(title="Error", message="There is invalid symbol in the value")
        else:
            if self.datatype == "HEX":
                self.view = bin(int(self.view, 16))[2:]
            elif self.datatype == "DEC":
                self.view = bin(int(self.view))[2:]
            elif self.datatype == "OCT":
                self.view = bin(int(self.view, 8))[2:]

            self.datatype = "BIN"
            self.display.config(text=self.view)

Main()