# required libraries
import re  
   
# required functions

# function to extract coefficients and power
# a0x^0 + a1x^1 + a2x^2 + a3x^3 + .... + aix^i + ... + anx^n where
# i E (...,-3,-2,-1,0,1,2,3,...)
def function_identifier(polynomial):
    
    result = [] # result to extract ai and i as a list from the string
    func   = [] # store [ai,i] for all i in polynomial

    components = polynomial.split(" + ")  # splitting as components by " + "
    for word in components:
        if bool(re.fullmatch(r'^[-+]?\d+(\.\d+)?$',word)) == True :  # checking if it is just number x^0
            result=re.findall(r'-?\d+(?:\.\d+)?', word)
            result = [float(x) for x in result]
            result.append(float(0))
        elif bool(re.search(r".*[x]$",word)) == True :               # checking if it is number times  x^1
            result=re.findall(r'-?\d+(?:\.\d+)?', word)
            result = [float(x) for x in result]
            result.append(float(1))
        else :                                                       # for all other x^i 
            result=re.findall(r'-?\d+(?:\.\d+)?', word)
            result = [float(x) for x in result]
            if len(result) == 1:
                result.insert(0,1)
        func.append(result)                                          # adding to list func      
    return func

# function to calculate the value of the polynomial at a point
def fofx(x):
    global func

    value = 0 # for getting value of function at x
    for term in func:
        value = value + term[0]*(x**term[1]) # contribution of each term
    return value

# function to calculate the derivative of the polynomial at a point
def f_ofx(x):
    global d_func

    value = 0 # for getting value of function at x
    for term in d_func:
        value = value + term[0]*(x**term[1]) # contribution of each term
    return value

# function to calculate the derivative function
def calc_derivative():

    d_func  = []
    # calculating derivative of x^n as nx^n-1
    for term in func:
        insert = []
        insert.append(term[0]*(term[1])) 
        insert.append(term[1]-1)
        d_func.append(insert)

    return d_func

# function to calculate intial range
def intial_range():

    number_line = [-3,-2,-1,0,1,2,3]
    a = fofx(-3) # parameters of range: (a,b)
    b = 0
    for x in number_line:
        if fofx(x) > 0 : # going to right of number line to find fofx(x) > 0
            b = x
            break
        elif fofx(x) < 0 : # else changing the limit of a 
            a = x
    return a,b

# function to perform bisection method
def newton_raphson_method():

    # intial range within which x for f(x) = 0 lies
    global a
    global b
    count = 0
    
    # intial error and value of the function
    calc_e = 1    
    value  = fofx(a)
    x      = a
    # repeat untill error is less than required
    while calc_e != 0 :

        count = count + 1
        x = x - fofx(x)/f_ofx(x)
        x = round(x,rd)
        print("Iteration No. : ",count)
        print(" ")
        print("   a = ",a)
        print("   x = ",x)
        print("   b = ",b)
        
        if fofx(x) > 0 :  # updating a and b
            b = x
        else :
            a = x

        calc_e = abs(value - fofx(x)) # calculating error
        calc_e = round(calc_e,rd)
        value  = fofx(x)              # storing value at this point for error calculation
        
        print(" ")
        print("   error = ",calc_e)
        print(" ")
        
    return x

# default polynomial for testing f(x) = x^3 + -1x + -1
# calling required functions
print(" ")
print("      ROOTS OF NON-LINEAR EQUATION USING NEWTON RAPHSON METHOD")
print("   --------------------------------------------------------------")
print(" ")
polynomial = str(input("Enter the non-linear equation : "))
rd      = int(input("Enter the round of parameter  : "))
print(" ")
func   = function_identifier(polynomial)
d_func = calc_derivative()
a,b  = intial_range()
ans  = newton_raphson_method()
print('The root of the non-linear equation')
print(f'          {polynomial} = 0')
print(f'to a precision of {rd} decimal places is ')
print("         ",ans)
print(" ")
