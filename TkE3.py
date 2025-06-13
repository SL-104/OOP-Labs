# ************************************************************************
# Programmed by: Sophia Queen Lim
# Date Submitted: May 2024
# ************************************************************************


# Import the tkinter module so that all the necessary code/ classes/ functions/ programs can be used from the
# tkinter library
from tkinter import *

# Create the main window
Exe_3B = Tk()
# Set the title of the window into 'GUI Example 3B'
Exe_3B.title("GUI Example 3B")
# Set the window size into 350 pixels in width and 200 pixels in height
Exe_3B.geometry("375x200")

# Make a grid and configure it to make the frames expand whenever resized
# Grid on the row
Exe_3B.grid_rowconfigure(0, weight=1)
Exe_3B.grid_rowconfigure(1, weight=1)
# Grid on the column
Exe_3B.grid_columnconfigure(0, weight=1)
Exe_3B.grid_columnconfigure(1, weight=1)

# Create frames for each group
# relief="sunken" 'sunken' the label with the thickness of 3 pixels
A_B = Frame(Exe_3B, bd=3, relief="sunken")
C_D = Frame(Exe_3B, bd=3, relief="sunken")

# Place frame groups in a 2x2 grid, A and B at the left and C and D at the right
A_B.grid(row=0, column=0, rowspan=2, sticky="nsew")
C_D.grid(row=0, column=1, rowspan=2, sticky="nsew")

# Create the labels A, B, C, and D and put them to their respective groups
# fill=BOTH, fills entirety of the space so that there are no white spaces

# Label A is put at group A_B and its background color is blue
A = Label(A_B, text="A", bg="blue")
# When the window is resized the label expands and fill the window in tandem
A.pack(expand=True, fill=BOTH)

# Label B is put at group A_B and its background color is white
B = Label(A_B, text="B", bg="white")
# When the window is resized the label expands and fill the window in tandem
B.pack(expand=True, fill=BOTH)

# Label C is put at group C_D and its background color is white
C = Label(C_D, text="C", bg="white")
# When the window is resized the label expands and fill the window in tandem
C.pack(expand=True, fill=BOTH)

# Label D is put at group C_D and its background color is blue
D = Label(C_D, text="D", bg="blue")
# When the window is resized the label expands and fill the window in tandem
D.pack(expand=True, fill=BOTH)

# Initiate the main loop program
Exe_3B.mainloop()
