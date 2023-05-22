# importing required libraries
import numpy as np  # for performing matrix operations on simplex table
import pandas as pd # for labeling the data and introducing a data frame
import re           # regular expressions for manipulating strings


# required functions
# funtion to convert inequalities to equations by adding surplus and substracting slack variables
def ConvertToEquation(constraints):

    sVariableCount = 0  # count of slack or surplus variables to add new variable as -1/1s{sVariableCount}

    # adding slack or surplus variables and changing to equation
    # by iterating through constraints and checking for >/</>=/<= on each constraint
    # and modifing the constrints by replacing the symbol found with f'+ -1/1s{sVariableCount} ='
    for i,constraint in enumerate(constraints):

        # updating count variable
        # substituting the symbol in if-elif-else condition with f'+ -1s{sVariableCount} ='
        # same step repeated in other conditions depending on symbol encountered   
        if(constraint.find(">=")!=-1):
            sVariableCount +=1 
            constraints[i]=re.sub(">=",f'+ -1s{sVariableCount} =' ,constraint) 

        elif(constraint.find(">")!=-1 ): 
            sVariableCount +=1
            constraints[i]=re.sub(">",f'+ -1s{sVariableCount} =' ,constraint)

        elif(constraint.find("<=")!=-1):
            sVariableCount +=1
            constraints[i]=re.sub("<=",f'+ 1s{sVariableCount} =' ,constraint)

        elif(constraint.find("<")!=-1):
            sVariableCount +=1
            constraints[i]=re.sub("<",f'+ 1s{sVariableCount} =' ,constraint)

# to get the variables in the constraint equations
def GetVariables(constraints):

    # extracting actual and s variables to 2 separate list actualVariables and sVariables using 
    # list comprehension by going through each constrain in constraints and letter in each
    # constrain searching for "x" and "s" then the two list are removed of duplicates and sorted again
    # and joined to a single list variables in the order x1,x2,x3...,s1,s2,s3,...

    # extracting variables by checking "x","s"
    actualVariables = [constrain[i:i+2] for constrain in constraints for i,letter in enumerate(constrain)  if letter == "x" ]
    sVariables = [constrain[i:i+2] for constrain in constraints for i,letter in enumerate(constrain)  if letter == "s" ] 

    # sorting and removing duplicates 
    actualVariables = sorted(list(set(actualVariables)))
    sVariables = sorted(list(set(sVariables)))

    # creating list of variables by joining two lists
    variables = actualVariables + sVariables

    return variables

# completing constraints by adding 0 as coefficient to the s variables,
# rearranging each constraint by the order of variables in the list variables like 
# from 2x5 + 3x4 + 0s3 = -3 to a1x1 + a2x2 + ... +3x4 + 2x5 + ... + anxn + b1s1 + b2s2 + ... + 0s3 + ... + bnsn
#  and also extracting coefficients of each variable to form simplex table like CB XB x1 x2 .... xn s1 s2 ..... sn
def CompleteConstraintsAndGetCoefficients(constraints,variables):

    table = []             # list to get coefficients of each variable in each equation  
    finalConstraints = []  # final constraints with coefficient for each variable and in the correct order 
                           # a1x1 + a2x2 + ... + anxn + b1s1 + b2s2 + .. + bnsn

    for constraint in constraints:

        # updating to default state before going to each constraint
        coefficient = []  # list to get value of each coefficient in a particular constraint 
        equation = "CUT"  # string to get the new updated constraint

        for variable in variables:

            extractedValue =[]         # for getting coefficient-variable string of a variable
            extractedCoefficient = []  # to get the coefficient of a variable

            if(constraint.find(variable) !=-1): # checking for variable if present
                #extracting and adding to equation the coefficient-variable string of the variable
                extractedValue = re.search(r"[-]?\d+[.]\d+"+f'{variable}'+"|[-]?\d+"+f'{variable}',constraint )
                equation = equation + " + " + str(extractedValue.group())

            
                #extracting and adding to the coefficient the coefficient of the variable
                extractedCoefficient = re.search(r"[-]?\d+[.]\d+|[-]?\d+",str(extractedValue.group()) )
                coefficient.append(int(extractedCoefficient.group()))

            else:
                # if variable not present adding coefficient 0 and coefficient-variable string as f'0{variable}' 
                # to the coeeficient and equation respectively
                equation = equation + " + " + f'0{variable}'
                coefficient.append(0)

        equation = equation[6:len(equation)]                    # used to remove "CUT + " in begining
        RHS = re.split("=",constraint)                          # splitting by an equality sign
        value =  re.search(r"[-]?\d+[.]\d+|[-]?\d+",RHS[1])     # getting and inputting the solution part to the equation
        equation = equation + " = " + str(value.group())
        coefficient =[0] + [float(value.group())] + coefficient # making a row of simplex table with coefficients of
                                                                # CB XB x1 x2 .... xn s1 s2 ..... sn
       

        finalConstraints.append(equation)    # appending each updated constraint to finalConstraints
        table.append(coefficient)            # updating coefficients of each equation to the table

    return finalConstraints,table
        
