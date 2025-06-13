# ************************************************************************
# Programmed by: Sophia Queen Lim
# Date Submitted: May 2024
# ************************************************************************


# Import the tkinter module so that all the necessary code/ classes/ functions/ programs can be used from the
# tkinter library
from tkinter import *


# Make a def function on whenever the button is 'clicked'
def clicked():
    # Changed the output printed from "Clicked" to "Played"
    print("Played")


# Create a main frame with
# --- a title
# ---size 200 by 200 pixels
Exe_1B = Tk()

# Changed the title from "GUI Example 1" to "Playlist"
Exe_1B.title("Playlist")

# Changed the pixel size from "200x200" to "800x500"
Exe_1B.geometry('800x500')

# Create the button with
# --- suitable text
# --- a command to call when the button is pressed
button1 = Button(Exe_1B, text="Play Here", command=clicked)

# Changed the position of the button from "bottom" to "top"
# Make the button visible at the top of the frame
button1.pack(side='top')

# Start the application running
Exe_1B.mainloop()
