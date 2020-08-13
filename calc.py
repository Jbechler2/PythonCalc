from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

leftnum = None
rightnum = None
operand = ''

def button_click(new_char):
    current = e.get()

    if(current == ''):
        if(new_char == '.'):
            e.insert(0, '0.')
        else:
            e.insert(0, str(new_char))
    else:
        if(new_char != '.' or current.find('.') == -1):
            e.delete(0, END)
            e.insert(0, str(current) + str(new_char))

        
#    if(current != '0.0' and (new_char != '.' or current.find('.') == -1)):
#        e.delete(0, END)
#        e.insert(0, str(current) + str(new_char))
#    elif(new_char == '.' and current == ''):
#        e.delete(0, END)
#        e.insert(0, '0.0')
#    elif(current == '0.0'):
#        e.delete(0, END)
#        e.insert(0, '0.' + str(new_char))


def clear_screen():
    e.delete(0, 'end')

def clear_all():
    global leftnum
    global rightnum

    e.delete(0, END)
    leftnum = None
    rightnum = None
    operand = ''

def oper_click(oper):
    get_leftnum()
    e.delete(0, END)
    set_oper(oper)

def set_oper(oper):
    global operand
    operand = oper

def get_leftnum():
    global leftnum
    if(e.get() != "" and e.get() != "None"):
        leftnum = float(e.get())

def get_rightnum():
    global rightnum
    if(e.get() != "" and e.get() != "None"):
        rightnum = float(e.get())

def run_calc():
    if(leftnum != None and rightnum != None):
        if(operand == "+"):
            return float(leftnum) + float(rightnum)
        if(operand == "-"):
            return float(leftnum) - float(rightnum)
        if(operand == "*"):
            return float(leftnum) * float(rightnum)
        if(operand == "/"):
            return float(leftnum) / float(rightnum)

def print_nums():
    print(leftnum)
    print(rightnum)

def clear_lro():
    global leftnum
    global rightnum
    global operand
    leftnum = None
    rightnum = None
    operand = ''

# clicking equals twice, then operand, then equals causes operand to run again

def button_equal():
    get_rightnum()
    if(operand != ''):
        e.delete(0, END)
        result = str(run_calc())
        clear_lro()
        if(result != "None"):
            e.insert(0, str(result))

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
btndot = Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."))

 # add operands

btnAdd = Button(root, text="+", padx=39, pady=10, command=lambda: oper_click("+"))
btnMult = Button(root, text="*", padx=39, pady=10, command=lambda: oper_click("*"))
btnDiv = Button(root, text="/", padx=39, pady=10, command=lambda: oper_click("/")) 
btnMin = Button(root, text="-", padx=39, pady=10, command=lambda: oper_click("-"))

 # add functional

btnEqual = Button(root, text="=", padx=38, pady=50, command=button_equal)
btnClear = Button(root, text="Clear", padx=79, pady=10, command=clear_screen)
btnClearAll = Button(root, text="CE", padx=40, pady=20, command=clear_all)

# put buttons on screen

btnClear.grid(row=1, column=1, columnspan=2)
btnClearAll.grid(row=1, column=0)

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
btndot.grid(row=7, column=0)

root.mainloop()
