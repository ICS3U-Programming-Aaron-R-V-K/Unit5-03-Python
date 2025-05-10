# !/usr/bin/env python3
# Created By: Aaron Rivelino
# Date: May 05, 2025
# The program uses a function to calculate
# the user grade based on the user grade level
# It uses return, to return the value


# define the grade level function
def calc_mark(level):
    # IF statement for each level using if...elif statements
    # returning the corresponding value for the level
    if level == "4+":
        return 98
    elif level == "4":
        return 90
    elif level == "4-":
        return 83
    elif level == "3+":
        return 78
    elif level == "3":
        return 75
    elif level == "3-":
        return 71
    elif level == "2+":
        return 68
    elif level == "2":
        return 65
    elif level == "2-":
        return 61
    elif level == "1+":
        return 58
    elif level == "1":
        return 55
    elif level == "1-":
        return 51
    elif level == "0":
        return 50
    # else statement returning -1, for Invalid input
    else:
        return -1


def main():
    # Get user input as a string
    level_as_str = input("Enter your grade level: ")

    # Call the function  and store the value in a variable
    calc_grade = calc_mark(level_as_str)

    # If statement for any Invalid input
    if calc_grade == -1:
        print("Invalid input")

    # Displaying the grade
    else:
        print("Your grade is {}".format(calc_grade))


if __name__ == "__main__":
    main()