# completing the z relation by adding 0 as coefficient to the variables which are not present and
# creating a dictionary of the type variable : cj value
def CompleteZAndGetCj(z,variables):

    # final cost function with coefficient for each variable
    # updating to default state before going to each constraint
    variablesCj = {} # dictionary to get value of coefficient of each variable
    finalZ = 'CUT'   # string to get the new updated cost function

    for variable in variables:

        extractedValue =[]         # for getting coefficient-variable string of a variable
        extractedCoefficient = []  # to get the coefficient of a variable

        if(z.find(variable) !=-1): # checking for variable if present
            #extracting and adding to finalZ 
            extractedValue = re.search(r"[-]?\d+[.]\d+"+f'{variable}'+"|[-]?\d+"+f'{variable}',z )
            finalZ = finalZ + " + " + str(extractedValue.group())

            #extracting and adding to the extractedCoefficient the coeffient of the variable
            extractedCoefficient = re.search(r"[-]?\d+[.]\d+|[-]?\d+",str(extractedValue.group()) )
            variablesCj[variable]=(float(extractedCoefficient.group()))

        else:
            # if variable not present adding coefficient 0 and coefficient-variable string as f'0{variable}' 
            # to the coeeficient and equation respectively
            finalZ = finalZ + " + " + f'0{variable}'
            variablesCj[variable]=0

    finalZ = finalZ[6:len(finalZ)]  #  used to remove "CUT + " in begining

    return finalZ,variablesCj


