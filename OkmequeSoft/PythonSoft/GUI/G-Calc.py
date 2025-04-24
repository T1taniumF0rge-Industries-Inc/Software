import tkinter as tk
from tkinter import *
from tkinter import messagebox
def addition(num1,num2):
    try:
        add1 = float(num1)
        add2 = float(num2)
        addresult = add1 + add2
        returnstring = str(addresult)
        result.delete("1.0",END)
        result.insert(END,returnstring)
        return
    except ValueError:
        x = messagebox.showerror("G-Calc","Addition failed.Enter a valid number(2,45,67575) and try again\nError code : 0211")
        return
    except BaseException:
        x = messagebox.showerror("G-Calc","Addition failed.Check parameters and try again\nError code : 770A")
        return
def subtraction(num1,num2):
    try:
        sub1 = float(num1)
        sub2 = float(num2)
        subresult = sub1 - sub2
        returnstring = str(subresult)
        result.delete("1.0",END)
        result.insert(END,returnstring)
        return
    except ValueError:
        x = messagebox.showerror("G-Calc","Subtraction failed.Enter a valid number(2,45,67575) and try again\nError code : 0211")
        return
    except BaseException:
        x = messagebox.showerror("G-Calc","Subtraction failed.Check parameters and try again\nError code : 770A")
        return
def multiplication(num1,num2):
    try:
        mul1 = float(num1)
        mul2 = float(num2)
        mulresult = mul1 * mul2
        returnstring = str(mulresult)
        result.delete("1.0",END)
        result.insert(END,returnstring)
        return
    except ValueError:
        x = messagebox.showerror("G-Calc","Multiplication failed.Enter a valid number(2,45,67575) and try again\nError code : 0211")
        return
    except BaseException:
        x = messagebox.showerror("G-Calc","Multiplication failed.Check parameters and try again\nError code : 770A")
        return
def division(num1,num2):
    try:
        div1 = float(num1)
        div2 = float(num2)
        addresult = div1 / div2
        returnstring = str(addresult)
        result.delete("1.0",END)
        result.insert(END,returnstring)
        return
    except ValueError:
        x = messagebox.showerror("G-Calc","Division failed.Enter a valid number(2,45,67575) and try again\nError code : 0211")
        return
    except ZeroDivisionError:
        x = messagebox.showerror("G-Calc","Division by 0 not allowed.\nError code : 0255")
    except BaseException:
        x = messagebox.showerror("G-Calc","Division failed.Check parameters and try again\nError code : 770A")
        return
windows = Tk()
windows.title("G-Calc")
windows.geometry("200x240")
l1 = Label(windows,text="NUM1 : ")
e1 = Entry(windows,width=10)
l2 = Label(windows,text="NUM2 : ")
e2 = Entry(windows,width=10)
add = Button(windows,text="+",width=10,command = lambda: addition(e1.get(),e2.get()))
sub = Button(windows,text="-",width=10,command = lambda: subtraction(e1.get(),e2.get()))
mul = Button(windows,text="X",width=10,command = lambda: multiplication(e1.get(),e2.get()))
div = Button(windows,text="/",width=10,command = lambda: division(e1.get(),e2.get()))
l3 = Label(windows,text="↓ Result ↓")
result = Text(windows,height=1,width=23)
l1.pack()
e1.pack()
l2.pack()
e2.pack()
add.pack()
sub.pack()
mul.pack()
div.pack()
l3.pack()
result.pack()
windows.mainloop()
