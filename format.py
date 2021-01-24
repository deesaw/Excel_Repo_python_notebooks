# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:11:46 2021

@author: deesaw
"""


from xlrd import open_workbook

wb = open_workbook('D4MC2_Data ETL Tasks Tracker.xlsx', formatting_info=True)
sheet = wb.sheet_by_name("2")
