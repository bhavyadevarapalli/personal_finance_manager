# Generated from: file_manager.ipynb
# Converted at: 2026-01-02T11:41:05.757Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

import csv
import os

from ExpenseClass import Expense

HEADERS = ['amount', 'category', 'date', 'description']


def save_expense(exp, filename='expenses.csv'):
    """Append a single Expense object to CSV"""

    BASE_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(BASE_DIR, "data")
    os.makedirs(DATA_DIR, exist_ok=True)
    expenses = []
    filename = os.path.join(DATA_DIR, filename)

    file_exists = os.path.exists(filename)

    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(HEADERS)

        writer.writerow([
            exp.SpendAmount,
            exp.Category,
            exp.Date,
            exp.Description
        ])


def read_expenses(filename='expenses.csv'):
    """Read all expenses from CSV and return list of dicts"""
    BASE_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(BASE_DIR, "data")
    os.makedirs(DATA_DIR, exist_ok=True)
    expenses = []
    filename = os.path.join(DATA_DIR, filename)

    if not os.path.exists(filename):
        return expenses  # empty list if file not found

    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append({
                'amount': float(row['amount']),
                'category': row['category'],
                'date': row['date'],
                'description': row['description']
            })

    return expenses