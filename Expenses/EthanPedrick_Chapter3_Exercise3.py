# This program takes a list of monthly expenses, as submitted by the user, and returns the highest, lowest, and total expenses. Ethan Pedrick, Chapter 3, Exercise 3

from functools import reduce

EXPENSES = {}

def main():
    print("This program gives data about your monthly expenses.")

    compileExpenses()

    # outputs the key for the highest value and lowest values
    lowest = min(EXPENSES, key=EXPENSES.get)
    highest = max(EXPENSES, key=EXPENSES.get)

    # adds all EXPENSE values using reduce function
    total = reduce(lambda x, y: x + y, EXPENSES.values())

    # If two expenses are equal, it chooses the first one that occured; thus is the nature of the min and max functions.
    print(f"-------------------------------\nYour expenses cost you ${total} monthly.\n\nYour highest expense is {highest} at ${EXPENSES.get(highest)}.\n\nYour lowest expense is {lowest} at ${EXPENSES.get(lowest)}.")

# This function deals with all inputs, and puts them in a dictionary.
def compileExpenses():

    # "done" is somewhat of a placeholder. This is only done so it loops indefinitely until the user enters something specific.
    # Obviously, I could do this with a function that calls itself, but I would rather not do that.
    # If this is wrong, please let me know.
    x = ""
    while x != "done":

        # Resetting variables
        cost = ""
        x = ""

        # Get the name of the expense in question.
        x = input("Input the name of one of your expenses. Repeat names will overwrite the previous expense. If there are no more, input 'done'. ")

        # Stop the loop if the user enters "done"
        if x.lower() == "done":
            break

        # Ensure what the user enters is a number. Float is used in case they choose to use cents.
        # Another loop is used here until they enter the correct type of value.
        while cost == "":
            try:
                cost = float(input("Input the monthly cost of the previously entered expense. "))
            except (ValueError):
                print("Your input must be a number. Please try again.")

        # Add the name of expense and its cost to the dictionary and continue the loop.
        EXPENSES.update({x: cost})


main()