# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# TNord,8.30.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
objFile = None
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's price

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        TNord,8.30.2022,Modified code to complete assignment 8
    """

    def __init__(self, product_name = "", product_price = 0):
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        return self.product_name + " | " + self.product_price

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, name):
        self.__product_name = name

    @property
    def product_price(self):
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if value < 0:
            print("You must enter a valid price.")
        else:
            self.__product_price = value

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        read_data_from_file(file_name): -> (a list of product objects)
        save_data_to_file(file_name, list_of_product_objects):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        TNord,8.30.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for row in file:
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of object rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) containing your data:
        :return: (list) of objects
        """
        objFile = open(file_name, "w")
        for row in list_of_rows:
            objFile.write(str(row).strip() + "\n") # calls __str__()
        objFile.close()
        print("Data saved to file!")
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks

        methods:
            output_menu_tasks():
            input_menu_choice(): -> (string)
            show_current_data(list_of_rows):
            get_data_from_user(): -> (string),(float)

        changelog: (When,Who,What)
        TNord,8.30.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Products
        2) Add New Product
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (string) of user's menu choice
        """
        choice = str(input("Which option would you like to perform? [1 to 4]: ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def show_current_data(list_of_rows):
        """  Shows current list of products

        :param list_of_rows: (list) of current products:
        :return: nothing
        """
        print("******* The current Products are: *******")
        for row in list_of_rows:
            print(str(row).strip())
        print("*******************************************")

    @staticmethod
    def get_data_from_user():
        """  Gets product name and price values to be added to the list

        :return: (string, string) with product name and price
        """
        name = input("What is the name of the product: ")
        price = float(input("What is the price of the product: "))

        return name, price

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# When the program starts, if there is no file on disk, create one
if objFile == None:
    objFile = open(strFileName, "a")
    objFile.close()

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(file_name=strFileName, list_of_rows=lstOfProductObjects)  # read file data

# Show user a menu of options
while (True):
    # Step 3 Show current data
    IO.output_menu_tasks()  # Shows menu
    strchoice = IO.input_menu_choice()  # Get user's menu option choice

    if strchoice.strip() == '1':  # Show Current Data (Product Objects)
        IO.show_current_data(lstOfProductObjects)
        continue  # to show the menu

    elif strchoice == '2':  # Add New Product to List of Product Objects
        objprod = Product()
        objprod.product_name, objprod.product_price = IO.get_data_from_user()
        lstOfProductObjects.append(objprod)
        continue  # to show the menu

    elif strchoice == '3':  # Save Current Data to File
        FileProcessor.save_data_to_file(file_name=strFileName, list_of_rows=lstOfProductObjects)
        continue  # to show the menu

    elif strchoice == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop

# Main Body of Script  ---------------------------------------------------- #

