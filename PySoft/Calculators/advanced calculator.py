import tkinter as tk
from math import *
import time
print('*****|Advanced Calculator|*****')
print('Program version: 1.11.2.')
print('')
print('This is an advanced calculator coded in Python! You can check the basic version of it from: https://github.com/GamerSoft24/Python/blob/Main/PySoft/basic%20calculator.py')
print("You can either type the numbers & caracters in or click the buttons.")
time.sleep(3)
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def calculate_sqrt():
    current = entry.get()
    try:
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_enter(event):
    calculate()

window = tk.Tk()
window.title("Advanced Calculator")

entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6)

buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'sqrt',
    '(', ')', 'AC', 'ln', 'log'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button == 'sqrt':
        tk.Button(window, text=button, padx=20, pady=20, command=calculate_sqrt).grid(row=row_val, column=col_val)
    elif button == 'AC':
        tk.Button(window, text=button, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

for i in range(5):
    window.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    window.grid_rowconfigure(i, weight=1)

entry.bind('<Return>', on_enter)

window.mainloop()
