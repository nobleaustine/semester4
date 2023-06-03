# required libraries
from tabulate import tabulate   # tabulate data into tables
import numpy as np              # perform matrix calc

RED = '\033[38;2;225;0;0m'
END = '\033[0m'
superscript_chars = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵','6': '⁶','7': '⁷','8': '⁸', '9': '⁹','[': '⁽',']': '⁾',}
GREEN = "\u001b[32m"

U             = {}
V             = {}
ui_vj_table   = []
d_table       = []

# default table for test running
# cost_table = [z for z in [[19,30,50,10],[70,30,40,60],[40,8,70,20]]]
# supplies = [x for x in [7,9,18]]
# demands    = [y for y in [5,8,7,14]]
# ans_table  = np.zeros((3,4),dtype=int)

# -------------------------- LEAST COST METHOD ------------------------------------
def get_user_inputs():

    print(" ")
    print("-----------------------------------------------------------------")
    print(" ")
    print("User Inputs :")
    print(" ")

    no_sources      = int(input("Enter the number of sources      : "))         
    no_destinations = int(input("Enter the number of destinations : "))
    print(" ")
    
    ans_table  = np.zeros((no_sources,no_destinations),dtype=int)
    cost_table      = []

    print("Enter the cost of transportation in the")
    print("increasing order of destination label like,")
    print("D1, D2, D3, .... for each source, S1, S2, S3, ...")
    print(" ")
    for i in range(no_sources):
        input_row  = [int(x) for x in input(f'          O{i+1} : ').split()]
        cost_table.append(input_row)
    print(" ")

    print("Enter the supply form each origin in ")
    print("the increasing order of the origin label        : ",end=" ")
    supplies = [int(x) for x in input().split()]
    print(" ")

    print("Enter the demand of each destination in ")
    print("the increasing order of the destinations label  : ",end=" ")
    demands = [int(x) for x in input().split()]
    print(" ")

    return cost_table,ans_table,supplies,demands

def create_display_table():
    
    display_table = []
    length  = len(cost_table[0])
    breadth = len(cost_table)
    for row in range(breadth):
        insert_row = [str(cost_table[row][col]) for col in range(length)]
        insert_row = [f'S{row + 1}'] + insert_row + [str(supplies[row])]
        display_table.append(insert_row)
    insert_row = [str(value) for value in demands]
    insert_row = ["DEMAND"] + insert_row + ["-"]
    display_table.append(insert_row)
    
    head = [f"D{col+1}" for col in range(length)]
    head = ["S\D"] + head + ["SUPPLY"]
    print(" ")
    print("TRANSPORTATION TABLE")
    print(tabulate(display_table,headers=head,tablefmt="grid",stralign="right", numalign="right"))
    print(" ")
    return display_table

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
    head = ["S\D"] + head + ["SUPPLY"]
    print(tabulate(display_table,headers=head, tablefmt="grid",stralign="right", numalign="right"))
    print(" ")

def least_cost_method():

    print("----------------------- LEAST COST METHOD -----------------------")
    print(" ")
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

        print("Iteration No.: ",count,f'   min_value: T[{r+1},{c+1}]: {minValue}', )
        color_and_show_table(row_or_column,index,index_comp)

def calc_and_display_cost():
    total_cost = 0
    for r,row in enumerate(cost_table):
         for c,value in enumerate(row):
             total_cost = total_cost + value*ans_table[r][c]
    print("Total Transportation Cost : ",total_cost)

#----------------------------------calculation in modi----------------------------
    
