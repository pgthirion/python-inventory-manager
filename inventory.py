shoe_list = []
import statistics as stats

class Shoes():

    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    def get_cost(self):
        return self.cost


    def get_quanty(self):
        return self.quantity


def read_shoes_data():
    file = None
    shoes = []

    try:
        file = open('inventory.txt', 'r')

        with open("inventory.txt", "r") as shoe_txt:
            shoe_list_creator = []
            for line in shoe_txt:
                shoe_list_creator = line.split(',')
                shoes.append(Shoes(shoe_list_creator[0], shoe_list_creator[1], shoe_list_creator[2], shoe_list_creator[3], shoe_list_creator[4]))
    
    except FileNotFoundError as error:
        print("The file that you are trying to open does not exist...Creating a new file.")
        print(error)
        with open('inventory.txt', 'w+') as calc_out: # Creates the text file if it doesn't exist
            calc_out.close()
    finally:
        if file is not None: # If file is found close file
            file.close()   
    return shoes


def capture_shoes(shoe_list):
    print("\nAdding of a new shoe:\n")
    shoe_list.append(Shoes(input("Country: "), input("Code: "), input("Description: "), float(input("Cost (ZAR): ")), int(input("Quantity: "))))


def view_all(shoe_list):

    for products in shoe_list:
        print(f'''
            Country: {products.country}
            Code: {products.code}
            Description: {products.product}
            Cost: {products.cost}
            Quantity: {products.quantity}''')



def write_shoes(shoe_list):
    with open("inventory.txt", 'r+') as file:
        # Step 6: Write the modified contents back into the file
        for shoe in shoe_list:
                file.write(str(shoe))
                print(str(shoe))
        

def replace_in_file(file_path, old_string, new_string):
    # Step 1: Open the file in read mode
    with open(file_path, 'r') as file:
        # Step 2: Read the contents of the file
        content = file.read()

    # Step 3: Close the file

    # Step 4: Perform the replacement operation
    modified_content = content.replace(old_string, new_string)

    # Step 5: Open the file in write mode
    with open(file_path, 'w') as file:
        # Step 6: Write the modified contents back into the file
        file.write(modified_content)


# This function takes the shoe with the lowest qty number and prints it
# The user is then asked if they want to restock the product
# If yes they are promted with a input to enter the new qty
# The new qty is then updated.
def re_stock():

    file = None

    try:
        file = open('inventory.txt', 'r')
        

        # Sorting the quantities in order to find the lowest in stock item

        with open("inventory.txt", "r") as shoe_txt:
            shoe_qnty_list_creator = []
            shoe_qnty_list = []

            for line in shoe_txt:
                shoe_qnty_list_creator = line.split(',')
                DerCode = shoe_qnty_list_creator[4].strip("\n")
                shoe_qnty_list.append(DerCode)
                shoe_qnty_list.sort()
            if "Quantity" in shoe_qnty_list:
                shoe_qnty_list.remove("Quantity")
            for i in range(0, len(shoe_qnty_list)):
                shoe_qnty_list[i] = int(shoe_qnty_list[i])
            smallest_qty = min(shoe_qnty_list)

        # Printing all the details for the lowest in stock item   
        with open("inventory.txt", "r+") as shoe_txt:
            shoe_list_creator = []
            shoe_list_creatorx = []
            valuels =[]
            for fullline in shoe_txt:
                shoe_list_creator = fullline.split(',')
                if shoe_list_creator[4] == (str(smallest_qty)+"\n"):
                    valuels.append(Shoes(shoe_list_creator[0], shoe_list_creator[1], shoe_list_creator[2], shoe_list_creator[3], shoe_list_creator[4]))
            for products in valuels:
                print(f'''
                    Country: {products.country}
                    Code: {products.code}
                    Description: {products.product}
                    Cost: {products.cost}
                    Quantity: {products.quantity}''')    
                yn = input(f"Would you like to update the stock for {products.product}? (y/n): ")
                if yn.lower() == "y":
                    for x in shoe_txt:
                        shoe_list_creatorx = x.split(',')
                        if shoe_list_creatorx[4] == shoe_list_creator[1]:
                            shoe_list_creatorx.remove(x)
                            print(shoe_list_creatorx)
                    newstock = int(input("New stock number: "))
                    replace_in_file("inventory.txt",f"{products.country},{products.code},{products.product},{products.cost},{products.quantity}", 
                                    f"{products.country},{products.code},{products.product},{products.cost},{newstock}\n" )
    except FileNotFoundError as error:
        print("The file that you are trying to open does not exist...Creating a new file.")
        print(error)
        with open('inventory.txt', 'w+') as calc_out: # Creates the text file if it doesn't exist
            calc_out.close()
    finally:
        if file is not None: # If file is found close file
            file.close()  


