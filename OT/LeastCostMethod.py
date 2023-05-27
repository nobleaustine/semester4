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
# print(" ")

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
    
    print(" ")
# "\033[30mThis text is in black color.\033[0m"
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
        updated_row = ['\033[30m'+ "["+ str(ans_table[index][col]) +","+ str(cost_table[index][col]) +"]" + '\033[0m' for col in range(length)]
        # updated_row = ['\033[32m'+ "["+ str(ans_table[index][col]) +","+ str(cost_table[index][col]) +"]" + '\033[0m' for col in range(length)]
        display_table[index] = [display_table[index][0]] + updated_row + ['\033[30m'+ str(capacities[index]) + '\033[0m']
        # display_table[index] = [display_table[index][0]] + updated_row + ['\033[32m'+ str(capacities[index]) + '\033[0m']
        display_table[breadth][other_part +1] = str(demands[other_part]) 
        # print(tabulate(display_table, tablefmt="grid"))
        

    else:
        for i in range(breadth):
            display_table[i][index+1] = '\033[30m'+ "["+ str(ans_table[i][index]) +","+ str(cost_table[i][index]) +"]" + '\033[0m' 
            # print(tabulate(display_table, tablefmt="grid"))
        display_table[breadth][index+1] = '\033[30m'+ str(demands[index]) + '\033[0m'
        display_table[other_part][length+1] = str(capacities[other_part])

        # for i in range(breadth):
        #     display_table[i][index+1] = '\033[32m'+ "["+ str(ans_table[i][index]) +","+ str(cost_table[i][index]) +"]" + '\033[0m' 
        #     # print(tabulate(display_table, tablefmt="grid"))
        # display_table[breadth][index+1] = '\033[32m'+ str(demands[index]) + '\033[0m'
        # display_table[other_part][length+1] = str(capacities[other_part])

    head = [f"D{col}" for col in range(length)]
    head = ["O\D"] + head + ["CAPACITY"]
    print(tabulate(display_table,headers=head, tablefmt="grid"))
    print(" ")
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

def MODI_METHOD(cost_table,ans_table):
    print(" ")
    U = {}
    V = {}
    row_index = [0]
    U['u0']   =  0
    column_index = []

    d_row = []
    d_table = []
    min_Value = 0
    row = 0
    col = 0
    
    while(len(U) != len(ans_table) or len(V) != len(ans_table[0])):
    
        for index in row_index:
            for pos,value in enumerate(ans_table[index]):
                check = f'v{pos}' in V
                if(value!=0 and check == False):
                    column_index.append(pos)
                    V[f'v{pos}'] = cost_table[index][pos] -U[f'u{index}']
        
        for index in column_index:
            for pos in range (len(ans_table)):
                check = f'u{pos}' in U
                if(ans_table[pos][index]!=0 and check == False):
                    row_index.append(pos)
                    U[f'u{pos}'] = cost_table[pos][index] -V[f'v{index}']
    print(U,V)
    
    for index in range(len(ans_table)):
        d_row = []
        for pos,value in enumerate(ans_table[index]):
            if(value ==0):
                d_row.append(cost_table[index][pos] -(U[f'u{index}'] + V[f'v{pos}']))
                
            else:
                d_row.append(0)
        d_table.append(d_row)

    print(d_table)

    for r in range(len(d_table)):
        for c in range(len(d_table[0])):
            if(d_table[r][c]<min_Value):
                min_Value = d_table[r][c]
                row = r
                col = c
       
    print(min_Value,row,col)
    path = [[row,col]]
    start = [row,col]
    
    
    start_path_find(start,ans_table,path)
    path.pop(len(path)-1)
    print(path)

    new_allocations(ans_table,path)


def start_path_find(start,ans_table,path):
    start_row    = ans_table[start[0]]
    start_column = [ans_table[row][start[1]] for row in range(len(ans_table)) ]
    ans_table[start[0]][start[1]] = 1
    print(start_column,start_row)

    for col,value in enumerate(start_row):
        if(value != 0 and col != start[1]):
            path.append([start[0],col])
            print(path)
            find_path_col(start,ans_table,path)
            last = path[len(path)-1]
            if(start == last):
                return
            else:
                path.pop(len(path)-1)

    for row, value in enumerate(start_column):
            if(value != 0 and row != start[0]):
                path.append([row,start[1]])
                print(path)
                find_path_row(start,ans_table,path)
                last = path[len(path)-1]
                if(start == last):
                    return
                else:
                    path.pop(len(path)-1)
    
def find_path_row(start,ans_table,path):
    last = path[len(path)-1]
    if(start != last):
        for col,value in enumerate(ans_table[last[0]]):
            if(value !=0 and col != last[1]):
                path.append([last[0],col])
                print(path)
                find_path_col(start,ans_table,path)
                last = path[len(path)-1]
                if(start == last):
                    return
        path.pop(len(path)-1)
    else:
        return 

def find_path_col(start,ans_table,path):
    last = path[len(path)-1]
    if(start != last):
        for row in range(len(ans_table)):
            if(ans_table[row,last[1]] != 0 and row != last[0]):
                path.append([row,last[1]])
                print(path)
                find_path_row(start,ans_table,path)
                last = path[len(path)-1]
                if(start == last):
                    return
        path.pop(len(path)-1)
    else:
        return 

def new_allocations(ans_table,path):
    length = len(path)
    negative_values = [ans_table[path[i][0]][path[i][1]] for i in range(1,length,2)]
    minValue = min(negative_values)
    print(minValue,negative_values)
    ans_table[path[0][0]][path[0][1]] = 0
    if(minValue<0):
        return minValue
    else:
        for i,dim in enumerate(path):
            if(i%2 == 0):
                ans_table[dim[0]][dim[1]] = ans_table[dim[0]][dim[1]] + minValue
            else:
                ans_table[dim[0]][dim[1]] = ans_table[dim[0]][dim[1]] - minValue

       

    


# calling functions           
create_display_table(cost_table,ans_table,demands,capacities,display_table)
least_cost_method(cost_table,ans_table,demands,capacities,display_table)
show_cost(cost_table,ans_table)
MODI_METHOD(cost_table,ans_table)
create_display_table(cost_table,ans_table,demands,capacities,display_table)