def calculate_ui_vj():

    # initializing variables
    row_count = len(ans_table)       # count of rows and columns of ans_table
    col_count = len(ans_table[0])

    global U                           # dictionaries to store ui and vj values calculated  
    global V 

    U.clear()
    V.clear()                          # from cost_table with basic variables in ans_table
   
    U['u0'] = 0   # setting intial value u0 = 0 in dictionary U to calculate all ui and vj values
                  # also adding row index 0 of "u0" to row_indices_for_vj_calc
    row_indices_for_vj_calc   = [0]  # row E row_indices_for_vj_calc : iterate through columns of ans_table[row] to calc vj 
    column_index_for_ui_calc  = []   # col E column_index_for_ui_calc : iterate through rows of ans_table[][col] to calc uj
                   
    while(len(U) != row_count or len(V) != col_count):                  # should calc vj and uj and insert to U and V till  
                                                                        # len of U and V reach the row and column count res...  
        for row in row_indices_for_vj_calc:                             # enumerate through list ans_table[row] for row E   
            for col,variable_value in enumerate(ans_table[row]):        # row_indices_for_vj_calc with col as column for vj calc and 
                                                                        # variable_value to check if it is a basic variable or not
                check_if_present = f'v{col}' in V                       # (check_if_present = False => V has no V(col)  
                if(variable_value!= 0 and check_if_present == False):   # variable_value = ans_table(row,col) != 0 => variable_value
                                                                        # E m+n-1 basic variable) => calc V(col)
                    column_index_for_ui_calc.append(col)                # adding to column_index_for_ui_calc to use for ui calc
                    V[f'v{col}'] = cost_table[row][col] -U[f'u{row}']   # calc V(col) = C(row)(col) - U(row)
                                                                       
                    
        row_indices_for_vj_calc = [] # emptying row_indices_for_vj_calc to calc new rows by going through column E column_index_for_ui_calc
        # uncomment for detailed explanation
        # print("column indices for uj alocation : ",column_index_for_ui_calc)
        # print("modified V from the iteration   :",V)
        # print(" ")

        for col in column_index_for_ui_calc:                               # traverse through ans_table[row][col] for col E   
            for row in range (row_count):                                  # column_indices_for_uj_calc with row E (0,row_count) 

                check_if_present = f'u{row}' in U                          # (check_if_present = False => U has no U(row)
                if(ans_table[row][col]!=0 and check_if_present == False):  # ans_table(row,col) != 0 => ans_table(row,col)
                                                                           # E m+n-1 basic variable) => calc U(row)
                    row_indices_for_vj_calc.append(row)                    # adding to row_index_for_vj_calc to use for vj calc
                    U[f'u{row}'] = cost_table[row][col] -V[f'v{col}']      # calc U(row) = C(row)(col) - V(col)

        column_index_for_uj_calc = [] # emptying column_index_for_uj_calc to calc new columns by going through row E row_indices_for_vj_calc
        # uncomment for detailed explanation
        # print("row indices for vj alocation  : ",row_index_for_uj_calc)
        # print("modified U from the iteration :",U)
        #print(" ")

    # uncomment to view completed V and U
    # print(U,V)

def calc_d_table():
    
    d_row   = []
    global d_table 

    d_table.clear()
    row_count = len(ans_table)

    for row in range(row_count):
        d_row = []
        for col,value in enumerate(ans_table[row]):
            if(value == 0):
                d_row.append(cost_table[row][col] -(U[f'u{row}'] + V[f'v{col}']))
                
            else:
                d_row.append(0)
        d_table.append(d_row)
    
def calc_d_min_value():

    global d_table

    min_value = 0
    row       = 0
    col       = 0
    for r in range(len(d_table)):
        for c in range(len(d_table[0])):
            if(d_table[r][c]<min_value):
                min_value = d_table[r][c]
                row = r
                col = c
    
    return min_value,row,col

#-------------------------------------display in modi----------------------------

def display_ui_vj_table():

    
    ui_vj_table = []
    col_count   = len(ans_table[0])
    row_count   = len(ans_table)
    insert_row  = []

    for row in range(row_count):
        for col in range(col_count):

            if(ans_table[row][col] != 0):
                value = ''.join(superscript_chars.get(char, char) for char in ("["+str(ans_table[row][col])+"]"))
                insert_row.append(value + str(cost_table[row][col]))
            else:
                insert_row.append(str(cost_table[row][col]))

        insert_row = [f'O{row}'] + insert_row + [str(U[f'u{row}'])]
        ui_vj_table.append(insert_row)
        insert_row = []

    

    for col in range(col_count):
        insert_row.append(V[f'v{col}'])

    insert_row = ["vj"] + insert_row + ["-"]
    ui_vj_table.append(insert_row)
    
    head = [f"D{col}" for col in range(col_count)]
    head = ["O\D"] + head + ["ui"]
    print(tabulate(ui_vj_table,headers=head, tablefmt="grid",stralign="right", numalign="right"))

def display_d_table():

    global d_table

    col_count   = len(d_table[0])
    row_count   = len(d_table)

    for row in range(row_count):
        d_table[row].insert(0,f'O{row}')
        for col in range(col_count + 1):
            if(d_table[row][col] == 0):
                d_table[row][col] = "---"


    
    head = [f"D{col}" for col in range(col_count)]
    head = ["O\D"] + head
    print(tabulate(d_table,headers=head, tablefmt="grid",stralign="right", numalign="right"))
    
def find_path_col(start,path):

    global ans_table

    last = path[len(path)-1]
    if(start != last):
        for row in range(len(ans_table)):
            if(ans_table[row,last[1]] != 0 and row != last[0]):
                path.append([row,last[1]])
                # print(path)
                find_path_row(start,path)
                last = path[len(path)-1]
                if(start == last):
                    return
        path.pop(len(path)-1)
    else:
        return
    
def find_path_row(start,path):

    global ans_table
    last = path[len(path)-1]
    if(start != last):
        for col,value in enumerate(ans_table[last[0]]):
            if(value !=0 and col != last[1]):
                path.append([last[0],col])
                # print(path)
                find_path_col(start,path)
                last = path[len(path)-1]
                if(start == last):
                    return
        path.pop(len(path)-1)
    else:
        return 

