# ************************************************************************
# Programmed by: Sophia Queen Lim
# Date Submitted: May 2024
# ************************************************************************


# Import the tkinter module so that all the necessary code/ classes/ functions/ programs can be used from the
# tkinter library
from tkinter import *


# Make a def function on whenever the button is 'clicked'
def clicked():
    # Get the entered text in the Entry widget
    str_name = ent.get()

    # If the gotten input from the entry widget is none/ nothing is returned
    if str_name == "":

        # Configure the Entry widget color to be red through the code (bg="red")
        ent.config(bg="red")
    else:
        # Configure the Entry widget color to be white through the code (bg="white")
        ent.config(bg="white")

        # Make it so that the entered text is also shown in the label text
        hello["text"] = str_name

        # Get the current setting of the "text" of the button and confirms if it is "Copy Text" or not
        if bnt.cget("text") == "Copy Text":

            # Set the text displayed in the button from 'Copy Text' to 'Clear Text'
            bnt.config(text="Clear Text")

        # if the current setting of the "text" is "Clear Text instead of "Copy Text"
        else:
            # Clear the Entry widget after copying the text
            ent.delete(0, END)
            # Set the text displayed in the button from 'Clear Text' to 'Copy Text'
            bnt.config(text="Copy Text")


# Initialize the Main window
Exe_2C = Tk()

# Set the title of the window into 'GUI Example 2C'
Exe_2C.title("GUI Example 2C")

# Set the window size into 220 pixels in width and 110 pixels in height
Exe_2C.geometry('220x110')

# Making of the Entry widget
ent = Entry(Exe_2C)

# Place the position of the text in window with the coordinates of 50 in the x-axis and 30 in the y-axis
ent.place(x=50, y=30)

# Making of the button, it is assigned a text displayed and its command
# The text that is written in the button is 'Copy Text'
# The command=clicked is calling upon the def clicked function so that whenever the button is 'clicked'
# the following code in the def clicked function is run
bnt = Button(Exe_2C, text="Copy Text", command=clicked)

# Place the position of the text in window with the coordinates of 80 in the x-axis and 50 in the y-axis
bnt.place(x=80, y=50)

# Set the Label to be empty, to be filled by the def clicked function once called upon, hence the text=""
hello = Label(Exe_2C, text="")

# Place the position of the text in window with the coordinates of 50 in the x-axis and 80 in the y-axis
hello.place(x=50, y=80)

# Initiate the main loop program
Exe_2C.mainloop()
