
import os

def main():

    # If the file exists, it will be opened. Otherwise, the file is created, then opened.
    try:
        f = open("data.txt", "r")
    except FileNotFoundError:
        create_file()
        f = open("data.txt", "r")

    # Grabs the amount of tickets available for use in the program.
    tickets = int(f.readline())

    # If there are more than 0
    if tickets > 0:

        wanted = ""

        # loops as many times as the user fails to input a proper number
        while wanted == "":
            try:
                wanted = int(input(f"How many tickets would you like to buy?\nCurrent stock: {tickets} "))
                print(wanted)
            except ValueError:
                print("Your input must be an integer.")

        # If the amount of wanted tickets is in stock, is less than 4, and is more than 0, continue
        if (wanted <= tickets) & (4 >= wanted) & (wanted > 0):

            # increment here
            tickets -= wanted

            # update file with new data
            update_file(tickets, f)

            # close file
            f.close()

            # Restart in case the customer would like to buy again.
            print(f"You have successfully purchased {wanted} tickets!")
            main()

        # If the customer decides they don't want to buy any tickets, close the program.
        elif wanted == 0:
            f.close()
            return

        else:
            print(f"Tickets are limited to a maximum of 4 per customer, and our current stock is {tickets}. Try again.")
            f.close()
            main()

    else:
        f.close()
        out_of_stock()




# Creates a new file with reset data (20 tickets, 0 buyers)
def create_file():

    # Delete the file if it exists
    if os.path.exists("data.txt"):
        os.remove("data.txt")

    # Recreate and set the data
    f = open("data.txt", "w")
    f.write("20 \n0")
    f.close()

# Updates file with new data
def update_file(tickets, f):

    # gets current amount of buyers
    buyers = int(f.readline(1))
    buyers += 1
    f.close()
    fwrite = open("data.txt", "w")
    fwrite.write(f"{tickets}\n{buyers}")
    fwrite.close()

# If there are no tickets left to buy, return the data, and allow for a devreset.
def out_of_stock():
    checkforreset = input("We are currently out of stock. Press ENTER to return.")
    f = open("data.txt", "r")
    buyers = f.readline(1)
    print(f"There were {buyers} ticket buyers!")
    f.close()
    if checkforreset == "devreset":
        create_file()
        print("Reset Successful.")

main()