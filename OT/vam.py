# required libraries
from tabulate import tabulate   # to tabulate data 
import numpy as np              # perform matrix operations

# required global constants
RED                = '\033[38;2;225;0;0m'
END                = '\033[0m'
superscript_chars  = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵','6': '⁶','7': '⁷','8': '⁸', '9': '⁹','[': '⁽',']': '⁾',}
GREEN              = "\u001b[32m"
BLUE               = '\u001b[34m'

# default values for test running with sum(supply) == sum(demand)

# default table for test running

# cost_table     = [z for z in [[11,13,17,14],[16,18,14,10],[21,24,13,10]]]
# cost_table_cut = [c for c in cost_table]
# demands        = [y for y in [200,225,275,250]]
# supplies       = [x for x in [250,300,400]]
# ans_table      = np.zeros((3,4),dtype=int)
# cost_table     = np.array(cost_table)

# cost_table     = [z for z in [[6,1,9,3],[11,5,2,8],[10,12,4,7]]]
# cost_table_cut = [c for c in cost_table]
# demands        = [y for y in [85,35,50,45]]
# supplies       = [x for x in [70,55,90]]
# ans_table      = np.zeros((3,4),dtype=int)

# cost_table     = [z for z in [[20,18,18,21,19],[21,22,23,20,24],[18,19,21,18,19]]]
# cost_table_cut = [c for c in cost_table]
# demands        = [y for y in [60,80,85,105,70]]
# supplies       = [x for x in [100,125,175]]
# ans_table      = np.zeros((3,5),dtype=int)

# cost_table     = [z for z in [[16,20,12],[14,8,18],[26,24,16]]]
# cost_table_cut = [c for c in cost_table]
# demands        = [y for y in [180,120,150]]
# supplies       = [x for x in [200,160,90]]
# ans_table      = np.zeros((3,3),dtype=int)
# cost_table     = np.array(cost_table)

# atozmath
# cost_table     = [z for z in [[19,30,50,10],[70,30,40,60],[40,8,70,20]]]
# cost_table_cut = [c for c in cost_table]
# demands        = [y for y in [5,8,7,14]]
# supplies       = [x for x in [7,9,18]]
# ans_table      = np.zeros((3,4),dtype=int)
# cost_table     = np.array(cost_table)

# default values for test running with sum(supply) != sum(demand)
# cost_table = [z for z in [[20,25,28,31],[32,28,32,41],[18,35,24,32]]]
# cost_table_cut = [c for c in cost_table]
# demands    = [y for y in [150,40,180,170]]
# supplies   = [x for x in [200,180,110]]
# ans_table  = np.zeros((3,4),dtype=int)


# To test by providing input
# 3
# 4
# 19 30 50 10
# 70 30 40 60
# 40 8 70 20
# 5 8 7 14
# 7 9 18

def get_user_inputs():

    print(" ")
    print("--------------------- TRANSPORTATION PROBLEM ---------------------")
    print(" ")
    print("User Inputs :")
    print(" ")

    # getting number of sources and destinations from user
    no_sources      = int(input("   Enter the number of sources      : "))         
    no_destinations = int(input("   Enter the number of destinations : "))
    print(" ")
    
    # setting up ans_table with dimensions : no_sources x no_destinations and cost_table
    ans_table  = np.zeros((no_sources,no_destinations))
    ans_table = ans_table.tolist()
    cost_table      = []

    # getting cost for transportation from each source to destination from user
    print("   Enter the cost of transportation in the")
    print("   increasing order of destination label like,")
    print("   D1, D2, D3, .... for sources S1, S2, S3, ...")
    print(" ")
    # taking the values to input_row and adding input row to cost_table
    for i in range(no_sources):
        input_row  = [int(x) for x in input(f'      S{i+1} : ').split()]
        cost_table.append(input_row)
    print(" ")
    
    # taking demands and supply from user
    print("   Enter the demand of each destination in the")
    print("   increasing order of the destinations label  : ",end=" ")
    demands = [int(x) for x in input().split()]
    print(" ")

    print("   Enter the capacity of each origin in the")
    print("   increasing order of the origin label        : ",end=" ")
    supplies = [int(x) for x in input().split()]
    print(" ")
    print("------------------------------------------------------------------")
    print(" ")
    
    return cost_table,ans_table,supplies,demands

