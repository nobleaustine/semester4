# required libraries
from tabulate import tabulate   #to tabulate data
import numpy as np

# default table for test running
display_table = []

capacities    = []
demands       = []
cost_table    = []
no_origins    = 3
no_destinations = 4

capacities = [x for x in [7,9,18]]
demands    = [y for y in [5,8,7,14]]
cost_table = [z for z in [[19,30,50,10],[70,30,40,60],[40,8,70,20]]]
 

# cost_table.append([1,2,3,4])
# cost_table.append([4,3,2,0])
# cost_table.append([0,2,2,1])
# print(" ")
# print("----------------------------------------------------------------- ")
# print(" ")
# print("User Inputs :")
# print(" ")

# no_origins = int(input("Enter the number of origins/sources   : "))
# no_destinations = int(input("Enter the number of destinations      : "))
# print(" ")

ans_table  = np.zeros((no_origins,no_destinations),dtype=int) 

# print("Enter the cost of transportation in the")
# print("increasing order of destinations label like,")
# print("D0, D1, D3, .... for each origin, O1, O2, O3, ...")
# print(" ")
# for i in range(no_origins):
#     input_row  = [int(x) for x in input(f'          O{i} : ').split()]
#     cost_table.append(input_row)
# print(" ")

# print("Enter the demand of each destination in the")
# print("increasing order of the destinations label  : ",end=" ")
# demands = [int(x) for x in input().split()]
# print(" ")

# print("Enter the capacity of each origin in the")
# print("increasing order of the origin label        : ",end=" ")
# capacities = [int(x) for x in input().split()]
# print(" ")
# print("----------------------------------------------------------------- ")
print(" ")

def create_display_table(cost_table,ans_table,demands,capacities,display_table):

    length  = len(cost_table[0])
    breadth = len(cost_table)

    for row in range(breadth):
        insert_row = ["["+ str(ans_table[row][col]) +","+ str(cost_table[row][col]) +"]" for col in range(length)]
        insert_row = [f'O{row}'] + insert_row + [str(capacities[row])]
        display_table.append(insert_row)
    insert_row = [str(value) for value in demands]
    insert_row = ["DEMANDS"] + insert_row + ["-"]
    display_table.append(insert_row)
    
    head = [f"D{col}" for col in range(length)]
    head = ["O\D"] + head + ["CAPACITY"]
    print("               TRANSPORTATION TABLE")
    print(tabulate(display_table,headers=head, tablefmt="grid"))
    print(" ")
    
def finish_or_not(list_check):
    for element in list_check:
        if element != 0:
            return True
    return False

def color_and_show_table(cost_table,ans_table,demands,capacities,display_table,row_or_column,index,other_part):
    length   = len(cost_table[0])
    breadth  = len(cost_table)
    updated_row = []
    if row_or_column == 'row':
        
        updated_row = ['\033[32m'+ "["+ str(ans_table[index][col]) +","+ str(cost_table[index][col]) +"]" + '\033[0m' for col in range(length)]
        display_table[index] = [display_table[index][0]] + updated_row + ['\033[32m'+ str(capacities[index]) + '\033[0m']
        display_table[breadth][other_part +1] = str(demands[other_part]) 
        

    else:
        for i in range(breadth):
            display_table[i][index+1] = '\033[32m'+ "["+ str(ans_table[i][index]) +","+ str(cost_table[i][index]) +"]" + '\033[0m' 
        display_table[breadth][index+1] = '\033[32m'+ str(demands[index]) + '\033[0m'
        display_table[other_part][length+1] = str(capacities[other_part])

    head = [f"D{col}" for col in range(length)]
    head = ["O\D"] + head + ["CAPACITY"]
    print(tabulate(display_table,headers=head, tablefmt="grid"))
    print(" ")

