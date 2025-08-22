from tkinter import *

# Create the main window
root = Tk()
root.title("Calculator")

# Entry widget to show the expression
entry = Entry(root, width=16, font=("Arial", 24), bd=10, relief=RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Function to handle button clicks
def click(symbol):
    entry.insert(END, symbol)

# Function to clear entry
def clear():
    entry.delete(0, END)

# Function to evaluate expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons and place them
for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, padx=30, pady=20, font=("Arial", 18), command=evaluate).grid(row=row, column=col)
    elif text == 'C':
        Button(root, text=text, padx=128, pady=20, font=("Arial", 18), command=clear).grid(row=row, column=col, columnspan=4)
    else:
        Button(root, text=text, padx=30, pady=20, font=("Arial", 18), command=lambda t=text: click(t)).grid(row=row, column=col)

# Run the GUI
root.mainloop()
