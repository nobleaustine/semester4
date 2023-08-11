from tabulate import tabulate   # tabulate data into tables
import numpy as np              # perform matrix calc
import re


GREEN = '\x1b[32m0\x1b[0m'
green = '\x1b[32m'
RED   = '\x1b[38;2;225;0;0m0\x1b[0m'
END   = '\033[0m'
TICK  = "\u2713"
WHITE_BG_B = "\033[30;47m"
WHITE_BG_R = "\033[38;2;225;0;0;47m0\033[0m"
WHITE_BG_G = "\033[32;47m0\033[0m"

table         = []
cost          = []
display_table = []
index         = 0
head          = []

# default table for test running
# table = np.array([[160,130,175,190,200],[135,120,130,160,175],[140,110,155,170,185],[50,50,80,80,110],[55,35,70,80,105]])
# cost  = np.array([[160,130,175,190,200],[135,120,130,160,175],[140,110,155,170,185],[50,50,80,80,110],[55,35,70,80,105]])
table = np.array([[99,4,7,3,4],[4,99,6,3,4],[7,6,99,7,5],[3,3,7,99,7],[4,4,5,7,99]])
cost  = np.array([[99,4,7,3,4],[4,99,6,3,4],[7,6,99,7,5],[3,3,7,99,7],[4,4,5,7,99]])

index = len(table)
head = [f'J{col + 1}' for col in range(index)]
head = ['W\J'] + head + ["---"]

def print_table(p_table):
    global head

    print(tabulate(p_table,headers = head, tablefmt="grid",stralign="right", numalign="right"))

def print_separator():
    print(" ")
    print("-----------------------------------------------------")
    print(" ")

def update_display_table():
    # global table
    global display_table
    global index
    display_table = [] # emptying the display_table to input new value after updating table

    for row in range(index):
        display_table.append([str(value) for value in table[row]])
        display_table[row] = [f'w{row + 1}'] + display_table[row]

def get_user_inputs():
    # global table
    # global cost
    # global display_table
    global head
    global index
    temp_table = []

    print_separator()
    print("User Inputs...")
    print(" ")

    index = int(input("Enter the number of workers/jobs : "))        
    print(" ")

    print("Enter the cost/charge of performing the")
    print("jobs in the increasing order of job label like,")
    print("j1, j2, j3, .... for each sworker, w1, w2, w33, ...")
    print(" ")
    

    for i in range(index):  # taking the data to a temporary variable
        input_row  = [int(x) for x in input(f'          w{i+1} : ').split()]
        temp_table.append(input_row)
    
    table = np.array(temp_table) # table to perform Hungarian Method
    
    for i in range(index):       # saving a copy of table as cost to calc total cost
        input_row  = [x for x in table[i]]
        cost.append(input_row)

    head = [f'J{col + 1}' for col in range(index)] # header or column label of table
    head = ['W\J'] + head + ["---"]

    update_display_table() # creating a table with column and row label
    
    print(" ")
    print("Hungarian Method Table")
    print(tabulate(display_table,headers = head, tablefmt="grid",stralign="right", numalign="right"))
    print_separator()

def substract_min():
    global table

    min_values = np.min(table,axis=1,keepdims=True)
    table = table - min_values

    min_values = np.min(table,axis=0,keepdims=True)
    table = table - min_values

def get_arbit_zero():
    global display_table
    global index

    for i in range(index):
        for j in range(index):
            if display_table[i][j] == '0':
                return True,i,j
    
    return False,0,0

def assign_values():

    # global table
    global display_table
    global index

    check_if_zero = True      # to check for zero and continue assigning 
    assign_happen = False     # to check if assigning is happening or its a loop
    pos_r_zero  = 0           # row of a aribitary zero
    pos_c_zero  = 0           # column of a aribitary zero
    
 
    while check_if_zero == True:

        # assigning values to zeros in a row if it has only one zero and marking all other
        for row in range(index):
            count = 0
            for col in range(1,index+1):
                if display_table[row][col] == '0' and count == 0:
                    pos   = col
                    count += 1
                else:
                    count += 1
                    break

            if count == 1 :
                for r in range(index):
                    if display_table[r][pos] == '0':
                        display_table[r][pos] = RED
                display_table[row][pos] = GREEN
                assign_happen = True # to check if assigning is happening

        # assigning values to zeros in a col if it has only one zero 
        for col in range(1,index+1):
            count = 0
            for row in range(index):
                if(display_table[row][col]=='0' and count == 0):
                    pos = row
                    count +=1
                else:
                    count +=1
                    break

            if count == 1:
                for c in range(1,index+1):
                    if display_table[pos][c] == '0':
                        display_table[pos][c] = RED 
                display_table[pos][col] = GREEN
                assign_happen = True

        check_if_zero,pos_r_zero,pos_c_zero = get_arbit_zero()

        if(assign_happen == False and check_if_zero == True):
            for r in range(index):
                    if display_table[r][pos_c_zero] == '0':
                        display_table[r][pos_c_zero] = RED 
            for c in range(1,index+1):
                    if display_table[pos_r_zero][c] == '0':
                        display_table[pos_r_zero][c] = RED 
            display_table[pos_r_zero][pos_c_zero] = GREEN

        assign_happen = False
    