def least_cost_method(cost_table,ans_table,demands,capacities,display_table):


    # length   = len(cost_table[0])
    # breadth  = len(cost_table)
    check = True
    row_or_column =""
    count = 0
    index = 0
    other_part = 0

    while(check == True):

        count = count + 1
        r = 0
        c = 0
        minValue = 999999
        for i,row in enumerate(cost_table):
            for j, cost in enumerate(row):
                if(cost<minValue and capacities[i] !=0 and demands[j]!=0):
                    r = i
                    c = j
                    minValue = cost
        if(demands[c]<capacities[r]):
            ans_table[r][c] = demands[c]
            capacities[r] = capacities[r] - demands[c]
            demands[c] = 0
            row_or_column = "col"
            index = c 
            other_part=r
        else :
            ans_table[r][c] = capacities[r]
            demands[c] = demands[c] - capacities[r]
            capacities[r] = 0
            row_or_column = "row"
            index = r
            other_part=c

        capacity_check = finish_or_not(capacities)
        demand_check   = finish_or_not(demands)

        if(capacity_check or demand_check):
            check = True
        else:
            check = False
        print("Iteration No. : ",count,f'| Minimum Value T({r+1},{c+1}) : {minValue}', )
        color_and_show_table(cost_table,ans_table,demands,capacities,display_table,row_or_column,index,other_part)

def show_cost(cost_table,ans_table):
    sum = 0
    for r,row in enumerate(cost_table):
         for c,value in enumerate(row):
             sum = sum + value*ans_table[r][c]
    print("Transportation Cost : ",sum)

def calculate_ui_vi(cost_table,ans_table):
    # initializing variables
    row_count = len(ans_table)       # count of rows and columns of ans_table
    col_count = len(ans_table[0])

    U = {}                           # dictionaries to store ui and vj values calculated  
    V = {}                           # from cost_table with basic variables in ans_table
   
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
    return U,V

def display_ui_vj_table(cost_table,ans_table,ui_vj_table,V,U):

    superscript_chars = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵',
                         '6': '⁶','7': '⁷','8': '⁸', '9': '⁹','[': '⁽',']': '⁾',}
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
    
def calc_d_table(d_table,V,U,ans_table,cost_table):

    row_count = len(ans_table)
    for row in range(row_count):
        d_row = []
        for col,value in enumerate(ans_table[row]):
            if(value == 0):
                d_row.append(cost_table[row][col] -(U[f'u{row}'] + V[f'v{col}']))
                
            else:
                d_row.append(0)
        d_table.append(d_row)

def print_d_table(d_table):

    col_count   = len(d_table[0])
    row_count   = len(d_table)

    for row in range(row_count):
        d_table[row].insert(0,f'O{row}')
        for col in range(col_count + 1):
            if(d_table[row][col] == 0):
                d_table[row][col] = "---"


    
    head = [f"D{col}" for col in range(col_count)]
    head = ["O\D"] + head
    print(tabulate(d_table,headers=head, tablefmt="grid"))
    
def calc_d_minValue(d_table):

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

def find_path_col(start,ans_table,path):
    last = path[len(path)-1]
    if(start != last):
        for row in range(len(ans_table)):
            if(ans_table[row,last[1]] != 0 and row != last[0]):
                path.append([row,last[1]])
                # print(path)
                find_path_row(start,ans_table,path)
                last = path[len(path)-1]
                if(start == last):
                    return
        path.pop(len(path)-1)
    else:
        return
    
def find_path_row(start,ans_table,path):
    last = path[len(path)-1]
    if(start != last):
        for col,value in enumerate(ans_table[last[0]]):
            if(value !=0 and col != last[1]):
                path.append([last[0],col])
                # print(path)
                find_path_col(start,ans_table,path)
                last = path[len(path)-1]
                if(start == last):
                    return
        path.pop(len(path)-1)
    else:
        return 

def start_path_find(start,ans_table,path):
    start_row    = ans_table[start[0]]
    start_column = [ans_table[row][start[1]] for row in range(len(ans_table)) ]
    ans_table[start[0]][start[1]] = 1
    # print(start_column,start_row)

    for col,value in enumerate(start_row):
        if(value != 0 and col != start[1]):
            path.append([start[0],col])
            # print(path)
            find_path_col(start,ans_table,path)
            last = path[len(path)-1]
            if(start == last):
                return
            else:
                path.pop(len(path)-1)

    for row, value in enumerate(start_column):
            if(value != 0 and row != start[0]):
                path.append([row,start[1]])
                # print(path)
                find_path_row(start,ans_table,path)
                last = path[len(path)-1]
                if(start == last):
                    return
                else:
                    path.pop(len(path)-1)

