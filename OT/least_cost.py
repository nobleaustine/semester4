# required libraries
from tabulate import tabulate   #to tabulate data
import numpy as np

RED = '\033[38;2;225;0;0m'
END = '\033[0m'
superscript_chars = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵','6': '⁶','7': '⁷','8': '⁸', '9': '⁹','[': '⁽',']': '⁾',}



# default table for test running
cost_table = [z for z in [[19,30,50,10],[70,30,40,60],[40,8,70,20]]]
supplies = [x for x in [7,9,18]]
demands    = [y for y in [5,8,7,14]]
ans_table  = np.zeros((3,4),dtype=int)
 
def get_user_inputs():

    print(" ")
    print("----------------------------------------------------------------- ")
    print(" ")
    print("User Inputs :")
    print(" ")

    no_sources      = int(input("Enter the number of sources      : "))         
    no_destinations = int(input("Enter the number of destinations : "))
    print(" ")
    
    ans_table  = np.zeros((no_sources,no_destinations),dtype=int)
    cost_table      = []

    print("Enter the total_costof transportation in the")
    print("increasing order of destination label like,")
    print("D1, D2, D3, .... for each origin, O1, O2, O3, ...")
    print(" ")
    for i in range(no_sources):
        input_row  = [int(x) for x in input(f'          O{i+1} : ').split()]
        cost_table.append(input_row)
    print(" ")

    print("Enter the demand of each destination in the")
    print("increasing order of the destinations label  : ",end=" ")
    demands = [int(x) for x in input().split()]
    print(" ")

    print("Enter the capacity of each origin in the")
    print("increasing order of the origin label        : ",end=" ")
    supplies = [int(x) for x in input().split()]
    print(" ")
    print("----------------------------------------------------------------- ")
    print(" ")
    
    return cost_table,ans_table,supplies,demands

def create_display_table():
    
    # intializing transportation table and its dimensions as display_table and length*breadth
    display_table = []
    length  = len(cost_table[0])
    breadth = len(cost_table)

    # looping through cost_table and creating rows (insert_row) of transportation table as
    # S(row count) | cost(1) | cost(2) | ..... | cost(length) | supply(row count)
    for row in range(breadth):
        insert_row = [str(cost_table[row][col]) for col in range(length)]
        insert_row = [f'S{row + 1}'] + insert_row + [str(supplies[row])]
        display_table.append(insert_row)

    # adding final row of demands for each destination
    insert_row = [str(value) for value in demands]
    insert_row = ["DEMANDS"] + insert_row + ["-"]
    display_table.append(insert_row)
    
    # header row of the form "S\D" | D(1) | D(2) | ..... | D(length) | "SUPPLY"
    head = [f"D{col+1}" for col in range(length)]
    head = ["S\D"] + head + ["SUPPLY"]

    # displaying and returning the transportation table
    print("               TRANSPORTATION TABLE")
    print(tabulate(display_table,headers=head,tablefmt="grid",stralign="right", numalign="right"))
    print(" ")
    return display_table,head

def check_supply_or_demand_exsist():

    for supply in supplies:
        if supply != 0:
            return True
    for demand in demands:
        if demand !=0:
            return True
    return False

def color_and_show_table(row_or_column,index,index_comp):

    col_count   = len(cost_table[0])
    row_count  = len(cost_table)
    
    if row_or_column == 'row':
        for col in range(col_count):
            if(demands[col] != 0 or col == index_comp):
                if(col == index_comp):
                    key_cell = ''.join(superscript_chars.get(char, char) for char in ("["+str(ans_table[index][col])+"]"))
                    display_table[index][col+1] = RED + key_cell + str(cost_table[index][col]) + END
                else:
                    display_table[index][col+1] = RED + str(cost_table[index][col]) + END

        display_table[index][col_count + 1] =  RED + str(supplies[index]) + END 
        display_table[row_count][index_comp +1] = str(demands[index_comp])
    else:
        for row in range(row_count):
            if(supplies[row] != 0 or row == index_comp):
                if(row == index_comp):
                    key_cell = ''.join(superscript_chars.get(char, char) for char in ("["+str(ans_table[row][index])+"]"))
                    display_table[row][index+1] = RED + key_cell + str(cost_table[row][index]) + END
                else:
                    display_table[row][index+1] = RED + str(cost_table[row][index]) + END
        display_table[row_count][index+1] = RED + str(demands[index]) + END
        display_table[index_comp][col_count+1] = str(supplies[index_comp])

    head = [f"D{col + 1}" for col in range(col_count)]
    head = ["O\D"] + head + ["CAPACITY"]
    print(tabulate(display_table,headers=head, tablefmt="grid",stralign="right", numalign="right"))
    print(" ")
    print(" ")

def least_cost_method():


    # length   = len(cost_table[0])
    # breadth  = len(cost_table)
    check = True
    row_or_column =""
    count = 0
    index = 0
    index_comp = 0

    while(check == True):

        count = count + 1
        r = 0
        c = 0
        minValue = 999999
        for i,row in enumerate(cost_table):
            for j, cost in enumerate(row):
                if(cost<minValue and supplies[i] !=0 and demands[j]!=0):
                    r = i
                    c = j
                    minValue = cost
        if(demands[c]<supplies[r]):
            ans_table[r][c] = demands[c]
            supplies[r] = supplies[r] - demands[c]
            demands[c] = 0
            row_or_column = "col"
            index = c 
            index_comp=r
        else :
            ans_table[r][c] = supplies[r]
            demands[c] = demands[c] - supplies[r]
            supplies[r] = 0
            row_or_column = "row"
            index = r
            index_comp=c

        check = check_supply_or_demand_exsist()

        print("Iteration No. : ",count,f'        Minimum Value T({r+1},{c+1}) : {minValue}', )
        color_and_show_table(row_or_column,index,index_comp)

def calc_and_display_cost():
    total_cost = 0
    for r,row in enumerate(cost_table):
         for c,value in enumerate(row):
             total_cost = total_cost + value*ans_table[r][c]
    print("Total Transportation Cost : ",total_cost)

# calling functions 
# comment to use default values   
# cost_table,ans_table,supplies,demands = get_user_inputs()
display_table,head = create_display_table()
least_cost_method()
calc_and_display_cost()

