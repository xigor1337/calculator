import tkinter as tk
from tkinter import messagebox

class main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Calculator")

        # top bar functions
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Force Close", command=exit)

        self.menubar.add_cascade(menu=self.filemenu, label="File")

        self.root.config(menu=self.menubar)

        # calculator
        # display
        self.view = ""
        self.display = tk.Label(text="")
        self.display.pack(pady=10)

        # buttons
        self.calc = tk.Frame(self.root)
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
        self.btn = tk.Button(self.calc, text=text, command=command)
        self.btn.grid(row=row, column=col, sticky=tk.W + tk.E)

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
        if self.view[0].isdecimal() == False or self.view[-1].isdecimal() == False:
            messagebox.showinfo(title="Error", message="Calculation must start and end with a number")
        else:
            # change to list
            current_numer = ""
            list = []
            for object in self.view:
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

main()