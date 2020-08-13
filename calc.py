from tkinter import *

root = Tk()
root.title("Simple Calculator")


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear_screen():
    e.delete(0, 'end')

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def get_operand(oper):
    global f_num 
    f_num = int(e.get())
    e.delete(0, END)
    global operand
    operand = oper


def run_calc(num1, num2):
    if(operand == "+"):
        return num1 + num2
    if(operand == "-"):
        return num1 - num2
    if(operand == "*"):
        return num1 * num2
    if(operand == "/"):
        return num1 / num2

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, int(run_calc(f_num, int(second_number))))

 # add numbers

btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

 # add operands

btnAdd = Button(root, text="+", padx=39, pady=10, command=lambda: get_operand("+"))
btnMult = Button(root, text="*", padx=39, pady=10, command=lambda: get_operand("*"))
btnDiv = Button(root, text="/", padx=39, pady=10, command=lambda: get_operand("/")) 
btnMin = Button(root, text="-", padx=39, pady=10, command=lambda: get_operand("-"))

 # add functional

btnEqual = Button(root, text="=", padx=38, pady=50, command=button_equal)
btnClear = Button(root, text="Clear", padx=79, pady=10, command=clear_screen)

# put buttons on screen

btnClear.grid(row=1, column=1, columnspan=2)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)

btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)

btn0.grid(row=5, column=0)
btnAdd.grid(row=5, column=1)
btnEqual.grid(row=5, column=2, rowspan=2)

btnMult.grid(row=6, column=0)
btnMin.grid(row=6, column=1)

btnDiv.grid(row=7, column=1)

root.mainloop()
