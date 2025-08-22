from tkinter import *
from time import strftime

# Create the main window
root = Tk()
root.title("Digital Clock")

# Customize the clock appearance
label = Label(root, font=("Arial", 60), background="black", foreground="cyan")
label.pack(anchor="center")

# Function to update time
def time():
    current_time = strftime('%H:%M:%S')  # Get current time in hours:minutes:seconds
    label.config(text=current_time)      # Set time on the label
    label.after(1000, time)              # Update every 1000 milliseconds (1 second)

time()  # Call the function once to start
root.mainloop()  # Run the GUI
