# ************************************************************************
# Programmed by: Sophia Queen D. Lim
# Date Submitted: April 6, 2024
# ************************************************************************

# create class for COLORS, used for aesthetic purposes within the code.
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"


# Create the definitions of arithmetic operations
# Print what the chosen operation is
# Initiate the required operation, for example {num1 +num2}
def addition(num1, num2):
    print("\nYou have picked the ADDITION operation\n"
          f"The sum of your given numbers is: {num1 + num2}")


def subtraction(num1, num2):
    print("\nYou have picked the SUBTRACTION operation\n"
          f"The difference of your given numbers is: {num1 - num2}")


def multiplication(num1, num2):
    print("\nYou have picked the MULTIPLICATION operation\n"
          f"The product of your given numbers is: {num1 * num2}")


def division(num1, num2):
    try:
        print("\nYou have picked the DIVISION operation\n"
              f"The quotient of your given numbers is: {num1 / num2}")

    # Initiating the ZeroDivisionError when cases like 1/0 arises where there is no answer for it
    except ZeroDivisionError:
        print(f"{Colors.RED}\n<Error>\n{Colors.RESET}\n>Can't divide by zero<")


# Used for asking if the user would like to use the calculator once again
def again():
    while True:
        use_again = input("\nWould you like to use the calculator again? (Yes/No): ").upper()
        if use_again == "YES" or use_again == "Y":

            # Opening the fun() def function, for initiating the whole program from the top
            fun()
        elif use_again == "NO" or use_again == "N":
            print("Thank you!")

            # Ending the loop and program
            break

        # Making the user input the proper input (Yes/No) so that the program can proceed
        else:
            print("Invalid input. Please enter either 'Yes' or 'No'.")


# Create a def function for the choosing process and also the initiation of the respective operations
def fun():

    # Initiate a while function
    while True:
        try:
            print(">>SIMPLE CALCULATOR<<\nPlease pick an operation"
                  "\n<1> ADDITION\n<2> SUBTRACTION\n<3> MULTIPLICATION\n<4> DIVISION")

            # Create input for choosing an operation
            user_choice = input("Enter your choice(1, 2, 3, 4): ")

            # If the user inputted a number, but it is not among the following (1,2,3,4) then it will go straight to the
            # ValueError (raise ValueError) where it states that the user sis not input one of the right options
            if user_choice not in ["1", "2", "3", "4"]:
                raise ValueError

            # This is for the number inputs, initiate a while function
            while True:

                # Initiate try function so that ValueError can be used
                try:
                    num1 = float(input("Enter the first number: "))
                    break

                # Show an error message making the user know that they did not input a number and
                # making them input a valid number
                except ValueError:
                    print(f"{Colors.RED}\n<Error>\n{Colors.RESET}\n"
                          f"Invalid input for the first number. Please enter a valid number.")

            while True:

                # Initiate try function so that ValueError can be used
                try:
                    num2 = float(input("Enter the second number: "))
                    break

                # Show an error message making the user know that they did not input a number and
                # making them input a valid number
                except ValueError:
                    print(f"{Colors.RED}\n<Error>\n{Colors.RESET}\n"
                          f"Invalid input for the second number. Please enter a valid number.")

            # If loop for when the user chooses either 1, 2, 3, or 4
            # The respective operation is done when its respective number is picked
            # break is for ending the loop
            if user_choice == "1":
                addition(num1, num2)

            elif user_choice == "2":
                subtraction(num1, num2)
                break

            elif user_choice == "3":
                multiplication(num1, num2)
                break

            elif user_choice == "4":
                division(num1, num2)
                break
            # End loop
            break

        # If the user did not input a number or any of the options
        # the error message will appear and will make the user input again
        except ValueError:
            print(f"{Colors.RED}\n<Error>\n{Colors.RESET}\nPlease input one of the right options\n")


# Combine the two def function created for easy management, this is the main program
def main():
    fun()
    again()


# Initiate the main program
main()
