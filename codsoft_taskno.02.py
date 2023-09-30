from tkinter import *

def on_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, END)

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get()
        if expression:
            result = eval(expression)
            entry.delete(0, END)
            entry.insert(0, str(result))
        else:
            entry.delete(0, END)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

def clear_entry(event):
    entry.delete(0, END)

root = Tk()
root.title("Calculator App")
root.geometry("300x650")

bg_color = "#E0E0E0"
button_color = "#D1D1D1"

title_label = Label(root, text="Calculator", font=("Arial", 20))
title_label.grid(row=0, column=0, columnspan=4, pady=(10, 20), padx=10, sticky="w")

entry = Entry(root, width=10, font=("Arial", 28), bd=10, bg=bg_color, justify="right")
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
entry.bind("<FocusIn>", clear_entry)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val, col_val = 2, 0

for button in buttons:
    if button == '=':
        Button(root, text=button, padx=8, pady=20, font=("Arial", 18), command=calculate, bg=button_color).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    elif button == '0':
        Button(root, text=button, padx=8, pady=20, font=("Arial", 18), command=lambda num=button: on_click(num), bg=button_color).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    elif button == '.':
        Button(root, text=button, padx=8, pady=20, font=("Arial", 18), command=lambda num=button: on_click(num), bg=button_color).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    else:
        Button(root, text=button, padx=8, pady=20, font=("Arial", 18), command=lambda num=button: on_click(num), bg=button_color).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

Button(root, text="C", padx=8, pady=20, font=("Arial", 18), command=clear, bg=button_color).grid(row=row_val, column=0, padx=5, pady=5, sticky="nsew")

Button(root, text="<-", padx=8, pady=20, font=("Arial", 18), command=backspace, bg=button_color).grid(row=row_val, column=1, padx=5, pady=5, sticky="nsew")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
