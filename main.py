# Generated from: main.ipynb
# Converted at: 2026-01-05T12:05:41.598Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

from menuhandler import menuhandler 
 
def print_menu():
    print("=================================================================================================================================================")
    print("                                                         PERSONAL FINANCE MANAGER                                                               ")
    print("==================================================================================================================================================\n")

    print("    MAIN MENU :\n")
    
    print("1)   Add New Expense")
    print("2)   View All Expenses")
    print("3)   View Category-wise Summary")
    print("4)   Generate Monthly Report")
    print("5)   Search Expenses")
    print("6)   Backup Data")
    print("7)   Exit")
   
def main():
    while True:
        print_menu()

        while True:
            try:
                OptionSelect = int(input("Enter your choice (1-7): "))
                print("\n")
                break
            except ValueError:
                print("Please enter a number for the choice.")

        menuhandler(OptionSelect)
        input("\nPress Enter to return to main menu...")

  
            
        


# This makes sure the program starts from here when you run the file
if __name__ == "__main__":
    main()