def ticking_rows_cols(view_table):

    global display_table
    global index
    ticking = False
    
    # marking row if its not assigned
    for row in range(index):
        
        insert_row = [value for value in display_table[row]]
        view_table.append(insert_row)

        if GREEN not in view_table[row] and RED in view_table[row]:
           view_table[row].append(TICK)
        else:
            view_table[row].append('---')
    
    insert_row = ["---" for i in range(index+2)]
    view_table.append(insert_row)

    while ticking == True:

        ticking = False
        for row in range(index):

            if(view_table[row][index+1] == TICK):

                for col in range(index):
                    if(view_table[row][col] == RED):
                        view_table[index][col] = TICK
                        ticking = True
                        
        for col in range(1,index+1):

            if(view_table[index][col] == TICK):

                for row in range(index):
                    if(view_table[row][col] == GREEN):
                        view_table[row][index+1] = TICK
                        ticking = True
                  
def draw_color_line(view_table):

    global table
    global display_table

    count = 0

    for i in range(index):
        if view_table[i][index+1] != TICK:
            count = count + 1
            for j in range(index+1):
                if view_table[i][j] == GREEN:
                    view_table[i][j] = WHITE_BG_G 
                elif view_table[i][j] == RED:
                    view_table[i][j] = WHITE_BG_R
                elif view_table[i][j].isdigit() == True:
                  view_table[i][j] = WHITE_BG_B +  view_table[i][j] + END 
      
    for j in range(index + 1):
        if view_table[index][j] == TICK:
            count = count+1
            for i in range(index):
                if view_table[i][j] == GREEN:
                    view_table[i][j] = WHITE_BG_G 
                elif view_table[i][j] == RED:
                    view_table[i][j] = WHITE_BG_R
                elif view_table[i][j].isdigit() == True:
                  view_table[i][j] = WHITE_BG_B +  view_table[i][j] + END

    return count

def find_min_value_and_modify(view_table):

    global table
    global index
   
    min_value = 999

    for r in range(index):
        for c in range(index):
            if view_table[r][c+1].isdigit() == True and table[r][c] < min_value:
                min_value = table[r][c]

    for r in range(index):
        for c in range(index):
            if view_table[r][c+1].isdigit() == True :
                table[r][c] = table[r][c] - min_value
            elif view_table[r][index+1] != TICK and view_table[index][c+1] == TICK:
                table[r][c] = table[r][c] + min_value

    return min_value   

def calc_cost():

    global index
    global display_table
    global cost
    sum = 0

    for row in range(index):
        for col in range(1,index+1):
            if display_table[row][col] == GREEN:
                sum = sum + cost[row][col-1]
    print(sum)

def calc_final_table(view_table):
    global display_table
    global cost
    global index
    
    
    for row in range(index):
        for col in range(index):
            if view_table[row][col+1] == WHITE_BG_G:
                display_table[row][col+1] = green + str(cost[row][col]) + END
            else :
                display_table[row][col+1] = str(cost[row][col])

def hungarian_method():
    
    global table
    global display_table
    global index
    global head

    count         = 0
    no_allocation = 0
    view_table    = []

    update_display_table()
    
    while(no_allocation < index):

        count +=1
        view_table = []

        assign_values()
        ticking_rows_cols(view_table)
        no_allocation = draw_color_line(view_table)
        
        if no_allocation < index :
            print("Iteration No : ",count)
            print(" ")
            print("allocating jobs to workers...")
            print(tabulate(display_table,headers = head, tablefmt="grid",stralign="right", numalign="right"))
            print("Total no. of allocations :",no_allocation)
            print("Total cost :",end="")
            calc_cost()
            print("")

            print("marking rows and columns...")
            print(tabulate(view_table,headers = head, tablefmt="grid",stralign="right", numalign="right"))
            print("")

            min_value = find_min_value_and_modify(view_table)
            update_display_table()

            print("updating table...")
            print(tabulate(display_table,headers = head, tablefmt="grid",stralign="right", numalign="right"))
            print("Minimum Value :",min_value)
            print("") 
            print("-----------------------------------------------------")
            print("")
        else:
            calc_final_table(view_table)
            print("Final Hungarian Method Table")
            print(tabulate(display_table,headers = head, tablefmt="grid",stralign="right", numalign="right"))
            update_display_table()
            assign_values()
            print("Total no. of allocations :",no_allocation)
            print("Minimum total cost :",end="")
            calc_cost()
            print("-----------------------------------------------------")
            print("")





        




    

