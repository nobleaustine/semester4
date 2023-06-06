from tabulate import tabulate   # tabulate data into tables
import numpy as np              # perform matrix calc
import re

RED = '\033[38;2;225;0;0m'
END = '\033[0m'
GREEN = "\u001b[32m"

table         = []
display_table = []

# default table for test running
table = np.array([[160,130,175,190,200],[135,120,130,160,175],[140,110,155,170,185],[50,50,80,80,110],[55,35,70,80,105]])
# supplies = [x for x in [7,9,18]]
# demands    = [y for y in [5,8,7,14]]
# ans_table  = np.zeros((3,4),dtype=int)

def substract_min():

    global table
    min_values = np.min(table,axis=1,keepdims=True)
    table = table - min_values

    min_values = np.min(table,axis=0,keepdims=True)
    table = table - min_values
    print(tabulate(table,tablefmt='grid'))

def create_display_table():
    global display_table
    for row in range(len(table[0])):
        display_table.append([str(value) for value in table[row]])

def assign_values():

    global table
    global display_table
    
    row_count    = len(table)
    col_count = len(table[0])
    
    for i,row in enumerate(display_table):
        count = 0
        for j,value in enumerate(row):
            if(value == '0'):
                pos   = j
                count +=1
        if count == 1 :
            for k in range(len(table)):
                if display_table[k][pos] == '0':
                    display_table[k][pos] = RED + "0" + END
            display_table[i][pos] = GREEN + "0" + END
        
    # print(tabulate(display_table,tablefmt="grid"))

    for col in range(col_count):
        count = 0
        for row in range(row_count):
            if(display_table[row][col]=='0'):
                index = row
                count +=1
        if count == 1:
            for k in range(col_count):
                if display_table[index][k] == '0':
                    display_table[index][k] = RED + "0" + END
            display_table[index][col] = GREEN + "0" + END
    print(tabulate(display_table,tablefmt="grid"))

substract_min()
print(" ")
create_display_table()
assign_values()



        




    

