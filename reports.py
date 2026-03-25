# Generated from: reports.ipynb
# Converted at: 2026-01-05T11:57:51.687Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from file_manager import read_expenses

from datetime import datetime


def ViewAllExp():
            print(" ")
            print("View All Expenses: ")
            print("  ")
            print("{:>15}       {:<15}{:<15}{:<30}".format("SPEND AMOUNT","CATEGORY","DATE","DESCRIPTION"))
            print("--------------------------------------------------------------")
            expen = []
            expen = read_expenses()
            for exp in expen:
                print("{:>15}       {:<15}{:<15}{:<30}".format(exp['amount'],exp['category'],exp['date'],exp['description']))
                # print(exp['amount'],exp['category'],exp['date'],exp['description'])

def CatWiseSummary():
    Expens = []

    FoodTotal = 0
    TransportTotal = 0
    EntertainmentTotal = 0
    ShoppingTotal = 0
    OtherTotal = 0

    
    expens = read_expenses()
    for exp in expens:
        CatUpper  = exp['category'].upper()
        if( CatUpper == "FOOD"):
            FoodTotal = FoodTotal + exp['amount']
        if(CatUpper == "TRANSPORT"):
            TransportTotal = TransportTotal + exp['amount']
        if(CatUpper == "ENTERTAINMENT"):
            EntertainmentTotal = EntertainmentTotal + exp['amount']
        if(CatUpper == "SHOPPING"):
            ShoppingTotal = ShoppingTotal + exp['amount']
        if(CatUpper == "OTHER"):
            OtherTotal = OtherTotal + exp['amount']

    print("{:<17}  {:>17}".format("CATEGORY","TOTALSPENT"))
    print("-------------------------------------")
    print("{:<17}  {:>17}".format("FOOD",FoodTotal))
    print("{:<17}  {:>17}".format("Transport",TransportTotal))
    print("{:<17}  {:>17}".format("Entertainment",EntertainmentTotal))
    print("{:<17}  {:>17}".format("Shopping",ShoppingTotal))
    print("{:<17}  {:>17}".format("OtherTotal",OtherTotal))

def MonthlyReport():

    FoodTotal = 0
    TransportTotal = 0
    EntertainmentTotal = 0
    ShoppingTotal = 0
    OtherTotal = 0

    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year (YYYY): "))

    expens = read_expenses()

    for exp in expens:
        # Convert string date to datetime
        exp_date = datetime.strptime(exp['date'], "%Y-%m-%d")

        # Filter by selected month & year
        if exp_date.month == month and exp_date.year == year:
            cat = exp['category'].upper()
            amt = exp['amount']

            if cat == "FOOD":
                FoodTotal += amt
            elif cat == "TRANSPORT":
                TransportTotal += amt
            elif cat == "ENTERTAINMENT":
                EntertainmentTotal += amt
            elif cat == "SHOPPING":
                ShoppingTotal += amt
            elif cat == "OTHER":
                OtherTotal += amt

    x = ["FOOD","Transport","Entertainment","Shopping","Other"]
    y = [FoodTotal,TransportTotal,EntertainmentTotal,ShoppingTotal,OtherTotal]

    plt.title(f"Expenses for {month}/{year}",color = "orange",fontweight = "bold")
    plt.xlabel("Category",color = "red")
    plt.ylabel("Amount",color = "purple")
    plt.bar(x,y)

    os.makedirs("reports", exist_ok=True)
    pdf_name = f"reports/Monthly_Report_{month}_{year}.pdf"


    plt.savefig(pdf_name)



    plt.show()
