import tkinter as tk

# Create a blank window
root = tk.Tk()
root.title("Simple Paint App")

# Create a Canvas (drawing area)
canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

# Variable to store old mouse position
old_x = None
old_y = None

# Brush settings
brush_color = "black"
brush_size = 3

# When mouse is moved while pressed (draw line)
def draw(event):
    global old_x, old_y
    if old_x and old_y:
        canvas.create_line(old_x, old_y, event.x, event.y,
                           width=brush_size, fill=brush_color,
                           capstyle=tk.ROUND, smooth=True)
    old_x = event.x
    old_y = event.y

# When mouse is released (reset position)
def reset(event):
    global old_x, old_y
    old_x = None
    old_y = None

# Clear the canvas
def clear_canvas():
    canvas.delete("all")

# Add clear button
clear_btn = tk.Button(root, text="Clear", command=clear_canvas)
clear_btn.pack()

# Bind mouse events
canvas.bind("<B1-Motion>", draw)   # Left click & drag
canvas.bind("<ButtonRelease-1>", reset)

# Run the app
root.mainloop()