# Searches for the shoe in the list and prints the output based on its ID
def search_shoe():
    codein = input("Enter the code of the shoe to find: ")
    read_shoes_data()
    for products in shoe_list:
        if products.code == codein: 
            print(f'''
                Country: {products.country}
                Code: {products.code}
                Description: {products.product}
                Cost: {products.cost}
                Quantity: {products.quantity}''')


# Prints the total combined value (qty*cost) of all shoes
def value_per_item():
    read_shoes_data()
    totalvalue = 0.00
    for products in shoe_list:
        # Fixed the error by removing the new line text
        test = products.quantity[:len(products.quantity)].strip("\n")
        totalvalue = totalvalue + int(test) * float(products.cost) 
    print(f"The total value for all the products is: {round(totalvalue,2)} ZAR")


# Looks for the shoe with the highest qty value and prints it
def highest_qty():
        with open("inventory.txt", "r") as shoe_txt:
            shoe_qnty_list_creator = []
            shoe_qnty_list = []

            for line in shoe_txt:
                shoe_qnty_list_creator = line.split(',')
                DerCode = shoe_qnty_list_creator[4].strip("\n")
                shoe_qnty_list.append(DerCode)
                shoe_qnty_list.sort()
            if "Quantity" in shoe_qnty_list:
                shoe_qnty_list.remove("Quantity")
            for i in range(0, len(shoe_qnty_list)):
                shoe_qnty_list[i] = int(shoe_qnty_list[i])
            max_qty = max(shoe_qnty_list)

        # Printing all the details for the highest in stock item   
        with open("inventory.txt", "r+") as shoe_txt:
            shoe_list_creator = []
            shoe_list_creatorx = []
            valuels =[]
            for fullline in shoe_txt:
                shoe_list_creator = fullline.split(',')
                if shoe_list_creator[4] == (str(max_qty)+"\n"):
                    valuels.append(Shoes(shoe_list_creator[0], shoe_list_creator[1], shoe_list_creator[2], shoe_list_creator[3], shoe_list_creator[4]))
            for products in valuels:
                print("Highest QTY Shoe: ") 
                print(f'''
                    Country: {products.country}
                    Code: {products.code}
                    Description: {products.product}
                    Cost: {products.cost}
                    Quantity: {products.quantity}''')       


while True:
    # presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    print(f"\nNumber of shoes {len(shoe_list)}") if len(shoe_list) > 0 else print("Please load shoe data")
    menu = input('''\nSelect one of the following options below:\n
r - read shoes data
cs - capture shoes
va - view all shoes
rs - re stock
s - search shoe
vpi - value per item
hq - highest qty
w - write shoes
e - Exit
    
\nPlease enter your selection: ''').lower()
                
    if menu == 'r':
        shoe_list = read_shoes_data()

    elif menu == 'cs':
        capture_shoes(shoe_list)

    elif menu == 'va':  
        view_all(shoe_list)
    
    elif menu == 'rs':
        re_stock()
        shoe_list = read_shoes_data()

    elif menu == 's':
        search_shoe()

    elif menu == 'vpi':
        value_per_item()

    elif menu == 'hq':
        highest_qty()

    elif menu == 'w':
        write_shoes(shoe_list)

    elif menu == 'e':
        print('Goodbye!')
        exit()    

    else:
        print("You have made a wrong choice, Please Try again")