# Generated from: menuhandler.ipynb
# Converted at: 2026-01-05T11:53:14.528Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import csv
import os
import sys
from ExpenseClass import Expense
from datetime import datetime

from file_manager import save_expense
from file_manager import read_expenses
from reports import ViewAllExp
from reports import CatWiseSummary
from reports import MonthlyReport

# def save_expenses(Exp, filename='D:/expenses.csv'):
#     folder = os.path.dirname(filename)
#     if folder and not os.path.exists(folder):
#         os.makedirs(folder, exist_ok=True)

    
#     file_exists = os.path.exists(filename)
#     with open(filename, 'a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         if not file_exists:
#             writer.writerow(['amount', 'category', 'date', 'description'])
#         writer.writerow([Exp.SpendAmount, Exp.Category, Exp.Date, Exp.Description])

def menuhandler(choice):
    match choice:
        case 1:
            print("ADD NEW EXPENSE: ")

            # amount
            while True:
                try:
                    Amount = float(input("Enter amount: ").strip())
                except ValueError:
                    print("Please enter a valid number (e.g. 120.50)")
                else:
                    break

            # category
            valid_categories = ["food", "transport", "entertainment", "shopping", "other"]
            while True:
                category = input("Enter category (Food/Transport/Entertainment/Shopping/Other): ").strip().lower()
                if category in valid_categories:
                    break
                else:
                    print("Invalid category! Please enter one of: Food, Transport, Entertainment, Shopping, Other")

            # date
            while True:
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                if date_input == "":
                    entered_date = datetime.today().strftime("%Y-%m-%d")
                    break
                try:
                    valid_date = datetime.strptime(date_input, "%Y-%m-%d")
                    entered_date = valid_date.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date! Please enter in YYYY-MM-DD format.")

            # description
            while True:
                Description = input("Enter description: ").strip()
                try:
                    if not Description:
                        raise ValueError("Input cannot be empty.")
                    if not Description.replace(" ", "").isalpha():
                        raise ValueError("Only alphabets and spaces allowed.")
                    break   # <-- IMPORTANT: break, not return
                except ValueError as e:
                    print(e)

            # now call save

         
            #print("Saved:", Amount, category, entered_date, Description)
            expense1 = Expense(Amount,category,entered_date,Description)
            save_expense(expense1)
            print(expense1)

        case 2:
            ViewAllExp()

        case 3:
             CatWiseSummary()

        case 4:
             MonthlyReport()
        
        case 7:
            sys.exit()


            
        case _:
            print("Option not implemented.")

if __name__ == "__main__":
    menuhandler(1)