def create_display_table():

    global ans_table
    
    # intializing transportation table and its dimensions as display_table and length x breadth
    display_table = []
    length  = len(cost_table[0])
    breadth = len(cost_table)

    # looping through cost_table and creating rows (insert_row) of transportation table as
    # S(row count) | cost(1) | cost(2) | ..... | cost(length) | supply(row count)
    for row in range(breadth):
        insert_row = [str(cost_table[row][col]) for col in range(length)]
        insert_row = [f'S{row + 1}'] + insert_row + [str(supplies[row])]
        display_table.append(insert_row)

    # checking if transportation table is unbalanced : sum(supply) != sum(demand)
    if sum(demands)>sum(supplies) :
       
        insert_row = np.zeros(length)        # creating dummy row with all cost values as 0
        insert_row = insert_row.tolist()     # converting to list

        cost_table.append([x for x in insert_row]) # updating to cost_table &
        ans_table.append([x for x in insert_row])  # ans_table

        # adding dummy row to display_table and updating supplies with reminder
        insert_row = ["Dummy"] + insert_row + [sum(demands) - sum(supplies)]
        display_table.append(insert_row)
        supplies.append(sum(demands) - sum(supplies))

        # header row of the form "S\D" | D(1) | D(2) | ..... | D(length) | "SUPPLY"
        head = [f"D{col+1}" for col in range(length)]
        head = ["S\D"] + head + ["SUPPLY"]

    elif sum(demands)<sum(supplies) :

        for i,row in enumerate(cost_table):
            cost_table[i].append(0)
            ans_table[i].append(0)
            demands.append(sum(demands) - sum(supplies))

            display_table[i].append(0)
            head = [f"D{col+1}" for col in range(length)]
            head = ["S\D"] + head + ["Dummy"] + ["SUPPLY"]
    
    else :
         # header row of the form "S\D" | D(1) | D(2) | ..... | D(length) | "SUPPLY"
        head = [f"D{col+1}" for col in range(length)]
        head = ["S\D"] + head + ["SUPPLY"]

    cost_table_cut = [c for c in cost_table]

    # adding final row of demands for each destination
    insert_row = [str(value) for value in demands]
    insert_row = ["DEMANDS"] + insert_row 
    display_table.append(insert_row)
    
    length  = len(cost_table[0])
    breadth = len(cost_table)
    
    # displaying the transportation table
    print("               TRANSPORTATION TABLE")
    print(tabulate(display_table,headers=head,tablefmt="grid",stralign="right", numalign="right"))
    print(" ")
    
   
    # adding row penality part
    head = head + ["PENALITY"]
    for i in range(breadth):
        display_table[i].append("0")
    display_table[breadth] = display_table[breadth] + ['-','-']

    # adding column penality part
    penality_col  = np.zeros(length)
    penality_col  = penality_col.tolist()
    penality_col  = ["PENALITY"] + penality_col + ['-','-']
    display_table.append(penality_col)

    return display_table,cost_table_cut,head

def check_supply_or_demand_exsist():

    for supply in supplies:
        if supply != 0:
            return True
    for demand in demands:
        if demand !=0:
            return True
    return False