def start_path_search(start,path):


    start_row    = ans_table[start[0]]
    start_column = [ans_table[row][start[1]] for row in range(len(ans_table)) ]
    ans_table[start[0]][start[1]] = 1
    # print(start_column,start_row)

    for col,value in enumerate(start_row):
        if(value != 0 and col != start[1]):
            path.append([start[0],col])
            # print(path)
            find_path_col(start,path)
            last = path[len(path)-1]
            if(start == last):
                return
            else:
                path.pop(len(path)-1)

    for row, value in enumerate(start_column):
            if(value != 0 and row != start[0]):
                path.append([row,start[1]])
                # print(path)
                find_path_row(start,path)
                last = path[len(path)-1]
                if(start == last):
                    return
                else:
                    path.pop(len(path)-1)

def display_new_allocations(path):
    
    length = len(path)
    col_count   = len(ans_table[0])
    row_count   = len(ans_table)
    
    insert_row  = []
    view_table  = []

    head = [f"D{col}" for col in range(col_count)]
    head = ["O\D"] + head #+ ["SUPPLY"]

    negative_values = [ans_table[path[i][0]][path[i][1]] for i in range(1,length,2)]
    min_value_neg_label = min(negative_values)
    ans_table[path[0][0]][path[0][1]] = 0

    for i,dim in enumerate(path):
        if(i%2 == 0):
            ans_table[dim[0]][dim[1]] = ans_table[dim[0]][dim[1]] + min_value_neg_label
        else:
            ans_table[dim[0]][dim[1]] = ans_table[dim[0]][dim[1]] - min_value_neg_label
    
    
    for row in range(row_count):
        for col in range(col_count):

            if(ans_table[row][col] != 0):
                value = ''.join(superscript_chars.get(char, char) for char in ("["+str(ans_table[row][col])+"]"))
                insert_row.append(value + str(cost_table[row][col]))
            else:
                insert_row.append(str(cost_table[row][col]))

        insert_row = [f'O{row}'] + insert_row #+ [str(final_table_supplies[row])]
        view_table.append(insert_row)
        insert_row = []
    
    for i,dim in enumerate(path):
        if(i%2 == 0):
            view_table[dim[0]][dim[1]+1] = GREEN + view_table[dim[0]][dim[1]+1] + END
        else:
            view_table[dim[0]][dim[1]+1] = RED + view_table[dim[0]][dim[1]+1] + END
    
    # insert_row = [str(value) for value in final_table_demands]
    # insert_row = ["DEMANDS"] + insert_row + ["-"]
    # view_table.append(insert_row)
    
    print("Allocation Modification   value:",min_value_neg_label)
    print(tabulate(view_table,headers=head, tablefmt="grid",stralign="right", numalign="right"))
    print(" ")

def display_final_table():
     
    global display_table
    display_table.clear()
    col_count  = len(cost_table[0])
    row_count  = len(cost_table)
    insert_row = []

    for row in range(row_count):
        insert_row=[]
        for col in range(col_count):

            if(ans_table[row][col] != 0):
                value = ''.join(superscript_chars.get(char, char) for char in ("["+str(ans_table[row][col])+"]"))
                insert_row.append(value + str(cost_table[row][col]))
            else:
                insert_row.append(str(cost_table[row][col]))
        insert_row = [f'O{row}'] + insert_row + [str(final_table_supplies[row])]
        display_table.append(insert_row)

    insert_row = [str(value) for value in final_table_demands]
    insert_row = ["DEMANDS"] + insert_row + ["-"]
    display_table.append(insert_row)
    
    head = [f"D{col}" for col in range(col_count)]
    head = ["O\D"] + head + ["CAPACITY"]
    print("FINAL TRANSPORTATION TABLE")
    print(tabulate(display_table,headers=head, tablefmt="grid",stralign="right", numalign="right"))
    print(" ")

def modi_method():
    
    
    calculate_ui_vj()
    calc_d_table()
    min_value,row,col = calc_d_min_value()
    count     =  0

    print(" ")
    print("-------------------------- MODI METHOD --------------------------")
    print(" ")
    while(min_value<0):
        
        count += 1
        
        print("Iteration No.: ",count)
        print(" ")
        print("ui-vj Table")
        display_ui_vj_table()
        print(" ")

        print("d_Table","   min_value: T["+str(row)+","+str(col) + "]:",min_value)
        display_d_table()
        print(" ")
        
        start = [row,col]
        path = [[row,col]]

        start_path_search(start,path)
        path.pop(len(path)-1)

        display_new_allocations(path)
        print(" ")
        calc_and_display_cost()
        print(" ")
        
        calculate_ui_vj()
        calc_d_table()
        min_value,row,col = calc_d_min_value()
    

        
    display_final_table()
    print("Least ",end='')
    calc_and_display_cost()
    print(" ")
    print("-----------------------------------------------------------------")


# calling functions     
cost_table,ans_table,supplies,demands = get_user_inputs()
display_table = create_display_table()
print("-----------------------------------------------------------------")

final_table_supplies = [supply for supply in supplies]
final_table_demands = [demand for demand in demands]

least_cost_method()
calc_and_display_cost()
print(" ")
print("-----------------------------------------------------------------")
modi_method()