def new_allocations_print(ans_table,path):
    
    length = len(path)
    col_count   = len(ans_table[0])
    row_count   = len(ans_table)
    superscript_chars = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵',
                         '6': '⁶','7': '⁷','8': '⁸', '9': '⁹','[': '⁽',']': '⁾',}
    insert_row  = []
    view_table  = []

    head = [f"D{col}" for col in range(col_count)]
    head = ["O\D"] + head 

    negative_values = [ans_table[path[i][0]][path[i][1]] for i in range(1,length,2)]
    min_value_neg_label = min(negative_values)
    # print(min_value_neg_label,negative_values)
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

        insert_row = [f'O{row}'] + insert_row 
        view_table.append(insert_row)
        insert_row = []
    
    for i,dim in enumerate(path):
        if(i%2 == 0):
            view_table[dim[0]][dim[1]+1] = "\u001b[32m" + view_table[dim[0]][dim[1]+1] + '\033[0m'
        else:
            view_table[dim[0]][dim[1]+1] = "\u001b[31m" + view_table[dim[0]][dim[1]+1] + '\033[0m'
    
    print("Transportation Table Adding value ",min_value_neg_label)
    print(tabulate(view_table,headers=head, tablefmt="grid",stralign="right", numalign="right"))
    print(" ")

def final_table(cost_table,ans_table,demands,capacities,display_table):
    
    superscript_chars = {'0': '⁰','1': '¹','2': '²','3': '³','4': '⁴','5': '⁵',
                         '6': '⁶','7': '⁷','8': '⁸', '9': '⁹','[': '⁽',']': '⁾',}
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
        insert_row = [f'O{row}'] + insert_row + [str(capacities[row])]
        display_table.append(insert_row)

    insert_row = [str(value) for value in demands]
    insert_row = ["DEMANDS"] + insert_row + ["-"]
    display_table.append(insert_row)
    
    head = [f"D{col}" for col in range(col_count)]
    head = ["O\D"] + head + ["CAPACITY"]
    print("            FINAL TRANSPORTATION TABLE")
    print(tabulate(display_table,headers=head, tablefmt="grid",stralign="right", numalign="right"))
    print(" ")

def MODI_METHOD(cost_table,ans_table):
    d_table       = []
    ui_vj_table   = []
    U             = {}
    V             = {}
    min_value      = -1
    row           = 0
    col           = 0
    count         = 0
    print(" ")
    print("                 MODI METHOD")
    print(" ")
    while(min_value<0):
        d_table       = []
        ui_vj_table   = []
        U             = {}
        V             = {}
        count += 1
        U,V = calculate_ui_vi(cost_table,ans_table)
        calc_d_table(d_table,V,U,ans_table,cost_table)
        min_value,row,col = calc_d_minValue(d_table)
        
        if(min_value<0):
            print("Iteration No. : ",count)
            print(" ")
            print("Ui-Vj_Table")
            display_ui_vj_table(cost_table,ans_table,ui_vj_table,V,U)
            print(" ")
            print("D_Table")
            print("min_value: d_table("+str(row)+","+str(col) + "):",min_value)
            print_d_table(d_table)
            print(" ")
            start = [row,col]
            path = [[row,col]]

            start_path_find(start,ans_table,path)
            path.pop(len(path)-1)
            new_allocations_print(ans_table,path)
            print(" ")
        else:
            capacities = [x for x in [7,9,18]]
            demands    = [y for y in [5,8,7,14]]
            display_table = []
            final_table(cost_table,ans_table,demands,capacities,display_table)
            show_cost(cost_table,ans_table)

# calling functions           
create_display_table(cost_table,ans_table,demands,capacities,display_table)
least_cost_method(cost_table,ans_table,demands,capacities,display_table)
show_cost(cost_table,ans_table)
MODI_METHOD(cost_table,ans_table)




