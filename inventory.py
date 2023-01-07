# importing tabulate to make a table for the view all function
from tabulate import tabulate

#========The beginning of the class==========

# defining the shoe class
class Shoe:

    # creating a class definition for Shoe and initialising the data
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # getting the cost of the shoes
    def get_cost(self):
        return self.cost

    # getting the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # returning a string representation of the class
    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

#=============Shoe list===========

# creating a list to store a list of shoe objects
shoe_list = []

#==========Functions outside the class==============

# defining a function to read from the file
def read_shoes_data():

    # trying to open the file
    try:
        with open("inventory.txt", "r") as file:

            # skipping the first line as this will interfere with the data
            next(file)

            # for each line in the file
            for line in file:

                # creating variables to store the data in the correct area
                country, code, product, cost, quantity = line.strip().split(",")
                cost = float(cost)
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)

                # adding the data stored in the shoe variable to the shoe list
                shoe_list.append(shoe)
        
        # closing the file
        file.close()
    
    # unless any errors occur then create an exception printing an error message
    except Exception as x:
        print(f"There was a problem reading the data: {x}")

# defining a function to get new shoes
def capture_shoes():

    # asking the user to input the information about the new shoes
    country = input("Enter the country of origin: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))

    # creating a variable to store all of the data recieved from the user and adding it to the shoe list
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe added successfully")

# defining a function to view all of the data
def view_all():
    read_shoes_data()

    # if there is no data printing an appropriate error message
    if not shoe_list:
        print("No shoes in the inventory")
        return

    # storing the data for the shoes 
    data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]

    # generating the table using the tabulate function
    table = tabulate(data, headers=["Country", "Code", "Product", "Cost", "Quantity"])

    # printing the table
    print(table)

# defining a function to re-stock the least numerous shoe
def re_stock():
    read_shoes_data()

    # if there is no data printing an appropriate error message
    if not shoe_list:
        print("No shoes in the inventory")
        return

    # finding the least numerous shoe
    least_numerous_shoe = min(shoe_list, key=get_quantity)

    # asking the user how much they would like to add to the quantity of this shoe
    user_input = int(input(f"Enter the amount to add to {least_numerous_shoe.product}: "))

    # adding the user_input onto the already existing quantity
    least_numerous_shoe.quantity += user_input
    print(f"{user_input} shoes added to the {least_numerous_shoe.product} product")

    # creating a list to add to the file
    lines = []

    # opening the file
    with open("inventory.txt", "r") as file:

        # for each line in the file
        for line in file:

            # storing each piece of data in this variable
            data = line.strip().split(",")

            # if the data at index 1 is the same as the least numerous shoe code
            if data[1] == least_numerous_shoe.code:

                # changing the data at index 4 to the new quantity
                data[4] = str(least_numerous_shoe.quantity)
            
            # joining the data back in the correct format
            lines.append(",".join(data))
    
    # closing the file
    file.close()

    # opening the file to write back to with the new line and updated data
    with open("inventory.txt", "w") as file:
        for line in lines:
            file.write(f"{line}\n")
    
    # closing the file
    file.close()

# defining a function to search for the shoe code
def search_shoe():
    read_shoes_data()

    # asking the user to enter the code of the shoe they want to see
    user_input = input("Enter the code of the shoe to search: ")

    # creating a variable to store the shoe codes
    matching_shoe_code = [shoe for shoe in shoe_list if shoe.code == user_input]

    # if the user_input doesn't match the code for a shoe printing out an appropriate error message
    if not matching_shoe_code:
        print("No shoes with that code can be found")
        return
    
    # otherwise the line for the shoe is printed out
    for shoe in matching_shoe_code:
        print(shoe)

# defining a function to get the total value for each shoe item
def value_per_item():
    read_shoes_data()

    # for each shoe in the list
    for shoe in shoe_list:

        # calculating the total value for ever shoe and printing it out
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: {value}")

# defining a function to find the most numerous shoe
def highest_qty():
    read_shoes_data()

    # finding the most numerous shoe
    most_numerous_shoe = max(shoe_list, key=get_quantity)

    # printing out the most numerous shoe along with a statement saying it is for sale
    print(f"{most_numerous_shoe.product} is the most numerous shoe and is for sale")

# defining a function to get the quantity of a shoe
def get_quantity(shoe):
    return shoe.quantity

user_choice = ""

# while the user choice isn't "quit"
while user_choice != "quit":

    # asking the user to enter what they want from the menu
    user_choice = input('''\nEnter what you would like to do:
RSD - Read shoes data
CS - Capture shoes
VA - View all
RS - Re-stock
SS - Search shoe
VPI - Value per item
HQ - Highest quantity
Q - Quit
''').lower()
    
    # if the user's choice is "read shoes data", pulling up the function to read the data
    if user_choice == "rsd":
        read_shoes_data()
    
    # if the user's choice is "capture shoes", pulling up the function to capture the data for a new shoe
    elif user_choice == "cs":
        capture_shoes()
    
    # if the user's choice is "view all", pulling up the function to view all of the data
    elif user_choice == "va":
        view_all()
    
    # if the user's choice is "re-stock", pulling up the function to re-stock the least numerous shoe
    elif user_choice == "rs":
        re_stock()

    # if the user's choice is "search shoe", pulling up the function to search for a specific shoe
    elif user_choice == "ss":
        search_shoe()
    
    # if the user's choice is "value per item", pulling up the function to get the value of each shoe item
    elif user_choice == "vpi":
        value_per_item()
    
    # if the user's choice is "highest quantity", pulling up the function to get teh most numerous shoe and put it up for sale
    elif user_choice == "hq":
        highest_qty()
    
    # if the user's choice is "quit", ending the loop and program
    elif user_choice == "q":
        print("Goodbye")

    # otherwise printing an error message and asking looping back to the user's choice
    else:
        print("Invalid choice")