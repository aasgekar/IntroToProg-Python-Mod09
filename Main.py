# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# RRoot,1.1.2020,Added pseudo-code to start assignment 9
# AAsgekar,6.15.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as P
    from IOClasses import EmployeeIO as Eio

strFileName = "EmployeeData.txt"
currentList = ""
objP1 = Emp(1, "", "")
# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
currentList = P.read_data_from_file(strFileName)

choice = " "
while choice != "4":
    # Show user a menu of options
    Eio.print_menu_items()
    # Get user's menu option choice
    choice = Eio.input_menu_options()

    if choice == "1":
        # Show user current data in the list of employee objects
        if currentList != []: # Check if there is any data in the list
            Eio.print_current_list_items(currentList)
            input("Press Enter to return to the Menu.")
        else:
            print("The list is currently empty.")
            input("Press Enter to return to the Menu.")
    elif choice == "2":
        # Let user add data to the list of employee objects
        try: # Check for a user input that doesn't obey properties
            objP1 = Eio.input_employee_data()
            currentList.append(objP1)
        except UnboundLocalError: # Let the user know they need to re-input their data
            print("Please try again.")
        input("Press Enter to return to the Menu.")
    elif choice == "3":
        # let user save current data to file
        x = P.save_data_to_file(strFileName,currentList)
        if x == True:
            print("Your data was saved successfully.")
            input("Press Enter to return to the Menu.")
    elif choice == "4": # Let user exit program
        print("Thank you for using the program")
        input("Press Enter to Exit.")
        break
    else:
        print("That was not an option on the Menu.")
        input("Press Enter to return to the Menu")

# Main Body of Script  ---------------------------------------------------- #
