#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-12-12T13:23:07.459Z
"""

class Expense:
    def __init__(self, amount, category, date, description):
        self.SpendAmount = amount
        self.Category = category
        self.Date = date
        self.Description = description
    def __str__(self):
        opd = "{:<12}{:<15}{:<10}{:<30}".format(self.Date,self.Category,self.SpendAmount,self.Description)
        return opd