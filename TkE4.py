# ************************************************************************
# Programmed by: Sophia Queen Lim
# Date Submitted: May 2024
# ************************************************************************


# Import the tkinter module so that all the necessary code/ classes/ functions/ programs can be used from the
# tkinter library
from tkinter import *

# Define the size of the square and circle
square_size = 55
circle_size = 55

# Initialize global variables so that they can be used when changing its assignment
# A variable for changing its shape, checking if it is filled or not, and changing its color
# I've set temporary holders for the variables to be changed depending on what key is pressed later on
shape = "shape"
filled = False
color = "white"
# Set the outline's width
outline_width = 5


# Make a def function where it is an event whenever the mouse is 'clicked' then it will receive the mouse's coordinates
def draw(event):
    # Get the variables through the global function
    global shape, filled, color, outline_width
    # Get the x and y coordinates of the mouse click
    x, y = event.x, event.y
    # Prints the coordinates/ where the mouse is clicked
    print(f"Mouse click at x = {event.x} y = {event.y}")
    # Calculate half the size of the shape (square and circle have the same size)
    half = square_size // 2

    # Check if the shape is returned as 'square'
    if shape == 'square':
        # Check if the filled is True
        if filled:
            # Draw a square with using the coordinates received and fill the inside to be the color that is
            # received/ assigned to it (Can be either be 'red' or 'yellow')
            canvas.create_rectangle(x - half, y - half, x + half, y + half, fill=color)
        # If filled is not true
        else:
            # Draw a square with using the coordinates received, with an outline of the chosen color
            canvas.create_rectangle(x - half, y - half, x + half, y + half, outline=color, width=outline_width)

    # Check if the shape is returned as 'circle'
    elif shape == 'circle':
        # Check if the filled is True
        if filled:
            # Draw a circle with using the coordinates received and fill the inside to be the color that is
            # received/ assigned to it (Can be either be 'red' or 'yellow')
            canvas.create_oval(x - half, y - half, x + half, y + half, fill=color)
        # If filled is not true
        else:
            # Draw a circle with using the coordinates received, with an outline of the chosen color
            canvas.create_oval(x - half, y - half, x + half, y + half, outline=color, width=outline_width)

# Make a def function that whenever a key specific is pressed
def key(event):
    # Get the variables through the global function
    global shape, filled, color, outline_width

    # if the key 's' is pressed
    if event.char == 's':
        # Let the shape be assigned to be 'square'
        shape = "square"
        # Print out "Lower case h key pressed" once the key 's' is pressed
        print("Lower case s key pressed")
    # if the key 'c' is pressed
    elif event.char == 'c':
        # Let the shape be assigned to be 'circle'
        shape = "circle"
        # Print out "Lower case h key pressed" once the key 'c' is pressed
        print("Lower case c key pressed")
    # if the key 'F' is pressed
    elif event.char == 'F':
        # Let the filled be assigned to be True
        filled = True
        # Print out "Lower case h key pressed" once the key 'F' is pressed
        print("Upper case F key pressed")
    # if the key 'f' is pressed
    elif event.char == 'f':
        # Let the filled be assigned to be False
        filled = False
        # Print out "Lower case h key pressed" once the key 'f' is pressed
        print("Lower case f key pressed")
    # if the key 'r' is pressed
    elif event.char == 'r':
        # Let the color be assigned to be 'red'
        color = "red"
        # Print out "Lower case h key pressed" once the key 'r' is pressed
        print("Lower case r key pressed")
    # if the key 'y' is pressed
    elif event.char == 'y':
        # Let the color be assigned to be 'yellow'
        color = 'yellow'
        # Print out "Lower case h key pressed" once the key 'y' is pressed
        print("Lower case y key pressed")


# Initialize the Main window
Exe_4B = Tk()
# Set the title of the window into 'GUI Example 4B'
Exe_4B.title("GUI Example 4B")
# Set the canvas size into 500 pixels in width and 500 pixels in height and make the color of the background to be blue
canvas = Canvas(Exe_4B, width=500, height=500, bg="blue")
# Add the canvas to the main window
canvas.pack()
# Bind the mouse click event to the draw function
canvas.bind("<Button-1>", draw)
# Bind the key press event to the key function
Exe_4B.bind("<Key>", key)

# Initiate the main loop program
Exe_4B.mainloop()
