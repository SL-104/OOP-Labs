# ************************************************************************
# Programmed by: Sophia Queen Lim
# Date Submitted: April 21, 2024
# ************************************************************************


# This imports the math module, this includes several mathematical functions
import math


def square_root(number):
    # Checks if the number is positive or negative if number is < 0 then it is a negative because a negative
    # is lesser than 0
    if number < 0:
        # Initiate ValueError from the try function
        raise ValueError("Input is a negative number, the calculator cannot compute "
                         "the square root of a negative number.")
    # This calculates the square root of a number
    return math.sqrt(number)


try:
    # The digit variable inputs a number and that number will be turned into a float (e.g. 5.25)
    digit = float(input("Please enter a number: "))
    # Call upon the def of square_root and have it initiate on the digit variable
    sqrt_re = square_root(digit)

    # Opens a .txt file named sqrt_results.txt
    with open("sqrt_results.txt", 'w') as file_sqrt:
        # Writes on the .txt file the result of the calculation
        file_sqrt.write(f"Square root of {digit} is {sqrt_re}")

# Value Error for if the number is not a positive number
except ValueError as e_file:
    with open("sqrt_results.txt", 'w') as file_sqrt:
        file_sqrt.write(str(e_file) + "\nPlease input a positive number (e.g. 1, 2, 3, 4, 5)")



