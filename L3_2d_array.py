#creating 2d array by taking user input
import numpy as np
array_rows = int(input("how many rows:"))
array_coloumns = int(input("how many coloumns:"))
array_storage = []

for r in range(array_rows):#making a loop for number of rows
    row = []#making an empty class for rows
    print("enter the value for row number",r+1)
    for c in range(array_coloumns):#making a loop for number of coloumns
        element = int(input("enter the value for coloumn number"))#asking for numbers
        row.append(element)#adding the requested number in a row
    array_storage.append(row)#adding the complete row into the array

for i in array_storage:
    print(i)