# implementation of dual simplex method 
def dualSimplexMethod(table,variablesCj):

    # getting variables and cj values to list from dictionary
    variables = list(variablesCj.keys())
    cj        = list(variablesCj.values())

    # intializing labels for dataframe
    columnLabel = ["CB","XB"] + variables
    rowLabel    = []
    for variable in variables:
        if(re.match(r"[s]\d+",variable)):
         rowLabel.append(variable)            # extracting s variables to insert into rowLabel as intial basic solution

    # intializing variables
    zj_cj     = [-1]                    # to satisfy the check condition in the loop 
    column    = 0                       # the column of the key value
    row       = 0                       # the row of the key value
    count     = 0                       # count of iteration
    zValue    = 0                       # final value of cost function
    dualValue = min(list(table[:,1]))   # lowest basic infeasible value
    solution  = {}                      # to get the final solution of the lpp
    
    
    
    # inserting the table and labels into the dataframe
    df = pd.DataFrame(table, index = rowLabel,columns =columnLabel)
    

    while(min(list(zj_cj))<0 or dualValue<0):
        
        #---------------------------------------------- finding the key value ------------------------------------------------

        # intializing all values to empty set
        zj_cj = []
        zj    = []
        zj_cj_xj = []
        
        # setting the row of the key element as the index of dualValue(minimum of basis values) 
        row = list(table[:,1]).index(dualValue)
        # incrementing iteration count
        count = count+1  

        # calculating zj = sum of (cj*xj (table[:,0]*table[:,i]))
        for i in range(2,table.shape[1]):
            value = np.multiply(table[:,0],table[:,i])
            zj.append(np.sum(value))
        
        # calculating zj-cj
        zj_cj = np.subtract(zj,cj)
       
       # calculating zj-cj/xi = zj_cj_xj
        for i in range(2,table.shape[1]):
            if(table[row,i]<0):
                zj_cj_xj.append(zj_cj[i-2]/table[row,i])
            else:
                zj_cj_xj.append(None)

        # setting the column of the key element as the index of the maximum ratio in zj_cj_xj
        # for that making a np array ratio to handle None data types to nan
        # then using the method nanmax maximum ratio is found neglecting the nan value
        ratio = np.array(zj_cj_xj,dtype=np.float64)
        maxRatio = np.nanmax(ratio)
        column = zj_cj_xj.index(maxRatio) + 2 

        # for var in zj_cj_xj:
        #     if(var<0 and var!=1):
        #       column = list(zj_cj_xj).index(var)
        #       column = column + 2

        #------------------------------------------- printing the df and key value details -----------------------------------------
        
        print("Iteration No : ",count)
        print(" ")
        print(df)
        print(" ")
        
        print("zj       : ",zj)
        print("zj-cj    : ",zj_cj)
        print("zj-cj/xj : ",zj_cj_xj)
        print(" ")

        print("row      : ",row)
        print("column   : ",column)
        print("key      : ",table[row,column])
        print(" ")
        print("----------------------------------------------------------------- ")
        print(" ")

        #-------------------------------------------------------- modifying the table ----------------------------------------------------
        
        inVariable = df.columns[column]    # variable to enter the basis
        df = df.rename(index={df.index[row]: df.columns[column]})   # renaming the row by the entering inVariable
        table[row,0] = variablesCj[inVariable]

        # dividing the row of the key element to make the key value to 1
        table[row,1:] = np.divide(table[row,1:],table[row,column])

       # substracting each row by the key row to make all elements of key column except key to 0
        for i in range(table.shape[0]):
            if(i!=row):
                table[i,1:] = table[i,1:] - (table[i,column]/table[row,column])*table[row,1:] 

        # transfering the updated table to the dataframe
        df[:] = table
        
        # finding new dualValue to continue the iteration if its negative
        dualValue = min(list(table[:,1]))
     #--------------------------------------------------------------------------------------------------------------------------------
    
    #--------------------------- final solution and table ---------------------------------------------

    # getting the basic solution from the rowLabel index of the dataframe df
    basicSolution = list(df.index)

    # updating the solution dictionary with each variable and its 
    # corresponding value as key value pair by iterating through
    # variables and taking value from XB of df if variable is in
    # basicSolution else its given as 0
    for variable in variables:
        if variable in basicSolution:
            solution[variable] = df.loc[variable].iat[1]
        else:
            solution[variable] = 0

           
    # calculting the optimal value of cost function z
    for variable, value in solution.items():
        zValue = zValue + value*variablesCj[variable]

    # printing the final solution table 
    print(" ")
    print("Final Table : ") 
    print(" ") 
    
    print(df)
    print(" ")

    # printing each variable and its value
    print("Solution : ")  
    print(" ")
    for variable, value in solution.items():
        print(variable," : ",round(value,3))

    print(" ")
    print("Optimum Value of Z : ",-1*zValue)  
    print(" ") 
    print("----------------------------------------------------------------- ")
          
    
#default values for testing : uncomment from 293-295 and  comment from 298 to 299 and 305 to 327
# constraints = ["-1x1 + -1x2 < -1","-2x1 + -3x2 < -2"]
# z           = "-3x1 + -1x2"

# values for user inputting
constraints =[]
z = ""
variables   = []         # variables of the lpp
table       = []         # table to take values of constraints
variablesCj = {}        # cj : coefficients of z with variable as key


# requesting inputs
# getting the z relation to be optimized
print(" ")
z = input(("Maximize/Minimize : "))
print(" ")

# getting the number of constraints
constraintsCount = int(input("Enter the number of constraints : "))
print(" ")

# getting constraints as user inputs
print("Enter constraints of the form : w1x1 + w2x2 + ..... + wnxn ~ w0 where, ~ = >/</=/>=/<=")
print(" ")
for i in range (1,constraintsCount+1):
    if(i==1):
        constraint = str(input("Enter the 1st constraint : "))
    elif(i==2):
        constraint = str(input("Enter the 2nd constraint : "))
    elif(i==3):
        constraint = str(input("Enter the 3rd constraint : "))
    else:
        constraint = str(input(f"Enter the {constraintsCount}th constraint : "))
    constraints.append(constraint)       
print(" ")

print(" ")
print("------------- Solving LPP using Dual Simplex Method -------------")
print(" ")

# calling functions with parameters
ConvertToEquation(constraints)
variables         = GetVariables(constraints)
constraints,table = CompleteConstraintsAndGetCoefficients(constraints,variables)
z,variablesCj     = CompleteZAndGetCj(z,variables)

# printing the modified constraints and z
print("Modified LPP : Maximize/Minimize : ",z)
print(" ")
print("subject to :")

for constraint in constraints:
    print(constraint)
print(" ")

# making the np array and calling dualSimplexMethod
table = np.array(table)
dualSimplexMethod(table,variablesCj)



