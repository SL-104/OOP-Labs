# ************************************************************************
# Programmed by: Sophia Queen Lim
# Date Submitted: May 2024
# ************************************************************************


# Import the tkinter module so that all the necessary code/ classes/ functions/ programs can be used from the
# tkinter library
import tkinter as tk

# Import the functions needed from the tkinter library such as the messagebox and the filedialog
# messagebox - for displaying message boxes
# filedialog - for opening file dialogs
from tkinter import messagebox, filedialog

# Initialize global variables so that they can be used when changing its assignment
current_path = None
unsaved = False


# def function of file dialog
# def function whenever the menu of 'Open' that is under the 'File' is selected
def open_file():
    # Get the variables through the global function
    global current_path, unsaved
    # Check for unsaved changes
    if unsaved:
        save = messagebox.askyesnocancel("Unsaved Changes",
                                         "You have unsaved changes. Do you want to save them?")
        # Do nothing
        if save is None:
            return
        # Initiate the def save_file function
        elif save:
            save_file()

    # This will lead to the file explorer that allows you to select a file
    path = filedialog.askopenfilename()
    # Once a 'path' is selected, in this case a file
    if path:
        # Open the file and read the file
        with open(path, 'r') as file:
            content = file.read()
        # Have a message box that show the file's content
        messagebox.showinfo("File Content", f"Content: \n{content}")
        # Close the file
        file.close()
        # Update current file path and reset unsaved changes
        current_path = path
        unsaved = False


# def function for saving a file
def save_file():
    # Get the variables through the global function
    global current_path, unsaved

    # If there is no current path then show an error message
    if current_path is None:
        messagebox.showerror("Error", "No file is currently open.")
        return

    # Write content to the current file path
    with open(current_path, 'w') as file:
        # Show that the file can be saved here
        file.write("File content to be saved here")

    # Set it to be saved
    unsaved = False
    # Show that it has been saved successfully
    messagebox.showinfo("Information", "File saved successfully.")


# def function for quitting the program
def quit_program():
    # Get the variable through the global function
    global unsaved

    # Check if there are any unsaved changes
    if unsaved:
        save_changes = messagebox.askyesnocancel("Unsaved",
                                                 "You have unsaved changes. Do you want to save them?")
        # Do nothing
        if save_changes is None:
            return
        # Initiate the def save_file function
        elif save_changes:
            save_file()
    # Quit the window after saving
    Exe_5C.quit()


# def function for converting file content to uppercase
def edit_upper():
    # Get the variable through the global function
    global unsaved
    # This will lead to the file explorer that allows you to select a file
    if current_path is None:
        messagebox.showerror("Error", "No file is currently open.")
        return

    # Open the file and read the file
    with open(current_path, 'r') as file:
        content = file.read()
    # Convert the text within the file into uppercase letters
    up_content = content.upper()
    # Write the uppercase content back to the file
    with open(current_path, 'w') as file:
        file.write(up_content)
    unsaved = False
    # Have a message box that show the file's content now being in uppercase
    messagebox.showinfo("File Content in Uppercase", f"Content: \n{up_content}")


# def function of messagebox

# def function whenever the menu of 'About' that is under the 'Help' is selected
def message_box():
    messagebox.showinfo("Information", "You have called for help")


# def function whenever the menu of 'Option One' that is under the 'New-Menu' is selected
def message_for_one():
    # Get the variable through the global function
    global unsaved
    # Open the file and set it to write
    with open("Test_FILE.txt", 'w') as file:
        # Write on the opened file
        file.write("The one that got away")
    # Have a message box display the text
    messagebox.showinfo("Opened Option One", "You have selected Option 1, file successfully written")
    # Set unsaved changes to True
    unsaved = True


# def function whenever the menu of 'Option Two' that is under the 'New-Menu' is selected
def message_for_two():
    # Open the file and set it to read
    with open("Test_FILE.txt", 'r') as file:
        # Read the opened file
        content = file.read()
    # Have a message box display the text
    messagebox.showinfo("Opened Option Two", f"Option 2 has been selected \n\n '{content}'")


# def function whenever the menu of 'Option Three' that is under the 'New-Menu' is selected
def message_for_three():
    # Have a message box display the text
    messagebox.showinfo("Opened Option Three", "Third times a charm")


# Make a def function that creates the menus, the 'File', 'Help', 'Edit', and 'New-Menu'
def menus(event):
    see_menu = tk.Menu(event)

    # File Menu
    # Have three under it, the 'Open', 'Save', and the 'Exit' menus
    # Make the menu not be 'torn off'/ be a standard drop down menu
    file_menu = tk.Menu(see_menu, tearoff=0)
    # Create the Open menu and when selected it will run the def open_file function
    file_menu.add_command(label="Open", command=open_file)
    # Create the Save menu and when selected it will run the def save_file function
    file_menu.add_command(label="Save", command=save_file)
    # Separated by a separator
    file_menu.add_separator()
    # Create the Quit menu and when selected it will run the def quit_program function
    file_menu.add_command(label="Quit", command=quit_program)
    # Create the Main menu 'File'
    see_menu.add_cascade(label="File", menu=file_menu)

    # Edit Menu
    # Have one under it, the 'Edit to Uppercase' menu
    # Make the menu not be 'torn off'/ be a standard drop down menu
    edit_menu = tk.Menu(see_menu, tearoff=0)
    # Create the Edit to Uppercase menu and when selected it will run the def edit_upper function
    edit_menu.add_command(label="Edit to Uppercase", command=edit_upper)
    # Create the Main menu 'Edit'
    see_menu.add_cascade(label="Edit", menu=edit_menu)

    # Help Menu
    # Have one under it, the About menu
    # Make the menu not be 'torn off'/ be a standard drop down menu
    help_menu = tk.Menu(see_menu, tearoff=0)
    # Create the About menu and when selected it show the contents of the message_box function
    help_menu.add_command(label="About", command=message_box)
    # Create the Main menu 'Help'
    see_menu.add_cascade(label="Help", menu=help_menu)

    # New Menu
    # Have one under it, the 'Option One', 'Option Two', and 'Option Three' menus
    # Make the menu not be 'torn off'/ be a standard drop down menu
    new_menu = tk.Menu(see_menu, tearoff=0)
    # Create the Option One menu and when selected it show the contents of the message_for_one function
    new_menu.add_command(label="Option One", command=message_for_one)
    # Separated by a separator
    new_menu.add_separator()
    # Create the Option Two menu and when selected it show the contents of the message_for_two function
    new_menu.add_command(label="Option Two", command=message_for_two)
    # Separated by a separator
    new_menu.add_separator()
    # Create the Option Three menu and when selected it show the contents of the message_for_three function
    new_menu.add_command(label="Option Three", command=message_for_three)
    # Create the Main menu 'New-Menu'
    see_menu.add_cascade(label="New-Menu", menu=new_menu)

    # Make the 'see_menu' be the menu bar seen in the window
    event.config(menu=see_menu)


# Make the def function for the main window seen
def main():
    global Exe_5C
    # Create the main window
    Exe_5C = tk.Tk()
    # Set the title of the window into 'GUI Example'
    Exe_5C.title("GUI Example")
    # Set the window size into 400 pixels in width and 300 pixels in height
    Exe_5C.geometry("400x300")
    # Create the menus
    menus(Exe_5C)
    # Initiate the main loop program
    Exe_5C.mainloop()


# Initiate the main def function/ run the program
main()
