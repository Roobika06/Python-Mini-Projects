import tkinter as tk
from tkinter import messagebox

# Create a window
window = tk.Tk()
window.title("Tic Tac Toe")

# Player turn variable
current_player = "X"

# 3x3 buttons (empty at start)
buttons = [[None for _ in range(3)] for _ in range(3)]

# Function to check for winner
def check_winner():
    for i in range(3):
        # Check rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        # Check columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

# Function to check for tie
def check_tie():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

# What happens when you click a button
def on_click(row, col):
    global current_player

    # If cell already filled, do nothing
    if buttons[row][col]["text"] != "":
        return

    # Set the button text to current player ("X" or "O")
    buttons[row][col]["text"] = current_player

    # Check winner
    if check_winner():
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        window.quit()

    # Check tie
    elif check_tie():
        messagebox.showinfo("Game Over", "It's a tie!")
        window.quit()

    # Change player
    current_player = "O" if current_player == "X" else "X"

# Create 3x3 buttons
for i in range(3):
    for j in range(3):
        button = tk.Button(window, text="", width=10, height=3,
                           font=("Arial", 20),
                           command=lambda row=i, col=j: on_click(row, col))
        button.grid(row=i, column=j)
        buttons[i][j] = button

# Run the app
window.mainloop()