def calc_penality():

    global cost_table
    global cost_table_cut
    global display_table

    sorted_list = []
    penality_col = []
    penality_row = []
    row = 0
    col = 0
    length  = len(cost_table_cut[0])
    breadth = len(cost_table_cut)

    # calculate row penality 
    for i,row in enumerate(cost_table_cut):
        if(supplies[i]!=0) :
            sorted_list = np.sort(row)
            if(sorted_list[1] !="z"):
                display_table[i][length+2]= float(sorted_list[1]) - float(sorted_list[0])
                penality_row.append(float(sorted_list[1]) - float(sorted_list[0]))
            else:
                display_table[i][length+2]=(float(sorted_list[0]))
                penality_row.append(float(sorted_list[0]))

        else :
            display_table[i][length+2] = 0
            penality_row.append(0)


    penality_row = np.array(penality_row)
    cost_table_cut   = np.transpose(cost_table_cut)

    # calculate col penality 
    for j,col in enumerate(cost_table_cut):
        if(demands[j]!=0) :
            sorted_list = np.sort(col)
            if(sorted_list[1] !="z"):
                display_table[breadth+1][j+1]=float(sorted_list[1]) - float(sorted_list[0])
                penality_col.append(float(sorted_list[1]) - float(sorted_list[0]))
            else:
                display_table[breadth+1][j+1]=(float(sorted_list[0]))
                penality_col.append(float(sorted_list[0]))
        
        else :
            display_table[breadth+1][j+1] = 0
            penality_col.append(0)
    penality_col = np.array(penality_col)
    cost_table_cut = np.transpose(cost_table_cut)

    if np.max(penality_row)>np.max(penality_col) :
        row = penality_row.argmax()
        col = cost_table_cut[row].argmin()
        display_table[row][length+2] = GREEN + str(display_table[row][length+2]) + END
    else :
        cost_table_cut = np.transpose(cost_table_cut)
        col = penality_col.argmax()
        row = cost_table_cut[col].argmin()
        display_table[breadth+1][col+1] = GREEN + str(display_table[breadth+1][col+1]) + END
        cost_table_cut = np.transpose(cost_table_cut)
    return row,col

def color_and_show_table(row_or_column,index,index_comp):
    
    global cost_table_cut
    col_count   = len(cost_table[0])
    row_count  = len(cost_table)
    cost_table_cut = cost_table_cut.tolist()
    
    if row_or_column == 'row':
        for col in range(col_count):
            if(demands[col] != 0 or col == index_comp):
                if(col == index_comp):
                    key_cell = ''.join(superscript_chars.get(char, char) for char in ("["+str(ans_table[index][col])+"]"))
                    display_table[index][col+1] = RED + key_cell + str(cost_table[index][col]) + END
                else:
                    display_table[index][col+1] = RED + str(cost_table[index][col]) + END
                cost_table_cut[index][col]  = "z"

        display_table[index][col_count + 1] =  RED + str(supplies[index]) + END 
        display_table[row_count][index_comp +1] = str(demands[index_comp])
        display_table[index][0] = RED + display_table[index][0] + END
        

    else:
        for row in range(row_count):
            if(supplies[row] != 0 or row == index_comp):
                if(row == index_comp):
                    key_cell = ''.join(superscript_chars.get(char, char) for char in ("["+str(ans_table[row][index])+"]"))
                    display_table[row][index+1] = RED + key_cell + str(cost_table[row][index]) + END
                else:
                    display_table[row][index+1] = RED + str(cost_table[row][index]) + END
                cost_table_cut[row][index]  = "z"
        display_table[row_count][index+1] = RED + str(demands[index]) + END
        display_table[index_comp][col_count+1] = str(supplies[index_comp])
        head[index + 1] = RED + head[index + 1] + END

    # head = [f"D{col + 1}" for col in range(col_count)]
    # head = ["O\D"] + head + ["CAPACITY"]

    # remove penality
    # data_to_display = [row[:-1] for row in display_table[:-1]]
    # head1 = head[:-1]
    # print(tabulate(data_to_display ,headers=head1, tablefmt="grid",stralign="right", numalign="right"))
    # print(" ")

    
    print(tabulate(display_table,headers=head,tablefmt="grid",stralign="right", numalign="right"))
    print(" ")
    
def vam():


    # intializing local variables
    check = True
    row_or_column =""
    count = 0
    index = 0
    index_comp = 0
   
    while(check == True):

        count = count + 1
        r,c = calc_penality()
    
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

        # print("Iteration No. : ",count,f'        Allocation T({r+1},{c+1}) : {cost_table[r][c]}', )
        # print(tabulate(display_table,headers=head,tablefmt="grid",stralign="right", numalign="right"))
        # print(" ")
        print("   Iteration No. : ",count)
        color_and_show_table(row_or_column,index,index_comp)

def calc_and_display_cost():
    total_cost = 0
    for r,row in enumerate(cost_table):
         for c,value in enumerate(row):
             total_cost = total_cost + value*ans_table[r][c]
    print("Total Transportation Cost : ",total_cost)
    print(" ")

# calling functions 
# comment to use default values   
cost_table,ans_table,supplies,demands = get_user_inputs()
display_table,cost_table_cut,head = create_display_table()
vam()
calc_and_display_cost()

