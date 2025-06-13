# ************************************************************************
# Programmed by: Sophia Queen Lim
# Date Submitted: May 2024
# ************************************************************************


# Import the tkinter module so that all the necessary code/ classes/ functions/ programs can be used from the
# tkinter library
from tkinter import *

# Initialize the Main window
Exe_6 = Tk()

# Set the window size into 200 pixels in width and 150 pixels in height
Exe_6.geometry("200x150")


# Make a def function on whenever a radio button is 'clicked'
def clicked():
    # The value of the radio is the order they are presented in the window (radio.get() == 1, is the first/ top
    # radio button presented in the window
    if radio.get() == 1:

        # Assign the text of that will be presented once the radio button is 'clicked', the background of the text
        # will also be changed in correlation with its text
        hello = Label(Exe_6, text="You selected the option 1", bg="red")

        # Place the position of the text in window with the coordinates of 20 in the x-axis and 125 in the y-axis
        hello.place(x=20, y=125)

    # Repeat the following with the remaining 2 radio buttons and assign it with its respective text
    # and background color

    # For the 2nd radio button the text is 'You selected the option 2' and the background is 'green2'
    # The coordinates is the same as the 1st radio button
    elif radio.get() == 2:
        hello = Label(Exe_6, text="You selected the option 2", bg="green2")
        hello.place(x=20, y=125)

    # For the 3rd radio button the text is 'You selected the option 3' and the background is 'dodger blue'
    # The coordinates is the same as the 1st radio button
    elif radio.get() == 3:
        hello = Label(Exe_6, text="You selected the option 3", bg="dodger blue")
        hello.place(x=20, y=125)

    # For the 4th radio button the text is 'You selected the option 4' and the background is 'purple1'
    # The coordinates is the same as the 1st radio button
    elif radio.get() == 4:
        hello = Label(Exe_6, text="You selected the option 4", bg="purple1")
        hello.place(x=20, y=125)

    # For the 5th radio button the text is 'You selected the option 5' and the background is 'yellow'
    # The coordinates is the same as the 1st radio button
    elif radio.get() == 5:
        hello = Label(Exe_6, text="You selected the option 5", bg="yellow")
        hello.place(x=20, y=125)


# IntVar is used to hold integer values. It will store the value of the selected radio button. The IntVar is used when
# we call upon the radio.get() == 1, this is for arrangement and for easy calling so instead of individually coding the
# radio button we can simply call upon their respective assigned number
radio = IntVar()

# Making of the respective radio buttons
# Each radio button is assigned a text displayed, its variable, its value, and its command
# The value="1" is assigning the radio button's respective value to be called upon
# The command=clicked is calling upon the def clicked function so that whenever the radio button is 'clicked'
# the following code in the def clicked function is run

# radio_1 has the text of "Red" and the value of "1"
radio_1 = Radiobutton(Exe_6, text="Red", variable=radio, value="1", command=clicked)

# Place the position of the text in window with the coordinates of 10 in the x-axis and 0 in the y-axis
radio_1.place(x=10, y=0)


# radio_2 has the text of "Green" and the value of "2"
radio_2 = Radiobutton(Exe_6, text="Green", variable=radio, value="2", command=clicked)

# Place the position of the text in window with the coordinates of 10 in the x-axis and 25 in the y-axis,
# slightly lower than the 1st radio button
radio_2.place(x=10, y=25)


# radio_3 has the text of "Blue" and the value of "3"
radio_3 = Radiobutton(Exe_6, text="Blue", variable=radio, value="3", command=clicked)

# Place the position of the text in window with the coordinates of 10 in the x-axis and 50 in the y-axis,
# slightly lower than the 2nd radio button
radio_3.place(x=10, y=50)


# radio_4 has the text of "Purple" and the value of "4"
radio_4 = Radiobutton(Exe_6, text="Purple", variable=radio, value="4", command=clicked)

# Place the position of the text in window with the coordinates of 10 in the x-axis and 75 in the y-axis,
# slightly lower than the 3rd radio button
radio_4.place(x=10, y=75)


# radio_5 has the text of "Yellow" and the value of "5"
radio_5 = Radiobutton(Exe_6, text="Yellow", variable=radio, value="5", command=clicked)

# Place the position of the text in window with the coordinates of 10 in the x-axis and 100 in the y-axis,
# slightly lower than the 4th radio button
radio_5.place(x=10, y=100)


# Initiate the main loop program
Exe_6.mainloop()
